import random
from enum import Enum, auto

ABNORMAL_RATE = 0.1

# fmt: off
NL = "%0a" # New line
FS = "%E3%80%80" # Full space
HS = "%20" # Half space
SL = "%2F" # Slash
NORMAL_TEXT = (
    f"にじのとう{NL}"
    f"{FS}🟥🟥{NL}"
    f"{FS}🟧🟧{NL}"
    f"{FS}🟨🟨{NL}"
    f"{FS}🟩🟩{NL}"
    f"{FS}🟦🟦{NL}"
    f"{FS}🟪🟪{NL}"
)
REVERSE_TEXT = (
    f"とうのにじ{NL}"
    f"{FS}🟪🟪{NL}"
    f"{FS}🟦🟦{NL}"
    f"{FS}🟩🟩{NL}"
    f"{FS}🟨🟨{NL}"
    f"{FS}🟧🟧{NL}"
    f"{FS}🟥🟥{NL}"
)
SLEEPING_TEXT = (
    f"...ｽﾔｧ{NL}"
    f"🟥🟧🟨🟩🟦🟪{NL}"
    f"🟥🟧🟨🟩🟦🟪{NL}"
)
DANCING_TEXT = (
    f"にじのとう{NL}"
    f"{FS}{FS}🟥🟥{NL}"
    f"{FS}₍₍⁽⁽🟧🟧{NL}"
    f"{FS}{FS}🟨🟨₎₎⁾⁾{NL}"
    f"{FS}₍₍⁽⁽🟩🟩{NL}"
    f"{FS}{FS}🟦🟦₎₎⁾⁾{NL}"
    f"{FS}{FS}🟪🟪{NL}"
)
TWINS_TEXT = (
    f"にじのとう{NL}"
    f"🟪🟪　🟪🟪{NL}"
    f"👁️👁️　👁️👁️{NL}"
    f"🟩🟩　🟩🟩{NL}"
    f"🟨🟨　🟨🟨{NL}"
    f"🟧🟧　🟧🟧{NL}"
    f"🟥🟥　🟥🟥{NL}"
)
FAT_TEXT = (
    f"にじのとう{NL}"
    f"{FS}🟥🟥🟥{NL}"
    f"{FS}🟧🟧🟧{NL}"
    f"{FS}🟨🟨🟨{NL}"
    f"{FS}🟩🟩🟩{NL}"
    f"{FS}🟦🟦🟦{NL}"
    f"{FS}🟪🟪🟪{NL}"
)
PUSHED_TEXT = (
    f"にじのとう{NL}"
    f"{FS}🟥🟥{NL}"
    f"{FS}🟧🟧{NL}"
    f"{FS}{HS}🟨🟨{NL}"
    f"{FS}👉🟩🟩{NL}"
    f"{FS}{HS}🟦🟦{NL}"
    f"{FS}🟪🟪{NL}"
)
KEBAB_TEXT = (
    f"にじのとう{NL}"
    f"{FS}🟥🟥{NL}"
    f"{FS}🟧🟧{NL}"
    f"{FS}🟨🟨{NL}"
    f"{FS}🟩🟩{NL}"
    f"{FS}🟦🟦{FS}🚛💨{NL}"
    f"{FS}🟪🟪{FS}🥙🥙🥙{NL}"
)
PHOTO_TEXT = (
    f"にじのとう{NL}"
    f"{FS}🟥🟥{NL}"
    f"{FS}🟧🟧{NL}"
    f"{FS}🟨🟨✌️{NL}"
    f"{FS}🟩🟩{NL}"
    f"{FS}🟦🟦{NL}"
    f"{FS}🟪🟪{NL}"
)
MOUSE_TEXT = (
    f"にじのとう{NL}"
    f"{FS}🟥🟥🟥{NL}"
    f"{FS}🟧👁️🟧{NL}"
    f"{FS}👁️🟨👁️{NL}"
    f"{FS}🟩🟩🟩{NL}"
    f"{FS}🟦👄🟦{NL}"
    f"{FS}🟪🟪🟪{NL}"
)
LOVE_TEXT = (
    f"にじのとう{NL}"
    f"{FS}🟥🟥{FS}{FS}{FS}🟥🟥{NL}"
    f"{FS}🟧🟧{FS}{FS}{FS}🟧🟧＜{SL}{SL}{SL}{SL}ｶｧ{NL}"
    f"{FS}🟨🟨❤️{FS}{FS}🟨🟨{NL}"
    f"{FS}🟩🟩💌{FS}{FS}🟩🟩{NL}"
    f"{FS}🟦🟦{FS}{FS}{FS}🟦🟦{NL}"
    f"{FS}🟪🟪{FS}{FS}{FS}🟪🟪{NL}"
)
LOW_TEXT = (
    f"にじのとう{NL}"
    f"{FS}🟧🟧{NL}"
    f"{FS}🟨🟨{NL}"
    f"{FS}🟩🟩{NL}"
    f"{FS}🟦🟦{NL}"
)
TETRIS_TEXT = (
    f"🟦🟦🟥{NL}"
    f"🟦🟥🟥{NL}"
    f"🟦🟥🟧🟩{NL}"
    f"🟨🟨🟧🟩🟩{NL}"
    f"🟨🟨🟧🟧🟩{NL}"
)
# fmt: on


class AbnormalType(Enum):
    SHUFFLE = auto()
    REVERSE = auto()
    PLAIN = auto()
    DANCING = auto()
    SLEEPING = auto()
    WORDLE = auto()
    TWINS = auto()
    FAT = auto()
    PUSHED = auto()
    PARKING = auto()
    PHOTO = auto()
    MOUSE = auto()
    LOVE = auto()
    LOW = auto()
    TETRIS = auto()


def gen_shuffle_text() -> str:
    colors = ["🟥", "🟥", "🟧", "🟧", "🟨", "🟨", "🟩", "🟩", "🟦", "🟦", "🟪", "🟪"]
    random.shuffle(colors)
    return (
        f"にじのとう{NL}"
        f"{FS}{colors[0]}{colors[1]}{NL}"
        f"{FS}{colors[2]}{colors[3]}{NL}"
        f"{FS}{colors[4]}{colors[5]}{NL}"
        f"{FS}{colors[6]}{colors[7]}{NL}"
        f"{FS}{colors[8]}{colors[9]}{NL}"
        f"{FS}{colors[10]}{colors[11]}{NL}"
    )


def gen_plain_text() -> str:
    colors = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫", "⬛", "⬜"]
    c = random.choice(colors)
    return (
        f"むじのとう{NL}"
        f"{FS}{c}{c}{NL}"
        f"{FS}{c}{c}{NL}"
        f"{FS}{c}{c}{NL}"
        f"{FS}{c}{c}{NL}"
        f"{FS}{c}{c}{NL}"
        f"{FS}{c}{c}{NL}"
    )


def gen_wordle_text() -> str:
    """
    Wordle 風のテキストを生成する
    """

    def next_color(color: int) -> int:
        """
        - 1/4で1増える
        - 1/16で2増える
        - 1/8で1減る
        - 1/32で2減る
        """
        r = random.random()
        if r < 1.0 / 4:
            return min(color + 1, 2)
        elif r < 1.0 / 4 + 1.0 / 16:
            return min(color + 2, 2)
        elif r < 1.0 / 4 + 1.0 / 16 + 1.0 / 8:
            return max(color - 1, 0)
        elif r < 1.0 / 4 + 1.0 / 16 + 1.0 / 8 + 1.0 / 32:
            return max(color - 2, 0)
        else:
            return color

    text = ""
    # 0 (black)
    # 1 (yellow)
    # 2 (green)
    line = [0, 0, 0, 0, 0]
    for i in range(6):
        for j in range(5):
            line[j] = next_color(line[j])
            text += ["⬛", "🟨", "🟩"][line[j]]

        text += NL
        if line == [2, 2, 2, 2, 2]:
            break
    text = f"{i+1}/6{NL}" + text
    return text


def gen_random_text(abnormal_rate: int = ABNORMAL_RATE) -> str:
    if random.random() > abnormal_rate:
        return NORMAL_TEXT
    else:
        match random.choice(list(AbnormalType)):
            case AbnormalType.SHUFFLE:
                return gen_shuffle_text()
            case AbnormalType.REVERSE:
                return REVERSE_TEXT
            case AbnormalType.PLAIN:
                return gen_plain_text()
            case AbnormalType.DANCING:
                return DANCING_TEXT
            case AbnormalType.SLEEPING:
                return SLEEPING_TEXT
            case AbnormalType.WORDLE:
                return gen_wordle_text()
            case AbnormalType.TWINS:
                return TWINS_TEXT
            case AbnormalType.FAT:
                return FAT_TEXT
            case AbnormalType.PUSHED:
                return PUSHED_TEXT
            case AbnormalType.PARKING:
                return KEBAB_TEXT
            case AbnormalType.PHOTO:
                return PHOTO_TEXT
            case AbnormalType.MOUSE:
                return MOUSE_TEXT
            case AbnormalType.LOVE:
                return LOVE_TEXT
            case AbnormalType.LOW:
                return LOW_TEXT
            case AbnormalType.TETRIS:
                return TETRIS_TEXT


if __name__ == "__main__":
    X_POST_URL = "https://twitter.com/intent/tweet?text={text}"
    # 動作確認

    for _ in range(20):
        print(gen_random_text(abnormal_rate=0.9))
        print()

    print(NORMAL_TEXT)
    print(X_POST_URL.format(text=NORMAL_TEXT))
