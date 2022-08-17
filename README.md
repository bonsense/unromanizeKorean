**Unromanize Korean**

These are python codes that translate romanized korean to korean. <br />
It only works for romanized korean that follows McCune–Reischauer rule.<br />

Since there was a data loss when korean romanizes,<br />
this translator cannot unromanize with 100% accuracy.<br />
For example, "그것은 꿈이었을까?" romanizes into "kŭgŏsŭn kkumiŏssŭlkka", <br />
and if you unromanize "kŭgŏsŭn kkumiŏssŭlkka", you'll get this result: "그거슨 꿈이어쓸까"<br />
This is because romanizations are meant to be used to<br />
covert Korean to Roman charactors BY HOW IT SOUNDS.<br />

TO solve this problem, I used few extra logics.<br />
For example, I unromanized "ŭn" and "ŭl" first <br />
and added 'ㅇ(이응)' at front: "kŭgŏs은 kkumiŏss을kka".<br />
Then I changed 's' to 't': "kŭgŏt은 kkumiŏtt을kka"<br />
Finally, I unromanized the full sentence; "그것은 꿈이었을까"<br />

Although these logics fix some data losses,<br />
there are unrestorable losses.<br />
To solve this problem, AI technology is needed.<br />


p.s. <br />
I uesed 'hangul_jamos' package to assemble Korean 자모(jamo) together.<br />
For example, this package assembles 'ㄱㅡㄱㅓㅅㅇㅡㄴ' to '그것은'<br />
