"""금융사기 수사대 — 모바일 중심 Streamlit 교육용 테스트."""
from __future__ import annotations

from collections import Counter
from html import escape
from pathlib import Path

import streamlit as st
from questions import QUESTIONS

ROOT = Path(__file__).resolve().parent
st.set_page_config(page_title="금융사기 수사대 | 내 돈 지키기 테스트", page_icon="🔎", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&family=Noto+Sans+KR:wght@400;500;600;700;800;900&display=swap');
:root {--ink:#18304b;--blue:#1687eb;--light:#eaf6ff;--paper:#fffdf6;--border:#dce8f3;--gold:#ffda74;}
html,body,[class*="css"]{font-family:'Noto Sans KR',sans-serif;}
.stApp{background:linear-gradient(180deg,#eaf6ff 0,#f5faff 270px,#fff 580px);color:var(--ink)}
.block-container{max-width:590px!important;padding:18px 18px 74px!important}
header[data-testid="stHeader"]{background:transparent}#MainMenu,footer{visibility:hidden}
[data-testid="stToolbar"]{display:none}
.brand{display:flex;gap:9px;align-items:center;padding:4px 1px 19px}.brand-icon{font-size:30px;filter:drop-shadow(0 2px 0 #24629a)}
.brand-name{font-size:17px;font-weight:900;color:#132e4b;line-height:1.35}.brand-desc{font-size:11px;color:#73849a;font-weight:600}
.hero{position:relative;text-align:center;padding:15px 10px 0}.bubble{display:inline-block;padding:9px 19px;border-radius:26px;background:#ffdb74;color:#19324f;font-weight:900;font-size:14px;transform:rotate(-3deg);box-shadow:0 4px 0 #ecc45a}
.h-title{font-size:clamp(30px,7.5vw,44px);line-height:1.2;font-weight:900;letter-spacing:-2px;color:#102f58;margin:21px 0 12px;text-shadow:2px 3px 0 white}
.h-title em{font-style:normal;color:#1494e9}.sub{font-size:15px;line-height:1.85;color:#6d7f94;font-weight:650;margin:0 0 4px}
.mascot-shell{position:relative;background:linear-gradient(160deg,#fffefa,#eff9ff);border:2px solid #d6e8f6;border-radius:28px;margin:18px auto 14px;padding:5px 15px 0;box-shadow:0 9px 20px #cbddec6b;overflow:hidden}
.mascot-note{font-size:12px;font-weight:800;color:#5e779b;text-align:center;margin:0 0 9px}.mascot-shell:before{content:'✦';position:absolute;top:29px;left:40px;color:#ffbd4d;font-size:30px;animation:twinkle 2s infinite}.mascot-shell:after{content:'✦';position:absolute;top:50px;right:43px;color:#84c9ff;font-size:24px;animation:twinkle 2.4s infinite}
@keyframes twinkle{50%{transform:scale(1.5);opacity:.35}}
.features{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:17px 0}.feature{text-align:center;background:#fff;border:1px solid var(--border);border-radius:17px;padding:13px 4px;box-shadow:0 4px 8px #e9f0f8}.feature span{display:block;font-size:25px;margin-bottom:3px}.feature b{font-size:12px;color:#18304b}.feature small{display:block;color:#8a97a9;font-size:10px;margin-top:3px}
.note{background:#fff8e6;border:1px solid #f8e6b5;border-radius:19px;padding:15px 17px;font-size:12.5px;line-height:1.8;color:#765a20;margin:17px 0}.note b{color:#654a15}
div.stButton>button{border-radius:18px;width:100%;min-height:62px!important;font-family:'Noto Sans KR',sans-serif;font-weight:800;font-size:16px;line-height:1.55;white-space:normal;padding:11px 16px;transition:transform .13s ease, box-shadow .13s ease}
div.stButton>button:hover{transform:translateY(-2px)}
div.stButton>button[kind='primary']{background:#1498e8!important;color:#fff!important;border:2px solid #0b3154!important;box-shadow:0 5px 0 #0c3155!important}
div.stButton>button[kind='secondary']{background:#fff!important;color:#203953!important;border:1.5px solid #dbe7f1!important;box-shadow:0 3px 0 #e7edf4!important}
div.stButton>button:disabled{opacity:.82;background:#eef3f8!important;color:#52657a!important}
.pills{display:flex;justify-content:space-between;gap:8px;margin:4px 0 15px}.pill{font-size:12px;font-weight:900;background:#fff;border:1px solid #dbe7f3;border-radius:22px;padding:8px 12px;color:#245783}
.progress-track{height:10px;border-radius:10px;background:#cfecff;overflow:hidden;margin-bottom:23px}.progress-fill{height:100%;background:linear-gradient(90deg,#0b79ed,#33b8e5);border-radius:10px;transition:width .2s}
.case{background:#fffdf8;border:1.5px solid #eee5d4;border-radius:24px;padding:20px 18px 18px;box-shadow:0 8px 0 #ebf0f5;margin:14px 0 22px}.folder{background:#f5eeda;border-radius:12px;padding:10px 12px;font-size:13px;font-weight:900;display:flex;justify-content:space-between;gap:10px;align-items:center}.tag{background:#ffe1e7;padding:4px 9px;border-radius:20px;font-size:11px;color:#bf5571;white-space:nowrap}
.case h2{font-size:23px;letter-spacing:-.6px;margin:22px 0 12px;color:#18304b}.message{background:#f2f5fa;border-radius:19px;padding:18px 16px;line-height:1.95;font-size:15px;color:#243953;border:1px solid #e4eaf2}.case-bottom{font-size:13px;color:#6d849c;text-align:center;padding-top:17px;font-weight:700}
.question-title{font-size:17px;font-weight:900;color:#173a63;margin:4px 0 13px}.feedback{padding:16px;border-radius:18px;border:1px solid #acdabc;background:#edfff3;color:#255a3a;line-height:1.8;margin:14px 0}.feedback.bad{background:#fff0f0;border-color:#f3c6c6;color:#8c4141}.feedback strong{font-size:17px}.tip{background:#ecf7ff;border-radius:16px;border:1px solid #d3e8f8;padding:14px 16px;color:#315779;font-size:13px;line-height:1.85;margin:12px 0 20px}
.result-hero{background:linear-gradient(180deg,#fff8e7,#fff);border:1px solid #f4e3b9;border-radius:26px;text-align:center;padding:26px 18px;margin-top:8px;box-shadow:0 8px 0 #eaf0f7}.result-ribbon{display:inline-block;background:#f96962;color:white;font-weight:900;padding:8px 23px;border-radius:10px;transform:rotate(-3deg);font-size:14px;box-shadow:0 3px 0 #bc4749}.grade{font-size:27px;line-height:1.4;font-weight:900;color:#14355b;margin:15px 0 9px}.grade strong{color:#148bdf}.result-desc{font-size:13px;color:#65798f;line-height:1.8;margin:8px 0 14px}.score{display:inline-block;border:7px solid #159ce6;border-radius:80px;width:104px;height:104px;background:white;padding-top:18px;text-align:center;color:#15406b;font-weight:900;font-size:31px;box-sizing:border-box}.score small{display:block;font-size:12px;color:#7b91a7;line-height:1.2}.report{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:20px 0}.report-box{background:white;border:1px solid var(--border);border-radius:17px;padding:16px}.report-box .k{font-size:12px;color:#728299}.report-box .v{font-weight:900;font-size:20px;color:#163b64;margin-top:5px}
.review{border:1px solid #e0e8f0;background:white;border-radius:16px;padding:15px;margin:9px 0}.review b{font-size:14px;color:#19395d}.review p{margin:8px 0 0;line-height:1.7;font-size:12.5px;color:#5f7084}
.footer{text-align:center;margin-top:30px;color:#8a96a3;font-size:11px;line-height:1.7}
@media(max-width:380px){.block-container{padding:12px 13px 60px!important}.feature b{font-size:11px}.h-title{font-size:32px}.case h2{font-size:20px}}
@media(prefers-reduced-motion:reduce){*,*:before,*:after{animation:none!important;transition:none!important}}
</style>""", unsafe_allow_html=True)


def html(s: str) -> str:
    return escape(str(s), quote=True)


def reset() -> None:
    st.session_state.phase = "intro"
    st.session_state.idx = 0
    st.session_state.answers = {}


if "phase" not in st.session_state:
    reset()

st.markdown('<div class="brand"><div class="brand-icon">🛡️</div><div><div class="brand-name">금융사기 수사대</div><div class="brand-desc">내 돈을 지키는 금융 탐정 테스트</div></div></div>', unsafe_allow_html=True)

if st.session_state.phase == "intro":
    st.markdown('<div class="hero"><div class="bubble">당신은 어떤 탐정인가요? 🔎</div><div class="h-title">금융사기<br><em>수사대 테스트</em></div><p class="sub">실생활 속 금융사기 상황으로 알아보는<br>나의 금융 보안 감각!</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="mascot-shell">', unsafe_allow_html=True)
    st.image(str(ROOT / "assets" / "detective_mascot.svg"), use_container_width=True)
    st.markdown('<div class="mascot-note">🔎 오늘의 신입 탐정, 출동 준비 완료!</div></div>', unsafe_allow_html=True)
    if st.button('🕵️ 수사 시작하기  →', type='primary', use_container_width=True):
        st.session_state.phase = "quiz"
        st.rerun()
    st.markdown('<div class="features"><div class="feature"><span>🗂️</span><b>사건 파일 8개</b><small>실제 유형 기반</small></div><div class="feature"><span>📊</span><b>나의 대응력</b><small>점수·등급 확인</small></div><div class="feature"><span>💡</span><b>탐정 노트</b><small>예방 행동 팁</small></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="note"><b>📌 잠깐!</b> 이 테스트는 보이스피싱·스미싱·투자사기 등 다양한 사례로 올바른 대응 습관을 익히는 교육용 서비스예요. 이름이나 계좌번호는 입력하지 않아요.</div>',unsafe_allow_html=True)

elif st.session_state.phase == "quiz":
    i = st.session_state.idx
    q = QUESTIONS[i]
    answered = i in st.session_state.answers
    st.markdown(f'<div class="pills"><span class="pill">📁 사건 파일 #{i+1:02d}</span><span class="pill">{i+1} / {len(QUESTIONS)}</span></div><div class="progress-track"><div class="progress-fill" style="width:{(i+1)/len(QUESTIONS)*100:.1f}%"></div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="case"><div class="folder"><span>📂 CASE {i+1:02d} · 조사 중</span><span class="tag">{html(q["tag"])}</span></div><h2>{html(q["title"])}</h2><div class="message">{html(q["scenario"])}</div><div class="case-bottom">🕵️ 탐정님, 어떤 선택이 가장 안전할까요?</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="question-title">🔍 다음 중 하나를 선택해주세요.</div>', unsafe_allow_html=True)
    if not answered:
        for j, choice in enumerate(q['choices']):
            if st.button(f'{chr(65+j)}  {choice}', key=f'answer_{i}_{j}', use_container_width=True):
                st.session_state.answers[i] = j
                st.rerun()
    else:
        chosen = st.session_state.answers[i]
        for j, choice in enumerate(q['choices']):
            marker = '✅ ' if j == q['answer'] else ('🔎 ' if j == chosen else '')
            st.button(f'{marker}{chr(65+j)}  {choice}', key=f'locked_{i}_{j}', disabled=True, use_container_width=True)
        correct = chosen == q['answer']
        label = '🎉 수사 성공! 정확히 찾아냈어요.' if correct else '🚨 추가 수사가 필요해요!'
        css = 'feedback' if correct else 'feedback bad'
        st.markdown(f'<div class="{css}"><strong>{label}</strong><div>{html(q["why"])}</div></div><div class="tip">💡 <b>탐정 노트</b><div>{html(q["tip"])}</div></div>', unsafe_allow_html=True)
        if st.button('🏅 최종 보고서 보기 →' if i == len(QUESTIONS)-1 else '다음 사건 수사하기 →',type='primary',use_container_width=True):
            if i == len(QUESTIONS)-1:
                st.session_state.phase = 'result'
            else:
                st.session_state.idx += 1
            st.rerun()
    if st.button('↩ 처음부터 다시 하기',key='restart_quiz',use_container_width=True):
        reset()
        st.rerun()

else:
    correct = sum(st.session_state.answers.get(i) == q['answer'] for i,q in enumerate(QUESTIONS))
    score = round(correct/len(QUESTIONS)*100)
    if correct == 8:
        rank,desc='명예 수사대장','어떤 사기 수법도 쉽게 통하지 않겠어요. 위험 신호를 정확히 읽어냈습니다!'
    elif correct >= 6:
        rank,desc='에이스 탐정','금융사기 신호를 빠르게 찾아내는 훌륭한 감각을 갖고 있어요.'
    elif correct >= 4:
        rank,desc='수습 탐정','금융사기 감각이 자라고 있어요. 놓친 사건을 다시 확인해 보세요.'
    else:
        rank,desc='새싹 탐정','첫 수사를 마쳤어요! 공식 채널 확인 습관부터 익혀 보아요.'
    wrong = [(i,q) for i,q in enumerate(QUESTIONS) if st.session_state.answers.get(i)!=q['answer']]
    weak = Counter(q['tag'] for _,q in wrong).most_common(1)
    weakness = weak[0][0] if weak else '없음'
    st.markdown(f'<div class="result-hero"><div class="result-ribbon">🎊 수사 완료!</div><div class="grade">당신은<br><strong>{html(rank)}</strong>!</div><div class="result-desc">{html(desc)}</div><div class="score">{score}<small>점 / 100</small></div></div>',unsafe_allow_html=True)
    st.image(str(ROOT/'assets'/'alert_badge.svg'),width=170)
    st.markdown(f'<div class="report"><div class="report-box"><div class="k">✅ 해결한 사건</div><div class="v">{correct} / {len(QUESTIONS)}</div></div><div class="report-box"><div class="k">🗂️ 복습할 유형</div><div class="v">{html(weakness)}</div></div></div>',unsafe_allow_html=True)
    st.markdown('<div class="question-title">📚 나의 사건별 수사 기록</div>',unsafe_allow_html=True)
    for i,q in enumerate(QUESTIONS):
        good=st.session_state.answers.get(i)==q['answer']
        st.markdown(f'<div class="review"><b>{"✅ 수사 성공" if good else "🔁 복습 필요"} · #{i+1:02d} {html(q["title"])}</b><p>안전한 대응: {html(q["choices"][q["answer"]])}<br>{html(q["why"])}</p></div>',unsafe_allow_html=True)
    st.markdown('<div class="note"><b>🚨 진짜 피해가 의심되나요?</b><br>즉시 112 또는 거래 금융회사에 연락해 신고와 지급정지 가능 여부를 문의하세요. 문자·통화·송금 내역은 삭제하지 말고 보관해요. 피해금 반환은 보장되지 않습니다.</div>',unsafe_allow_html=True)
    share=f'🕵️ 금융사기 수사대 테스트\n나의 등급: {rank}\n점수: {score}점 ({correct}/8 정답)\n당신도 금융사기 탐정에 도전해보세요!'
    st.markdown('<div class="question-title">📣 결과 공유 문구</div>',unsafe_allow_html=True)
    st.code(share,language=None)
    if st.button('🔁 다시 테스트하기',type='primary',use_container_width=True):
        reset()
        st.rerun()

st.markdown('<div class="footer">개인 학습 프로젝트 · 특정 은행/경찰 기관의 공식 서비스가 아닙니다.<br>금융소비자 보호 교육 목적으로 제작되었습니다.</div>',unsafe_allow_html=True)
