document.addEventListener("DOMContentLoaded", () => {
  const trendingBooks = [
      { title: "The Midnight Library", author: "Matt Haig", cover: "https://via.placeholder.com/150", rating: 4.7 },
      { title: "Atomic Habits", author: "James Clear", cover: "https://via.placeholder.com/150", rating: 4.8 },
      { title: "Project Hail Mary", author: "Andy Weir", cover: "https://via.placeholder.com/150", rating: 4.6 }
  ];

  const topReviewers = [
      "📖 @booklover22",
      "📝 @reviewqueen",
      "📚 @avid_reader"
  ];

  const trendingContainer = document.getElementById("trending-books");
  trendingBooks.forEach(book => {
      trendingContainer.innerHTML += `
          <div class="book-card">
              <img src="${book.cover}" alt="${book.title} cover">
              <h4>${book.title}</h4>
              <p>by ${book.author}</p>
              <p>⭐ ${book.rating}</p>
          </div>
      `;
  });

  const reviewerList = document.getElementById("top-reviewers");
  topReviewers.forEach(name => {
      const li = document.createElement("li");
      li.textContent = name;
      reviewerList.appendChild(li);
  });
});
