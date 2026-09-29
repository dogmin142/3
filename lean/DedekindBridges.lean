namespace DedekindBridges

/-- Valuation recovery atom used in obstruction ideals. -/
theorem recover_beta (a s : Nat) : a - min a s = max (a - s) 0 := by omega

/-- Counting first-difference atom. -/
theorem min_succ_diff (r b : Nat) :
    min (r + 1) b - min r b = if r < b then 1 else 0 := by
  by_cases h : r < b
  · have hrb : r ≤ b := Nat.le_of_lt h
    have hrsb : r + 1 ≤ b := h
    rw [if_pos h, Nat.min_eq_left hrsb, Nat.min_eq_left hrb]
    omega
  · have hbr : b ≤ r := Nat.le_of_not_gt h
    have hbs : b ≤ r + 1 := Nat.le_trans hbr (Nat.le_succ r)
    rw [if_neg h, Nat.min_eq_right hbs, Nat.min_eq_right hbr]
    simp

/-- Additive core of the generic Householder/Fitting bounds. -/
theorem generic_bounds_additive (n a s f t : Nat)
    (ht : n * a = 2 * a + t) (hs : s ≤ t) (hf : f = n * a - s) :
    2 * a ≤ f ∧ f ≤ n * a := by
  subst f
  constructor
  · rw [ht]; omega
  · exact Nat.sub_le _ _

/-- Common truncation reverses order as required by local exponent sorting. -/
theorem truncation_monotone (a x y : Nat) (hxy : x ≤ y) : a - y ≤ a - x := by omega

/-- Zero correction leaves an exponent unchanged. -/
theorem zero_correction (a : Nat) : a - 0 = a := by simp

end DedekindBridges
