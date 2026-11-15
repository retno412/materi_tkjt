import { initializeApp } from "https://www.gstatic.com/firebasejs/12.18.0/firebase-app.js";
import { getDatabase, ref, get, set, child, push, update, remove } from "https://www.gstatic.com/firebasejs/12.18.0/firebase-database.js";

const firebaseConfig = {
    apiKey: "AIzaSyBvY2ryMzSJjgHkadfuPWbzFBgL1kQpygI",
    authDomain: "materi-pnc.firebaseapp.com",
    projectId: "materi-pnc",
    storageBucket: "materi-pnc.firebasestorage.app",
    messagingSenderId: "631396189340",
    appId: "1:631396189340:web:c9b86c3f7face5b1635959",
    measurementId: "G-21R2MTPGQ4",
    databaseURL: "https://materi-pnc-default-rtdb.asia-southeast1.firebasedatabase.app"
};

const app = initializeApp(firebaseConfig);
const db = getDatabase(app);

// ✅ URL 1: Khusus untuk sistem Galeri & Verifikasi Admin/Club
const APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbwgo5StWu6Cq77Lo_UZijnFjnbpnwbFq74kc4aG9QAWJK05sUSURbF9YtmXmnbZ3jQxGA/exec";

// ✅ URL 2: Khusus untuk pengecekan Kredensial AWS Academy & Database Siswa
const AWS_APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzq3mIqs5FYZvSZTSmYULh3BI0dF3KQCio3kVV019XlaxiCl-jfztYtipypToHzwFZiRA/exec";

// Keamanan admin: hanya digest hash disimpan, never plain-text passphrase/token
const ADMIN_HASH = "f94e4a56e0a22dd26690ff08b72e709b7e4ac4ddaf4a41e5410e6daf32faeb07";
const HASH_PEPPER = "mpnc::v2::admin::2026";
const HASH_ROUNDS = 512;
const SESSION_KEY = "pnc_admin_session_v2";
const SESSION_TTL = 2 * 60 * 60 * 1000; // 2 jam
const KB_STORAGE_KEY = 'mpnc_ai_kb_semester3';

let isAdmin = false;
let dynamicKB = {};
const textEncoder = new TextEncoder();

async function sha256Hex(text) {
    if (window.crypto && window.crypto.subtle) {
        try {
            const buffer = await window.crypto.subtle.digest("SHA-256", textEncoder.encode(text));
            return Array.from(new Uint8Array(buffer), (b) => b.toString(16).padStart(2, "0")).join("");
        } catch (e) { /* fallthrough */ }
    }
    return sha256Fallback(text);
}

async function deriveHash(passphrase) {
    let digest = await sha256Hex(HASH_PEPPER + passphrase + HASH_PEPPER);
    for (let i = 1; i < HASH_ROUNDS; i += 1) {
        digest = await sha256Hex(digest + HASH_PEPPER);
    }
    return digest;
}

function timingSafeEqual(left, right) {
    if (typeof left !== "string" || typeof right !== "string" || left.length !== right.length) return false;
    let diff = 0;
    for (let i = 0; i < left.length; i += 1) diff |= left.charCodeAt(i) ^ right.charCodeAt(i);
    return diff === 0;
}

function randomToken() {
    const bytes = new Uint8Array(32);
    if (window.crypto && window.crypto.getRandomValues) window.crypto.getRandomValues(bytes);
    else for (let i = 0; i < bytes.length; i += 1) bytes[i] = Math.floor(Math.random() * 256);
    return Array.from(bytes, (b) => b.toString(16).padStart(2, "0")).join("");
}

async function sessionSignature(token, expiresAt) {
    return sha256Hex(ADMIN_HASH + ":" + token + ":" + expiresAt);
}

async function createSession() {
    const token = randomToken();
    const expiresAt = Date.now() + SESSION_TTL;
    const signature = await sessionSignature(token, expiresAt);
    try {
        sessionStorage.setItem(SESSION_KEY, JSON.stringify({ token: token, exp: expiresAt, sig: signature }));
    } catch (e) {}
}

async function hasValidSession() {
    let raw;
    try { raw = sessionStorage.getItem(SESSION_KEY); } catch (e) { return false; }
    if (!raw) return false;
    try {
        const session = JSON.parse(raw);
        if (!session || typeof session.token !== "string" || session.token.length < 32) {
            sessionStorage.removeItem(SESSION_KEY); return false;
        }
        if (!Number.isFinite(session.exp) || session.exp <= Date.now()) {
            sessionStorage.removeItem(SESSION_KEY); return false;
        }
        const expected = await sessionSignature(session.token, session.exp);
        if (!timingSafeEqual(expected, session.sig)) {
            sessionStorage.removeItem(SESSION_KEY); return false;
        }
        return true;
    } catch (e) {
        try { sessionStorage.removeItem(SESSION_KEY); } catch (ignored) {}
        return false;
    }
}

function clearSession() {
    try { sessionStorage.removeItem(SESSION_KEY); } catch (e) {}
}

function sha256Fallback(ascii) {
    function rightRotate(value, amount) { return (value >>> amount) | (value << (32 - amount)); }
    const mathPow = Math.pow;
    const maxWord = mathPow(2, 32);
    let result = "";
    const words = [];
    const hash = sha256Fallback.h = sha256Fallback.h || [];
    const k = sha256Fallback.k = sha256Fallback.k || [];
    let primeCounter = k.length;
    const isComposite = {};
    for (let candidate = 2; primeCounter < 64; candidate += 1) {
        if (!isComposite[candidate]) {
            for (let step = 0; step < 313; step += candidate) isComposite[step] = candidate;
            hash[primeCounter] = (mathPow(candidate, 0.5) * maxWord) | 0;
            k[primeCounter] = (mathPow(candidate, 1 / 3) * maxWord) | 0;
            primeCounter += 1;
        }
    }
    ascii += "\x80";
    while (ascii.length % 64 - 56) ascii += "\x00";
    for (let i = 0; i < ascii.length; i += 1) {
        const code = ascii.charCodeAt(i);
        if (code >> 8) return "";
        words[i >> 2] |= code << (((3 - i) % 4) * 8);
    }
    words[words.length] = (asciiBitLength / maxWord) | 0;
    words[words.length] = asciiBitLength;
    let working = hash.slice(0, 8);
    let asciiBitLength = ascii.length * 8;
    for (let offset = 0; offset < words.length;) {
        const chunk = words.slice(offset, offset += 16);
        const oldHash = working.slice(0, 8);
        for (let round = 0; round < 64; round += 1) {
            const w15 = chunk[round - 15];
            const w2 = chunk[round - 2];
            const a = working[0];
            const e = working[4];
            const word = round < 16
                ? chunk[round]
                : (chunk[round - 16] + (rightRotate(w15, 7) ^ rightRotate(w15, 18) ^ (w15 >>> 3)) + chunk[round - 7] + (rightRotate(w2, 17) ^ rightRotate(w2, 19) ^ (w2 >>> 10))) | 0;
            chunk[round] = word;
            const temp1 = (working[7] + (rightRotate(e, 6) ^ rightRotate(e, 11) ^ rightRotate(e, 25)) + ((e & working[5]) ^ ((~e) & working[6])) + k[round] + word) | 0;
            const temp2 = ((rightRotate(a, 2) ^ rightRotate(a, 13) ^ rightRotate(a, 22)) + ((a & working[1]) ^ (a & working[2]) ^ (working[1] & working[2]))) | 0;
            working.unshift((temp1 + temp2) | 0);
            working[4] = (working[4] + temp1) | 0;
        }
        for (let i = 0; i < 8; i += 1) working[i] = (working[i] + oldHash[i]) | 0;
    }
    for (let i = 0; i < 8; i += 1) {
        for (let shift = 3; shift + 1; shift -= 1) {
            const byte = (working[i] >> (shift * 8)) & 255;
            result += (byte < 16 ? "0" : "") + byte.toString(16);
        }
    }
    return result;
}

function loadDynamicKB() {
    try {
        const raw = localStorage.getItem(KB_STORAGE_KEY);
        if (raw) dynamicKB = JSON.parse(raw);
    } catch (e) { /* corrupted storage */ }
}

window.initApp = async function() {
    loadDynamicKB();
    // Verifikasi sesi admin berbasis tanda tangan (session signature) — tidak ada token mentah
    const valid = await hasValidSession();
    if (valid) {
        isAdmin = true;
        const btnProfile = document.getElementById('btn-profile');
        if(btnProfile) {
            btnProfile.innerText = "🔓 Keluar Mode Admin";
            btnProfile.style.background = "#ec4899";
        }
        window.enableEditMode();
    }

    const dbRef = ref(db);
    try {
        const snapshot = await get(child(dbRef, `site_content`));
        if (snapshot.exists()) {
            const savedData = snapshot.val();
            const editableElements = document.querySelectorAll('[data-edit-id]');
            editableElements.forEach(el => {
                const id = el.dataset.editId;
                if(savedData[id] && !el.querySelector('textarea')) {
                    el.innerText = savedData[id];
                }
            });
        }
    } catch (error) {
        console.error("Gagal memuat data:", error);
    }

    if(typeof window.muatGaleri === 'function') {
        await window.muatGaleri();
    }
};

window.checkAdmin = async function() {
    const valid = await hasValidSession();
    if (valid) {
        if(confirm("Anda yakin ingin keluar dari Mode Admin?")) {
            clearSession();
            window.location.reload();
        }
        return;
    }

    let pass = prompt("Masukkan kode otorisasi sistem:");
    if (!pass) return;

    const btnProfile = document.getElementById('btn-profile');
    const textAwal = btnProfile ? btnProfile.innerText : "";
    if(btnProfile) { btnProfile.innerText = "⏳ Memverifikasi..."; }

    try {
        const digest = await deriveHash(pass);
        if (!timingSafeEqual(digest, ADMIN_HASH)) {
            alert("Kode otorisasi tidak valid.");
            if(btnProfile) btnProfile.innerText = textAwal;
            return;
        }
        await createSession();
        isAdmin = true;
        if(btnProfile) {
            btnProfile.innerText = "🔓 Keluar Mode Admin";
            btnProfile.style.background = "#ec4899";
        }
        window.enableEditMode();
    } catch (error) {
        alert("Verifikasi gagal diproses. Muat ulang halaman lalu coba lagi.");
        if(btnProfile) btnProfile.innerText = textAwal;
        console.error("Verifikasi admin gagal:", error);
    }
};

// Fungsi Backend Delegation untuk Validasi Password Club
async function verifikasiPasswordClub(passInput) {
    try {
        const response = await fetch(APPS_SCRIPT_URL, {
            method: "POST",
            headers: { "Content-Type": "text/plain;charset=utf-8" },
            body: JSON.stringify({ action: "verify_auth", role: "club", password: passInput })
        });
        const result = await response.json();
        return result.status === "success";
    } catch (error) {
        return false;
    }
}

window.enableEditMode = function() {
    const links = document.querySelectorAll('a.btn-club, button.btn-semester');
    links.forEach(link => {
        let targetUrl = "";
        if (link.tagName === 'A') {
            targetUrl = link.getAttribute('href');
            if (targetUrl !== "javascript:void(0)") link.setAttribute('data-target', targetUrl);
            else targetUrl = link.getAttribute('data-target');
            link.href = "javascript:void(0)";
        } else if (link.tagName === 'BUTTON') {
            const onclickStr = link.getAttribute('onclick');
            if (onclickStr && onclickStr.includes("window.location.href")) {
                const match = onclickStr.match(/'([^']+)'/);
                if (match) targetUrl = match[1];
                link.removeAttribute('onclick');
                link.setAttribute('data-target', targetUrl);
            } else {
                targetUrl = link.getAttribute('data-target');
            }
        }
        link.title = "Klik 2x di luar area teks untuk buka halaman";
        link.onclick = (e) => { if(e.target.tagName !== 'TEXTAREA') e.preventDefault(); };
        link.ondblclick = (e) => {
            if (targetUrl && e.target.tagName !== 'TEXTAREA') window.location.href = targetUrl;
        };
    });

    const editableElements = document.querySelectorAll('[data-edit-id]');
    editableElements.forEach(el => {
        if(el.querySelector('textarea')) return;
        const currentText = el.innerText;
        const input = document.createElement('textarea');
        input.value = currentText;
        input.className = 'admin-input-field';
        input.dataset.bind = el.dataset.editId;
        input.rows = currentText.length > 30 ? 3 : 1;
        el.innerHTML = '';
        el.appendChild(input);
    });

    const adminPanel = document.getElementById('admin-panel');
    if(adminPanel) adminPanel.classList.remove('hidden');
};

window.saveChanges = async function() {
    const btnSave = document.querySelector('.btn-save-admin');
    const textAwal = btnSave ? btnSave.innerText : "";
    if(btnSave) btnSave.innerText = "⏳ Menyimpan ke Cloud...";

    const inputs = document.querySelectorAll('.admin-input-field');
    let newData = {};
    inputs.forEach(input => {
        newData[input.dataset.bind] = input.value;
    });

    try {
        await set(ref(db, 'site_content'), newData);
        alert("Perubahan Berhasil Tersimpan di Database Publik!");
        window.location.reload();
    } catch (error) {
        alert("Gagal menyimpan ke Firebase.");
        if(btnSave) btnSave.innerText = textAwal;
    }
};

window.bukaModalUpload = function() {
    const modal = document.getElementById('upload-modal');
    if(modal) modal.classList.remove('hidden');
};

window.tutupModalUpload = function() {
    const modal = document.getElementById('upload-modal');
    if(modal) modal.classList.add('hidden');
    const passEl = document.getElementById('up-password');
    const fileEl = document.getElementById('up-file');
    if(passEl) passEl.value = '';
    if(fileEl) fileEl.value = '';
    const btn = document.getElementById('btn-proses-upload');
    if (btn) {
        btn.innerText = "Publikasikan 🚀";
        btn.disabled = false;
    }
};

window.cekLainnya = function() {
    const select = document.getElementById('up-keperluan');
    const inputLain = document.getElementById('up-keperluan-lain');
    if (!select || !inputLain) return;
    if (select.value === 'Lainnya') inputLain.classList.remove('hidden');
    else inputLain.classList.add('hidden');
};

window.prosesUpload = async function() {
    const pass = document.getElementById('up-password').value;
    const nama = document.getElementById('up-nama').value;
    const selectKep = document.getElementById('up-keperluan').value;
    const kepLain = document.getElementById('up-keperluan-lain').value;
    const fileInput = document.getElementById('up-file');

    if (!nama || !selectKep || fileInput.files.length === 0) return alert("Lengkapi data dan pilih minimal 1 file foto/video.");

    const btn = document.getElementById('btn-proses-upload');
    btn.innerText = "⏳ Mengecek Akses...";
    const isAuthValid = await verifikasiPasswordClub(pass);
    if (!isAuthValid) {
        btn.innerText = "Publikasikan 🚀";
        return alert("Password Club salah atau server sibuk!");
    }

    const files = fileInput.files;
    const keperluanFinal = selectKep === 'Lainnya' ? kepLain : selectKep;
    const maxSize = 10 * 1024 * 1024; // Batas aman 10MB per file
    const allowedMime = /^(image\/|video\/)/i;

    // Validasi tipe MIME sebelum unggah
    const invalidType = Array.from(files).find((f) => !allowedMime.test(f.type || ""));
    if (invalidType) {
        btn.innerText = "Publikasikan 🚀";
        btn.disabled = false;
        return alert("Tipe berkas '" + invalidType.name + "' tidak diizinkan. Hanya foto dan video.");
    }

    // Validasi ukuran sebelum unggah
    const oversized = Array.from(files).find((f) => f.size > maxSize);
    if (oversized) {
        btn.innerText = "Publikasikan 🚀";
        btn.disabled = false;
        return alert("Berkas '" + oversized.name + "' melebihi batas 10 MB. Pilih berkas yang lebih kecil.");
    }

    btn.disabled = true;
    let sukses = 0;
    let gagal = 0;

    for (let i = 0; i < files.length; i++) {
        const file = files[i];
        btn.innerText = `⏳ Mengunggah ${i + 1} dari ${files.length} file...`;

        try {
            const base64Data = await new Promise((resolve, reject) => {
                const reader = new FileReader();
                reader.onload = (e) => resolve(e.target.result.split(',')[1]);
                reader.onerror = (e) => reject(e);
                reader.readAsDataURL(file);
            });

            const driveResponse = await fetch(APPS_SCRIPT_URL, {
                method: "POST",
                headers: { "Content-Type": "text/plain;charset=utf-8" },
                body: JSON.stringify({
                    action: "upload",
                    fileName: file.name,
                    mimeType: file.type,
                    base64: base64Data
                })
            });

            const driveResult = await driveResponse.json();

            if (driveResult.status === "success") {
                const now = new Date();
                const waktu = now.toLocaleString('id-ID', { timeZone: 'Asia/Jakarta', dateStyle: 'medium', timeStyle: 'short' });

                const galleryData = {
                    url_file: driveResult.url,
                    file_id: driveResult.file_id || "",
                    uploader: nama,
                    keperluan: keperluanFinal,
                    datetime: waktu,
                    timestamp: now.getTime()
                };

                await push(ref(db, 'gallery_data'), galleryData);
                sukses++;
            } else {
                console.error(`Gagal upload ${file.name}:`, driveResult.message);
                gagal++;
            }
        } catch (fileError) {
            console.error(`Kesalahan sistem/CORS pada ${file.name}:`, fileError);
            gagal++;
        }
    }

    alert(`Publikasi Selesai!\n✅ Berhasil: ${sukses} file\n❌ Gagal/Dilewati: ${gagal} file`);

    window.tutupModalUpload();
    window.muatGaleri();
    btn.innerText = "Publikasikan 🚀";
    btn.disabled = false;
};

window.hapusGaleri = async function(dbKey, fileId) {
    const pass = prompt("Masukkan Password Club untuk MENGHAPUS file ini:");
    if (!pass) return;

    const isAuthValid = await verifikasiPasswordClub(pass);
    if (!isAuthValid) {
        return alert("Password Salah atau Akses Ditolak!");
    }

    if(confirm("Yakin ingin menghapus secara permanen? File di Google Drive juga akan ditarik ke Trash.")) {
        try {
            await fetch(APPS_SCRIPT_URL, {
                method: "POST",
                headers: { "Content-Type": "text/plain;charset=utf-8" },
                body: JSON.stringify({ action: "delete", file_id: fileId })
            });
            await remove(ref(db, `gallery_data/${dbKey}`));
            alert("File berhasil dihapus sepenuhnya.");
            window.muatGaleri();
        } catch(error) {
            alert("Gagal menghapus file.");
            console.error(error);
        }
    }
};

window.editGaleri = async function(dbKey, namaLama, kepLama) {
    const pass = prompt("Masukkan Password Club untuk MENGEDIT info:");
    if (!pass) return;

    const isAuthValid = await verifikasiPasswordClub(pass);
    if (!isAuthValid) {
        return alert("Password Salah atau Akses Ditolak!");
    }

    const namaBaru = prompt("Ubah Nama Uploader:", namaLama);
    if (namaBaru === null) return;

    const kepBaru = prompt("Ubah Keperluan:", kepLama);
    if (kepBaru === null) return;

    if (namaBaru.trim() !== "" && kepBaru.trim() !== "") {
        try {
            await update(ref(db, `gallery_data/${dbKey}`), {
                uploader: namaBaru,
                keperluan: kepBaru
            });
            alert("Informasi berhasil diperbarui!");
            window.muatGaleri();
        } catch (error) {
            alert("Gagal mengupdate informasi.");
        }
    }
};

window.muatGaleri = async function() {
    try {
        const snapGaleri = await get(child(ref(db), `gallery_data`));
        const container = document.getElementById('galeri-container');
        if(!container) return;
        container.innerHTML = "";

        if (snapGaleri.exists()) {
            const data = snapGaleri.val();
            const arrayData = Object.keys(data).map(key => ({
                id_db: key,
                ...data[key]
            })).sort((a, b) => b.timestamp - a.timestamp);

            const counterEl = document.getElementById('counter-galeri');
            if(counterEl) {
                counterEl.innerText = `${arrayData.length} File Tersimpan`;
            }

            arrayData.forEach(item => {
                const safeNama = item.uploader.replace(/'/g, "\\'");
                const safeKep = item.keperluan.replace(/'/g, "\\'");

                container.innerHTML += `
                    <div class="interactive-card">
                        <div class="card-media-wrapper">
                            <img src="${item.url_file}" class="card-media" alt="Media Konten" onerror="this.src='https://via.placeholder.com/260x160?text=File+Video/Media'">
                        </div>
                        <div class="card-body">
                            <div>
                                <div class="card-title-meta">👤 ${item.uploader}</div>
                                <div class="card-sub-meta">📅 ${item.datetime}</div>
                                <div style="margin-top: 6px;"><span class="badge-keperluan">${item.keperluan}</span></div>
                            </div>

                            <div style="margin-top: 10px; display: flex; gap: 6px; flex-wrap: wrap;">
                                <a href="${item.url_file}" target="_blank" download style="flex: 2; text-align: center; font-size: 0.7rem; padding: 6px; background: #059669; border-radius: 6px; color: #fff; text-decoration: none; font-weight: bold;">📥 Tarik</a>
                                <button onclick="editGaleri('${item.id_db}', '${safeNama}', '${safeKep}')" style="flex: 1; font-size: 0.7rem; padding: 6px; background: #d97706; border: none; border-radius: 6px; color: #fff; cursor: pointer; font-weight: bold;">✏️</button>
                                <button onclick="hapusGaleri('${item.id_db}', '${item.file_id}')" style="flex: 1; font-size: 0.7rem; padding: 6px; background: #dc2626; border: none; border-radius: 6px; color: #fff; cursor: pointer; font-weight: bold;">🗑️</button>
                            </div>
                        </div>
                    </div>
                `;
            });
        } else {
            container.innerHTML = "<p style='color: #94a3b8; font-size: 0.9rem; grid-column: 1 / -1; text-align: center;'>Belum ada dokumentasi karya yang diunggah.</p>";
            const counterEl = document.getElementById('counter-galeri');
            if(counterEl) counterEl.innerText = "0 File Tersimpan";
        }
    } catch (error) {
        console.error("Gagal memuat galeri:", error);
    }
};

// ==========================================
// FUNGSI MODAL & FETCH KREDENSIAL AWS ACADEMY (Menggunakan URL 2)
// ==========================================
window.openAwsModal = function() {
    const modal = document.getElementById('awsModal');
    if(modal) modal.style.display = 'flex';
};

window.closeAwsModal = function() {
    const modal = document.getElementById('awsModal');
    if(modal) modal.style.display = 'none';

    const resBox = document.getElementById('credentialResult');
    const errBox = document.getElementById('errorMessage');
    if(resBox) resBox.style.display = 'none';
    if(errBox) errBox.style.display = 'none';

    const namaInput = document.getElementById('inputNama');
    const nisnInput = document.getElementById('inputNisn');
    if(namaInput) namaInput.value = '';
    if(nisnInput) nisnInput.value = '';
};

window.fetchAwsCredentials = async function() {
    const nama = document.getElementById('inputNama').value.trim();
    const nisn = document.getElementById('inputNisn').value.trim();
    const resBox = document.getElementById('credentialResult');
    const errBox = document.getElementById('errorMessage');

    if(resBox) resBox.style.display = 'none';
    if(errBox) errBox.style.display = 'none';

    if (!nama || !nisn) {
        if(errBox) {
            errBox.innerText = "Mohon isi Nama Lengkap dan NISN terlebih dahulu.";
            errBox.style.display = 'block';
        }
        return;
    }

    const submitBtn = document.querySelector('.btn-submit-credential');
    if(submitBtn) {
        submitBtn.innerText = "Mencari data...";
        submitBtn.disabled = true;
    }

    try {
        const response = await fetch(`${AWS_APPS_SCRIPT_URL}?nisn=${encodeURIComponent(nisn)}&nama=${encodeURIComponent(nama)}`);
        const data = await response.json();

        if(submitBtn) {
            submitBtn.innerText = "Cek Kredensial";
            submitBtn.disabled = false;
        }

        if (data.success) {
            document.getElementById('resUsername').innerText = data.username;
            document.getElementById('resPassword').innerText = data.password;
            if(resBox) resBox.style.display = 'block';
        } else {
            if(errBox) {
                errBox.innerText = data.message;
                errBox.style.display = 'block';
            }
        }
    } catch (error) {
        if(submitBtn) {
            submitBtn.innerText = "Cek Kredensial";
            submitBtn.disabled = false;
        }
        if(errBox) {
            errBox.innerText = "Terjadi kesalahan koneksi ke server.";
            errBox.style.display = 'block';
        }
        console.error('Error:', error);
    }
};

// Event listener tambahan untuk menutup modal jika klik area luar modal
window.addEventListener('click', (event) => {
    const modal = document.getElementById('awsModal');
    if (event.target === modal) {
        window.closeAwsModal();
    }
});

window.onload = window.initApp;
