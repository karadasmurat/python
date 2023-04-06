CREATE TABLE Album (
  AlbumID INTEGER PRIMARY KEY,
  Title TEXT,
  ReleaseDate TEXT,
  Genre TEXT,
  Artwork TEXT,
  RecordLabel TEXT
);

CREATE TABLE Artist (
  ArtistID INTEGER PRIMARY KEY,
  ArtistName TEXT
);

CREATE TABLE Album_Artist (
  AlbumID INTEGER,
  ArtistID INTEGER,
  PRIMARY KEY (AlbumID, ArtistID),
  FOREIGN KEY (AlbumID) REFERENCES Album(AlbumID),
  FOREIGN KEY (ArtistID) REFERENCES Artist(ArtistID)
);

CREATE TABLE Track (
  TrackID INTEGER PRIMARY KEY,
  Title TEXT,
  TrackNo INTEGER,
  TrackLength TEXT,
  AlbumID INTEGER,
  FOREIGN KEY (AlbumID) REFERENCES Album(AlbumID)
);