import { initializeApp } from "https://www.gstatic.com/firebasejs/12.18.0/firebase-app.js";
import { getDatabase, ref, get, set, child, push, update, remove } from "https://www.gstatic.com/firebasejs/12.18.0/firebase-database.js";

const firebaseConfig = {
    apiKey: "AIzaSyBvY2ryMzSJjgHkadfuPWbzFBgL1kQpygI",
    authDomain: "materi-pnc.firebaseapp.com",
    projectId: "materi-pnc",
    storageBucket: "materi-pnc.firebasestorage.app",
    messagingSenderId: "631396189340",
    appId: "1:631396189340:web:c9b86c3f7face5b1635959",
    measurementId: "G-21R2MTPGQ4"
};

const app = initializeApp(firebaseConfig);
const db = getDatabase(app);

const ADMIN_PASS = "RARTNUR";
const CLUB_PASSWORD = "CLUB_P&C";

// ⚠️ GANTI DENGAN URL WEB APP GOOGLE APPS SCRIPT ANDA SETELAH DI-DEPLOY
const APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbwHsYV1qGzqwwMMrOUxx2e7KYjmk7zcTF1G_kZ0L5_W2aEz4fLL7QcWYfF9OvUxvKeuJg/exec"; 

let isAdmin = false;

window.initApp = async function() {
    if (localStorage.getItem('isAdminActive') === 'true') {
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

    await window.muatGaleri();
}

window.checkAdmin = function() {
    if(isAdmin) {
        if(confirm("Anda yakin ingin keluar dari Mode Admin?")) {
            localStorage.removeItem('isAdminActive');
            window.location.reload();
        }
        return;
    }

    let pass = prompt("Masukkan kode otorisasi sistem:");
    if(pass === ADMIN_PASS) {
        isAdmin = true;
        localStorage.setItem('isAdminActive', 'true');
        const btnProfile = document.getElementById('btn-profile');
        if(btnProfile) {
            btnProfile.innerText = "🔓 Keluar Mode Admin";
            btnProfile.style.background = "#ec4899";
        }
        window.enableEditMode();
    } else if (pass !== null) {
        alert("Kode salah! Akses ditolak.");
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
}

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
}

window.bukaModalUpload = function() {
    const modal = document.getElementById('upload-modal');
    if(modal) modal.classList.remove('hidden');
}

window.tutupModalUpload = function() {
    const modal = document.getElementById('upload-modal');
    if(modal) modal.classList.add('hidden');
    document.getElementById('up-password').value = '';
    document.getElementById('up-file').value = '';
}

window.cekLainnya = function() {
    const select = document.getElementById('up-keperluan');
    const inputLain = document.getElementById('up-keperluan-lain');
    if (select.value === 'Lainnya') inputLain.classList.remove('hidden');
    else inputLain.classList.add('hidden');
}

window.prosesUpload = async function() {
    const pass = document.getElementById('up-password').value;
    const nama = document.getElementById('up-nama').value;
    const selectKep = document.getElementById('up-keperluan').value;
    const kepLain = document.getElementById('up-keperluan-lain').value;
    const fileInput = document.getElementById('up-file');
    
    if (pass !== CLUB_PASSWORD) return alert("Password Club salah!");
    if (!nama || !selectKep || fileInput.files.length === 0) return alert("Lengkapi data dan pilih file.");
    
    const keperluanFinal = selectKep === 'Lainnya' ? kepLain : selectKep;
    const file = fileInput.files[0];
    const btn = document.getElementById('btn-proses-upload');
    btn.innerText = "⏳ Sedang Mengunggah...";
    btn.disabled = true;

    const reader = new FileReader();
    reader.onload = async function(e) {
        const base64Data = e.target.result.split(',')[1];
        try {
            const driveResponse = await fetch(APPS_SCRIPT_URL, {
                method: "POST",
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
                    file_id: driveResult.file_id,
                    uploader: nama,
                    keperluan: keperluanFinal,
                    datetime: waktu,
                    timestamp: now.getTime()
                };

                await push(ref(db, 'gallery_data'), galleryData);
                alert("Berhasil! Karya tersimpan di Drive & Galeri.");
                window.tutupModalUpload();
                window.muatGaleri();
            } else {
                alert("Gagal upload ke Drive: " + driveResult.message);
            }
        } catch (error) {
            alert("Terjadi kesalahan jaringan.");
        } finally {
            btn.innerText = "Publikasikan 🚀";
            btn.disabled = false;
        }
    };
    reader.readAsDataURL(file);
}

window.hapusGaleri = async function(dbKey, fileId) {
    const pass = prompt("Masukkan Password Club untuk MENGHAPUS file ini:");
    if (pass !== CLUB_PASSWORD) {
        if (pass !== null) alert("Password Salah!");
        return;
    }

    if(confirm("Yakin ingin menghapus secara permanen? File di Google Drive juga akan ditarik ke Trash.")) {
        try {
            await fetch(APPS_SCRIPT_URL, {
                method: "POST",
                body: JSON.stringify({ action: "delete", file_id: fileId })
            });
            await remove(ref(db, `gallery_data/${dbKey}`));
            alert("File berhasil dihapus sepenuhnya.");
            window.muatGaleri();
        } catch(error) {
            alert("Gagal menghapus file.");
        }
    }
}

window.editGaleri = async function(dbKey, namaLama, kepLama) {
    const pass = prompt("Masukkan Password Club untuk MENGEDIT info:");
    if (pass !== CLUB_PASSWORD) {
        if (pass !== null) alert("Password Salah!");
        return;
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
}

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
        }
    } catch (error) {
        console.error("Gagal memuat galeri:", error);
    }
};

window.onload = window.initApp;