<script>
    alert("Hello world!");

    alert(`result: ${158 + 2}`);

    let name = "Archi";
    alert(`Hi, ${name}`);
    alert(`Hi ` + name);

    let usrName = prompt("What your name?", "your name");
    alert(`Hi, ${usrName}`);

    function getMassage() {
        let massage = `Hello, ${usrName}`;
    alert(massage);
    }
    getMassage()

    if (confirm("Are you sure?")) alert("Ok")
        else alert("Oh no...")

    let result = confirm("Are you sure?")
    if (result) {
        alert("Oh tes!");
     } else {
        alert("Oh no...")
    }

    let age = parseInt(promt("Your age is?"));
    if (age == 18) {
        alert('Вы совершеннолетний, все можно!');
    } else if (age == 10) {
        alert('Вам надо учить уроки!');
    } else if (age == 30) {
        alert('Ложитесь спать, завтра на работу');
    } else {
        alert('Мы не знаем что Вам делать');
    }

    let age = parseInt(prompt("How old are you?"))
    switch (age) {
        case 18: alert("It is nice!");
    break;
    case 30: alert("Not bad");
    break;
    case 40: alert("Not cool!");
    break;
    default: alert("Go sleep!");
    break;
    }
</script>