// import 파일명 from '경로' with { type: "json" };
import user from '../data/user.json' with { type: "json" };

console.log(user.name); // "김철수"
console.log(user.job);  // "디자이너"