// eslint-disable-next-line import/prefer-default-export
export function formatTime(duration) {
  const s = duration % 60;
  const m = Math.floor(duration / 60) % 60;
  const h = Math.floor(duration / 3600);
  const ss = ('0' + s).slice(-2); // eslint-disable-line prefer-template
  const mm = ('0' + m).slice(-2); // eslint-disable-line prefer-template
  if (h === 0) {
    return mm + ' : ' + ss; // eslint-disable-line prefer-template
  }
  return (h <= 9 ? '0' : '') + h + ' : ' + mm + ' : ' + ss; // eslint-disable-line prefer-template
}
