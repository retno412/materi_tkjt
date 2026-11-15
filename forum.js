const API_URL = "https://script.google.com/macros/s/AKfycbwZDWN6fcm9qveHpLQACp8iUDTHejuqj46RDlsYSo5CC-B_i1EGcOQV6Jf4FWqldanaPA/exec"; 

document.addEventListener("DOMContentLoaded", () => {
    verifyForumSession();
});

// Validasi Wajib Punya Nama dari Start Journey
function verifyForumSession() {
    const studentId = localStorage.getItem("student_journey_id");
    const studentName = localStorage.getItem("student_name");
    
    const inputArea = document.querySelector(".forum-input-box");
    
    if (!studentId || !studentName) {
        // Jika belum start journey, sembunyikan kotak kirim dan beri peringatan
        if (inputArea) {
            inputArea.innerHTML = `
                <div style="text-align: center; color: #ff5555; padding: 10px;" class="code-font">
                    ⚠️ Akses Terbatas! Kamu harus melakukan <strong>[ START NEW JOURNEY ]</strong> di halaman utama terlebih dahulu untuk menulis atau berkomentar di forum.
                </div>
            `;
        }
    }
    
    // Tarik data forum
    loadForumPosts();
}

async function loadForumPosts() {
    const feedContainer = document.getElementById("forum-feed-list");
    
    try {
        if(API_URL.includes("URL_WEB_APP")) throw new Error("API belum diset");

        const response = await fetch(`${API_URL}?action=get_forum`);
        const data = await response.json();
        
        renderForum(data.posts);
    } catch (error) {
        feedContainer.innerHTML = `<p style="text-align: center; color: #ff5555;">[OFFLINE] Gagal memuat forum dari server.</p>`;
    }
}

function renderForum(posts) {
    const feedContainer = document.getElementById("forum-feed-list");
    const studentName = localStorage.getItem("student_name");

    if (!posts || posts.length === 0) {
        feedContainer.innerHTML = `<p style="text-align: center; color: #6272a4;">Belum ada diskusi dalam bentuk card. Jadilah yang pertama bertanya!</p>`;
        return;
    }

    // Filter hanya postingan utama (MAIN / POST)
    const mainPosts = posts.filter(p => p.type === "POST");
    
    let html = "";
    mainPosts.reverse().forEach(post => {
        // Cari komentar yang targetId-nya cocok dengan rowId postingan ini
        const comments = posts.filter(p => p.type === "COMMENT" && String(p.targetId) === String(post.rowId));

        html += `
        <div class="forum-card">
            <div class="forum-meta">
                <span class="forum-author">👤 ${escapeHtml(post.senderName)}</span>
                <span class="forum-time">${new Date(post.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</span>
            </div>
            <p class="forum-text">${escapeHtml(post.message)}</p>
            
            <!-- Daftar Komentar Card -->
            <div class="comments-section">
        `;

        comments.forEach(com => {
            html += `
                <div class="comment-item">
                    <span class="comment-author">↳ ${escapeHtml(com.senderName)}:</span> 
                    <span class="comment-text">${escapeHtml(com.message)}</span>
                </div>
            `;
        });

        // Kotak input komentar hanya muncul jika siswa sudah memiliki sesi nama
        if (studentName) {
            html += `
                <div class="reply-box">
                    <input type="text" id="comment-input-${post.rowId}" class="code-font comment-input" placeholder="Tulis komentar balasan...">
                    <button class="btn pixel-btn comment-btn" onclick="postComment(${post.rowId})">Kirim</button>
                </div>
            `;
        } else {
            html += `
                <p style="font-size: 0.75rem; color: #6272a4; margin-top: 5px;">*Login / Start Journey di halaman utama untuk ikut berkomentar.</p>
            `;
        }

        html += `
            </div>
        </div>`;
    });

    feedContainer.innerHTML = html;
}

async function postToForum(targetId, type) {
    const studentId = localStorage.getItem("student_journey_id");
    const senderName = localStorage.getItem("student_name");

    if (!studentId || !senderName) {
        alert("Akses ditolak! Silakan buat nama melalui Start Journey di halaman utama terlebih dahulu.");
        return;
    }

    const inputField = document.getElementById("forum-msg");
    const message = inputField.value.trim();
    
    if (!message) {
        alert("Pesan diskusi tidak boleh kosong!");
        return;
    }

    const payload = {
        senderId: studentId,
        senderName: senderName,
        type: type,
        targetId: targetId,
        message: message
    };

    inputField.value = "Mengirim...";

    try {
        await fetch(API_URL, {
            method: 'POST',
            mode: 'no-cors',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ method: "POST_FORUM", payload: payload })
        });

        inputField.value = "";
        setTimeout(loadForumPosts, 1200); 
    } catch (error) {
        alert("Gagal mengirim pesan.");
        inputField.value = message;
    }
}

async function postComment(rowId) {
    const studentId = localStorage.getItem("student_journey_id");
    const senderName = localStorage.getItem("student_name");

    if (!studentId || !senderName) {
        alert("Akses ditolak! Silakan Start Journey terlebih dahulu.");
        return;
    }

    const inputField = document.getElementById(`comment-input-${rowId}`);
    const message = inputField.value.trim();

    if (!message) return;

    const payload = {
        senderId: studentId,
        senderName: senderName,
        type: "COMMENT",
        targetId: rowId,
        message: message
    };

    try {
        await fetch(API_URL, {
            method: 'POST',
            mode: 'no-cors',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ method: "POST_FORUM", payload: payload })
        });

        setTimeout(loadForumPosts, 1200);
    } catch (error) {
        alert("Gagal mengirim komentar.");
    }
}

function escapeHtml(text) {
    if (!text) return "";
    return text.toString().replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}