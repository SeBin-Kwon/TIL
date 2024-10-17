//
//  ContentView.swift
//  PixoVideoTrackView
//
//  Created by Sebin Kwon on 10/8/24.
//

import SwiftUI
import AVFoundation
import AVKit

struct TrackView: View {
    @State private var currentTime = 0.0
    @State private var player = AVPlayer(url: Bundle.main.url(forResource: "1", withExtension: "mp4")!)
    @State private var isPlaying = false
    @State private var currentVideoIndex = 0
    @State private var trackOffset: CGFloat = 0
    @State private var accumulatedTime = 0.0
    private let thumbnailWidth: CGFloat = 180
    private var imageWidth: CGFloat = 60
    private var trackLength: CGFloat {
        return CGFloat(videos.count) * thumbnailWidth
    }
    private var startOffset: CGFloat {
        return trackLength/2 + CGFloat(videos.count * 4)
    }
    private let screenWidth: CGFloat = UIScreen.main.bounds.width
    @State private var timeObserverToken: Any?
    var body: some View {
        VStack {
            VideoPlayer(player: player)
                .frame(height: 500)
                .disabled(true)
            playButton
            Text("\(formatTime(currentTime))")
            
            ZStack {
                HStack {
                    ForEach(videos.indices, id: \.self) { index in
                        Image(uiImage: generateThumbnail(asset: videos[index].currentItem?.asset)!)
                            .resizable()
                            .frame(width: calculateThumbnailWidth(for: index), height: 120)
                            .cornerRadius(10)
                            .onTapGesture {
                                player = videos[index]
                                isPlaying = false
                            }
                    }
                }
                .padding(.horizontal)
                .offset(x: trackOffset)
                .gesture(
                    DragGesture(minimumDistance: 0)
                        .onChanged { value in
                            withAnimation {
                                let newOffset = trackOffset + value.translation.width
                                trackOffset = max(-startOffset, min(newOffset, startOffset))
                                updateVideoPosition()
                            }
                        }
                        .onEnded{ value in
                            setupTrack()
                        }
                )
                
                Capsule()
                    .fill(Color.blue)
                    .frame(width: 2, height: 150)
            }
            .padding(.vertical)
        }
        .onAppear {
            trackOffset = startOffset
            setupTrack()
        }
        .padding(.vertical)
        Spacer()
    }
    
    private var playButton: some View {
        HStack {
            Button(action: {
                if isPlaying {
                    player.pause()
                } else {
                    player.play()
                }
                isPlaying.toggle()
            }) {
                Image(systemName: isPlaying ? "pause" : "play")
                    .resizable()
                    .aspectRatio(contentMode: .fit)
                    .frame(height: 25)
            }
        }
    }
    
    private func setupTrack() {
        player = videos[currentVideoIndex]
        
        NotificationCenter.default.addObserver(forName: .AVPlayerItemDidPlayToEndTime, object: player.currentItem, queue: .main) { _ in
            moveToNextVideo()
            
        }
        
        let interval = CMTime(seconds: 0.1, preferredTimescale: 600)
        timeObserverToken = player.addPeriodicTimeObserver(forInterval: interval, queue: .main) { time in
            updateTrackPosition(time: time)
        }
    }
    
    private func updateVideoPosition() {
        let progress = (startOffset - trackOffset) / (2 * startOffset)
        let totalDuration = videos.reduce(0.0) { $0 + ($1.currentItem?.duration.seconds ?? 0) }
        let targetTime = progress * totalDuration
        
        var accumulatedTime: Double = 0
        for (index, video) in videos.enumerated() {
            let videoDuration = video.currentItem?.duration.seconds ?? 0
            if accumulatedTime + videoDuration > targetTime {
                currentVideoIndex = index
                player = videos[currentVideoIndex]
                let timeInCurrentVideo = targetTime - accumulatedTime
                player.seek(to: CMTime(seconds: timeInCurrentVideo, preferredTimescale: 600))
                self.accumulatedTime = accumulatedTime
                currentTime = targetTime
                break
            }
            accumulatedTime += videoDuration
        }
    }
    
    private func moveToNextVideo() {
        accumulatedTime += player.currentItem?.duration.seconds ?? 0
        currentVideoIndex = currentVideoIndex + 1
        if currentVideoIndex >= videos.count {
            currentVideoIndex = videos.count - 1
            stopUpdatingTrack()
            return
        }
        player = videos[currentVideoIndex]
        if isPlaying {
            player.play()
        }
        player.seek(to: CMTime.zero)
        currentTime = accumulatedTime
        setupTrack()
    }
    
    private func updateTrackPosition(time: CMTime) {
        let playerCurrentTime = time.seconds
        currentTime = accumulatedTime + playerCurrentTime
        
        let totalDuration = videos.reduce(0.0) { $0 + ($1.currentItem?.duration.seconds ?? 0) }
        let progress = currentTime / totalDuration
        trackOffset = startOffset - progress * (2 * startOffset)
        if currentTime >= totalDuration {
            stopUpdatingTrack()
        }
    }
    
    private func stopUpdatingTrack() {
        if let timeObserverToken = timeObserverToken {
            player.removeTimeObserver(timeObserverToken)
            self.timeObserverToken = nil
        }
        isPlaying = false
    }
    
    private func generateThumbnail(asset: AVAsset?) -> UIImage? {
        guard let asset = asset else { return nil }
        
        let imageGenerator = AVAssetImageGenerator(asset: asset)
        imageGenerator.appliesPreferredTrackTransform = true
        imageGenerator.maximumSize = CGSize(width: thumbnailWidth / CGFloat(3), height: 90)
        
        let duration = asset.duration.seconds
        let frameInterval = duration / Double(3)
        
        var images: [UIImage] = []
        
        for i in 0..<3 {
            let time = CMTime(seconds: frameInterval * Double(i), preferredTimescale: 600)
            do {
                let cgImage = try imageGenerator.copyCGImage(at: time, actualTime: nil)
                let image = UIImage(cgImage: cgImage)
                images.append(image)
            } catch {
                print("Error generating thumbnail: \(error.localizedDescription)")
            }
        }
        
        let totalSize = CGSize(width: thumbnailWidth, height: 90)
        UIGraphicsBeginImageContextWithOptions(totalSize, false, 0.0)
        
        for (index, image) in images.enumerated() {
            let xPosition = CGFloat(index) * (thumbnailWidth / CGFloat(3))
            image.draw(in: CGRect(x: xPosition, y: 0, width: thumbnailWidth / CGFloat(3), height: 90))
        }
        
        let combinedImage = UIGraphicsGetImageFromCurrentImageContext()
        UIGraphicsEndImageContext()
        
        return combinedImage
    }
    
    private func calculateThumbnailWidth(for videoIndex: Int) -> CGFloat {
        let totalDuration = videos.reduce(0.0) { $0 + ($1.currentItem?.duration.seconds ?? 0) }
        let videoDuration = videos[videoIndex].currentItem?.duration.seconds ?? 0
        
        guard totalDuration > 0, videoDuration > 0 else {
            return thumbnailWidth
        }
        
        let proportion = videoDuration / totalDuration
        
        let minThumbnailWidth: CGFloat = 60
        let maxThumbnailWidth: CGFloat = 300
        
        guard trackLength > 0 else {
            print("Invalid trackLength: \(trackLength)")
            return thumbnailWidth
        }
        
        let calculatedWidth = proportion * trackLength
        let finalWidth = max(min(calculatedWidth, maxThumbnailWidth), minThumbnailWidth)
        
        return finalWidth.isFinite ? finalWidth : thumbnailWidth
    }
    
    private func formatTime(_ time: Double) -> String {
        let minutes = Int(time) / 60
        let seconds = Int(time) % 60
        return String(format: "%02d:%02d", minutes, seconds)
    }
}


#Preview {
    TrackView()
}
