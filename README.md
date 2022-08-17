**Unromanize Korean**

These are python codes that translate romanized korean to korean. /n
It only works for romanized korean that follows McCune–Reischauer rule.

Since there was a data loss when korean romanizes,
this translator cannot unromanize with 100% accuracy.
For example, "그것은 꿈이었을까?" romanizes into "kŭgŏsŭn kkumiŏssŭlkka", 
and if you unromanize "kŭgŏsŭn kkumiŏssŭlkka", you'll get this result: "그거슨 꿈이어쓸까"
This is because romanizations are meant to be used to
covert Korean to Roman charactors BY HOW IT SOUNDS.

TO solve this problem, I used few extra logics.
For example, I unromanized "ŭn" and "ŭl" first 
and added 'ㅇ(이응)' at front: "kŭgŏs은 kkumiŏss을kka".
Then I changed 's' to 't': "kŭgŏt은 kkumiŏtt을kka"
Finally, I unromanized the full sentence; "그것은 꿈이었을까"

Although these logics fix some data losses,
there are unrestorable losses.
To solve this problem, AI technology is needed.


p.s. 
I uesed 'hangul_jamos' package to assemble Korean 자모(jamo) together.
For example, this package assembles 'ㄱㅡㄱㅓㅅㅇㅡㄴ' to '그것은'
