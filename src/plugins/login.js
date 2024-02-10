// import apiInstance from "./interceptor";

// export default login;
// export async function login(username, password) {
//   try {
//     const hashedPassword = await hashPassword(password);
//     // 调用登录API`
//     const response = await apiInstance.post("/login", { username, password: hashedPassword });

//     // 处理登录成功的逻辑
//     if (response.data.success) {
//       // 更新用户信息
//       this.$store.commit("user/setUser", username);
//       return true; // 表示登录成功
//     } else {
//       // 处理登录失败的逻辑
//       console.error(response.data.message);
//       return false; // 表示登录失败
//     }
//   } catch (error) {
//     // 处理登录过程中的错误
//     console.error(error);
//     return false; // 表示登录失败
//   }
// }

// async function hashPassword(password) {
//   const encoder = new TextEncoder();
//   const data = encoder.encode(password);

//   const hashBuffer = await crypto.subtle.digest("SHA-256", data);

//   const hashArray = Array.from(new Uint8Array(hashBuffer));
//   const hashHex = hashArray.map(byte => byte.toString(16).padStart(2, "0")).join("");

//   return hashHex;
// }
