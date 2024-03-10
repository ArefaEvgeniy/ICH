# ¬((A ∨ B) ∧ (C ∨ D)) и ((¬A ∧ ¬B) ∨ (¬C ∧ ¬D))

A = True
B = False

not(A and B) -> True

(not A) or (not B) = False or True -> True

not(A and B) = (not A) or (not B)

not(A or B) = (not A) and (not B)


not((A or B) and (C or D)) и ((not A and not B) or (not C and not D))
not((A or B) and (C or D)) = not(A or B) or not(C or D) = (not A and not B) or (not C and not D)

