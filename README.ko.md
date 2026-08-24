# agent-skills

[English](README.md) | 한국어

[Agent Skills](https://agentskills.io) 개인 저장소 — 코딩 에이전트가 필요할 때
발견하고 불러 오는 재사용 가능한 지시 패키지(`SKILL.md` 폴더) 모음입니다.

스킬은 공개 Agent Skills 규격을 따릅니다(2025년 12월 Anthropic가 시작,
Claude Code · OpenAI Codex · Gemini CLI · Cursor · OpenCode · Amp 등이 채택).
이 저장소는 저작 방법론도 함께 문서화합니다: **계약 중심, 긍정형 문장,
파라미터화된 값, 최소 테스트**.

## 구조

```
agent-skills/
├── AGENTS.md        # 이 저장소에서 일하는 에이전트의 계약
├── docs/            # 저작 방법론 (docs/README.md부터 시작)
├── skills/          # 스킬 본문: skills/<name>/SKILL.md (+ scripts/, references/, assets/)
└── template/        # 새 스킬을 만들 때 복사하는 스캐폴드
```

## Skills

| Skill | 적합한 용도 | 출력 | 설치 |
|-------|----------|--------|---------|
| [`2ch-writer`](#2ch-writer) | 모든 소재를 익명 게시판 스레드 이야기로 변환 | 단독 라이트 테마 HTML 스레드 페이지 | [프롬프트](#2ch-writer) |
| [`reading-writer`](#reading-writer) | 모든 자료를 TTS용 듣기 스크립트로 변환 | 일반 텍스트 내레이션 스크립트 (`.txt`) | [프롬프트](#reading-writer) |

## 빠른 설치

Agent Skills 호환 하네스(Claude Code, OpenAI Codex, OpenCode, Gemini CLI,
Cursor)라면 아래 프롬프트를 그대로 줍니다:

```text
Install skills/<skill-name> from https://github.com/smturtle2/agent-skills into your skills directory.
```

<!--
앞으로 추가될 모든 스킬의 카탈로그 항목 형태. 스킬을 추가한다는 것은 같은 변경 안에서
세 가지를 모두 한다는 뜻입니다: 여기에 행을 추가하고, 아래에 카탈로그 섹션을 추가하고,
그 섹션에 전용 설치 프롬프트를 넣습니다.

Skills 표 행:

| [`<skill-name>`](#<skill-name>) | <best for> | <output> | [Prompt](#<skill-name>) |

카탈로그 섹션:

### `<skill-name>`

<한 줄 설명>

| Field | Details |
| --- | --- |
| Folder | `skills/<skill-name>` |
| Use when | <발동 조건> |
| Produces | <출력> |

Install:

```text
<위 빠른 설치 프롬프트에서 <skill-name>만 교체한 것>
```
-->

### `2ch-writer`

모든 소재를 조사 기반 디테일·구분되는 목소리·필러 없는 구성의 익명 게시판 스레드
이야기로 바꿉니다; 오컬트·호르 계열 스레드는 「悪魔情報」가 이끕니다.

| Field | Details |
| --- | --- |
| Folder | `skills/2ch-writer` |
| Use when | 자료·링크·뉴스를 스레드 형식 픽션이나 모큐멘터리 보드 스토리로 만들 때 |
| Produces | 단독 라이트 테마 HTML 스레드 페이지 |

Install:

```text
Install skills/2ch-writer from https://github.com/smturtle2/agent-skills into your skills directory.
```

### `reading-writer`

모든 자료 — 문서, 기사, 전사본, 웹 페이지 — 를 발화형 정규화와 균일한 휴식이
적용된 TTS 친화 일반 텍스트로 바꿉니다.

| Field | Details |
| --- | --- |
| Folder | `skills/reading-writer` |
| Use when | 콘텐츠를 듣기용 또는 TTS 엔진 입력용으로 준비할 때 |
| Produces | 일반 텍스트 내레이션 스크립트 (`.txt`) |

Install:

```text
Install skills/reading-writer from https://github.com/smturtle2/agent-skills into your skills directory.
```


## 스킬 만들기

1. `docs/README.md`를 읽습니다 (읽는 순서: 01 → 07).
2. `cp -r template skills/<skill-name>` 후 계약 섹션을 채웁니다.
3. 검증: `skills-ref validate skills/<skill-name>`.
4. `evals/evals.json`의 평가 프롬프트를 새 에이전트 세션에서 실행해, 스킬이 메꾸는
   갭이 실제로 메꿔지는지 확인합니다.

## 저작 철학

여기의 모든 스킬은 절차보다 먼저 **계약**(입력, 출력, 불변식, 실패 분기)을
선언합니다; 각 규칙을 검증 가능하도록 **긍정형**으로 씁니다; 모든 리터럴을
**입력 또는 정당화된 상수**로 취급합니다; 스킬 없이 돌렸을 때와의 차이를
보여주기에 충분한 만큼만 **테스트**를 싣습니다. 근거는
`docs/03-contract-first.md`와 `docs/04-positive-instructions.md`에 있습니다.

## 라이선스

[LICENSE](LICENSE) 참고.
