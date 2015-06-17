using UnityEngine;
using System.Collections;

public class AnimationController : MonoBehaviour {

	Animation anim;

	// Use this for initialization
	void Start () {
		anim = GetComponent<Animation> ();

		anim["idle"].wrapMode = WrapMode.Loop;
		anim ["leap"].wrapMode = WrapMode.Once;
	}
	
	// Update is called once per frame
	void Update () {
		if (Input.GetKeyDown ("w"))
			anim.CrossFade("leap", 0.2f);
	}
}
