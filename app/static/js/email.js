function EmailUnobsfuscate() {
    // find all links in HTML
    var link = document.getElementsByTagName && document.getElementsByTagName("a");
    var email, e;
    // examine all links
    for (e = 0; link && e < link.length; e++) {
	// does the link have use a class named "email"
	if ((" "+link[e].className+" ").indexOf(" email ") >= 0) {
	    // get the obfuscated email address
	    email = link[e].firstChild.nodeValue.toLowerCase() || "";
	    // transform into real email address
	    email = email.replace(/dot/ig, ".");
	    email = email.replace(/\(at\)/ig, "@");
	    email = email.replace(/\s/g, "");
	    // is email valid?
	    if (/^[^@]+@[a-z0-9]+([_\.\-]{0,1}[a-z0-9]+)*([\.]{1}[a-z0-9]+)+$/.test(email)) {
		// change into a real mailto link
		link[e].href = "mailto:" + email;
		link[e].firstChild.nodeValue = email;
	    }
	}
    }
}