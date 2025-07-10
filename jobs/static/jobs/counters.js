// Animated counters for jobs, users, applications
function animateCounter(id, end) {
  const el = document.getElementById(id);
  if (!el) return;
  let start = 0;
  const duration = 1200;
  const step = Math.ceil(end / (duration / 16));
  function update() {
    start += step;
    if (start >= end) {
      el.innerText = end;
    } else {
      el.innerText = start;
      requestAnimationFrame(update);
    }
  }
  update();
}
