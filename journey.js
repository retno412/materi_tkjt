// GANTI DENGAN URL WEB APP ANDA
const API_URL = "https://script.google.com/macros/s/AKfycbwZDWN6fcm9qveHpLQACp8iUDTHejuqj46RDlsYSo5CC-B_i1EGcOQV6Jf4FWqldanaPA/exec"; 

let currentActiveSkillId = -1;
let currentActiveSkillName = "";
let l2lAnalysisResult = ""; 
let l2lScores = [];

document.addEventListener("DOMContentLoaded", () => {
    checkSession();
});

function checkSession() {
    const studentId = localStorage.getItem("student_journey_id");
    const btnContinue = document.getElementById("btn-continue");
    
    if (studentId) {
        btnContinue.classList.remove("hidden");
    }
}

function switchScreen(hideId, showId) {
    document.getElementById(hideId).classList.replace("active", "hidden");
    document.getElementById(showId).classList.replace("hidden", "active");
}

function startNewJourney() {
    const name = prompt("Masukkan nama lengkapmu:");
    if (!name || name.trim() === "") return;
    
    const majorClass = prompt("Masukkan Jurusan / Kelas / Angkatan (Contoh: PPLG / X-1 / 2026):");
    if (!majorClass || majorClass.trim() === "") return;
    
    const newId = "SMK_" + Math.floor(Math.random() * 100000);
    localStorage.setItem("student_journey_id", newId);
    localStorage.setItem("student_name", name);
    localStorage.setItem("student_major", majorClass);
    
    document.getElementById("student-name").innerText = `${name} (${majorClass})`;
    switchScreen("welcome-screen", "dashboard-screen");
    
    registerStudentToCloud(newId, name, majorClass);
    renderSkillMap(0, null, []); 
}

function continueJourney() {
    const name = localStorage.getItem("student_name");
    const majorClass = localStorage.getItem("student_major") || "";
    const id = localStorage.getItem("student_journey_id");
    
    document.getElementById("student-name").innerText = majorClass ? `${name} (${majorClass})` : name;
    switchScreen("welcome-screen", "dashboard-screen");
    
    fetchHistory(id);
}

async function registerStudentToCloud(studentId, name, majorClass) {
    const payload = {
        studentId: studentId,
        name: name,
        skill: "Register / Start Journey",
        notes: `Siswa bergabung dari jurusan/kelas: ${majorClass}`
    };

    try {
        if(!API_URL.includes("URL_WEB_APP")) {
            await fetch(API_URL, {
                method: 'POST',
                mode: 'no-cors',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ method: "SUBMIT_QUEST", payload: payload })
            });
        }
    } catch (error) {
        console.error("Gagal simpan registrasi:", error);
    }
}

async function fetchHistory(studentId) {
    const companion = document.getElementById("companion-message");
    companion.innerText = "Sinkronisasi riwayat perjalanan...";
    
    try {
        if(API_URL.includes("URL_WEB_APP")) throw new Error("API belum diset");

        const response = await fetch(`${API_URL}?action=get_journey&studentId=${studentId}`);
        const data = await response.json();
        
        renderSkillMap(data.unlockedLevel, data.teacherReply, data.pendingSkills);
    } catch (error) {
        console.error("Fetch error:", error);
        companion.innerText = "[OFFLINE MODE] Koneksi ke database gagal/belum diatur. Akses level 1 dibuka.";
        renderSkillMap(0, null, []); 
    }
}

function renderSkillMap(unlockedIndex, teacherReply, pendingSkills = []) {
    const companion = document.getElementById("companion-message");
    if (teacherReply) {
        companion.innerText = `Pesan Guru: "${teacherReply}"`;
    } else if (companion.innerText.includes("Sinkronisasi")) {
        companion.innerText = "Sistem siap. Peta perjalananmu telah terbentang.";
    }

    for (let i = 0; i < 8; i++) {
        const btn = document.getElementById(`skill-${i}`);
        
        const skillNameMap = [
            "Learning How to Learn", "Problem Solving", "Communication", 
            "Public Speaking", "Teamwork", "Networking", 
            "Time Management", "Adaptability"
        ];
        const currentSkillTitle = skillNameMap[i];

        btn.classList.remove('locked', 'completed', 'active-quest', 'show-on-map');
        
        const isPending = pendingSkills.includes(currentSkillTitle);

        if (i < unlockedIndex) {
            btn.classList.add('completed');
        } else if (i === unlockedIndex) {
            if (isPending) {
                btn.classList.add('locked');
            } else {
                btn.classList.add('active-quest');
            }
        } else {
            btn.classList.add('locked');
        }

        setTimeout(() => {
            btn.classList.add('show-on-map');
        }, i * 200);
    }
}

function openQuest(skillId, skillName) {
    currentActiveSkillId = skillId;
    currentActiveSkillName = skillName;
    l2lAnalysisResult = ""; 
    
    document.getElementById("modal-title").innerText = skillName;
    document.getElementById("quest-notes").value = "";
    
    const questionnaireArea = document.getElementById("l2l-questionnaire");
    const inputArea = document.getElementById("quest-input-area");
    const resultArea = document.getElementById("l2l-result");
    const instruction = document.getElementById("modal-instruction");

    if (skillId === 0) {
        questionnaireArea.classList.remove("hidden");
        inputArea.classList.add("hidden");
        resultArea.classList.add("hidden");
        resetL2LWizard();
    } else {
        questionnaireArea.classList.add("hidden");
        inputArea.classList.remove("hidden");
        resultArea.classList.add("hidden");
        instruction.innerText = "Tuliskan dokumentasi progres/kendalamu di sini.";
    }

    document.getElementById("quest-modal").classList.remove("hidden");
}

function resetL2LWizard() {
    l2lScores = [];
    for (let i = 1; i <= 10; i++) {
        const stepEl = document.getElementById(`l2l-step-${i}`);
        if (stepEl) {
            if (i === 1) stepEl.classList.remove("hidden");
            else stepEl.classList.add("hidden");
        }
    }
    const indicator = document.getElementById("l2l-step-indicator");
    if(indicator) {
        indicator.classList.remove("hidden");
        indicator.innerText = "Pertanyaan 1 dari 10";
    }
    document.querySelectorAll('.opt-btn').forEach(btn => btn.classList.remove('selected'));
}

function nextL2LStep(currentStep, groupId, score) {
    const selected = document.querySelector(`#${groupId} .opt-btn.selected`);
    if (selected) selected.classList.remove('selected');
    
    event.currentTarget.classList.add('selected');
    l2lScores.push(score);

    setTimeout(() => {
        document.getElementById(`l2l-step-${currentStep}`).classList.add("hidden");
        const nextStep = currentStep + 1;
        const nextEl = document.getElementById(`l2l-step-${nextStep}`);
        if (nextEl) {
            nextEl.classList.remove("hidden");
            document.getElementById("l2l-step-indicator").innerText = `Pertanyaan ${nextStep} dari 10`;
        }
    }, 250);
}

function nextL2LMultiStep(currentStep) {
    const selectedMulti = document.querySelectorAll(`#l2l-step-${currentStep} .opt-btn.selected`);
    if (selectedMulti.length === 0) {
        alert("Pilih setidaknya satu opsi sebelum melanjutkan!");
        return;
    }

    let subScore = 0;
    selectedMulti.forEach(btn => subScore += parseInt(btn.getAttribute('data-score')));
    l2lScores.push(subScore);

    document.getElementById(`l2l-step-${currentStep}`).classList.add("hidden");
    const nextStep = currentStep + 1;
    const nextEl = document.getElementById(`l2l-step-${nextStep}`);
    if (nextEl) {
        nextEl.classList.remove("hidden");
        document.getElementById("l2l-step-indicator").innerText = `Pertanyaan ${nextStep} dari 10`;
    }
}

function finishL2LWizard() {
    const selectedMulti10 = document.querySelectorAll('#l2l-step-10 .opt-btn.selected');
    if (selectedMulti10.length === 0) {
        alert("Pilih setidaknya satu opsi pada pertanyaan terakhir!");
        return;
    }

    let subScore10 = 0;
    selectedMulti10.forEach(btn => subScore10 += parseInt(btn.getAttribute('data-score')));
    l2lScores.push(subScore10);

    let totalRaw = l2lScores.reduce((a, b) => a + b, 0);
    let normalized = (totalRaw / 28.0) * 10;
    if (normalized > 10) normalized = 10;
    if (normalized < 0) normalized = 0;
    
    const finalScore = parseFloat(normalized.toFixed(1));

    document.getElementById("l2l-step-indicator").classList.add("hidden");
    document.getElementById("l2l-questionnaire").classList.add("hidden");
    document.getElementById("quest-input-area").classList.remove("hidden");
    document.getElementById("l2l-result").classList.remove("hidden");

    document.getElementById("l2l-score-text").innerText = finalScore;
    setTimeout(() => {
        document.getElementById("l2l-progress").style.width = (finalScore * 10) + "%";
    }, 100);

    document.getElementById("modal-instruction").innerText = "Analisis selesai. Tuliskan refleksi tambahan belajarmu.";

    l2lAnalysisResult = `[L2L Comprehensive Score: ${finalScore}/10]\n- Evaluasi 10 Tahap Berhasil Dilakukan.\n\nRefleksi Siswa:\n`;
}

function selectMultiple(element) {
    element.classList.toggle('selected');
}

function closeModal() {
    document.getElementById("quest-modal").classList.add("hidden");
}

function openForumModal() {
    window.location.href = 'forum.html';
}

async function submitQuest() {
    const rawNotes = document.getElementById("quest-notes").value;
    if (!rawNotes) {
        alert("Dokumentasi tidak boleh kosong!");
        return;
    }

    const finalNotes = (currentActiveSkillId === 0) ? l2lAnalysisResult + rawNotes : rawNotes;

    const studentId = localStorage.getItem("student_journey_id");
    const name = localStorage.getItem("student_name");
    const majorClass = localStorage.getItem("student_major") || "-";
    
    document.getElementById("companion-message").innerText = `Mengirim laporan ${currentActiveSkillName}...`;
    closeModal();

    const payload = {
        studentId: studentId,
        name: `${name} (${majorClass})`,
        skill: currentActiveSkillName,
        notes: finalNotes
    };

    try {
        if(!API_URL.includes("URL_WEB_APP")) {
            await fetch(API_URL, {
                method: 'POST',
                mode: 'no-cors',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ method: "SUBMIT_QUEST", payload: payload })
            });
        }
        document.getElementById("companion-message").innerText = `Laporan terkirim! Menunggu validasi guru.`;
        setTimeout(() => fetchHistory(studentId), 1500);
    } catch (error) {
        document.getElementById("companion-message").innerText = `Gagal mengirim data.`;
    }
}