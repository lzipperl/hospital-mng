"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path


def root_view(request):
    html = """
    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8" />
      <title>ApexCare Hospital</title>
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" />
      <style>
        body {
          min-height: 100vh;
          background: radial-gradient(circle at top left, #0d6efd11, #0d6efd22 20%, #f8f9fa 55%);
        }
        .hero-card {
          border-radius: 1.5rem;
          box-shadow: 0 18px 45px rgba(15, 23, 42, 0.25);
        }
        .blur-bg {
          backdrop-filter: blur(14px);
          background: rgba(15, 23, 42, 0.85);
        }
        .pill {
          border-radius: 999px;
          background: rgba(13, 110, 253, 0.12);
          color: #0d6efd;
          padding: 0.3rem 0.9rem;
          font-size: 0.78rem;
          letter-spacing: 0.08em;
          text-transform: uppercase;
        }
        .stat-label {
          font-size: 0.8rem;
          text-transform: uppercase;
          letter-spacing: 0.06em;
        }
        .endpoint-link {
          text-decoration: none;
        }
        .endpoint-link code {
          transition: all 0.15s ease-in-out;
        }
        .endpoint-link:hover code {
          transform: translateX(2px);
          color: #0d6efd;
        }
      </style>
    </head>
    <body class="d-flex align-items-center">
      <div class="container py-5">
        <div class="row justify-content-center">
          <div class="col-xl-9">
            <div class="hero-card blur-bg text-white p-4 p-md-5">
              <div class="row g-4 align-items-center">
                <div class="col-md-6 border-md-end border-light border-opacity-10 pe-md-4">
                  <div class="d-flex align-items-center gap-2 mb-3">
                    <span class="pill">Hospital Control Center</span>
                  </div>
                  <h1 class="fw-semibold mb-3">ApexCare Hospital Console</h1>
                  <p class="text-white-50 mb-4">
                    Secure backend for managing doctors, patients, appointments,
                    prescriptions and billing. Use this console, the admin panel,
                    or any REST client to operate the system.
                  </p>

                  <div class="d-flex flex-wrap gap-3 mb-4">
                    <a href="/admin/" class="btn btn-primary btn-lg px-4">
                      Open Admin Panel
                    </a>
                    <a href="/api/accounts/register/" class="btn btn-outline-light btn-lg px-4">
                      Create First User
                    </a>
                  </div>

                  <div class="d-flex gap-4 flex-wrap text-white-50">
                    <div>
                      <div class="stat-label">Security</div>
                      <div class="fw-semibold">JWT Protected API</div>
                    </div>
                    <div>
                      <div class="stat-label">Performance</div>
                      <div class="fw-semibold">Redis Ready</div>
                    </div>
                    <div>
                      <div class="stat-label">Deploy</div>
                      <div class="fw-semibold">Docker & Gunicorn</div>
                    </div>
                  </div>
                </div>

                <div class="col-md-6 ps-md-4">
                  <div class="row g-3">
                    <div class="col-12">
                      <div class="bg-light bg-opacity-10 rounded-4 p-3 h-100">
                        <h6 class="text-uppercase text-white-50 mb-2 small">Quick Auth</h6>
                        <ul class="list-unstyled small mb-0">
                          <li class="mb-1">
                            <code>POST /api/accounts/register/</code>
                            <span class="text-white-50"> – create admin/doctor/patient</span>
                          </li>
                          <li class="mb-1">
                            <code>POST /api/accounts/token/</code>
                            <span class="text-white-50"> – obtain JWT access/refresh</span>
                          </li>
                          <li>
                            <code>GET /api/accounts/me/</code>
                            <span class="text-white-50"> – current profile</span>
                          </li>
                        </ul>
                      </div>
                    </div>

                    <div class="col-12">
                      <div class="bg-light bg-opacity-10 rounded-4 p-3 h-100">
                        <h6 class="text-uppercase text-white-50 mb-2 small">Core Modules</h6>
                        <ul class="list-unstyled small mb-0">
                          <li class="mb-1">
                            <a class="endpoint-link" href="/api/doctors/">
                              <code>/api/doctors/</code>
                            </a>
                            <span class="text-white-50"> – doctor profiles</span>
                          </li>
                          <li class="mb-1">
                            <a class="endpoint-link" href="/api/patients/">
                              <code>/api/patients/</code>
                            </a>
                            <span class="text-white-50"> – patient records</span>
                          </li>
                          <li class="mb-1">
                            <a class="endpoint-link" href="/api/appointments/">
                              <code>/api/appointments/</code>
                            </a>
                            <span class="text-white-50"> – schedule & status</span>
                          </li>
                          <li class="mb-1">
                            <a class="endpoint-link" href="/api/prescriptions/">
                              <code>/api/prescriptions/</code>
                            </a>
                            <span class="text-white-50"> – treatment plans</span>
                          </li>
                          <li>
                            <a class="endpoint-link" href="/api/billing/">
                              <code>/api/billing/</code>
                            </a>
                            <span class="text-white-50"> – invoices & revenue</span>
                          </li>
                        </ul>
                      </div>
                    </div>

                    <div class="col-12">
                      <div class="bg-dark rounded-4 p-3 border border-light border-opacity-10">
                        <div class="d-flex justify-content-between align-items-center mb-2">
                          <span class="text-white-50 small">API Connection</span>
                          <span class="badge bg-success-subtle text-success border border-success border-opacity-50">
                            Online
                          </span>
                        </div>
                        <code class="small text-white-50">
                          Base URL: http://127.0.0.1:8000<br />
                          Auth: Bearer &lt;access_token&gt;
                        </code>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </body>
    </html>
    """
    return HttpResponse(html)


urlpatterns = [
    path("", root_view, name="root"),
    path("admin/", admin.site.urls),
    path("api/accounts/", include("accounts.urls")),
    path("api/doctors/", include("doctors.urls")),
    path("api/patients/", include("patients.urls")),
    path("api/appointments/", include("appointments.urls")),
    path("api/prescriptions/", include("prescriptions.urls")),
    path("api/billing/", include("billing.urls")),
]
