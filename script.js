async function getTargets() {
    const coin = document.getElementById("coin").value.toUpperCase();
    const res = await fetch(`/predict/${coin}`);
    const data = await res.json();
    document.getElementById("output").textContent = JSON.stringify(data, null, 2);
}
