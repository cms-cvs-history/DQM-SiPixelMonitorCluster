import FWCore.ParameterSet.Config as cms

process = cms.Process("SiPixelMonitorClusterProcess")
process.load("Geometry.TrackerSimData.trackerSimGeometryXML_cfi")

process.load("Geometry.TrackerGeometryBuilder.trackerGeometry_cfi")

process.load("Geometry.TrackerNumberingBuilder.trackerNumberingGeometry_cfi")

process.load("CalibTracker.SiPixelESProducers.SiPixelFakeGainOfflineESSource_cfi")

process.load("CondTools.SiPixel.SiPixelGainCalibrationService_cfi")

process.load("RecoLocalTracker.SiPixelClusterizer.SiPixelClusterizer_cfi")

process.load("DQM.SiPixelMonitorCluster.SiPixelMonitorCluster_cfi")

process.load("DQMServices.Core.DQM_cfg")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
process.source = cms.Source("PoolSource",
    debugFlag = cms.untracked.bool(True),
    debugVebosity = cms.untracked.uint32(10),
    fileNames = cms.untracked.vstring('rfio:/castor/cern.ch/cms/store/relval/2008/6/12/RelVal-RelValSingleMuPt10-ChainTest-02/RelValSingleMuPt10/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/CMSSW_2_1_0_pre5-RelVal-ChainTest-02-IDEAL_V1-unmerged/0000/6E294919-F83D-DD11-BBF0-000423D6B358.root')
)

process.LockService = cms.Service("LockService",
    labels = cms.untracked.vstring('source')
)

#process.p1 = cms.Path(process.siPixelClusters*process.SiPixelClusterSource)
process.p1 = cms.Path(process.SiPixelClusterSource)
process.SiPixelClusterSource.saveFile = True
process.SiPixelClusterSource.isPIB = False
process.SiPixelClusterSource.slowDown = False
process.SiPixelClusterSource.modOn = True
process.SiPixelClusterSource.ladOn = False
process.SiPixelClusterSource.layOn = False
process.SiPixelClusterSource.phiOn = False
process.SiPixelClusterSource.ringOn = False
process.SiPixelClusterSource.bladeOn = False
process.SiPixelClusterSource.diskOn = False
process.DQM.collectorHost = ''

