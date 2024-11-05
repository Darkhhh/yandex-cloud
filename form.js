let loginForm = document.getElementById("upload_form");

loginForm.addEventListener("submit", (e) => {
    e.preventDefault();

    let storage_key_element = document.getElementById("storage_key");
    let storage_key = "users/uploads/" + storage_key_element.value;

    storage_key_element.value = storage_key;
    console.log("Uploading file with key: " + storage_key);

    loginForm.submit();
});