# FreeFire API Manager

A beautiful web interface for managing FreeFire accounts and friends through a powerful API.

## Features

- **Friend Management**: Add or remove friends from your FreeFire account
- **Player Information**: Retrieve detailed information about any player
- **Token Generation**: Generate authentication tokens for API access
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Modern UI**: Sleek dark theme with glowing accents

## Screenshots

![Friend Management](screenshots/friend-management.png)
*Friend Management Interface*

![Player Information](screenshots/player-info.png)
*Player Information Dashboard*

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd FRIEND-API
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://localhost:5000`

## Usage

### Authentication Methods

The API supports two authentication methods:

1. **Using Token**: Provide a valid JWT token
2. **Using Credentials**: Provide UID and Password to generate a token

### API Endpoints

#### Core Functionality
- `/add_friend` - Add a friend
- `/remove_friend` - Remove a friend
- `/get_player_info` - Get player information
- `/token` - Generate authentication token

#### Utility Endpoints
- `/health` - Health check endpoint
- `/status` - Detailed status information
- `/version` - API version information
- `/metrics` - System metrics and performance data
- `/info` - Comprehensive API information and documentation

### Web Interface

The web interface provides a user-friendly way to interact with all API endpoints:

1. **Friend Management Tab**: Add or remove friends
2. **Player Info Tab**: Retrieve player details
3. **Token Generator Tab**: Generate authentication tokens

## Deployment Options

### Local Development

```bash
python app.py
```

### Production Deployment

#### Using Gunicorn (Recommended)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

#### Using Docker

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

Build and run:

```bash
docker build -t freefire-api .
docker run -p 5000:5000 freefire-api
```

#### Deploy to Heroku

1. Create a `Procfile`:
   ```
   web: gunicorn app:app
   ```

2. Deploy to Heroku:
   ```bash
   heroku create
   git push heroku master
   ```

#### Deploy to Render

1. Create a `render.yaml`:
   ```yaml
   services:
     - type: web
       name: freefire-api
       env: python
       buildCommand: pip install -r requirements.txt
       startCommand: gunicorn app:app
   ```

2. Connect your GitHub repository to Render

## Configuration

The application can be configured using environment variables:

- `PORT` - Port to run the server on (default: 5000)

## API Documentation

### Add Friend

```
GET /add_friend?player_id={player_id}&token={token}
```

Parameters:
- `player_id` (required): Target player ID
- `token` (required if not using uid/password): Authentication token
- `uid` (required if not using token): User ID
- `password` (required if not using token): Password
- `server_name` (optional): Server region

### Remove Friend

```
GET /remove_friend?player_id={player_id}&token={token}
```

Parameters:
- `player_id` (required): Target player ID
- `token` (required if not using uid/password): Authentication token
- `uid` (required if not using token): User ID
- `password` (required if not using token): Password
- `server_name` (optional): Server region

### Get Player Info

```
GET /get_player_info?player_id={player_id}&token={token}
```

Parameters:
- `player_id` (required): Target player ID
- `token` (required if not using uid/password): Authentication token
- `uid` (required if not using token): User ID
- `password` (required if not using token): Password
- `server_name` (optional): Server region

### Generate Token

```
GET /token?uid={uid}&password={password}
```

Parameters:
- `uid` (required): User ID
- `password` (required): Password

## Troubleshooting

### Common Issues

1. **Protobuf Compatibility Errors**: Make sure you're using protobuf version 6.33.1 or higher
2. **CORS Issues**: The application includes CORS support by default
3. **SSL Verification Errors**: The application disables SSL verification for internal requests

### Updating Dependencies

```bash
pip install --upgrade -r requirements.txt
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is for educational purposes only. Use responsibly and in accordance with FreeFire's terms of service.