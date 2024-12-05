document.addEventListener("DOMContentLoaded", () => {
    // Kiểm tra trạng thái lưu trong LocalStorage
    const isNightMode = localStorage.getItem("nightMode") === "true";

    // Nếu Night Mode đang được bật, thêm lớp "night-mode"
    if (isNightMode) {
        document.body.classList.add("night-mode");
    }

    // Gắn sự kiện click cho nút chuyển chế độ
    const toggleButton = document.querySelector(".night-mode-toggle");
    toggleButton.addEventListener("click", () => {
        document.body.classList.toggle("night-mode");

        // Lưu trạng thái vào LocalStorage
        const nightModeActive = document.body.classList.contains("night-mode");
        localStorage.setItem("nightMode", nightModeActive);
    });
});
