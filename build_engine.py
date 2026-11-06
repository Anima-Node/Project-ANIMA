import os

print("GENERATING FACTORY-CLEAN SCORING ENGINE ENGINE...")

code_lines = [
    "class AnimaScoringEngine:",
    "    def __init__(self):",
    "        self.max_base_score = 115",
    "    def calculate_compatibility(self, vector_a, vector_b):",
    "        if len(vector_a) != 10 or len(vector_b) != 10:",
    "            raise ValueError('Vectors must contain exactly 10 discrete integer elements.')",
    "        base_score = 0; penalty_pool = 0",
    "        for i in range(10):",
    "            if vector_a[i] == vector_b[i]:",
    "                if 0 <= i <= 2: base_score += 5",
    "                elif 3 <= i <= 6: base_score += 10",
    "                elif 7 <= i <= 9: base_score += 20",
    "        if (vector_a[4] == 1 and vector_b[4] == 2) or (vector_a[4] == 2 and vector_b[4] == 1):",
    "            penalty_pool += 5",
    "        if (vector_a[9] == 1 and vector_b[9] == 2) or (vector_a[9] == 2 and vector_b[9] == 1):",
    "            penalty_pool += 5",
    "        a_isolated = (vector_a[2] == 3 and vector_a[7] == 4)",
    "        b_isolated = (vector_b[2] == 3 and vector_b[7] == 4)",
    "        a_chaotic = (vector_a[2] == 4 and vector_a[7] == 2)",
    "        b_chaotic = (vector_b[2] == 4 and vector_b[7] == 2)",
    "        if (a_isolated and b_chaotic) or (b_isolated and a_chaotic):",
    "            penalty_pool += 10",
    "        final_score = base_score - penalty_pool",
    "        if final_score < 0: final_score = 0",
    "        return {'base_score': base_score, 'penalties': penalty_pool, 'final': final_score, 'pct': round((final_score / self.max_base_score) * 100, 2)}",
    "if __name__ == '__main__':",
    "    engine = AnimaScoringEngine()",
    "    user_vector = [3, 3, 2, 1, 1, 2, 1, 3, 1, 3]",
    "    lone_wolf_vector = [1, 1, 3, 4, 2, 3, 4, 4, 3, 1]",
    "    catalyst_vector = [3, 3, 2, 1, 1, 2, 1, 3, 1, 3]",
    "    print('==================================================')",
    "    print('      PROJECT ANIMA: LOCAL CALCULATOR ENGINE      ')",
    "    print('==================================================\\n')",
    "    print(f'Your Profile Vector: {user_vector}\\n')",
    "    r_wolf = engine.calculate_compatibility(user_vector, lone_wolf_vector)",
    "    print('--> SIMULATION 01: PROFILE vs. LONE WOLF')",
    "    print(f'    Base Score: {r_wolf[\"base_score\"]} pts | Penalties: -{r_wolf[\"penalties\"]} pts')",
    "    print(f'    TOTAL COMPATIBILITY: {r_wolf[\"pct\"]}%\\n')",
    "    r_mirror = engine.calculate_compatibility(user_vector, catalyst_vector)",
    "    print('--> SIMULATION 02: PROFILE vs. MIRROR MATCH')",
    "    print(f'    Base Score: {r_mirror[\"base_score\"]} pts | Penalties: -{r_mirror[\"penalties\"]} pts')",
    "    print(f'    TOTAL COMPATIBILITY: {r_mirror[\"pct\"]}%')",
    "    print('==================================================')"
]
with open('anima_scoring_engine.py', 'w', encoding='utf-8') as f:
    f.write('\n'.join(code_lines) + '\n')
print("SUCCESS: anima_scoring_engine.py generated with correct structural indents.")