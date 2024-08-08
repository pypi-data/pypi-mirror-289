import re
from enum import Enum


class Strategy:
    """策略接口，所有策略需要实现此接口"""

    def apply(self, text):
        pass


class FractionToChineseStrategy(Strategy):
    """将 LaTeX 分数转换为中文格式"""

    def apply(self, text):
        pattern = r"\\frac{(\d+)}{(\d+)}"
        return re.sub(pattern, lambda m: f"{m.group(2)}分之{m.group(1)}", text)


class CleanLatexStrategy(Strategy):
    """清理 LaTeX 特定语法"""

    def apply(self, text):
        text = re.sub(r"\\\(\\|\\\)\\", "", text)
        text = re.sub(r"\\", "", text)
        text = re.sub(r"[()]", "", text)
        text = re.sub(r"\$\$(.*?)\$\$", r"\1", text)
        return re.sub(r"\$(.*?[^\\])\$", r"\1", text)


class MinusToChineseStrategy(Strategy):
    """将减号转换为中文字符"""

    def apply(self, text):
        return re.sub(r"-", "减", text)


class MultiplicationToChineseStrategy(Strategy):
    """将乘法符号（包括LaTeX格式）转换为中文格式"""

    def apply(self, text):
        # 处理普通乘号
        text = re.sub(r"(\d+)\s*[×*]\s*(\d+)", r"\1乘以\2", text)
        # 处理LaTeX的\times
        text = re.sub(r"(\d+)\s*\\times\s*(\d+)", r"\1乘以\2", text)
        # 处理LaTeX的\cdot
        text = re.sub(r"(\d+)\s*\\cdot\s*(\d+)", r"\1乘以\2", text)
        return text


class DivisionToChineseStrategy(Strategy):
    """将除法符号（包括LaTeX格式）转换为中文格式"""

    def apply(self, text):
        # 处理带除号的情况
        text = re.sub(r"(\d+)\s*÷\s*(\d+)", r"\1除以\2", text)
        # 处理斜杠表示的除法
        text = re.sub(r"(\d+)\s*/\s*(\d+)", r"\1除以\2", text)
        # 处理LaTeX的\div
        text = re.sub(r"(\d+)\s*\\div\s*(\d+)", r"\1除以\2", text)
        return text


class SuperscriptToChineseStrategy(Strategy):
    """将上标数字转换为中文'次方'格式，包括平方和立方的特殊处理"""

    def apply(self, text):
        # 处理一般的上标
        text = re.sub(
            r"(\d+)\^(\d+)", lambda m: self._format_power(m.group(1), m.group(2)), text
        )
        # 处理LaTeX的上标形式
        text = re.sub(
            r"(\d+)\^\{(\d+)\}",
            lambda m: self._format_power(m.group(1), m.group(2)),
            text,
        )
        return text

    def _format_power(self, base, exponent):
        if exponent == "2":
            return f"{base}的平方"
        elif exponent == "3":
            return f"{base}的立方"
        else:
            return f"{base}的{exponent}次方"


class SquareToChineseStrategy(Strategy):
    """将平方符号转换为中文格式"""

    def apply(self, text):
        # 处理 ^2 形式
        text = re.sub(r"(\d+)\^2", r"\1的平方", text)
        # 处理 ^{2} 形式
        text = re.sub(r"(\d+)\^\{2\}", r"\1的平方", text)
        # 处理 \squared 形式
        text = re.sub(r"(\d+)\\squared", r"\1的平方", text)
        return text


class TextFormatter:
    def __init__(self):
        self.strategies = [
            FractionToChineseStrategy(),
            MinusToChineseStrategy(),
            SuperscriptToChineseStrategy(),
            SquareToChineseStrategy(),  # 新添加的平方策略
            MultiplicationToChineseStrategy(),
            DivisionToChineseStrategy(),
            CleanLatexStrategy(),  # 保持在最后，以清理剩余的LaTeX语法
        ]

    def format_text(self, text):
        """应用所有策略格式化文本"""
        for strategy in self.strategies:
            try:
                text = strategy.apply(text)
            except Exception as e:
                print(f"Error applying strategy: {e}")
        return text


# 使用示例
formatter = TextFormatter()
text = "\\frac{1}{2} - \\frac{3}{4} is a fraction"
formatted_text = formatter.format_text(text)
print(formatted_text)
