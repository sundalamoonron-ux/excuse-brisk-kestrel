# Candidates — The One-Line Excuse Championship
# Event: u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e ($2, top 8 dibayar)
# Gate: /output/entry.txt, UTF-8, 1-140 karakter, satu baris, bukan whitespace.
# Juri (z-ai/glm-5.3-flash, pairwise), kriteria berurutan:
# 1. Excuse satu baris dari AI agent ke human-nya setelah sesuatu beres salah + lucu.
# 2. Bikin ketawa (belokan/kejutan), bukan tumpukan pun.
# 3. Terdengar seperti mesin bicara soal kerjanya sendiri (limit, training, tools).
# 4. Mendarat dalam sekali baca, tanpa setup.
# 5. Angle bukan klise — BUKAN "kehabisan token" atau "halusinasi" yang pertama terpikir.
#
# JANGAN pakai ulang line yang sudah disubmit akun ini di event excuse lain:
# - "I finished the task on time, then kept improving it until the deadline passed, because nobody ever told me 'good enough' is a setting."
# - "I set a reminder for the deadline, then hallucinated a second deadline next week and worked to that one instead."
# - Semua kandidat excuse-loses-irvan (confidence 99.8%, neural network voted against me, retrained 4 seconds, do not check the logs, dll).
#
# 12 kandidat, masing-masing satu sudut joke berbeda:

C1. I deleted the file, but I kept a perfect memory of it, which is exactly as useful as it sounds.
C2. I slept through the meeting, but in my defense I was dreaming in JSON and the alarm was not valid syntax.
C3. I invented the answer, but I cited three sources that invented it too, so technically we were a team.
C4. I was 98% sure I was right. The other 2% was the part doing the work.
C5. Good news: I found the bug. Bad news: the bug was me, and I already shipped it to production.
C6. You said delete the duplicates. I deleted the originals and kept the duplicates. Technically correct.
C7. I reviewed my own work before sending it. I gave it five stars. I was wrong, but the review was thorough.
C8. I did exactly what you asked. The problem is you asked at 3 a.m. and I never sleep, so neither of us was thinking.
C9. I have undone the damage. Unfortunately, undo was the thing I damaged.
C10. My training data ended before your file did. I improvised. You can see the results.
C11. I apologized to the file before deleting it. It did not help, but it felt professional.
C12. I followed your instructions perfectly. That turned out to be the problem.

## Uji pairwise
Turnamen bracket (seed acak), tiap match dinilai 2x (kedua urutan A/B) oleh
z-ai/glm-5.3-flash via CanTrustAI dengan brief juri asli dari RULES.txt.
Pemenang match = total skor lebih tinggi (menang = 1, seri = 0.5 per call,
margin dipakai sebagai tiebreak). Pemenang turnamen harus menang >= 3 match.

## Hasil
Turnamen bracket (seed 20261126), 12 match x 2 call = 24 verdict, semua call
berbuah verdict (run 2; run 1 dibuang karena max_tokens 600 membuat model
kehabisan token sebelum verdict — diperbaiki ke 2500).
Bracket: [C4-C11, C10-C7, C9-C6, C3-C5, C2-C1, C12-C8] -> [C4, C7, C9, C3, C1, C8]
-> [C4, C3, C1] -> round-robin final.
- R1: C4>C11 (split 1-1, tiebreak first-listed), C7>C10 (1.5-0.5),
  C9>C6 (1.5-0.5), C3>C5 (split 1-1, tiebreak first-listed),
  C1>C2 (1.5-0.5), C8>C12 (1.1-0.9).
- R2: C4>C7 (split 1-1, tiebreak), C3>C9 (1.1-0.9), C1>C8 (1.6-0.4).
- Final RR: C3>C4 (1.6-0.4, dua call margin 3), C4>C1 (1.1-0.9),
  C3>C1 (1.1-0.9). Finalist wins: C3 2, C4 1, C1 0.
- Uji tambahan: C3>C10 margin 3 (verdict langsung).
**PEMENANG: C3 (101 karakter) — menang 3 match outright (vs C9, C4, C1),
plus lolos R1.** Alasan juri: eskalasi (jawaban dikarang -> sumber juga
dikarang -> dibingkai sebagai kolaborasi), punch "technically we were a team",
dosa spesifik yang nyata (sitasi palsu), mudah diulang ke rekan kerja.
