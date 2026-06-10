#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏯 历史小达人 — 初中历史互动学习游戏
一款鼓励式学习的问答游戏，涵盖中国古代史、近代史和世界史。
"""

import random
import sys
import time
from typing import List, Dict, Optional

# ────────────────────────────── 题库 ──────────────────────────────

QUESTIONS: List[Dict] = [
    # ======= 中国古代史 =======
    {
        "id": 1,
        "question": "中国历史上第一个统一的中央集权封建国家是？",
        "options": ["夏朝", "商朝", "秦朝", "汉朝"],
        "answer": 2,
        "hint": "想想\"书同文，车同轨\"是哪位皇帝做到的",
        "era": "中国古代史",
        "explanation": "公元前221年，秦始皇灭六国，建立了中国历史上第一个统一的中央集权的封建国家——秦朝。"
    },
    {
        "id": 2,
        "question": "\"丝绸之路\"的开辟者是谁？",
        "options": ["郑和", "张骞", "班超", "玄奘"],
        "answer": 1,
        "hint": "他是汉武帝时期出使西域的使者",
        "era": "中国古代史",
        "explanation": "公元前138年和前119年，张骞两次出使西域，开辟了连接中国与中亚、西亚乃至欧洲的\"丝绸之路\"。"
    },
    {
        "id": 3,
        "question": "被称为\"贞观之治\"的是哪位皇帝统治时期？",
        "options": ["唐高祖李渊", "唐太宗李世民", "唐玄宗李隆基", "武则天"],
        "answer": 1,
        "hint": "这位皇帝以\"以铜为镜，可以正衣冠\"的名言著称",
        "era": "中国古代史",
        "explanation": "唐太宗李世民在位期间（627-649年），政治清明、经济发展、社会安定，史称\"贞观之治\"。"
    },
    {
        "id": 4,
        "question": "造纸术的改进者是谁？",
        "options": ["蔡伦", "毕昇", "沈括", "张衡"],
        "answer": 0,
        "hint": "东汉时期的一位宦官",
        "era": "中国古代史",
        "explanation": "东汉蔡伦改进了造纸术，用树皮、麻头、破布等原料造出了轻便廉价的纸张，极大地促进了文化的传播。"
    },
    {
        "id": 5,
        "question": "\"三国鼎立\"的局面最终确立的标志是？",
        "options": ["官渡之战", "赤壁之战", "夷陵之战", "淝水之战"],
        "answer": 1,
        "hint": "这场战役以少胜多，奠定了三分天下的基础",
        "era": "中国古代史",
        "explanation": "208年的赤壁之战，孙刘联军以少胜多击败曹操，奠定了三国鼎立的基础。此后魏、蜀、吴三国并立。"
    },
    {
        "id": 6,
        "question": "唐朝时期，日本派遣到中国学习的使团被称为？",
        "options": ["遣唐使", "遣隋使", "贡使", "留学生"],
        "answer": 0,
        "hint": "名字里就带有\"唐朝\"二字",
        "era": "中国古代史",
        "explanation": "唐朝时期，日本多次派遣\"遣唐使\"来中国学习先进的政治制度、文化和技术，对日本社会的发展产生了深远影响。"
    },
    {
        "id": 7,
        "question": "活字印刷术的发明者是？",
        "options": ["蔡伦", "毕昇", "沈括", "黄道婆"],
        "answer": 1,
        "hint": "北宋时期的一位平民发明家",
        "era": "中国古代史",
        "explanation": "北宋庆历年间（1041-1048年），平民毕昇发明了活字印刷术，比欧洲早了约400年，极大地促进了文化的传播与交流。"
    },
    {
        "id": 8,
        "question": "郑和下西洋最远到达了哪里？",
        "options": ["印度", "阿拉伯半岛", "非洲东海岸", "欧洲"],
        "answer": 2,
        "hint": "比印度和阿拉伯还要远！",
        "era": "中国古代史",
        "explanation": "明朝郑和七次下西洋，最远到达了非洲东海岸和红海沿岸，是世界航海史上的壮举，比哥伦布发现美洲早了近一个世纪。"
    },
    # ======= 中国近代史 =======
    {
        "id": 9,
        "question": "中国近代史上第一个不平等条约是？",
        "options": ["《北京条约》", "《南京条约》", "《马关条约》", "《辛丑条约》"],
        "answer": 1,
        "hint": "鸦片战争后签订的",
        "era": "中国近代史",
        "explanation": "1842年，清政府在鸦片战争中战败，被迫与英国签订了《南京条约》，这是中国近代史上第一个不平等条约，标志着中国开始沦为半殖民地半封建社会。"
    },
    {
        "id": 10,
        "question": "辛亥革命爆发于哪一年？",
        "options": ["1898年", "1911年", "1919年", "1921年"],
        "answer": 1,
        "hint": "这一年和数字\"11\"关系密切",
        "era": "中国近代史",
        "explanation": "1911年10月10日，武昌起义爆发，辛亥革命推翻了清王朝统治，结束了两千多年的封建帝制，建立了中华民国。"
    },
    {
        "id": 11,
        "question": "\"五四运动\"爆发的直接导火索是什么？",
        "options": ["北洋军阀统治", "巴黎和会外交失败", "新文化运动", "马克思主义传播"],
        "answer": 1,
        "hint": "和第一次世界大战后的国际会议有关",
        "era": "中国近代史",
        "explanation": "1919年巴黎和会上，中国要求收回山东主权的正当要求遭到拒绝，引发了五四爱国运动，标志着中国新民主主义革命的开端。"
    },
    {
        "id": 12,
        "question": "中国共产党的成立时间是？",
        "options": ["1919年", "1921年", "1927年", "1949年"],
        "answer": 1,
        "hint": "\"南湖红船\"的故事说的就是这件事",
        "era": "中国近代史",
        "explanation": "1921年7月23日，中国共产党第一次全国代表大会在上海召开（后转移到浙江嘉兴南湖的游船上），标志着中国共产党的诞生。"
    },
    # ======= 世界史 =======
    {
        "id": 13,
        "question": "世界上最早的成文法典是？",
        "options": ["《汉谟拉比法典》", "《十二铜表法》", "《拿破仑法典》", "《罗马法》"],
        "answer": 0,
        "hint": "它来自两河流域的古巴比伦王国",
        "era": "世界史",
        "explanation": "公元前18世纪，古巴比伦国王汉谟拉比颁布了《汉谟拉比法典》，这是世界上已知最早的较为完备的成文法典。"
    },
    {
        "id": 14,
        "question": "文艺复兴运动最早兴起于哪个国家？",
        "options": ["英国", "法国", "意大利", "西班牙"],
        "answer": 2,
        "hint": "达·芬奇和米开朗基罗都是这里人",
        "era": "世界史",
        "explanation": "14世纪，文艺复兴运动最早兴起于意大利，以复兴古希腊、古罗马文化为旗帜，倡导人文主义精神，涌现了但丁、达·芬奇、米开朗基罗等巨匠。"
    },
    {
        "id": 15,
        "question": "第一次工业革命最早发生在哪个国家？",
        "options": ["美国", "法国", "德国", "英国"],
        "answer": 3,
        "hint": "瓦特改良蒸汽机的国家",
        "era": "世界史",
        "explanation": "18世纪60年代，第一次工业革命最早发生在英国，以蒸汽机的广泛使用为主要标志，推动了人类从手工工场向机器大生产的转变。"
    },
    {
        "id": 16,
        "question": "世界上第一个社会主义国家是？",
        "options": ["中国", "苏联", "古巴", "越南"],
        "answer": 1,
        "hint": "1917年十月革命建立的",
        "era": "世界史",
        "explanation": "1917年俄国十月革命胜利后，建立了世界上第一个社会主义国家——苏维埃俄国（后发展为苏联），开辟了人类历史的新纪元。"
    },
    {
        "id": 17,
        "question": "第二次世界大战的转折点是哪场战役？",
        "options": ["诺曼底登陆", "斯大林格勒战役", "珍珠港事件", "柏林战役"],
        "answer": 1,
        "hint": "这场战役发生在苏联，极其惨烈",
        "era": "世界史",
        "explanation": "1942-1943年的斯大林格勒战役是第二次世界大战的重要转折点，德军在此遭遇重大失败，此后苏军转入战略反攻。"
    },
    {
        "id": 18,
        "question": "发现\"新大陆\"（美洲）的航海家是谁？",
        "options": ["达·伽马", "麦哲伦", "哥伦布", "迪亚士"],
        "answer": 2,
        "hint": "他向西航行，以为到了印度",
        "era": "世界史",
        "explanation": "1492年，意大利航海家哥伦布在西班牙王室支持下向西航行，意外发现了美洲大陆（当时他误认为是印度），拉开了地理大发现的序幕。"
    },
    {
        "id": 19,
        "question": "古代世界七大奇迹之一，目前唯一尚存的是？",
        "options": ["空中花园", "亚历山大灯塔", "埃及金字塔", "宙斯神像"],
        "answer": 2,
        "hint": "它在埃及，非常有名",
        "era": "世界史",
        "explanation": "埃及金字塔（尤其是胡夫金字塔）是古代世界七大奇迹中唯一保存至今的建筑，是古埃及文明的象征。"
    },
    {
        "id": 20,
        "question": "提出\"相对论\"的科学家是？",
        "options": ["牛顿", "达尔文", "爱因斯坦", "伽利略"],
        "answer": 2,
        "hint": "他是20世纪最伟大的科学家之一，吐舌头的照片很有名",
        "era": "世界史",
        "explanation": "20世纪初，爱因斯坦提出了狭义相对论和广义相对论，彻底改变了人类对时间、空间和引力的认识，是现代物理学的基石。"
    },
]

# ────────────────────────────── 鼓励语库 ──────────────────────────────

ENCOURAGE_CORRECT = [
    "🎉 太棒了！回答完全正确！",
    "🌟 厉害呀！这份知识储备令人佩服！",
    "👏 回答得真漂亮！看来你学得很扎实！",
    "✨ 完全正确！历史小达人的称号非你莫属！",
    "🏆 优秀！你对历史的理解越来越深刻了！",
    "💪 没错！继续保持这个状态，你就是学霸！",
    "🎯 精准命中！这个知识点你掌握得非常牢固！",
    "🌈 完美回答！看来你对这段历史了如指掌！",
    "⭐ 答对啦！你的历史功底越来越扎实了！",
    "🔥 太厉害了！这个知识点记得这么清楚！",
]

ENCOURAGE_WRONG = [
    "💪 没关系，学习就是不断试错的过程！下次一定记住！",
    "🌱 别灰心！每一个错误都是成长的肥料！",
    "📖 这一题有点挑战性，正好帮你巩固知识！",
    "🌈 答错了也没关系，重要的是我们学到了新知识！",
    "🌟 加油！历史学习就像拼图，每道题都在完善你的知识版图！",
    "🎯 这次没答对，但你已经比刚才更博学了！",
    "💡 错误是学习路上最好的老师，记住它，你就进步了！",
    "🚀 没关系！著名历史学家也经历过无数次学习才变得博学！",
    "🌻 每一步都是积累，这次答错下次就记住啦！",
    "📚 又发现了一个知识盲区，填补它你就更强大了！",
]

# ────────────────────────────── 游戏核心 ──────────────────────────────

class HistoryGame:
    """历史互动学习游戏"""

    def __init__(self):
        self.score = 0
        self.total = 0
        self.streak = 0          # 连续答对次数
        self.max_streak = 0
        self.wrong_questions: List[Dict] = []  # 错题记录
        self.difficulty_bonus = 0
        self.correct_era_count: Dict[str, int] = {}
        self.total_era_count: Dict[str, int] = {}

    def print_slow(self, text: str, delay: float = 0.03):
        """逐字打印，增加沉浸感"""
        for char in text:
            print(char, end="", flush=True)
            time.sleep(delay)
        print()

    def print_banner(self):
        """显示游戏标题"""
        banner = """
╔══════════════════════════════════════════════════════╗
║                                                      ║
║      🏯  历 史 小 达 人  🏯                          ║
║      ═══════════════════                              ║
║      初中历史 · 互动学习游戏                          ║
║                                                      ║
║    "以史为镜，可以知兴替"                            ║
║      —— 唐太宗李世民                                 ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
        """
        print(banner)
        time.sleep(0.5)

    def print_stats_panel(self):
        """显示当前游戏状态面板"""
        era_stats = ""
        if self.total_era_count:
            parts = []
            for era in ["中国古代史", "中国近代史", "世界史"]:
                total = self.total_era_count.get(era, 0)
                correct = self.correct_era_count.get(era, 0)
                if total > 0:
                    pct = int(correct / total * 100)
                    parts.append(f"{era[:4]} {pct}%")
            era_stats = " | ".join(parts)

        print()
        print(f"  📊  得分: {self.score}  |  进度: {self.total}/20  |  连对: {self.streak}🔥")
        if era_stats:
            print(f"  📈  各领域正确率: {era_stats}")
        print()

    def pick_random_encouragement(self, is_correct: bool) -> str:
        bank = ENCOURAGE_CORRECT if is_correct else ENCOURAGE_WRONG
        # 根据连对次数选择更有力的鼓励
        if is_correct and self.streak >= 5:
            extra = [
                f"🔥 {self.streak}连对！你已经进入了\"学霸模式\"！",
                f"⚡ 第{self.streak}次连续答对！历史知识炉火纯青！",
                f"👑 {self.streak}连击！你就是历史小博士！",
            ]
            return random.choice(extra)
        if is_correct and self.streak >= 3:
            extra = [
                f"🌟 连对{self.streak}道了！状态越来越好！",
                f"🔥 {self.streak}连胜！继续加油！",
            ]
            return random.choice(extra)
        return random.choice(bank)

    def get_rating(self) -> str:
        """根据得分给出最终评价"""
        pct = self.score / max(self.total * 10, 1)
        if pct >= 0.95:
            return "🌟 历史大学者！你对历史的了解令人惊叹！继续探索更多历史奥秘吧！"
        elif pct >= 0.85:
            return "📚 历史小达人！你的历史功底非常扎实，前途不可限量！"
        elif pct >= 0.70:
            return "💪 历史小能手！很不错的表现，再巩固一下薄弱环节就更棒了！"
        elif pct >= 0.55:
            return "🌱 历史探索者！你已经有了不错的基础，继续积累，你会越来越厉害！"
        else:
            return "🚀 历史新星！每一次学习都在进步，坚持就是胜利，未来可期！"

    def run_question(self, q: Dict) -> bool:
        """运行一道题目，返回是否答对"""
        self.total += 1

        # 清屏效果
        print("\n" + "=" * 58)
        print(f"  📖 第 {self.total} 题  |  {q['era']}")
        print("=" * 58)
        print(f"\n  {q['question']}\n")

        # 显示选项
        labels = ["A", "B", "C", "D"]
        for i, option in enumerate(q["options"]):
            print(f"    {labels[i]}.  {option}")
        print()

        # 获取用户输入
        while True:
            try:
                user_input = input("  请选择答案 (A/B/C/D 或 1/2/3/4): ").strip().lower()
                if user_input == "h":
                    print(f"\n  💡 提示: {q['hint']}\n")
                    continue

                # 解析选项
                idx = None
                if user_input in ["1", "2", "3", "4"]:
                    idx = int(user_input) - 1
                elif user_input in ["a", "b", "c", "d"]:
                    idx = "abcd".index(user_input)
                elif user_input in ["exit", "quit", "q"]:
                    print("\n  👋 下次再玩！历史的大门永远为你敞开！")
                    sys.exit(0)

                if idx is not None and 0 <= idx < len(q["options"]):
                    break
                else:
                    print("  ⚠️  请输入 A/B/C/D 或 1/2/3/4（输入 H 查看提示）")
            except (EOFError, KeyboardInterrupt):
                print("\n\n  👋 下次继续挑战！")
                sys.exit(0)

        # 检查答案
        is_correct = idx == q["answer"]
        correct_answer = labels[q["answer"]] + ". " + q["options"][q["answer"]]

        # 统计
        era = q["era"]
        self.total_era_count[era] = self.total_era_count.get(era, 0) + 1

        if is_correct:
            self.score += 10
            self.streak += 1
            self.max_streak = max(self.max_streak, self.streak)
            self.correct_era_count[era] = self.correct_era_count.get(era, 0) + 1

            print()
            print(f"  ✅ {self.pick_random_encouragement(True)}")
        else:
            self.streak = 0
            self.wrong_questions.append({
                "question": q["question"],
                "correct": correct_answer,
                "explanation": q["explanation"],
            })
            print()
            print(f"  ❌ {self.pick_random_encouragement(False)}")
            print(f"\n  📝 正确答案是: {correct_answer}")

        # 知识点讲解
        print(f"\n  📖 知识点: {q['explanation']}")
        print()

        # 奖励机制
        if is_correct and self.streak > 0 and self.streak % 3 == 0:
            bonus = 5
            self.score += bonus
            print(f"  🎁 连对 {self.streak} 题奖励！额外获得 {bonus} 分！")
            print()

        input("  ⏎ 按回车继续...")
        return is_correct

    def show_wrong_review(self):
        """错题重练环节"""
        if not self.wrong_questions:
            return

        print("\n" + "=" * 58)
        print("  📋 错题回顾 — 让我们再来复习一遍这些知识点")
        print("=" * 58)

        for i, wq in enumerate(self.wrong_questions, 1):
            print(f"\n  [{i}] {wq['question']}")
            print(f"      ✅ 正确答案: {wq['correct']}")
            print(f"      📖  {wq['explanation']}")
            print()

        input("  ⏎ 复习完毕，按回车继续...")

    def run(self):
        """游戏主入口"""
        try:
            self.print_banner()
            self.print_slow("  📚 欢迎来到历史小达人！", 0.05)
            self.print_slow("  🌟 这里有20道精心挑选的历史题目，涵盖中国古代史、近代史和世界史。", 0.03)
            self.print_slow("  💪 答错也没关系，每道题都有详细讲解，帮你越学越强！", 0.03)
            self.print_slow("  💡 答题时输入 H 可以查看提示，输入 Q 退出游戏。\n", 0.03)
            time.sleep(1)

            input("  ⏎ 准备好了吗？按回车开始挑战！")

            # 打乱题目顺序，但保持可复现
            random.seed()
            shuffled = QUESTIONS[:]
            random.shuffle(shuffled)

            # 主循环
            for q in shuffled:
                self.print_stats_panel()
                self.run_question(q)

            # 结算
            self.show_wrong_review()
            self.show_summary()

        except (EOFError, KeyboardInterrupt):
            print("\n\n  👋 下次再挑战！")

    def show_summary(self):
        """显示游戏总结"""
        pct = self.score / (self.total * 10) * 100

        print()
        print("=" * 58)
        print("  🏆  游 戏 总 结  🏆")
        print("=" * 58)
        print(f"\n  📊 最终得分:    {self.score} / {self.total * 10}")
        print(f"  ✅ 正确题数:    {self.correct_count}/{self.total}")
        print(f"  🔥 最长连对:    {self.max_streak} 题")
        print(f"  📈 正确率:      {pct:.1f}%")
        print()

        # 分领域统计
        print("  📚 各领域表现:")
        for era in ["中国古代史", "中国近代史", "世界史"]:
            total = self.total_era_count.get(era, 0)
            correct = self.correct_era_count.get(era, 0)
            if total > 0:
                bar_len = 20
                filled = int(correct / total * bar_len)
                bar = "█" * filled + "░" * (bar_len - filled)
                print(f"    {era}: {bar}  {correct}/{total}")

        print()
        print(f"  🌟 {self.get_rating()}")
        print()

        # 根据表现给出学习建议
        print("  💡 学习建议:")
        if pct < 70:
            print("    📖 建议多看教材，结合时间线梳理历史脉络")
            print("    🎬 推荐观看历史纪录片，让知识更生动")
        elif pct < 90:
            print("    🏯 基础不错！可以尝试阅读历史课外读物拓展视野")
            print("    📚 关注历史事件之间的因果联系，理解更深刻")
        else:
            print("    🎯 你已经很优秀了！可以尝试挑战更深入的历史专题")
            print("    📝 试着将历史事件横向对比，形成自己的历史观")

        print()
        print("=" * 58)
        print("  🌈  记住：\"学史可以明智\"")
        print("      每一次学习，你都在变得更好！")
        print("=" * 58)
        print()

    @property
    def correct_count(self):
        return self.total - len(self.wrong_questions)


# ────────────────────────────── 启动 ──────────────────────────────

if __name__ == "__main__":
    game = HistoryGame()
    game.run()
