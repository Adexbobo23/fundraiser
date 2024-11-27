<div class="row pb50">
    <div class="col-lg-12">
      <div class="dashboard_title_area">
        <h2>Profile Details</h2>
        {% if user.is_authenticated %}
          <p class="para">Welcome {{ user.first_name }} {{ user.last_name }}</p>
  
          <!-- Success/Error Messages -->
          {% if messages %}
            <div class="alert alert-success">
              {% for message in messages %}
                <div>{{ message }}</div>
              {% endfor %}
            </div>
          {% endif %}
  
          <!-- Display User Profile Details -->
          {% if user.userprofile %}
            <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 20px;">
              <!-- Profile Details -->
              <ul class="profile-details" style="flex: 1 1 45%; list-style-type: none; padding: 0;">
                <li style="margin-bottom: 15px;"><strong>Phone Number:</strong> {{ user.userprofile.phone_number|default:"Not provided" }}</li>
                <li style="margin-bottom: 15px;"><strong>Country:</strong> {{ user.userprofile.country|default:"Not provided" }}</li>
                <li style="margin-bottom: 15px;"><strong>State:</strong> {{ user.userprofile.state|default:"Not provided" }}</li>
                <li style="margin-bottom: 15px;"><strong>Description:</strong> {{ user.userprofile.profile_description|default:"No description available" }}</li>
              </ul>
  
              <!-- Avatar Image -->
              <div style="flex: 1 1 45%; display: flex; flex-direction: column; align-items: center; text-align: center;">
                <strong>Profile Image:</strong><br>
                {% if user.userprofile.avatar %}
                  <img src="{{ user.userprofile.avatar.url }}" alt="Avatar" style="width: 150px; height: 150px; border-radius: 75px; border: 2px solid #007bff; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
                {% else %}
                  <p>No avatar available.</p>
                {% endif %}
              </div>
            </div>
          {% else %}
            <p>No profile details available.</p>
          {% endif %}
        {% endif %}
      </div>
    </div>
  </div>