function isKeyPressed(e) {
    alert(`The ALT or CTRL or Shift key was ${e.altKey || e.ctrlKey || e.shiftKey ? "pressed!" : "NOT pressed!"}`);
}
