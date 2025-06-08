# SNMP MIB module (CISCO-FIREPOWER-BIOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-BIOS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:21:40 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(CfprManagedObjectDn,
 CfprManagedObjectId,
 ciscoFirepowerMIBObjects) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-MIB",
    "CfprManagedObjectDn",
    "CfprManagedObjectId",
    "ciscoFirepowerMIBObjects")

(CfprBiosBootDevErrorCode,
 CfprBiosBootDevGrpType,
 CfprBiosBootDevOrder,
 CfprBiosDefaultAction,
 CfprBiosSupportedAction,
 CfprBiosVfACPI10SupportVpACPI10Support,
 CfprBiosVfAllUSBDevicesVpAllUSBDevices,
 CfprBiosVfAltitudeVpAltitude,
 CfprBiosVfAssertNMIOnPERRVpAssertNMIOnPERR,
 CfprBiosVfAssertNMIOnSERRVpAssertNMIOnSERR,
 CfprBiosVfBootOptionRetryVpBootOptionRetry,
 CfprBiosVfCPUPerformanceVpCPUPerformance,
 CfprBiosVfConsoleRedirectionVpBaudRate,
 CfprBiosVfConsoleRedirectionVpConsoleRedirection,
 CfprBiosVfConsoleRedirectionVpFlowControl,
 CfprBiosVfConsoleRedirectionVpLegacyOSRedirection,
 CfprBiosVfConsoleRedirectionVpPuttyKeyPad,
 CfprBiosVfConsoleRedirectionVpTerminalType,
 CfprBiosVfCoreMultiProcessingVpCoreMultiProcessing,
 CfprBiosVfDRAMClockThrottlingVpDRAMClockThrottling,
 CfprBiosVfDirectCacheAccessVpDirectCacheAccess,
 CfprBiosVfDramRefreshRateVpDramRefreshRate,
 CfprBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech,
 CfprBiosVfExecuteDisableBitVpExecuteDisableBit,
 CfprBiosVfFPRMBootModeControlVpUEFIBootMode,
 CfprBiosVfFPRMBootOrderRuleControlVpFPRMBootOrderRule,
 CfprBiosVfFRB2TimerVpFRB2Timer,
 CfprBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride,
 CfprBiosVfFrontPanelLockoutVpFrontPanelLockout,
 CfprBiosVfIntelEntrySASRAIDModuleVpSASRAID,
 CfprBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule,
 CfprBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech,
 CfprBiosVfIntelTurboBoostTechVpIntelTurboBoostTech,
 CfprBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport,
 CfprBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport,
 CfprBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping,
 CfprBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport,
 CfprBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO,
 CfprBiosVfIntelVirtualizationTechnologyVpIntelVirtTechnology,
 CfprBiosVfInterleaveConfigurationVpChannelInterleaving,
 CfprBiosVfInterleaveConfigurationVpMemoryInterleaving,
 CfprBiosVfInterleaveConfigurationVpRankInterleaving,
 CfprBiosVfLocalX2ApicVpLocalX2Apic,
 CfprBiosVfLvDIMMSupportVpLvDDRMode,
 CfprBiosVfMaxVariableMTRRSettingVpProcessorMtrr,
 CfprBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB,
 CfprBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB,
 CfprBiosVfMirroringModeVpMirroringMode,
 CfprBiosVfNUMAOptimizedVpNUMAOptimized,
 CfprBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy,
 CfprBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout,
 CfprBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer,
 CfprBiosVfOnboardSATAControllerVpOnboardSATAController,
 CfprBiosVfOnboardSATAControllerVpSATAMode,
 CfprBiosVfOnboardStorageVpOnboardSCUStorageSupport,
 CfprBiosVfOptionROMEnableVpState,
 CfprBiosVfOptionROMLoadVpLoad,
 CfprBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed,
 CfprBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed,
 CfprBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed,
 CfprBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed,
 CfprBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed,
 CfprBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed,
 CfprBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed,
 CfprBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed,
 CfprBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed,
 CfprBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed,
 CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM,
 CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM,
 CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM,
 CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM,
 CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM,
 CfprBiosVfPCISlotOptionROMEnableVpSlot10State,
 CfprBiosVfPCISlotOptionROMEnableVpSlot1State,
 CfprBiosVfPCISlotOptionROMEnableVpSlot2State,
 CfprBiosVfPCISlotOptionROMEnableVpSlot3State,
 CfprBiosVfPCISlotOptionROMEnableVpSlot4State,
 CfprBiosVfPCISlotOptionROMEnableVpSlot5State,
 CfprBiosVfPCISlotOptionROMEnableVpSlot6State,
 CfprBiosVfPCISlotOptionROMEnableVpSlot7State,
 CfprBiosVfPCISlotOptionROMEnableVpSlot8State,
 CfprBiosVfPCISlotOptionROMEnableVpSlot9State,
 CfprBiosVfPCISlotOptionROMEnableVpSlotMezzState,
 CfprBiosVfPOSTErrorPauseVpPOSTErrorPause,
 CfprBiosVfPSTATECoordinationVpPSTATECoordination,
 CfprBiosVfPackageCStateLimitVpPackageCStateLimit,
 CfprBiosVfProcessorC1EVpProcessorC1E,
 CfprBiosVfProcessorC3ReportVpProcessorC3Report,
 CfprBiosVfProcessorC6ReportVpProcessorC6Report,
 CfprBiosVfProcessorC7ReportVpProcessorC7Report,
 CfprBiosVfProcessorCStateVpProcessorCState,
 CfprBiosVfProcessorEnergyConfigurationVpEnergyPerformance,
 CfprBiosVfProcessorEnergyConfigurationVpPowerTechnology,
 CfprBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher,
 CfprBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher,
 CfprBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch,
 CfprBiosVfProcessorPrefetchConfigVpHardwarePrefetcher,
 CfprBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect,
 CfprBiosVfQuietBootVpQuietBoot,
 CfprBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss,
 CfprBiosVfScrubPoliciesVpDemandScrub,
 CfprBiosVfScrubPoliciesVpPatrolScrub,
 CfprBiosVfSelectMemoryRASConfigurationVpSelectMemoryRASConf,
 CfprBiosVfSerialPortAEnableVpSerialPortAEnable,
 CfprBiosVfSparingModeVpSparingMode,
 CfprBiosVfSriovConfigVpSriov,
 CfprBiosVfTPMSupportVpTPMSupport,
 CfprBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo,
 CfprBiosVfUSBBootConfigVpLegacyUSBSupport,
 CfprBiosVfUSBBootConfigVpMakeDeviceNonBootable,
 CfprBiosVfUSBConfigurationVpLegacyUSBSupport,
 CfprBiosVfUSBConfigurationVpXHCIMode,
 CfprBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock,
 CfprBiosVfUSBPortConfigurationVpPort6064Emulation,
 CfprBiosVfUSBPortConfigurationVpUSBPortFront,
 CfprBiosVfUSBPortConfigurationVpUSBPortInternal,
 CfprBiosVfUSBPortConfigurationVpUSBPortKVM,
 CfprBiosVfUSBPortConfigurationVpUSBPortRear,
 CfprBiosVfUSBPortConfigurationVpUSBPortSDCard,
 CfprBiosVfUSBPortConfigurationVpUSBPortVMedia,
 CfprBiosVfUSBSysIdlePowerOptimizingSettingVpUSBIdlePowerOptimize,
 CfprBiosVfVGAPriorityVpVGAPriority,
 CfprPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprBiosBootDevErrorCode",
    "CfprBiosBootDevGrpType",
    "CfprBiosBootDevOrder",
    "CfprBiosDefaultAction",
    "CfprBiosSupportedAction",
    "CfprBiosVfACPI10SupportVpACPI10Support",
    "CfprBiosVfAllUSBDevicesVpAllUSBDevices",
    "CfprBiosVfAltitudeVpAltitude",
    "CfprBiosVfAssertNMIOnPERRVpAssertNMIOnPERR",
    "CfprBiosVfAssertNMIOnSERRVpAssertNMIOnSERR",
    "CfprBiosVfBootOptionRetryVpBootOptionRetry",
    "CfprBiosVfCPUPerformanceVpCPUPerformance",
    "CfprBiosVfConsoleRedirectionVpBaudRate",
    "CfprBiosVfConsoleRedirectionVpConsoleRedirection",
    "CfprBiosVfConsoleRedirectionVpFlowControl",
    "CfprBiosVfConsoleRedirectionVpLegacyOSRedirection",
    "CfprBiosVfConsoleRedirectionVpPuttyKeyPad",
    "CfprBiosVfConsoleRedirectionVpTerminalType",
    "CfprBiosVfCoreMultiProcessingVpCoreMultiProcessing",
    "CfprBiosVfDRAMClockThrottlingVpDRAMClockThrottling",
    "CfprBiosVfDirectCacheAccessVpDirectCacheAccess",
    "CfprBiosVfDramRefreshRateVpDramRefreshRate",
    "CfprBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech",
    "CfprBiosVfExecuteDisableBitVpExecuteDisableBit",
    "CfprBiosVfFPRMBootModeControlVpUEFIBootMode",
    "CfprBiosVfFPRMBootOrderRuleControlVpFPRMBootOrderRule",
    "CfprBiosVfFRB2TimerVpFRB2Timer",
    "CfprBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride",
    "CfprBiosVfFrontPanelLockoutVpFrontPanelLockout",
    "CfprBiosVfIntelEntrySASRAIDModuleVpSASRAID",
    "CfprBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule",
    "CfprBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech",
    "CfprBiosVfIntelTurboBoostTechVpIntelTurboBoostTech",
    "CfprBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport",
    "CfprBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport",
    "CfprBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping",
    "CfprBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport",
    "CfprBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO",
    "CfprBiosVfIntelVirtualizationTechnologyVpIntelVirtTechnology",
    "CfprBiosVfInterleaveConfigurationVpChannelInterleaving",
    "CfprBiosVfInterleaveConfigurationVpMemoryInterleaving",
    "CfprBiosVfInterleaveConfigurationVpRankInterleaving",
    "CfprBiosVfLocalX2ApicVpLocalX2Apic",
    "CfprBiosVfLvDIMMSupportVpLvDDRMode",
    "CfprBiosVfMaxVariableMTRRSettingVpProcessorMtrr",
    "CfprBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB",
    "CfprBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB",
    "CfprBiosVfMirroringModeVpMirroringMode",
    "CfprBiosVfNUMAOptimizedVpNUMAOptimized",
    "CfprBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy",
    "CfprBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout",
    "CfprBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer",
    "CfprBiosVfOnboardSATAControllerVpOnboardSATAController",
    "CfprBiosVfOnboardSATAControllerVpSATAMode",
    "CfprBiosVfOnboardStorageVpOnboardSCUStorageSupport",
    "CfprBiosVfOptionROMEnableVpState",
    "CfprBiosVfOptionROMLoadVpLoad",
    "CfprBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed",
    "CfprBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed",
    "CfprBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed",
    "CfprBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed",
    "CfprBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed",
    "CfprBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed",
    "CfprBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed",
    "CfprBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed",
    "CfprBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed",
    "CfprBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed",
    "CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM",
    "CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM",
    "CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM",
    "CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM",
    "CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM",
    "CfprBiosVfPCISlotOptionROMEnableVpSlot10State",
    "CfprBiosVfPCISlotOptionROMEnableVpSlot1State",
    "CfprBiosVfPCISlotOptionROMEnableVpSlot2State",
    "CfprBiosVfPCISlotOptionROMEnableVpSlot3State",
    "CfprBiosVfPCISlotOptionROMEnableVpSlot4State",
    "CfprBiosVfPCISlotOptionROMEnableVpSlot5State",
    "CfprBiosVfPCISlotOptionROMEnableVpSlot6State",
    "CfprBiosVfPCISlotOptionROMEnableVpSlot7State",
    "CfprBiosVfPCISlotOptionROMEnableVpSlot8State",
    "CfprBiosVfPCISlotOptionROMEnableVpSlot9State",
    "CfprBiosVfPCISlotOptionROMEnableVpSlotMezzState",
    "CfprBiosVfPOSTErrorPauseVpPOSTErrorPause",
    "CfprBiosVfPSTATECoordinationVpPSTATECoordination",
    "CfprBiosVfPackageCStateLimitVpPackageCStateLimit",
    "CfprBiosVfProcessorC1EVpProcessorC1E",
    "CfprBiosVfProcessorC3ReportVpProcessorC3Report",
    "CfprBiosVfProcessorC6ReportVpProcessorC6Report",
    "CfprBiosVfProcessorC7ReportVpProcessorC7Report",
    "CfprBiosVfProcessorCStateVpProcessorCState",
    "CfprBiosVfProcessorEnergyConfigurationVpEnergyPerformance",
    "CfprBiosVfProcessorEnergyConfigurationVpPowerTechnology",
    "CfprBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher",
    "CfprBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher",
    "CfprBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch",
    "CfprBiosVfProcessorPrefetchConfigVpHardwarePrefetcher",
    "CfprBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect",
    "CfprBiosVfQuietBootVpQuietBoot",
    "CfprBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss",
    "CfprBiosVfScrubPoliciesVpDemandScrub",
    "CfprBiosVfScrubPoliciesVpPatrolScrub",
    "CfprBiosVfSelectMemoryRASConfigurationVpSelectMemoryRASConf",
    "CfprBiosVfSerialPortAEnableVpSerialPortAEnable",
    "CfprBiosVfSparingModeVpSparingMode",
    "CfprBiosVfSriovConfigVpSriov",
    "CfprBiosVfTPMSupportVpTPMSupport",
    "CfprBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo",
    "CfprBiosVfUSBBootConfigVpLegacyUSBSupport",
    "CfprBiosVfUSBBootConfigVpMakeDeviceNonBootable",
    "CfprBiosVfUSBConfigurationVpLegacyUSBSupport",
    "CfprBiosVfUSBConfigurationVpXHCIMode",
    "CfprBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock",
    "CfprBiosVfUSBPortConfigurationVpPort6064Emulation",
    "CfprBiosVfUSBPortConfigurationVpUSBPortFront",
    "CfprBiosVfUSBPortConfigurationVpUSBPortInternal",
    "CfprBiosVfUSBPortConfigurationVpUSBPortKVM",
    "CfprBiosVfUSBPortConfigurationVpUSBPortRear",
    "CfprBiosVfUSBPortConfigurationVpUSBPortSDCard",
    "CfprBiosVfUSBPortConfigurationVpUSBPortVMedia",
    "CfprBiosVfUSBSysIdlePowerOptimizingSettingVpUSBIdlePowerOptimize",
    "CfprBiosVfVGAPriorityVpVGAPriority",
    "CfprPolicyPolicyOwner")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoAlarmSeverity,
 CiscoInetAddressMask,
 CiscoNetworkAddress,
 TimeIntervalSec,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "CiscoInetAddressMask",
    "CiscoNetworkAddress",
    "TimeIntervalSec",
    "Unsigned64")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowPointer,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cfprBiosObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprBiosBOTTable_Object = MibTable
cfprBiosBOTTable = _CfprBiosBOTTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cfprBiosBOTTable.setStatus("current")
_CfprBiosBOTEntry_Object = MibTableRow
cfprBiosBOTEntry = _CfprBiosBOTEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 1, 1)
)
cfprBiosBOTEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosBOTInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosBOTEntry.setStatus("current")
_CfprBiosBOTInstanceId_Type = CfprManagedObjectId
_CfprBiosBOTInstanceId_Object = MibTableColumn
cfprBiosBOTInstanceId = _CfprBiosBOTInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 1, 1, 1),
    _CfprBiosBOTInstanceId_Type()
)
cfprBiosBOTInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosBOTInstanceId.setStatus("current")
_CfprBiosBOTDn_Type = CfprManagedObjectDn
_CfprBiosBOTDn_Object = MibTableColumn
cfprBiosBOTDn = _CfprBiosBOTDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 1, 1, 2),
    _CfprBiosBOTDn_Type()
)
cfprBiosBOTDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosBOTDn.setStatus("current")
_CfprBiosBOTRn_Type = SnmpAdminString
_CfprBiosBOTRn_Object = MibTableColumn
cfprBiosBOTRn = _CfprBiosBOTRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 1, 1, 3),
    _CfprBiosBOTRn_Type()
)
cfprBiosBOTRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosBOTRn.setStatus("current")
_CfprBiosBOTLastUpdate_Type = DateAndTime
_CfprBiosBOTLastUpdate_Object = MibTableColumn
cfprBiosBOTLastUpdate = _CfprBiosBOTLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 1, 1, 4),
    _CfprBiosBOTLastUpdate_Type()
)
cfprBiosBOTLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosBOTLastUpdate.setStatus("current")
_CfprBiosBootDevTable_Object = MibTable
cfprBiosBootDevTable = _CfprBiosBootDevTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cfprBiosBootDevTable.setStatus("current")
_CfprBiosBootDevEntry_Object = MibTableRow
cfprBiosBootDevEntry = _CfprBiosBootDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 2, 1)
)
cfprBiosBootDevEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosBootDevInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosBootDevEntry.setStatus("current")
_CfprBiosBootDevInstanceId_Type = CfprManagedObjectId
_CfprBiosBootDevInstanceId_Object = MibTableColumn
cfprBiosBootDevInstanceId = _CfprBiosBootDevInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 2, 1, 1),
    _CfprBiosBootDevInstanceId_Type()
)
cfprBiosBootDevInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosBootDevInstanceId.setStatus("current")
_CfprBiosBootDevDn_Type = CfprManagedObjectDn
_CfprBiosBootDevDn_Object = MibTableColumn
cfprBiosBootDevDn = _CfprBiosBootDevDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 2, 1, 2),
    _CfprBiosBootDevDn_Type()
)
cfprBiosBootDevDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosBootDevDn.setStatus("current")
_CfprBiosBootDevRn_Type = SnmpAdminString
_CfprBiosBootDevRn_Object = MibTableColumn
cfprBiosBootDevRn = _CfprBiosBootDevRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 2, 1, 3),
    _CfprBiosBootDevRn_Type()
)
cfprBiosBootDevRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosBootDevRn.setStatus("current")
_CfprBiosBootDevDescr_Type = SnmpAdminString
_CfprBiosBootDevDescr_Object = MibTableColumn
cfprBiosBootDevDescr = _CfprBiosBootDevDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 2, 1, 4),
    _CfprBiosBootDevDescr_Type()
)
cfprBiosBootDevDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosBootDevDescr.setStatus("current")
_CfprBiosBootDevDeviceName_Type = SnmpAdminString
_CfprBiosBootDevDeviceName_Object = MibTableColumn
cfprBiosBootDevDeviceName = _CfprBiosBootDevDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 2, 1, 5),
    _CfprBiosBootDevDeviceName_Type()
)
cfprBiosBootDevDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosBootDevDeviceName.setStatus("current")
_CfprBiosBootDevErrValue_Type = CfprBiosBootDevErrorCode
_CfprBiosBootDevErrValue_Object = MibTableColumn
cfprBiosBootDevErrValue = _CfprBiosBootDevErrValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 2, 1, 6),
    _CfprBiosBootDevErrValue_Type()
)
cfprBiosBootDevErrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosBootDevErrValue.setStatus("current")
_CfprBiosBootDevOrder_Type = CfprBiosBootDevOrder
_CfprBiosBootDevOrder_Object = MibTableColumn
cfprBiosBootDevOrder = _CfprBiosBootDevOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 2, 1, 7),
    _CfprBiosBootDevOrder_Type()
)
cfprBiosBootDevOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosBootDevOrder.setStatus("current")
_CfprBiosBootDevGrpTable_Object = MibTable
cfprBiosBootDevGrpTable = _CfprBiosBootDevGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 3)
)
if mibBuilder.loadTexts:
    cfprBiosBootDevGrpTable.setStatus("current")
_CfprBiosBootDevGrpEntry_Object = MibTableRow
cfprBiosBootDevGrpEntry = _CfprBiosBootDevGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 3, 1)
)
cfprBiosBootDevGrpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosBootDevGrpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosBootDevGrpEntry.setStatus("current")
_CfprBiosBootDevGrpInstanceId_Type = CfprManagedObjectId
_CfprBiosBootDevGrpInstanceId_Object = MibTableColumn
cfprBiosBootDevGrpInstanceId = _CfprBiosBootDevGrpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 3, 1, 1),
    _CfprBiosBootDevGrpInstanceId_Type()
)
cfprBiosBootDevGrpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosBootDevGrpInstanceId.setStatus("current")
_CfprBiosBootDevGrpDn_Type = CfprManagedObjectDn
_CfprBiosBootDevGrpDn_Object = MibTableColumn
cfprBiosBootDevGrpDn = _CfprBiosBootDevGrpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 3, 1, 2),
    _CfprBiosBootDevGrpDn_Type()
)
cfprBiosBootDevGrpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosBootDevGrpDn.setStatus("current")
_CfprBiosBootDevGrpRn_Type = SnmpAdminString
_CfprBiosBootDevGrpRn_Object = MibTableColumn
cfprBiosBootDevGrpRn = _CfprBiosBootDevGrpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 3, 1, 3),
    _CfprBiosBootDevGrpRn_Type()
)
cfprBiosBootDevGrpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosBootDevGrpRn.setStatus("current")
_CfprBiosBootDevGrpDescr_Type = SnmpAdminString
_CfprBiosBootDevGrpDescr_Object = MibTableColumn
cfprBiosBootDevGrpDescr = _CfprBiosBootDevGrpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 3, 1, 4),
    _CfprBiosBootDevGrpDescr_Type()
)
cfprBiosBootDevGrpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosBootDevGrpDescr.setStatus("current")
_CfprBiosBootDevGrpDeviceName_Type = SnmpAdminString
_CfprBiosBootDevGrpDeviceName_Object = MibTableColumn
cfprBiosBootDevGrpDeviceName = _CfprBiosBootDevGrpDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 3, 1, 5),
    _CfprBiosBootDevGrpDeviceName_Type()
)
cfprBiosBootDevGrpDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosBootDevGrpDeviceName.setStatus("current")
_CfprBiosBootDevGrpErrVal_Type = CfprBiosBootDevErrorCode
_CfprBiosBootDevGrpErrVal_Object = MibTableColumn
cfprBiosBootDevGrpErrVal = _CfprBiosBootDevGrpErrVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 3, 1, 6),
    _CfprBiosBootDevGrpErrVal_Type()
)
cfprBiosBootDevGrpErrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosBootDevGrpErrVal.setStatus("current")
_CfprBiosBootDevGrpOrder_Type = CfprBiosBootDevOrder
_CfprBiosBootDevGrpOrder_Object = MibTableColumn
cfprBiosBootDevGrpOrder = _CfprBiosBootDevGrpOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 3, 1, 7),
    _CfprBiosBootDevGrpOrder_Type()
)
cfprBiosBootDevGrpOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosBootDevGrpOrder.setStatus("current")
_CfprBiosBootDevGrpType_Type = CfprBiosBootDevGrpType
_CfprBiosBootDevGrpType_Object = MibTableColumn
cfprBiosBootDevGrpType = _CfprBiosBootDevGrpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 3, 1, 8),
    _CfprBiosBootDevGrpType_Type()
)
cfprBiosBootDevGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosBootDevGrpType.setStatus("current")
_CfprBiosFeatureRefTable_Object = MibTable
cfprBiosFeatureRefTable = _CfprBiosFeatureRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 4)
)
if mibBuilder.loadTexts:
    cfprBiosFeatureRefTable.setStatus("current")
_CfprBiosFeatureRefEntry_Object = MibTableRow
cfprBiosFeatureRefEntry = _CfprBiosFeatureRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 4, 1)
)
cfprBiosFeatureRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosFeatureRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosFeatureRefEntry.setStatus("current")
_CfprBiosFeatureRefInstanceId_Type = CfprManagedObjectId
_CfprBiosFeatureRefInstanceId_Object = MibTableColumn
cfprBiosFeatureRefInstanceId = _CfprBiosFeatureRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 4, 1, 1),
    _CfprBiosFeatureRefInstanceId_Type()
)
cfprBiosFeatureRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosFeatureRefInstanceId.setStatus("current")
_CfprBiosFeatureRefDn_Type = CfprManagedObjectDn
_CfprBiosFeatureRefDn_Object = MibTableColumn
cfprBiosFeatureRefDn = _CfprBiosFeatureRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 4, 1, 2),
    _CfprBiosFeatureRefDn_Type()
)
cfprBiosFeatureRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosFeatureRefDn.setStatus("current")
_CfprBiosFeatureRefRn_Type = SnmpAdminString
_CfprBiosFeatureRefRn_Object = MibTableColumn
cfprBiosFeatureRefRn = _CfprBiosFeatureRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 4, 1, 3),
    _CfprBiosFeatureRefRn_Type()
)
cfprBiosFeatureRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosFeatureRefRn.setStatus("current")
_CfprBiosFeatureRefFtrMoClassName_Type = SnmpAdminString
_CfprBiosFeatureRefFtrMoClassName_Object = MibTableColumn
cfprBiosFeatureRefFtrMoClassName = _CfprBiosFeatureRefFtrMoClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 4, 1, 4),
    _CfprBiosFeatureRefFtrMoClassName_Type()
)
cfprBiosFeatureRefFtrMoClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosFeatureRefFtrMoClassName.setStatus("current")
_CfprBiosFeatureRefIsSupported_Type = CfprBiosSupportedAction
_CfprBiosFeatureRefIsSupported_Object = MibTableColumn
cfprBiosFeatureRefIsSupported = _CfprBiosFeatureRefIsSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 4, 1, 5),
    _CfprBiosFeatureRefIsSupported_Type()
)
cfprBiosFeatureRefIsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosFeatureRefIsSupported.setStatus("current")
_CfprBiosFeatureRefName_Type = SnmpAdminString
_CfprBiosFeatureRefName_Object = MibTableColumn
cfprBiosFeatureRefName = _CfprBiosFeatureRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 4, 1, 6),
    _CfprBiosFeatureRefName_Type()
)
cfprBiosFeatureRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosFeatureRefName.setStatus("current")
_CfprBiosParameterRefTable_Object = MibTable
cfprBiosParameterRefTable = _CfprBiosParameterRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 5)
)
if mibBuilder.loadTexts:
    cfprBiosParameterRefTable.setStatus("current")
_CfprBiosParameterRefEntry_Object = MibTableRow
cfprBiosParameterRefEntry = _CfprBiosParameterRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 5, 1)
)
cfprBiosParameterRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosParameterRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosParameterRefEntry.setStatus("current")
_CfprBiosParameterRefInstanceId_Type = CfprManagedObjectId
_CfprBiosParameterRefInstanceId_Object = MibTableColumn
cfprBiosParameterRefInstanceId = _CfprBiosParameterRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 5, 1, 1),
    _CfprBiosParameterRefInstanceId_Type()
)
cfprBiosParameterRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosParameterRefInstanceId.setStatus("current")
_CfprBiosParameterRefDn_Type = CfprManagedObjectDn
_CfprBiosParameterRefDn_Object = MibTableColumn
cfprBiosParameterRefDn = _CfprBiosParameterRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 5, 1, 2),
    _CfprBiosParameterRefDn_Type()
)
cfprBiosParameterRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosParameterRefDn.setStatus("current")
_CfprBiosParameterRefRn_Type = SnmpAdminString
_CfprBiosParameterRefRn_Object = MibTableColumn
cfprBiosParameterRefRn = _CfprBiosParameterRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 5, 1, 3),
    _CfprBiosParameterRefRn_Type()
)
cfprBiosParameterRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosParameterRefRn.setStatus("current")
_CfprBiosParameterRefIsSupported_Type = CfprBiosSupportedAction
_CfprBiosParameterRefIsSupported_Object = MibTableColumn
cfprBiosParameterRefIsSupported = _CfprBiosParameterRefIsSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 5, 1, 4),
    _CfprBiosParameterRefIsSupported_Type()
)
cfprBiosParameterRefIsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosParameterRefIsSupported.setStatus("current")
_CfprBiosParameterRefName_Type = SnmpAdminString
_CfprBiosParameterRefName_Object = MibTableColumn
cfprBiosParameterRefName = _CfprBiosParameterRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 5, 1, 5),
    _CfprBiosParameterRefName_Type()
)
cfprBiosParameterRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosParameterRefName.setStatus("current")
_CfprBiosParameterRefPropertyName_Type = SnmpAdminString
_CfprBiosParameterRefPropertyName_Object = MibTableColumn
cfprBiosParameterRefPropertyName = _CfprBiosParameterRefPropertyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 5, 1, 6),
    _CfprBiosParameterRefPropertyName_Type()
)
cfprBiosParameterRefPropertyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosParameterRefPropertyName.setStatus("current")
_CfprBiosRefTable_Object = MibTable
cfprBiosRefTable = _CfprBiosRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 6)
)
if mibBuilder.loadTexts:
    cfprBiosRefTable.setStatus("current")
_CfprBiosRefEntry_Object = MibTableRow
cfprBiosRefEntry = _CfprBiosRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 6, 1)
)
cfprBiosRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosRefEntry.setStatus("current")
_CfprBiosRefInstanceId_Type = CfprManagedObjectId
_CfprBiosRefInstanceId_Object = MibTableColumn
cfprBiosRefInstanceId = _CfprBiosRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 6, 1, 1),
    _CfprBiosRefInstanceId_Type()
)
cfprBiosRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosRefInstanceId.setStatus("current")
_CfprBiosRefDn_Type = CfprManagedObjectDn
_CfprBiosRefDn_Object = MibTableColumn
cfprBiosRefDn = _CfprBiosRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 6, 1, 2),
    _CfprBiosRefDn_Type()
)
cfprBiosRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosRefDn.setStatus("current")
_CfprBiosRefRn_Type = SnmpAdminString
_CfprBiosRefRn_Object = MibTableColumn
cfprBiosRefRn = _CfprBiosRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 6, 1, 3),
    _CfprBiosRefRn_Type()
)
cfprBiosRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosRefRn.setStatus("current")
_CfprBiosRefIsSupported_Type = CfprBiosSupportedAction
_CfprBiosRefIsSupported_Object = MibTableColumn
cfprBiosRefIsSupported = _CfprBiosRefIsSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 6, 1, 4),
    _CfprBiosRefIsSupported_Type()
)
cfprBiosRefIsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosRefIsSupported.setStatus("current")
_CfprBiosSettingRefTable_Object = MibTable
cfprBiosSettingRefTable = _CfprBiosSettingRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 7)
)
if mibBuilder.loadTexts:
    cfprBiosSettingRefTable.setStatus("current")
_CfprBiosSettingRefEntry_Object = MibTableRow
cfprBiosSettingRefEntry = _CfprBiosSettingRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 7, 1)
)
cfprBiosSettingRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosSettingRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosSettingRefEntry.setStatus("current")
_CfprBiosSettingRefInstanceId_Type = CfprManagedObjectId
_CfprBiosSettingRefInstanceId_Object = MibTableColumn
cfprBiosSettingRefInstanceId = _CfprBiosSettingRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 7, 1, 1),
    _CfprBiosSettingRefInstanceId_Type()
)
cfprBiosSettingRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosSettingRefInstanceId.setStatus("current")
_CfprBiosSettingRefDn_Type = CfprManagedObjectDn
_CfprBiosSettingRefDn_Object = MibTableColumn
cfprBiosSettingRefDn = _CfprBiosSettingRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 7, 1, 2),
    _CfprBiosSettingRefDn_Type()
)
cfprBiosSettingRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosSettingRefDn.setStatus("current")
_CfprBiosSettingRefRn_Type = SnmpAdminString
_CfprBiosSettingRefRn_Object = MibTableColumn
cfprBiosSettingRefRn = _CfprBiosSettingRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 7, 1, 3),
    _CfprBiosSettingRefRn_Type()
)
cfprBiosSettingRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosSettingRefRn.setStatus("current")
_CfprBiosSettingRefConstantName_Type = SnmpAdminString
_CfprBiosSettingRefConstantName_Object = MibTableColumn
cfprBiosSettingRefConstantName = _CfprBiosSettingRefConstantName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 7, 1, 4),
    _CfprBiosSettingRefConstantName_Type()
)
cfprBiosSettingRefConstantName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosSettingRefConstantName.setStatus("current")
_CfprBiosSettingRefIsDefault_Type = CfprBiosDefaultAction
_CfprBiosSettingRefIsDefault_Object = MibTableColumn
cfprBiosSettingRefIsDefault = _CfprBiosSettingRefIsDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 7, 1, 5),
    _CfprBiosSettingRefIsDefault_Type()
)
cfprBiosSettingRefIsDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosSettingRefIsDefault.setStatus("current")
_CfprBiosSettingRefIsSupported_Type = CfprBiosSupportedAction
_CfprBiosSettingRefIsSupported_Object = MibTableColumn
cfprBiosSettingRefIsSupported = _CfprBiosSettingRefIsSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 7, 1, 6),
    _CfprBiosSettingRefIsSupported_Type()
)
cfprBiosSettingRefIsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosSettingRefIsSupported.setStatus("current")
_CfprBiosSettingRefName_Type = SnmpAdminString
_CfprBiosSettingRefName_Object = MibTableColumn
cfprBiosSettingRefName = _CfprBiosSettingRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 7, 1, 7),
    _CfprBiosSettingRefName_Type()
)
cfprBiosSettingRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosSettingRefName.setStatus("current")
_CfprBiosSettingsTable_Object = MibTable
cfprBiosSettingsTable = _CfprBiosSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 8)
)
if mibBuilder.loadTexts:
    cfprBiosSettingsTable.setStatus("current")
_CfprBiosSettingsEntry_Object = MibTableRow
cfprBiosSettingsEntry = _CfprBiosSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 8, 1)
)
cfprBiosSettingsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosSettingsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosSettingsEntry.setStatus("current")
_CfprBiosSettingsInstanceId_Type = CfprManagedObjectId
_CfprBiosSettingsInstanceId_Object = MibTableColumn
cfprBiosSettingsInstanceId = _CfprBiosSettingsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 8, 1, 1),
    _CfprBiosSettingsInstanceId_Type()
)
cfprBiosSettingsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosSettingsInstanceId.setStatus("current")
_CfprBiosSettingsDn_Type = CfprManagedObjectDn
_CfprBiosSettingsDn_Object = MibTableColumn
cfprBiosSettingsDn = _CfprBiosSettingsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 8, 1, 2),
    _CfprBiosSettingsDn_Type()
)
cfprBiosSettingsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosSettingsDn.setStatus("current")
_CfprBiosSettingsRn_Type = SnmpAdminString
_CfprBiosSettingsRn_Object = MibTableColumn
cfprBiosSettingsRn = _CfprBiosSettingsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 8, 1, 3),
    _CfprBiosSettingsRn_Type()
)
cfprBiosSettingsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosSettingsRn.setStatus("current")
_CfprBiosUnitTable_Object = MibTable
cfprBiosUnitTable = _CfprBiosUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 9)
)
if mibBuilder.loadTexts:
    cfprBiosUnitTable.setStatus("current")
_CfprBiosUnitEntry_Object = MibTableRow
cfprBiosUnitEntry = _CfprBiosUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 9, 1)
)
cfprBiosUnitEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosUnitInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosUnitEntry.setStatus("current")
_CfprBiosUnitInstanceId_Type = CfprManagedObjectId
_CfprBiosUnitInstanceId_Object = MibTableColumn
cfprBiosUnitInstanceId = _CfprBiosUnitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 9, 1, 1),
    _CfprBiosUnitInstanceId_Type()
)
cfprBiosUnitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosUnitInstanceId.setStatus("current")
_CfprBiosUnitDn_Type = CfprManagedObjectDn
_CfprBiosUnitDn_Object = MibTableColumn
cfprBiosUnitDn = _CfprBiosUnitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 9, 1, 2),
    _CfprBiosUnitDn_Type()
)
cfprBiosUnitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosUnitDn.setStatus("current")
_CfprBiosUnitRn_Type = SnmpAdminString
_CfprBiosUnitRn_Object = MibTableColumn
cfprBiosUnitRn = _CfprBiosUnitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 9, 1, 3),
    _CfprBiosUnitRn_Type()
)
cfprBiosUnitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosUnitRn.setStatus("current")
_CfprBiosUnitInitSeq_Type = SnmpAdminString
_CfprBiosUnitInitSeq_Object = MibTableColumn
cfprBiosUnitInitSeq = _CfprBiosUnitInitSeq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 9, 1, 4),
    _CfprBiosUnitInitSeq_Type()
)
cfprBiosUnitInitSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosUnitInitSeq.setStatus("current")
_CfprBiosUnitInitTs_Type = DateAndTime
_CfprBiosUnitInitTs_Object = MibTableColumn
cfprBiosUnitInitTs = _CfprBiosUnitInitTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 9, 1, 5),
    _CfprBiosUnitInitTs_Type()
)
cfprBiosUnitInitTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosUnitInitTs.setStatus("current")
_CfprBiosUnitModel_Type = SnmpAdminString
_CfprBiosUnitModel_Object = MibTableColumn
cfprBiosUnitModel = _CfprBiosUnitModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 9, 1, 6),
    _CfprBiosUnitModel_Type()
)
cfprBiosUnitModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosUnitModel.setStatus("current")
_CfprBiosUnitRevision_Type = SnmpAdminString
_CfprBiosUnitRevision_Object = MibTableColumn
cfprBiosUnitRevision = _CfprBiosUnitRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 9, 1, 7),
    _CfprBiosUnitRevision_Type()
)
cfprBiosUnitRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosUnitRevision.setStatus("current")
_CfprBiosUnitSerial_Type = SnmpAdminString
_CfprBiosUnitSerial_Object = MibTableColumn
cfprBiosUnitSerial = _CfprBiosUnitSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 9, 1, 8),
    _CfprBiosUnitSerial_Type()
)
cfprBiosUnitSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosUnitSerial.setStatus("current")
_CfprBiosUnitVendor_Type = SnmpAdminString
_CfprBiosUnitVendor_Object = MibTableColumn
cfprBiosUnitVendor = _CfprBiosUnitVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 9, 1, 9),
    _CfprBiosUnitVendor_Type()
)
cfprBiosUnitVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosUnitVendor.setStatus("current")
_CfprBiosVIdentityParamsTable_Object = MibTable
cfprBiosVIdentityParamsTable = _CfprBiosVIdentityParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 10)
)
if mibBuilder.loadTexts:
    cfprBiosVIdentityParamsTable.setStatus("current")
_CfprBiosVIdentityParamsEntry_Object = MibTableRow
cfprBiosVIdentityParamsEntry = _CfprBiosVIdentityParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 10, 1)
)
cfprBiosVIdentityParamsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVIdentityParamsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVIdentityParamsEntry.setStatus("current")
_CfprBiosVIdentityParamsInstanceId_Type = CfprManagedObjectId
_CfprBiosVIdentityParamsInstanceId_Object = MibTableColumn
cfprBiosVIdentityParamsInstanceId = _CfprBiosVIdentityParamsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 10, 1, 1),
    _CfprBiosVIdentityParamsInstanceId_Type()
)
cfprBiosVIdentityParamsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVIdentityParamsInstanceId.setStatus("current")
_CfprBiosVIdentityParamsDn_Type = CfprManagedObjectDn
_CfprBiosVIdentityParamsDn_Object = MibTableColumn
cfprBiosVIdentityParamsDn = _CfprBiosVIdentityParamsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 10, 1, 2),
    _CfprBiosVIdentityParamsDn_Type()
)
cfprBiosVIdentityParamsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVIdentityParamsDn.setStatus("current")
_CfprBiosVIdentityParamsRn_Type = SnmpAdminString
_CfprBiosVIdentityParamsRn_Object = MibTableColumn
cfprBiosVIdentityParamsRn = _CfprBiosVIdentityParamsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 10, 1, 3),
    _CfprBiosVIdentityParamsRn_Type()
)
cfprBiosVIdentityParamsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVIdentityParamsRn.setStatus("current")
_CfprBiosVIdentityParamsLsServerName_Type = SnmpAdminString
_CfprBiosVIdentityParamsLsServerName_Object = MibTableColumn
cfprBiosVIdentityParamsLsServerName = _CfprBiosVIdentityParamsLsServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 10, 1, 4),
    _CfprBiosVIdentityParamsLsServerName_Type()
)
cfprBiosVIdentityParamsLsServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVIdentityParamsLsServerName.setStatus("current")
_CfprBiosVIdentityParamsLsServerTmplName_Type = SnmpAdminString
_CfprBiosVIdentityParamsLsServerTmplName_Object = MibTableColumn
cfprBiosVIdentityParamsLsServerTmplName = _CfprBiosVIdentityParamsLsServerTmplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 10, 1, 5),
    _CfprBiosVIdentityParamsLsServerTmplName_Type()
)
cfprBiosVIdentityParamsLsServerTmplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVIdentityParamsLsServerTmplName.setStatus("current")
_CfprBiosVIdentityParamsSysName_Type = SnmpAdminString
_CfprBiosVIdentityParamsSysName_Object = MibTableColumn
cfprBiosVIdentityParamsSysName = _CfprBiosVIdentityParamsSysName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 10, 1, 6),
    _CfprBiosVIdentityParamsSysName_Type()
)
cfprBiosVIdentityParamsSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVIdentityParamsSysName.setStatus("current")
_CfprBiosVProfileTable_Object = MibTable
cfprBiosVProfileTable = _CfprBiosVProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 11)
)
if mibBuilder.loadTexts:
    cfprBiosVProfileTable.setStatus("current")
_CfprBiosVProfileEntry_Object = MibTableRow
cfprBiosVProfileEntry = _CfprBiosVProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 11, 1)
)
cfprBiosVProfileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVProfileEntry.setStatus("current")
_CfprBiosVProfileInstanceId_Type = CfprManagedObjectId
_CfprBiosVProfileInstanceId_Object = MibTableColumn
cfprBiosVProfileInstanceId = _CfprBiosVProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 11, 1, 1),
    _CfprBiosVProfileInstanceId_Type()
)
cfprBiosVProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVProfileInstanceId.setStatus("current")
_CfprBiosVProfileDn_Type = CfprManagedObjectDn
_CfprBiosVProfileDn_Object = MibTableColumn
cfprBiosVProfileDn = _CfprBiosVProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 11, 1, 2),
    _CfprBiosVProfileDn_Type()
)
cfprBiosVProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVProfileDn.setStatus("current")
_CfprBiosVProfileRn_Type = SnmpAdminString
_CfprBiosVProfileRn_Object = MibTableColumn
cfprBiosVProfileRn = _CfprBiosVProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 11, 1, 3),
    _CfprBiosVProfileRn_Type()
)
cfprBiosVProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVProfileRn.setStatus("current")
_CfprBiosVProfileDescr_Type = SnmpAdminString
_CfprBiosVProfileDescr_Object = MibTableColumn
cfprBiosVProfileDescr = _CfprBiosVProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 11, 1, 4),
    _CfprBiosVProfileDescr_Type()
)
cfprBiosVProfileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVProfileDescr.setStatus("current")
_CfprBiosVProfileIntId_Type = SnmpAdminString
_CfprBiosVProfileIntId_Object = MibTableColumn
cfprBiosVProfileIntId = _CfprBiosVProfileIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 11, 1, 5),
    _CfprBiosVProfileIntId_Type()
)
cfprBiosVProfileIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVProfileIntId.setStatus("current")
_CfprBiosVProfileName_Type = SnmpAdminString
_CfprBiosVProfileName_Object = MibTableColumn
cfprBiosVProfileName = _CfprBiosVProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 11, 1, 6),
    _CfprBiosVProfileName_Type()
)
cfprBiosVProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVProfileName.setStatus("current")
_CfprBiosVProfilePolicyLevel_Type = Gauge32
_CfprBiosVProfilePolicyLevel_Object = MibTableColumn
cfprBiosVProfilePolicyLevel = _CfprBiosVProfilePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 11, 1, 7),
    _CfprBiosVProfilePolicyLevel_Type()
)
cfprBiosVProfilePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVProfilePolicyLevel.setStatus("current")
_CfprBiosVProfilePolicyOwner_Type = CfprPolicyPolicyOwner
_CfprBiosVProfilePolicyOwner_Object = MibTableColumn
cfprBiosVProfilePolicyOwner = _CfprBiosVProfilePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 11, 1, 8),
    _CfprBiosVProfilePolicyOwner_Type()
)
cfprBiosVProfilePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVProfilePolicyOwner.setStatus("current")
_CfprBiosVProfileRebootOnUpdate_Type = TruthValue
_CfprBiosVProfileRebootOnUpdate_Object = MibTableColumn
cfprBiosVProfileRebootOnUpdate = _CfprBiosVProfileRebootOnUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 11, 1, 9),
    _CfprBiosVProfileRebootOnUpdate_Type()
)
cfprBiosVProfileRebootOnUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVProfileRebootOnUpdate.setStatus("current")
_CfprBiosVfACPI10SupportTable_Object = MibTable
cfprBiosVfACPI10SupportTable = _CfprBiosVfACPI10SupportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 12)
)
if mibBuilder.loadTexts:
    cfprBiosVfACPI10SupportTable.setStatus("current")
_CfprBiosVfACPI10SupportEntry_Object = MibTableRow
cfprBiosVfACPI10SupportEntry = _CfprBiosVfACPI10SupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 12, 1)
)
cfprBiosVfACPI10SupportEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfACPI10SupportInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfACPI10SupportEntry.setStatus("current")
_CfprBiosVfACPI10SupportInstanceId_Type = CfprManagedObjectId
_CfprBiosVfACPI10SupportInstanceId_Object = MibTableColumn
cfprBiosVfACPI10SupportInstanceId = _CfprBiosVfACPI10SupportInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 12, 1, 1),
    _CfprBiosVfACPI10SupportInstanceId_Type()
)
cfprBiosVfACPI10SupportInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfACPI10SupportInstanceId.setStatus("current")
_CfprBiosVfACPI10SupportDn_Type = CfprManagedObjectDn
_CfprBiosVfACPI10SupportDn_Object = MibTableColumn
cfprBiosVfACPI10SupportDn = _CfprBiosVfACPI10SupportDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 12, 1, 2),
    _CfprBiosVfACPI10SupportDn_Type()
)
cfprBiosVfACPI10SupportDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfACPI10SupportDn.setStatus("current")
_CfprBiosVfACPI10SupportRn_Type = SnmpAdminString
_CfprBiosVfACPI10SupportRn_Object = MibTableColumn
cfprBiosVfACPI10SupportRn = _CfprBiosVfACPI10SupportRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 12, 1, 3),
    _CfprBiosVfACPI10SupportRn_Type()
)
cfprBiosVfACPI10SupportRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfACPI10SupportRn.setStatus("current")
_CfprBiosVfACPI10SupportVpACPI10Support_Type = CfprBiosVfACPI10SupportVpACPI10Support
_CfprBiosVfACPI10SupportVpACPI10Support_Object = MibTableColumn
cfprBiosVfACPI10SupportVpACPI10Support = _CfprBiosVfACPI10SupportVpACPI10Support_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 12, 1, 4),
    _CfprBiosVfACPI10SupportVpACPI10Support_Type()
)
cfprBiosVfACPI10SupportVpACPI10Support.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfACPI10SupportVpACPI10Support.setStatus("current")
_CfprBiosVfACPI10SupportSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfACPI10SupportSupportedByDefault_Object = MibTableColumn
cfprBiosVfACPI10SupportSupportedByDefault = _CfprBiosVfACPI10SupportSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 12, 1, 5),
    _CfprBiosVfACPI10SupportSupportedByDefault_Type()
)
cfprBiosVfACPI10SupportSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfACPI10SupportSupportedByDefault.setStatus("current")
_CfprBiosVfAllUSBDevicesTable_Object = MibTable
cfprBiosVfAllUSBDevicesTable = _CfprBiosVfAllUSBDevicesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 13)
)
if mibBuilder.loadTexts:
    cfprBiosVfAllUSBDevicesTable.setStatus("current")
_CfprBiosVfAllUSBDevicesEntry_Object = MibTableRow
cfprBiosVfAllUSBDevicesEntry = _CfprBiosVfAllUSBDevicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 13, 1)
)
cfprBiosVfAllUSBDevicesEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfAllUSBDevicesInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfAllUSBDevicesEntry.setStatus("current")
_CfprBiosVfAllUSBDevicesInstanceId_Type = CfprManagedObjectId
_CfprBiosVfAllUSBDevicesInstanceId_Object = MibTableColumn
cfprBiosVfAllUSBDevicesInstanceId = _CfprBiosVfAllUSBDevicesInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 13, 1, 1),
    _CfprBiosVfAllUSBDevicesInstanceId_Type()
)
cfprBiosVfAllUSBDevicesInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfAllUSBDevicesInstanceId.setStatus("current")
_CfprBiosVfAllUSBDevicesDn_Type = CfprManagedObjectDn
_CfprBiosVfAllUSBDevicesDn_Object = MibTableColumn
cfprBiosVfAllUSBDevicesDn = _CfprBiosVfAllUSBDevicesDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 13, 1, 2),
    _CfprBiosVfAllUSBDevicesDn_Type()
)
cfprBiosVfAllUSBDevicesDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfAllUSBDevicesDn.setStatus("current")
_CfprBiosVfAllUSBDevicesRn_Type = SnmpAdminString
_CfprBiosVfAllUSBDevicesRn_Object = MibTableColumn
cfprBiosVfAllUSBDevicesRn = _CfprBiosVfAllUSBDevicesRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 13, 1, 3),
    _CfprBiosVfAllUSBDevicesRn_Type()
)
cfprBiosVfAllUSBDevicesRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfAllUSBDevicesRn.setStatus("current")
_CfprBiosVfAllUSBDevicesVpAllUSBDevices_Type = CfprBiosVfAllUSBDevicesVpAllUSBDevices
_CfprBiosVfAllUSBDevicesVpAllUSBDevices_Object = MibTableColumn
cfprBiosVfAllUSBDevicesVpAllUSBDevices = _CfprBiosVfAllUSBDevicesVpAllUSBDevices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 13, 1, 4),
    _CfprBiosVfAllUSBDevicesVpAllUSBDevices_Type()
)
cfprBiosVfAllUSBDevicesVpAllUSBDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfAllUSBDevicesVpAllUSBDevices.setStatus("current")
_CfprBiosVfAllUSBDevicesSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfAllUSBDevicesSupportedByDefault_Object = MibTableColumn
cfprBiosVfAllUSBDevicesSupportedByDefault = _CfprBiosVfAllUSBDevicesSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 13, 1, 5),
    _CfprBiosVfAllUSBDevicesSupportedByDefault_Type()
)
cfprBiosVfAllUSBDevicesSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfAllUSBDevicesSupportedByDefault.setStatus("current")
_CfprBiosVfAltitudeTable_Object = MibTable
cfprBiosVfAltitudeTable = _CfprBiosVfAltitudeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 14)
)
if mibBuilder.loadTexts:
    cfprBiosVfAltitudeTable.setStatus("current")
_CfprBiosVfAltitudeEntry_Object = MibTableRow
cfprBiosVfAltitudeEntry = _CfprBiosVfAltitudeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 14, 1)
)
cfprBiosVfAltitudeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfAltitudeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfAltitudeEntry.setStatus("current")
_CfprBiosVfAltitudeInstanceId_Type = CfprManagedObjectId
_CfprBiosVfAltitudeInstanceId_Object = MibTableColumn
cfprBiosVfAltitudeInstanceId = _CfprBiosVfAltitudeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 14, 1, 1),
    _CfprBiosVfAltitudeInstanceId_Type()
)
cfprBiosVfAltitudeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfAltitudeInstanceId.setStatus("current")
_CfprBiosVfAltitudeDn_Type = CfprManagedObjectDn
_CfprBiosVfAltitudeDn_Object = MibTableColumn
cfprBiosVfAltitudeDn = _CfprBiosVfAltitudeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 14, 1, 2),
    _CfprBiosVfAltitudeDn_Type()
)
cfprBiosVfAltitudeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfAltitudeDn.setStatus("current")
_CfprBiosVfAltitudeRn_Type = SnmpAdminString
_CfprBiosVfAltitudeRn_Object = MibTableColumn
cfprBiosVfAltitudeRn = _CfprBiosVfAltitudeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 14, 1, 3),
    _CfprBiosVfAltitudeRn_Type()
)
cfprBiosVfAltitudeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfAltitudeRn.setStatus("current")
_CfprBiosVfAltitudeVpAltitude_Type = CfprBiosVfAltitudeVpAltitude
_CfprBiosVfAltitudeVpAltitude_Object = MibTableColumn
cfprBiosVfAltitudeVpAltitude = _CfprBiosVfAltitudeVpAltitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 14, 1, 4),
    _CfprBiosVfAltitudeVpAltitude_Type()
)
cfprBiosVfAltitudeVpAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfAltitudeVpAltitude.setStatus("current")
_CfprBiosVfAltitudeSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfAltitudeSupportedByDefault_Object = MibTableColumn
cfprBiosVfAltitudeSupportedByDefault = _CfprBiosVfAltitudeSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 14, 1, 5),
    _CfprBiosVfAltitudeSupportedByDefault_Type()
)
cfprBiosVfAltitudeSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfAltitudeSupportedByDefault.setStatus("current")
_CfprBiosVfAssertNMIOnPERRTable_Object = MibTable
cfprBiosVfAssertNMIOnPERRTable = _CfprBiosVfAssertNMIOnPERRTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 15)
)
if mibBuilder.loadTexts:
    cfprBiosVfAssertNMIOnPERRTable.setStatus("current")
_CfprBiosVfAssertNMIOnPERREntry_Object = MibTableRow
cfprBiosVfAssertNMIOnPERREntry = _CfprBiosVfAssertNMIOnPERREntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 15, 1)
)
cfprBiosVfAssertNMIOnPERREntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfAssertNMIOnPERRInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfAssertNMIOnPERREntry.setStatus("current")
_CfprBiosVfAssertNMIOnPERRInstanceId_Type = CfprManagedObjectId
_CfprBiosVfAssertNMIOnPERRInstanceId_Object = MibTableColumn
cfprBiosVfAssertNMIOnPERRInstanceId = _CfprBiosVfAssertNMIOnPERRInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 15, 1, 1),
    _CfprBiosVfAssertNMIOnPERRInstanceId_Type()
)
cfprBiosVfAssertNMIOnPERRInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfAssertNMIOnPERRInstanceId.setStatus("current")
_CfprBiosVfAssertNMIOnPERRDn_Type = CfprManagedObjectDn
_CfprBiosVfAssertNMIOnPERRDn_Object = MibTableColumn
cfprBiosVfAssertNMIOnPERRDn = _CfprBiosVfAssertNMIOnPERRDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 15, 1, 2),
    _CfprBiosVfAssertNMIOnPERRDn_Type()
)
cfprBiosVfAssertNMIOnPERRDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfAssertNMIOnPERRDn.setStatus("current")
_CfprBiosVfAssertNMIOnPERRRn_Type = SnmpAdminString
_CfprBiosVfAssertNMIOnPERRRn_Object = MibTableColumn
cfprBiosVfAssertNMIOnPERRRn = _CfprBiosVfAssertNMIOnPERRRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 15, 1, 3),
    _CfprBiosVfAssertNMIOnPERRRn_Type()
)
cfprBiosVfAssertNMIOnPERRRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfAssertNMIOnPERRRn.setStatus("current")
_CfprBiosVfAssertNMIOnPERRVpAssertNMIOnPERR_Type = CfprBiosVfAssertNMIOnPERRVpAssertNMIOnPERR
_CfprBiosVfAssertNMIOnPERRVpAssertNMIOnPERR_Object = MibTableColumn
cfprBiosVfAssertNMIOnPERRVpAssertNMIOnPERR = _CfprBiosVfAssertNMIOnPERRVpAssertNMIOnPERR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 15, 1, 4),
    _CfprBiosVfAssertNMIOnPERRVpAssertNMIOnPERR_Type()
)
cfprBiosVfAssertNMIOnPERRVpAssertNMIOnPERR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfAssertNMIOnPERRVpAssertNMIOnPERR.setStatus("current")
_CfprBiosVfAssertNMIOnPERRSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfAssertNMIOnPERRSupportedByDefault_Object = MibTableColumn
cfprBiosVfAssertNMIOnPERRSupportedByDefault = _CfprBiosVfAssertNMIOnPERRSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 15, 1, 5),
    _CfprBiosVfAssertNMIOnPERRSupportedByDefault_Type()
)
cfprBiosVfAssertNMIOnPERRSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfAssertNMIOnPERRSupportedByDefault.setStatus("current")
_CfprBiosVfAssertNMIOnSERRTable_Object = MibTable
cfprBiosVfAssertNMIOnSERRTable = _CfprBiosVfAssertNMIOnSERRTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 16)
)
if mibBuilder.loadTexts:
    cfprBiosVfAssertNMIOnSERRTable.setStatus("current")
_CfprBiosVfAssertNMIOnSERREntry_Object = MibTableRow
cfprBiosVfAssertNMIOnSERREntry = _CfprBiosVfAssertNMIOnSERREntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 16, 1)
)
cfprBiosVfAssertNMIOnSERREntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfAssertNMIOnSERRInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfAssertNMIOnSERREntry.setStatus("current")
_CfprBiosVfAssertNMIOnSERRInstanceId_Type = CfprManagedObjectId
_CfprBiosVfAssertNMIOnSERRInstanceId_Object = MibTableColumn
cfprBiosVfAssertNMIOnSERRInstanceId = _CfprBiosVfAssertNMIOnSERRInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 16, 1, 1),
    _CfprBiosVfAssertNMIOnSERRInstanceId_Type()
)
cfprBiosVfAssertNMIOnSERRInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfAssertNMIOnSERRInstanceId.setStatus("current")
_CfprBiosVfAssertNMIOnSERRDn_Type = CfprManagedObjectDn
_CfprBiosVfAssertNMIOnSERRDn_Object = MibTableColumn
cfprBiosVfAssertNMIOnSERRDn = _CfprBiosVfAssertNMIOnSERRDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 16, 1, 2),
    _CfprBiosVfAssertNMIOnSERRDn_Type()
)
cfprBiosVfAssertNMIOnSERRDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfAssertNMIOnSERRDn.setStatus("current")
_CfprBiosVfAssertNMIOnSERRRn_Type = SnmpAdminString
_CfprBiosVfAssertNMIOnSERRRn_Object = MibTableColumn
cfprBiosVfAssertNMIOnSERRRn = _CfprBiosVfAssertNMIOnSERRRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 16, 1, 3),
    _CfprBiosVfAssertNMIOnSERRRn_Type()
)
cfprBiosVfAssertNMIOnSERRRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfAssertNMIOnSERRRn.setStatus("current")
_CfprBiosVfAssertNMIOnSERRVpAssertNMIOnSERR_Type = CfprBiosVfAssertNMIOnSERRVpAssertNMIOnSERR
_CfprBiosVfAssertNMIOnSERRVpAssertNMIOnSERR_Object = MibTableColumn
cfprBiosVfAssertNMIOnSERRVpAssertNMIOnSERR = _CfprBiosVfAssertNMIOnSERRVpAssertNMIOnSERR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 16, 1, 4),
    _CfprBiosVfAssertNMIOnSERRVpAssertNMIOnSERR_Type()
)
cfprBiosVfAssertNMIOnSERRVpAssertNMIOnSERR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfAssertNMIOnSERRVpAssertNMIOnSERR.setStatus("current")
_CfprBiosVfAssertNMIOnSERRSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfAssertNMIOnSERRSupportedByDefault_Object = MibTableColumn
cfprBiosVfAssertNMIOnSERRSupportedByDefault = _CfprBiosVfAssertNMIOnSERRSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 16, 1, 5),
    _CfprBiosVfAssertNMIOnSERRSupportedByDefault_Type()
)
cfprBiosVfAssertNMIOnSERRSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfAssertNMIOnSERRSupportedByDefault.setStatus("current")
_CfprBiosVfBootOptionRetryTable_Object = MibTable
cfprBiosVfBootOptionRetryTable = _CfprBiosVfBootOptionRetryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 17)
)
if mibBuilder.loadTexts:
    cfprBiosVfBootOptionRetryTable.setStatus("current")
_CfprBiosVfBootOptionRetryEntry_Object = MibTableRow
cfprBiosVfBootOptionRetryEntry = _CfprBiosVfBootOptionRetryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 17, 1)
)
cfprBiosVfBootOptionRetryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfBootOptionRetryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfBootOptionRetryEntry.setStatus("current")
_CfprBiosVfBootOptionRetryInstanceId_Type = CfprManagedObjectId
_CfprBiosVfBootOptionRetryInstanceId_Object = MibTableColumn
cfprBiosVfBootOptionRetryInstanceId = _CfprBiosVfBootOptionRetryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 17, 1, 1),
    _CfprBiosVfBootOptionRetryInstanceId_Type()
)
cfprBiosVfBootOptionRetryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfBootOptionRetryInstanceId.setStatus("current")
_CfprBiosVfBootOptionRetryDn_Type = CfprManagedObjectDn
_CfprBiosVfBootOptionRetryDn_Object = MibTableColumn
cfprBiosVfBootOptionRetryDn = _CfprBiosVfBootOptionRetryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 17, 1, 2),
    _CfprBiosVfBootOptionRetryDn_Type()
)
cfprBiosVfBootOptionRetryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfBootOptionRetryDn.setStatus("current")
_CfprBiosVfBootOptionRetryRn_Type = SnmpAdminString
_CfprBiosVfBootOptionRetryRn_Object = MibTableColumn
cfprBiosVfBootOptionRetryRn = _CfprBiosVfBootOptionRetryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 17, 1, 3),
    _CfprBiosVfBootOptionRetryRn_Type()
)
cfprBiosVfBootOptionRetryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfBootOptionRetryRn.setStatus("current")
_CfprBiosVfBootOptionRetryVpBootOptionRetry_Type = CfprBiosVfBootOptionRetryVpBootOptionRetry
_CfprBiosVfBootOptionRetryVpBootOptionRetry_Object = MibTableColumn
cfprBiosVfBootOptionRetryVpBootOptionRetry = _CfprBiosVfBootOptionRetryVpBootOptionRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 17, 1, 4),
    _CfprBiosVfBootOptionRetryVpBootOptionRetry_Type()
)
cfprBiosVfBootOptionRetryVpBootOptionRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfBootOptionRetryVpBootOptionRetry.setStatus("current")
_CfprBiosVfBootOptionRetrySupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfBootOptionRetrySupportedByDefault_Object = MibTableColumn
cfprBiosVfBootOptionRetrySupportedByDefault = _CfprBiosVfBootOptionRetrySupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 17, 1, 5),
    _CfprBiosVfBootOptionRetrySupportedByDefault_Type()
)
cfprBiosVfBootOptionRetrySupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfBootOptionRetrySupportedByDefault.setStatus("current")
_CfprBiosVfCPUPerformanceTable_Object = MibTable
cfprBiosVfCPUPerformanceTable = _CfprBiosVfCPUPerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 18)
)
if mibBuilder.loadTexts:
    cfprBiosVfCPUPerformanceTable.setStatus("current")
_CfprBiosVfCPUPerformanceEntry_Object = MibTableRow
cfprBiosVfCPUPerformanceEntry = _CfprBiosVfCPUPerformanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 18, 1)
)
cfprBiosVfCPUPerformanceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfCPUPerformanceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfCPUPerformanceEntry.setStatus("current")
_CfprBiosVfCPUPerformanceInstanceId_Type = CfprManagedObjectId
_CfprBiosVfCPUPerformanceInstanceId_Object = MibTableColumn
cfprBiosVfCPUPerformanceInstanceId = _CfprBiosVfCPUPerformanceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 18, 1, 1),
    _CfprBiosVfCPUPerformanceInstanceId_Type()
)
cfprBiosVfCPUPerformanceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfCPUPerformanceInstanceId.setStatus("current")
_CfprBiosVfCPUPerformanceDn_Type = CfprManagedObjectDn
_CfprBiosVfCPUPerformanceDn_Object = MibTableColumn
cfprBiosVfCPUPerformanceDn = _CfprBiosVfCPUPerformanceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 18, 1, 2),
    _CfprBiosVfCPUPerformanceDn_Type()
)
cfprBiosVfCPUPerformanceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfCPUPerformanceDn.setStatus("current")
_CfprBiosVfCPUPerformanceRn_Type = SnmpAdminString
_CfprBiosVfCPUPerformanceRn_Object = MibTableColumn
cfprBiosVfCPUPerformanceRn = _CfprBiosVfCPUPerformanceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 18, 1, 3),
    _CfprBiosVfCPUPerformanceRn_Type()
)
cfprBiosVfCPUPerformanceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfCPUPerformanceRn.setStatus("current")
_CfprBiosVfCPUPerformanceVpCPUPerformance_Type = CfprBiosVfCPUPerformanceVpCPUPerformance
_CfprBiosVfCPUPerformanceVpCPUPerformance_Object = MibTableColumn
cfprBiosVfCPUPerformanceVpCPUPerformance = _CfprBiosVfCPUPerformanceVpCPUPerformance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 18, 1, 4),
    _CfprBiosVfCPUPerformanceVpCPUPerformance_Type()
)
cfprBiosVfCPUPerformanceVpCPUPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfCPUPerformanceVpCPUPerformance.setStatus("current")
_CfprBiosVfCPUPerformanceSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfCPUPerformanceSupportedByDefault_Object = MibTableColumn
cfprBiosVfCPUPerformanceSupportedByDefault = _CfprBiosVfCPUPerformanceSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 18, 1, 5),
    _CfprBiosVfCPUPerformanceSupportedByDefault_Type()
)
cfprBiosVfCPUPerformanceSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfCPUPerformanceSupportedByDefault.setStatus("current")
_CfprBiosVfConsoleRedirectionTable_Object = MibTable
cfprBiosVfConsoleRedirectionTable = _CfprBiosVfConsoleRedirectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 19)
)
if mibBuilder.loadTexts:
    cfprBiosVfConsoleRedirectionTable.setStatus("current")
_CfprBiosVfConsoleRedirectionEntry_Object = MibTableRow
cfprBiosVfConsoleRedirectionEntry = _CfprBiosVfConsoleRedirectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 19, 1)
)
cfprBiosVfConsoleRedirectionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfConsoleRedirectionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfConsoleRedirectionEntry.setStatus("current")
_CfprBiosVfConsoleRedirectionInstanceId_Type = CfprManagedObjectId
_CfprBiosVfConsoleRedirectionInstanceId_Object = MibTableColumn
cfprBiosVfConsoleRedirectionInstanceId = _CfprBiosVfConsoleRedirectionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 19, 1, 1),
    _CfprBiosVfConsoleRedirectionInstanceId_Type()
)
cfprBiosVfConsoleRedirectionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfConsoleRedirectionInstanceId.setStatus("current")
_CfprBiosVfConsoleRedirectionDn_Type = CfprManagedObjectDn
_CfprBiosVfConsoleRedirectionDn_Object = MibTableColumn
cfprBiosVfConsoleRedirectionDn = _CfprBiosVfConsoleRedirectionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 19, 1, 2),
    _CfprBiosVfConsoleRedirectionDn_Type()
)
cfprBiosVfConsoleRedirectionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfConsoleRedirectionDn.setStatus("current")
_CfprBiosVfConsoleRedirectionRn_Type = SnmpAdminString
_CfprBiosVfConsoleRedirectionRn_Object = MibTableColumn
cfprBiosVfConsoleRedirectionRn = _CfprBiosVfConsoleRedirectionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 19, 1, 3),
    _CfprBiosVfConsoleRedirectionRn_Type()
)
cfprBiosVfConsoleRedirectionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfConsoleRedirectionRn.setStatus("current")
_CfprBiosVfConsoleRedirectionVpBaudRate_Type = CfprBiosVfConsoleRedirectionVpBaudRate
_CfprBiosVfConsoleRedirectionVpBaudRate_Object = MibTableColumn
cfprBiosVfConsoleRedirectionVpBaudRate = _CfprBiosVfConsoleRedirectionVpBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 19, 1, 4),
    _CfprBiosVfConsoleRedirectionVpBaudRate_Type()
)
cfprBiosVfConsoleRedirectionVpBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfConsoleRedirectionVpBaudRate.setStatus("current")
_CfprBiosVfConsoleRedirectionVpConsoleRedirection_Type = CfprBiosVfConsoleRedirectionVpConsoleRedirection
_CfprBiosVfConsoleRedirectionVpConsoleRedirection_Object = MibTableColumn
cfprBiosVfConsoleRedirectionVpConsoleRedirection = _CfprBiosVfConsoleRedirectionVpConsoleRedirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 19, 1, 5),
    _CfprBiosVfConsoleRedirectionVpConsoleRedirection_Type()
)
cfprBiosVfConsoleRedirectionVpConsoleRedirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfConsoleRedirectionVpConsoleRedirection.setStatus("current")
_CfprBiosVfConsoleRedirectionVpFlowControl_Type = CfprBiosVfConsoleRedirectionVpFlowControl
_CfprBiosVfConsoleRedirectionVpFlowControl_Object = MibTableColumn
cfprBiosVfConsoleRedirectionVpFlowControl = _CfprBiosVfConsoleRedirectionVpFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 19, 1, 6),
    _CfprBiosVfConsoleRedirectionVpFlowControl_Type()
)
cfprBiosVfConsoleRedirectionVpFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfConsoleRedirectionVpFlowControl.setStatus("current")
_CfprBiosVfConsoleRedirectionVpLegacyOSRedirection_Type = CfprBiosVfConsoleRedirectionVpLegacyOSRedirection
_CfprBiosVfConsoleRedirectionVpLegacyOSRedirection_Object = MibTableColumn
cfprBiosVfConsoleRedirectionVpLegacyOSRedirection = _CfprBiosVfConsoleRedirectionVpLegacyOSRedirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 19, 1, 7),
    _CfprBiosVfConsoleRedirectionVpLegacyOSRedirection_Type()
)
cfprBiosVfConsoleRedirectionVpLegacyOSRedirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfConsoleRedirectionVpLegacyOSRedirection.setStatus("current")
_CfprBiosVfConsoleRedirectionVpPuttyKeyPad_Type = CfprBiosVfConsoleRedirectionVpPuttyKeyPad
_CfprBiosVfConsoleRedirectionVpPuttyKeyPad_Object = MibTableColumn
cfprBiosVfConsoleRedirectionVpPuttyKeyPad = _CfprBiosVfConsoleRedirectionVpPuttyKeyPad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 19, 1, 8),
    _CfprBiosVfConsoleRedirectionVpPuttyKeyPad_Type()
)
cfprBiosVfConsoleRedirectionVpPuttyKeyPad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfConsoleRedirectionVpPuttyKeyPad.setStatus("current")
_CfprBiosVfConsoleRedirectionVpTerminalType_Type = CfprBiosVfConsoleRedirectionVpTerminalType
_CfprBiosVfConsoleRedirectionVpTerminalType_Object = MibTableColumn
cfprBiosVfConsoleRedirectionVpTerminalType = _CfprBiosVfConsoleRedirectionVpTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 19, 1, 9),
    _CfprBiosVfConsoleRedirectionVpTerminalType_Type()
)
cfprBiosVfConsoleRedirectionVpTerminalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfConsoleRedirectionVpTerminalType.setStatus("current")
_CfprBiosVfConsoleRedirectionSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfConsoleRedirectionSupportedByDefault_Object = MibTableColumn
cfprBiosVfConsoleRedirectionSupportedByDefault = _CfprBiosVfConsoleRedirectionSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 19, 1, 10),
    _CfprBiosVfConsoleRedirectionSupportedByDefault_Type()
)
cfprBiosVfConsoleRedirectionSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfConsoleRedirectionSupportedByDefault.setStatus("current")
_CfprBiosVfCoreMultiProcessingTable_Object = MibTable
cfprBiosVfCoreMultiProcessingTable = _CfprBiosVfCoreMultiProcessingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 20)
)
if mibBuilder.loadTexts:
    cfprBiosVfCoreMultiProcessingTable.setStatus("current")
_CfprBiosVfCoreMultiProcessingEntry_Object = MibTableRow
cfprBiosVfCoreMultiProcessingEntry = _CfprBiosVfCoreMultiProcessingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 20, 1)
)
cfprBiosVfCoreMultiProcessingEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfCoreMultiProcessingInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfCoreMultiProcessingEntry.setStatus("current")
_CfprBiosVfCoreMultiProcessingInstanceId_Type = CfprManagedObjectId
_CfprBiosVfCoreMultiProcessingInstanceId_Object = MibTableColumn
cfprBiosVfCoreMultiProcessingInstanceId = _CfprBiosVfCoreMultiProcessingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 20, 1, 1),
    _CfprBiosVfCoreMultiProcessingInstanceId_Type()
)
cfprBiosVfCoreMultiProcessingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfCoreMultiProcessingInstanceId.setStatus("current")
_CfprBiosVfCoreMultiProcessingDn_Type = CfprManagedObjectDn
_CfprBiosVfCoreMultiProcessingDn_Object = MibTableColumn
cfprBiosVfCoreMultiProcessingDn = _CfprBiosVfCoreMultiProcessingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 20, 1, 2),
    _CfprBiosVfCoreMultiProcessingDn_Type()
)
cfprBiosVfCoreMultiProcessingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfCoreMultiProcessingDn.setStatus("current")
_CfprBiosVfCoreMultiProcessingRn_Type = SnmpAdminString
_CfprBiosVfCoreMultiProcessingRn_Object = MibTableColumn
cfprBiosVfCoreMultiProcessingRn = _CfprBiosVfCoreMultiProcessingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 20, 1, 3),
    _CfprBiosVfCoreMultiProcessingRn_Type()
)
cfprBiosVfCoreMultiProcessingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfCoreMultiProcessingRn.setStatus("current")
_CfprBiosVfCoreMultiProcessingVpCoreMultiProcessing_Type = CfprBiosVfCoreMultiProcessingVpCoreMultiProcessing
_CfprBiosVfCoreMultiProcessingVpCoreMultiProcessing_Object = MibTableColumn
cfprBiosVfCoreMultiProcessingVpCoreMultiProcessing = _CfprBiosVfCoreMultiProcessingVpCoreMultiProcessing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 20, 1, 4),
    _CfprBiosVfCoreMultiProcessingVpCoreMultiProcessing_Type()
)
cfprBiosVfCoreMultiProcessingVpCoreMultiProcessing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfCoreMultiProcessingVpCoreMultiProcessing.setStatus("current")
_CfprBiosVfCoreMultiProcessingSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfCoreMultiProcessingSupportedByDefault_Object = MibTableColumn
cfprBiosVfCoreMultiProcessingSupportedByDefault = _CfprBiosVfCoreMultiProcessingSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 20, 1, 5),
    _CfprBiosVfCoreMultiProcessingSupportedByDefault_Type()
)
cfprBiosVfCoreMultiProcessingSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfCoreMultiProcessingSupportedByDefault.setStatus("current")
_CfprBiosVfDRAMClockThrottlingTable_Object = MibTable
cfprBiosVfDRAMClockThrottlingTable = _CfprBiosVfDRAMClockThrottlingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 21)
)
if mibBuilder.loadTexts:
    cfprBiosVfDRAMClockThrottlingTable.setStatus("current")
_CfprBiosVfDRAMClockThrottlingEntry_Object = MibTableRow
cfprBiosVfDRAMClockThrottlingEntry = _CfprBiosVfDRAMClockThrottlingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 21, 1)
)
cfprBiosVfDRAMClockThrottlingEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfDRAMClockThrottlingInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfDRAMClockThrottlingEntry.setStatus("current")
_CfprBiosVfDRAMClockThrottlingInstanceId_Type = CfprManagedObjectId
_CfprBiosVfDRAMClockThrottlingInstanceId_Object = MibTableColumn
cfprBiosVfDRAMClockThrottlingInstanceId = _CfprBiosVfDRAMClockThrottlingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 21, 1, 1),
    _CfprBiosVfDRAMClockThrottlingInstanceId_Type()
)
cfprBiosVfDRAMClockThrottlingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfDRAMClockThrottlingInstanceId.setStatus("current")
_CfprBiosVfDRAMClockThrottlingDn_Type = CfprManagedObjectDn
_CfprBiosVfDRAMClockThrottlingDn_Object = MibTableColumn
cfprBiosVfDRAMClockThrottlingDn = _CfprBiosVfDRAMClockThrottlingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 21, 1, 2),
    _CfprBiosVfDRAMClockThrottlingDn_Type()
)
cfprBiosVfDRAMClockThrottlingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfDRAMClockThrottlingDn.setStatus("current")
_CfprBiosVfDRAMClockThrottlingRn_Type = SnmpAdminString
_CfprBiosVfDRAMClockThrottlingRn_Object = MibTableColumn
cfprBiosVfDRAMClockThrottlingRn = _CfprBiosVfDRAMClockThrottlingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 21, 1, 3),
    _CfprBiosVfDRAMClockThrottlingRn_Type()
)
cfprBiosVfDRAMClockThrottlingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfDRAMClockThrottlingRn.setStatus("current")
_CfprBiosVfDRAMClockThrottlingVpDRAMClockThrottling_Type = CfprBiosVfDRAMClockThrottlingVpDRAMClockThrottling
_CfprBiosVfDRAMClockThrottlingVpDRAMClockThrottling_Object = MibTableColumn
cfprBiosVfDRAMClockThrottlingVpDRAMClockThrottling = _CfprBiosVfDRAMClockThrottlingVpDRAMClockThrottling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 21, 1, 4),
    _CfprBiosVfDRAMClockThrottlingVpDRAMClockThrottling_Type()
)
cfprBiosVfDRAMClockThrottlingVpDRAMClockThrottling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfDRAMClockThrottlingVpDRAMClockThrottling.setStatus("current")
_CfprBiosVfDRAMClockThrottlingSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfDRAMClockThrottlingSupportedByDefault_Object = MibTableColumn
cfprBiosVfDRAMClockThrottlingSupportedByDefault = _CfprBiosVfDRAMClockThrottlingSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 21, 1, 5),
    _CfprBiosVfDRAMClockThrottlingSupportedByDefault_Type()
)
cfprBiosVfDRAMClockThrottlingSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfDRAMClockThrottlingSupportedByDefault.setStatus("current")
_CfprBiosVfDirectCacheAccessTable_Object = MibTable
cfprBiosVfDirectCacheAccessTable = _CfprBiosVfDirectCacheAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 22)
)
if mibBuilder.loadTexts:
    cfprBiosVfDirectCacheAccessTable.setStatus("current")
_CfprBiosVfDirectCacheAccessEntry_Object = MibTableRow
cfprBiosVfDirectCacheAccessEntry = _CfprBiosVfDirectCacheAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 22, 1)
)
cfprBiosVfDirectCacheAccessEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfDirectCacheAccessInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfDirectCacheAccessEntry.setStatus("current")
_CfprBiosVfDirectCacheAccessInstanceId_Type = CfprManagedObjectId
_CfprBiosVfDirectCacheAccessInstanceId_Object = MibTableColumn
cfprBiosVfDirectCacheAccessInstanceId = _CfprBiosVfDirectCacheAccessInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 22, 1, 1),
    _CfprBiosVfDirectCacheAccessInstanceId_Type()
)
cfprBiosVfDirectCacheAccessInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfDirectCacheAccessInstanceId.setStatus("current")
_CfprBiosVfDirectCacheAccessDn_Type = CfprManagedObjectDn
_CfprBiosVfDirectCacheAccessDn_Object = MibTableColumn
cfprBiosVfDirectCacheAccessDn = _CfprBiosVfDirectCacheAccessDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 22, 1, 2),
    _CfprBiosVfDirectCacheAccessDn_Type()
)
cfprBiosVfDirectCacheAccessDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfDirectCacheAccessDn.setStatus("current")
_CfprBiosVfDirectCacheAccessRn_Type = SnmpAdminString
_CfprBiosVfDirectCacheAccessRn_Object = MibTableColumn
cfprBiosVfDirectCacheAccessRn = _CfprBiosVfDirectCacheAccessRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 22, 1, 3),
    _CfprBiosVfDirectCacheAccessRn_Type()
)
cfprBiosVfDirectCacheAccessRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfDirectCacheAccessRn.setStatus("current")
_CfprBiosVfDirectCacheAccessVpDirectCacheAccess_Type = CfprBiosVfDirectCacheAccessVpDirectCacheAccess
_CfprBiosVfDirectCacheAccessVpDirectCacheAccess_Object = MibTableColumn
cfprBiosVfDirectCacheAccessVpDirectCacheAccess = _CfprBiosVfDirectCacheAccessVpDirectCacheAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 22, 1, 4),
    _CfprBiosVfDirectCacheAccessVpDirectCacheAccess_Type()
)
cfprBiosVfDirectCacheAccessVpDirectCacheAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfDirectCacheAccessVpDirectCacheAccess.setStatus("current")
_CfprBiosVfDirectCacheAccessSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfDirectCacheAccessSupportedByDefault_Object = MibTableColumn
cfprBiosVfDirectCacheAccessSupportedByDefault = _CfprBiosVfDirectCacheAccessSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 22, 1, 5),
    _CfprBiosVfDirectCacheAccessSupportedByDefault_Type()
)
cfprBiosVfDirectCacheAccessSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfDirectCacheAccessSupportedByDefault.setStatus("current")
_CfprBiosVfDramRefreshRateTable_Object = MibTable
cfprBiosVfDramRefreshRateTable = _CfprBiosVfDramRefreshRateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 23)
)
if mibBuilder.loadTexts:
    cfprBiosVfDramRefreshRateTable.setStatus("current")
_CfprBiosVfDramRefreshRateEntry_Object = MibTableRow
cfprBiosVfDramRefreshRateEntry = _CfprBiosVfDramRefreshRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 23, 1)
)
cfprBiosVfDramRefreshRateEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfDramRefreshRateInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfDramRefreshRateEntry.setStatus("current")
_CfprBiosVfDramRefreshRateInstanceId_Type = CfprManagedObjectId
_CfprBiosVfDramRefreshRateInstanceId_Object = MibTableColumn
cfprBiosVfDramRefreshRateInstanceId = _CfprBiosVfDramRefreshRateInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 23, 1, 1),
    _CfprBiosVfDramRefreshRateInstanceId_Type()
)
cfprBiosVfDramRefreshRateInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfDramRefreshRateInstanceId.setStatus("current")
_CfprBiosVfDramRefreshRateDn_Type = CfprManagedObjectDn
_CfprBiosVfDramRefreshRateDn_Object = MibTableColumn
cfprBiosVfDramRefreshRateDn = _CfprBiosVfDramRefreshRateDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 23, 1, 2),
    _CfprBiosVfDramRefreshRateDn_Type()
)
cfprBiosVfDramRefreshRateDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfDramRefreshRateDn.setStatus("current")
_CfprBiosVfDramRefreshRateRn_Type = SnmpAdminString
_CfprBiosVfDramRefreshRateRn_Object = MibTableColumn
cfprBiosVfDramRefreshRateRn = _CfprBiosVfDramRefreshRateRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 23, 1, 3),
    _CfprBiosVfDramRefreshRateRn_Type()
)
cfprBiosVfDramRefreshRateRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfDramRefreshRateRn.setStatus("current")
_CfprBiosVfDramRefreshRateVpDramRefreshRate_Type = CfprBiosVfDramRefreshRateVpDramRefreshRate
_CfprBiosVfDramRefreshRateVpDramRefreshRate_Object = MibTableColumn
cfprBiosVfDramRefreshRateVpDramRefreshRate = _CfprBiosVfDramRefreshRateVpDramRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 23, 1, 4),
    _CfprBiosVfDramRefreshRateVpDramRefreshRate_Type()
)
cfprBiosVfDramRefreshRateVpDramRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfDramRefreshRateVpDramRefreshRate.setStatus("current")
_CfprBiosVfDramRefreshRateSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfDramRefreshRateSupportedByDefault_Object = MibTableColumn
cfprBiosVfDramRefreshRateSupportedByDefault = _CfprBiosVfDramRefreshRateSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 23, 1, 5),
    _CfprBiosVfDramRefreshRateSupportedByDefault_Type()
)
cfprBiosVfDramRefreshRateSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfDramRefreshRateSupportedByDefault.setStatus("current")
_CfprBiosVfEnhancedIntelSpeedStepTechTable_Object = MibTable
cfprBiosVfEnhancedIntelSpeedStepTechTable = _CfprBiosVfEnhancedIntelSpeedStepTechTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 24)
)
if mibBuilder.loadTexts:
    cfprBiosVfEnhancedIntelSpeedStepTechTable.setStatus("current")
_CfprBiosVfEnhancedIntelSpeedStepTechEntry_Object = MibTableRow
cfprBiosVfEnhancedIntelSpeedStepTechEntry = _CfprBiosVfEnhancedIntelSpeedStepTechEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 24, 1)
)
cfprBiosVfEnhancedIntelSpeedStepTechEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfEnhancedIntelSpeedStepTechInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfEnhancedIntelSpeedStepTechEntry.setStatus("current")
_CfprBiosVfEnhancedIntelSpeedStepTechInstanceId_Type = CfprManagedObjectId
_CfprBiosVfEnhancedIntelSpeedStepTechInstanceId_Object = MibTableColumn
cfprBiosVfEnhancedIntelSpeedStepTechInstanceId = _CfprBiosVfEnhancedIntelSpeedStepTechInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 24, 1, 1),
    _CfprBiosVfEnhancedIntelSpeedStepTechInstanceId_Type()
)
cfprBiosVfEnhancedIntelSpeedStepTechInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfEnhancedIntelSpeedStepTechInstanceId.setStatus("current")
_CfprBiosVfEnhancedIntelSpeedStepTechDn_Type = CfprManagedObjectDn
_CfprBiosVfEnhancedIntelSpeedStepTechDn_Object = MibTableColumn
cfprBiosVfEnhancedIntelSpeedStepTechDn = _CfprBiosVfEnhancedIntelSpeedStepTechDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 24, 1, 2),
    _CfprBiosVfEnhancedIntelSpeedStepTechDn_Type()
)
cfprBiosVfEnhancedIntelSpeedStepTechDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfEnhancedIntelSpeedStepTechDn.setStatus("current")
_CfprBiosVfEnhancedIntelSpeedStepTechRn_Type = SnmpAdminString
_CfprBiosVfEnhancedIntelSpeedStepTechRn_Object = MibTableColumn
cfprBiosVfEnhancedIntelSpeedStepTechRn = _CfprBiosVfEnhancedIntelSpeedStepTechRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 24, 1, 3),
    _CfprBiosVfEnhancedIntelSpeedStepTechRn_Type()
)
cfprBiosVfEnhancedIntelSpeedStepTechRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfEnhancedIntelSpeedStepTechRn.setStatus("current")
_CfprBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech_Type = CfprBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech
_CfprBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech_Object = MibTableColumn
cfprBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech = _CfprBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 24, 1, 4),
    _CfprBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech_Type()
)
cfprBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech.setStatus("current")
_CfprBiosVfEnhancedIntelSpeedStepTechSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfEnhancedIntelSpeedStepTechSupportedByDefault_Object = MibTableColumn
cfprBiosVfEnhancedIntelSpeedStepTechSupportedByDefault = _CfprBiosVfEnhancedIntelSpeedStepTechSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 24, 1, 5),
    _CfprBiosVfEnhancedIntelSpeedStepTechSupportedByDefault_Type()
)
cfprBiosVfEnhancedIntelSpeedStepTechSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfEnhancedIntelSpeedStepTechSupportedByDefault.setStatus("current")
_CfprBiosVfExecuteDisableBitTable_Object = MibTable
cfprBiosVfExecuteDisableBitTable = _CfprBiosVfExecuteDisableBitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 25)
)
if mibBuilder.loadTexts:
    cfprBiosVfExecuteDisableBitTable.setStatus("current")
_CfprBiosVfExecuteDisableBitEntry_Object = MibTableRow
cfprBiosVfExecuteDisableBitEntry = _CfprBiosVfExecuteDisableBitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 25, 1)
)
cfprBiosVfExecuteDisableBitEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfExecuteDisableBitInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfExecuteDisableBitEntry.setStatus("current")
_CfprBiosVfExecuteDisableBitInstanceId_Type = CfprManagedObjectId
_CfprBiosVfExecuteDisableBitInstanceId_Object = MibTableColumn
cfprBiosVfExecuteDisableBitInstanceId = _CfprBiosVfExecuteDisableBitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 25, 1, 1),
    _CfprBiosVfExecuteDisableBitInstanceId_Type()
)
cfprBiosVfExecuteDisableBitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfExecuteDisableBitInstanceId.setStatus("current")
_CfprBiosVfExecuteDisableBitDn_Type = CfprManagedObjectDn
_CfprBiosVfExecuteDisableBitDn_Object = MibTableColumn
cfprBiosVfExecuteDisableBitDn = _CfprBiosVfExecuteDisableBitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 25, 1, 2),
    _CfprBiosVfExecuteDisableBitDn_Type()
)
cfprBiosVfExecuteDisableBitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfExecuteDisableBitDn.setStatus("current")
_CfprBiosVfExecuteDisableBitRn_Type = SnmpAdminString
_CfprBiosVfExecuteDisableBitRn_Object = MibTableColumn
cfprBiosVfExecuteDisableBitRn = _CfprBiosVfExecuteDisableBitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 25, 1, 3),
    _CfprBiosVfExecuteDisableBitRn_Type()
)
cfprBiosVfExecuteDisableBitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfExecuteDisableBitRn.setStatus("current")
_CfprBiosVfExecuteDisableBitVpExecuteDisableBit_Type = CfprBiosVfExecuteDisableBitVpExecuteDisableBit
_CfprBiosVfExecuteDisableBitVpExecuteDisableBit_Object = MibTableColumn
cfprBiosVfExecuteDisableBitVpExecuteDisableBit = _CfprBiosVfExecuteDisableBitVpExecuteDisableBit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 25, 1, 4),
    _CfprBiosVfExecuteDisableBitVpExecuteDisableBit_Type()
)
cfprBiosVfExecuteDisableBitVpExecuteDisableBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfExecuteDisableBitVpExecuteDisableBit.setStatus("current")
_CfprBiosVfExecuteDisableBitSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfExecuteDisableBitSupportedByDefault_Object = MibTableColumn
cfprBiosVfExecuteDisableBitSupportedByDefault = _CfprBiosVfExecuteDisableBitSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 25, 1, 5),
    _CfprBiosVfExecuteDisableBitSupportedByDefault_Type()
)
cfprBiosVfExecuteDisableBitSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfExecuteDisableBitSupportedByDefault.setStatus("current")
_CfprBiosVfFRB2TimerTable_Object = MibTable
cfprBiosVfFRB2TimerTable = _CfprBiosVfFRB2TimerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 26)
)
if mibBuilder.loadTexts:
    cfprBiosVfFRB2TimerTable.setStatus("current")
_CfprBiosVfFRB2TimerEntry_Object = MibTableRow
cfprBiosVfFRB2TimerEntry = _CfprBiosVfFRB2TimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 26, 1)
)
cfprBiosVfFRB2TimerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfFRB2TimerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfFRB2TimerEntry.setStatus("current")
_CfprBiosVfFRB2TimerInstanceId_Type = CfprManagedObjectId
_CfprBiosVfFRB2TimerInstanceId_Object = MibTableColumn
cfprBiosVfFRB2TimerInstanceId = _CfprBiosVfFRB2TimerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 26, 1, 1),
    _CfprBiosVfFRB2TimerInstanceId_Type()
)
cfprBiosVfFRB2TimerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfFRB2TimerInstanceId.setStatus("current")
_CfprBiosVfFRB2TimerDn_Type = CfprManagedObjectDn
_CfprBiosVfFRB2TimerDn_Object = MibTableColumn
cfprBiosVfFRB2TimerDn = _CfprBiosVfFRB2TimerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 26, 1, 2),
    _CfprBiosVfFRB2TimerDn_Type()
)
cfprBiosVfFRB2TimerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfFRB2TimerDn.setStatus("current")
_CfprBiosVfFRB2TimerRn_Type = SnmpAdminString
_CfprBiosVfFRB2TimerRn_Object = MibTableColumn
cfprBiosVfFRB2TimerRn = _CfprBiosVfFRB2TimerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 26, 1, 3),
    _CfprBiosVfFRB2TimerRn_Type()
)
cfprBiosVfFRB2TimerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfFRB2TimerRn.setStatus("current")
_CfprBiosVfFRB2TimerVpFRB2Timer_Type = CfprBiosVfFRB2TimerVpFRB2Timer
_CfprBiosVfFRB2TimerVpFRB2Timer_Object = MibTableColumn
cfprBiosVfFRB2TimerVpFRB2Timer = _CfprBiosVfFRB2TimerVpFRB2Timer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 26, 1, 4),
    _CfprBiosVfFRB2TimerVpFRB2Timer_Type()
)
cfprBiosVfFRB2TimerVpFRB2Timer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfFRB2TimerVpFRB2Timer.setStatus("current")
_CfprBiosVfFRB2TimerSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfFRB2TimerSupportedByDefault_Object = MibTableColumn
cfprBiosVfFRB2TimerSupportedByDefault = _CfprBiosVfFRB2TimerSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 26, 1, 5),
    _CfprBiosVfFRB2TimerSupportedByDefault_Type()
)
cfprBiosVfFRB2TimerSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfFRB2TimerSupportedByDefault.setStatus("current")
_CfprBiosVfFrequencyFloorOverrideTable_Object = MibTable
cfprBiosVfFrequencyFloorOverrideTable = _CfprBiosVfFrequencyFloorOverrideTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 27)
)
if mibBuilder.loadTexts:
    cfprBiosVfFrequencyFloorOverrideTable.setStatus("current")
_CfprBiosVfFrequencyFloorOverrideEntry_Object = MibTableRow
cfprBiosVfFrequencyFloorOverrideEntry = _CfprBiosVfFrequencyFloorOverrideEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 27, 1)
)
cfprBiosVfFrequencyFloorOverrideEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfFrequencyFloorOverrideInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfFrequencyFloorOverrideEntry.setStatus("current")
_CfprBiosVfFrequencyFloorOverrideInstanceId_Type = CfprManagedObjectId
_CfprBiosVfFrequencyFloorOverrideInstanceId_Object = MibTableColumn
cfprBiosVfFrequencyFloorOverrideInstanceId = _CfprBiosVfFrequencyFloorOverrideInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 27, 1, 1),
    _CfprBiosVfFrequencyFloorOverrideInstanceId_Type()
)
cfprBiosVfFrequencyFloorOverrideInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfFrequencyFloorOverrideInstanceId.setStatus("current")
_CfprBiosVfFrequencyFloorOverrideDn_Type = CfprManagedObjectDn
_CfprBiosVfFrequencyFloorOverrideDn_Object = MibTableColumn
cfprBiosVfFrequencyFloorOverrideDn = _CfprBiosVfFrequencyFloorOverrideDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 27, 1, 2),
    _CfprBiosVfFrequencyFloorOverrideDn_Type()
)
cfprBiosVfFrequencyFloorOverrideDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfFrequencyFloorOverrideDn.setStatus("current")
_CfprBiosVfFrequencyFloorOverrideRn_Type = SnmpAdminString
_CfprBiosVfFrequencyFloorOverrideRn_Object = MibTableColumn
cfprBiosVfFrequencyFloorOverrideRn = _CfprBiosVfFrequencyFloorOverrideRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 27, 1, 3),
    _CfprBiosVfFrequencyFloorOverrideRn_Type()
)
cfprBiosVfFrequencyFloorOverrideRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfFrequencyFloorOverrideRn.setStatus("current")
_CfprBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride_Type = CfprBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride
_CfprBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride_Object = MibTableColumn
cfprBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride = _CfprBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 27, 1, 4),
    _CfprBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride_Type()
)
cfprBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride.setStatus("current")
_CfprBiosVfFrequencyFloorOverrideSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfFrequencyFloorOverrideSupportedByDefault_Object = MibTableColumn
cfprBiosVfFrequencyFloorOverrideSupportedByDefault = _CfprBiosVfFrequencyFloorOverrideSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 27, 1, 5),
    _CfprBiosVfFrequencyFloorOverrideSupportedByDefault_Type()
)
cfprBiosVfFrequencyFloorOverrideSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfFrequencyFloorOverrideSupportedByDefault.setStatus("current")
_CfprBiosVfFrontPanelLockoutTable_Object = MibTable
cfprBiosVfFrontPanelLockoutTable = _CfprBiosVfFrontPanelLockoutTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 28)
)
if mibBuilder.loadTexts:
    cfprBiosVfFrontPanelLockoutTable.setStatus("current")
_CfprBiosVfFrontPanelLockoutEntry_Object = MibTableRow
cfprBiosVfFrontPanelLockoutEntry = _CfprBiosVfFrontPanelLockoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 28, 1)
)
cfprBiosVfFrontPanelLockoutEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfFrontPanelLockoutInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfFrontPanelLockoutEntry.setStatus("current")
_CfprBiosVfFrontPanelLockoutInstanceId_Type = CfprManagedObjectId
_CfprBiosVfFrontPanelLockoutInstanceId_Object = MibTableColumn
cfprBiosVfFrontPanelLockoutInstanceId = _CfprBiosVfFrontPanelLockoutInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 28, 1, 1),
    _CfprBiosVfFrontPanelLockoutInstanceId_Type()
)
cfprBiosVfFrontPanelLockoutInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfFrontPanelLockoutInstanceId.setStatus("current")
_CfprBiosVfFrontPanelLockoutDn_Type = CfprManagedObjectDn
_CfprBiosVfFrontPanelLockoutDn_Object = MibTableColumn
cfprBiosVfFrontPanelLockoutDn = _CfprBiosVfFrontPanelLockoutDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 28, 1, 2),
    _CfprBiosVfFrontPanelLockoutDn_Type()
)
cfprBiosVfFrontPanelLockoutDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfFrontPanelLockoutDn.setStatus("current")
_CfprBiosVfFrontPanelLockoutRn_Type = SnmpAdminString
_CfprBiosVfFrontPanelLockoutRn_Object = MibTableColumn
cfprBiosVfFrontPanelLockoutRn = _CfprBiosVfFrontPanelLockoutRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 28, 1, 3),
    _CfprBiosVfFrontPanelLockoutRn_Type()
)
cfprBiosVfFrontPanelLockoutRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfFrontPanelLockoutRn.setStatus("current")
_CfprBiosVfFrontPanelLockoutVpFrontPanelLockout_Type = CfprBiosVfFrontPanelLockoutVpFrontPanelLockout
_CfprBiosVfFrontPanelLockoutVpFrontPanelLockout_Object = MibTableColumn
cfprBiosVfFrontPanelLockoutVpFrontPanelLockout = _CfprBiosVfFrontPanelLockoutVpFrontPanelLockout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 28, 1, 4),
    _CfprBiosVfFrontPanelLockoutVpFrontPanelLockout_Type()
)
cfprBiosVfFrontPanelLockoutVpFrontPanelLockout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfFrontPanelLockoutVpFrontPanelLockout.setStatus("current")
_CfprBiosVfFrontPanelLockoutSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfFrontPanelLockoutSupportedByDefault_Object = MibTableColumn
cfprBiosVfFrontPanelLockoutSupportedByDefault = _CfprBiosVfFrontPanelLockoutSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 28, 1, 5),
    _CfprBiosVfFrontPanelLockoutSupportedByDefault_Type()
)
cfprBiosVfFrontPanelLockoutSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfFrontPanelLockoutSupportedByDefault.setStatus("current")
_CfprBiosVfIntelEntrySASRAIDModuleTable_Object = MibTable
cfprBiosVfIntelEntrySASRAIDModuleTable = _CfprBiosVfIntelEntrySASRAIDModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 29)
)
if mibBuilder.loadTexts:
    cfprBiosVfIntelEntrySASRAIDModuleTable.setStatus("current")
_CfprBiosVfIntelEntrySASRAIDModuleEntry_Object = MibTableRow
cfprBiosVfIntelEntrySASRAIDModuleEntry = _CfprBiosVfIntelEntrySASRAIDModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 29, 1)
)
cfprBiosVfIntelEntrySASRAIDModuleEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfIntelEntrySASRAIDModuleInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfIntelEntrySASRAIDModuleEntry.setStatus("current")
_CfprBiosVfIntelEntrySASRAIDModuleInstanceId_Type = CfprManagedObjectId
_CfprBiosVfIntelEntrySASRAIDModuleInstanceId_Object = MibTableColumn
cfprBiosVfIntelEntrySASRAIDModuleInstanceId = _CfprBiosVfIntelEntrySASRAIDModuleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 29, 1, 1),
    _CfprBiosVfIntelEntrySASRAIDModuleInstanceId_Type()
)
cfprBiosVfIntelEntrySASRAIDModuleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfIntelEntrySASRAIDModuleInstanceId.setStatus("current")
_CfprBiosVfIntelEntrySASRAIDModuleDn_Type = CfprManagedObjectDn
_CfprBiosVfIntelEntrySASRAIDModuleDn_Object = MibTableColumn
cfprBiosVfIntelEntrySASRAIDModuleDn = _CfprBiosVfIntelEntrySASRAIDModuleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 29, 1, 2),
    _CfprBiosVfIntelEntrySASRAIDModuleDn_Type()
)
cfprBiosVfIntelEntrySASRAIDModuleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfIntelEntrySASRAIDModuleDn.setStatus("current")
_CfprBiosVfIntelEntrySASRAIDModuleRn_Type = SnmpAdminString
_CfprBiosVfIntelEntrySASRAIDModuleRn_Object = MibTableColumn
cfprBiosVfIntelEntrySASRAIDModuleRn = _CfprBiosVfIntelEntrySASRAIDModuleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 29, 1, 3),
    _CfprBiosVfIntelEntrySASRAIDModuleRn_Type()
)
cfprBiosVfIntelEntrySASRAIDModuleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfIntelEntrySASRAIDModuleRn.setStatus("current")
_CfprBiosVfIntelEntrySASRAIDModuleVpSASRAID_Type = CfprBiosVfIntelEntrySASRAIDModuleVpSASRAID
_CfprBiosVfIntelEntrySASRAIDModuleVpSASRAID_Object = MibTableColumn
cfprBiosVfIntelEntrySASRAIDModuleVpSASRAID = _CfprBiosVfIntelEntrySASRAIDModuleVpSASRAID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 29, 1, 4),
    _CfprBiosVfIntelEntrySASRAIDModuleVpSASRAID_Type()
)
cfprBiosVfIntelEntrySASRAIDModuleVpSASRAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfIntelEntrySASRAIDModuleVpSASRAID.setStatus("current")
_CfprBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule_Type = CfprBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule
_CfprBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule_Object = MibTableColumn
cfprBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule = _CfprBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 29, 1, 5),
    _CfprBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule_Type()
)
cfprBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule.setStatus("current")
_CfprBiosVfIntelEntrySASRAIDModuleSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfIntelEntrySASRAIDModuleSupportedByDefault_Object = MibTableColumn
cfprBiosVfIntelEntrySASRAIDModuleSupportedByDefault = _CfprBiosVfIntelEntrySASRAIDModuleSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 29, 1, 6),
    _CfprBiosVfIntelEntrySASRAIDModuleSupportedByDefault_Type()
)
cfprBiosVfIntelEntrySASRAIDModuleSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfIntelEntrySASRAIDModuleSupportedByDefault.setStatus("current")
_CfprBiosVfIntelHyperThreadingTechTable_Object = MibTable
cfprBiosVfIntelHyperThreadingTechTable = _CfprBiosVfIntelHyperThreadingTechTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 30)
)
if mibBuilder.loadTexts:
    cfprBiosVfIntelHyperThreadingTechTable.setStatus("current")
_CfprBiosVfIntelHyperThreadingTechEntry_Object = MibTableRow
cfprBiosVfIntelHyperThreadingTechEntry = _CfprBiosVfIntelHyperThreadingTechEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 30, 1)
)
cfprBiosVfIntelHyperThreadingTechEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfIntelHyperThreadingTechInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfIntelHyperThreadingTechEntry.setStatus("current")
_CfprBiosVfIntelHyperThreadingTechInstanceId_Type = CfprManagedObjectId
_CfprBiosVfIntelHyperThreadingTechInstanceId_Object = MibTableColumn
cfprBiosVfIntelHyperThreadingTechInstanceId = _CfprBiosVfIntelHyperThreadingTechInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 30, 1, 1),
    _CfprBiosVfIntelHyperThreadingTechInstanceId_Type()
)
cfprBiosVfIntelHyperThreadingTechInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfIntelHyperThreadingTechInstanceId.setStatus("current")
_CfprBiosVfIntelHyperThreadingTechDn_Type = CfprManagedObjectDn
_CfprBiosVfIntelHyperThreadingTechDn_Object = MibTableColumn
cfprBiosVfIntelHyperThreadingTechDn = _CfprBiosVfIntelHyperThreadingTechDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 30, 1, 2),
    _CfprBiosVfIntelHyperThreadingTechDn_Type()
)
cfprBiosVfIntelHyperThreadingTechDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfIntelHyperThreadingTechDn.setStatus("current")
_CfprBiosVfIntelHyperThreadingTechRn_Type = SnmpAdminString
_CfprBiosVfIntelHyperThreadingTechRn_Object = MibTableColumn
cfprBiosVfIntelHyperThreadingTechRn = _CfprBiosVfIntelHyperThreadingTechRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 30, 1, 3),
    _CfprBiosVfIntelHyperThreadingTechRn_Type()
)
cfprBiosVfIntelHyperThreadingTechRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfIntelHyperThreadingTechRn.setStatus("current")
_CfprBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech_Type = CfprBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech
_CfprBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech_Object = MibTableColumn
cfprBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech = _CfprBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 30, 1, 4),
    _CfprBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech_Type()
)
cfprBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech.setStatus("current")
_CfprBiosVfIntelHyperThreadingTechSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfIntelHyperThreadingTechSupportedByDefault_Object = MibTableColumn
cfprBiosVfIntelHyperThreadingTechSupportedByDefault = _CfprBiosVfIntelHyperThreadingTechSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 30, 1, 5),
    _CfprBiosVfIntelHyperThreadingTechSupportedByDefault_Type()
)
cfprBiosVfIntelHyperThreadingTechSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfIntelHyperThreadingTechSupportedByDefault.setStatus("current")
_CfprBiosVfIntelTurboBoostTechTable_Object = MibTable
cfprBiosVfIntelTurboBoostTechTable = _CfprBiosVfIntelTurboBoostTechTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 31)
)
if mibBuilder.loadTexts:
    cfprBiosVfIntelTurboBoostTechTable.setStatus("current")
_CfprBiosVfIntelTurboBoostTechEntry_Object = MibTableRow
cfprBiosVfIntelTurboBoostTechEntry = _CfprBiosVfIntelTurboBoostTechEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 31, 1)
)
cfprBiosVfIntelTurboBoostTechEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfIntelTurboBoostTechInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfIntelTurboBoostTechEntry.setStatus("current")
_CfprBiosVfIntelTurboBoostTechInstanceId_Type = CfprManagedObjectId
_CfprBiosVfIntelTurboBoostTechInstanceId_Object = MibTableColumn
cfprBiosVfIntelTurboBoostTechInstanceId = _CfprBiosVfIntelTurboBoostTechInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 31, 1, 1),
    _CfprBiosVfIntelTurboBoostTechInstanceId_Type()
)
cfprBiosVfIntelTurboBoostTechInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfIntelTurboBoostTechInstanceId.setStatus("current")
_CfprBiosVfIntelTurboBoostTechDn_Type = CfprManagedObjectDn
_CfprBiosVfIntelTurboBoostTechDn_Object = MibTableColumn
cfprBiosVfIntelTurboBoostTechDn = _CfprBiosVfIntelTurboBoostTechDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 31, 1, 2),
    _CfprBiosVfIntelTurboBoostTechDn_Type()
)
cfprBiosVfIntelTurboBoostTechDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfIntelTurboBoostTechDn.setStatus("current")
_CfprBiosVfIntelTurboBoostTechRn_Type = SnmpAdminString
_CfprBiosVfIntelTurboBoostTechRn_Object = MibTableColumn
cfprBiosVfIntelTurboBoostTechRn = _CfprBiosVfIntelTurboBoostTechRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 31, 1, 3),
    _CfprBiosVfIntelTurboBoostTechRn_Type()
)
cfprBiosVfIntelTurboBoostTechRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfIntelTurboBoostTechRn.setStatus("current")
_CfprBiosVfIntelTurboBoostTechVpIntelTurboBoostTech_Type = CfprBiosVfIntelTurboBoostTechVpIntelTurboBoostTech
_CfprBiosVfIntelTurboBoostTechVpIntelTurboBoostTech_Object = MibTableColumn
cfprBiosVfIntelTurboBoostTechVpIntelTurboBoostTech = _CfprBiosVfIntelTurboBoostTechVpIntelTurboBoostTech_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 31, 1, 4),
    _CfprBiosVfIntelTurboBoostTechVpIntelTurboBoostTech_Type()
)
cfprBiosVfIntelTurboBoostTechVpIntelTurboBoostTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfIntelTurboBoostTechVpIntelTurboBoostTech.setStatus("current")
_CfprBiosVfIntelTurboBoostTechSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfIntelTurboBoostTechSupportedByDefault_Object = MibTableColumn
cfprBiosVfIntelTurboBoostTechSupportedByDefault = _CfprBiosVfIntelTurboBoostTechSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 31, 1, 5),
    _CfprBiosVfIntelTurboBoostTechSupportedByDefault_Type()
)
cfprBiosVfIntelTurboBoostTechSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfIntelTurboBoostTechSupportedByDefault.setStatus("current")
_CfprBiosVfIntelVTForDirectedIOTable_Object = MibTable
cfprBiosVfIntelVTForDirectedIOTable = _CfprBiosVfIntelVTForDirectedIOTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 32)
)
if mibBuilder.loadTexts:
    cfprBiosVfIntelVTForDirectedIOTable.setStatus("current")
_CfprBiosVfIntelVTForDirectedIOEntry_Object = MibTableRow
cfprBiosVfIntelVTForDirectedIOEntry = _CfprBiosVfIntelVTForDirectedIOEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 32, 1)
)
cfprBiosVfIntelVTForDirectedIOEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfIntelVTForDirectedIOInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfIntelVTForDirectedIOEntry.setStatus("current")
_CfprBiosVfIntelVTForDirectedIOInstanceId_Type = CfprManagedObjectId
_CfprBiosVfIntelVTForDirectedIOInstanceId_Object = MibTableColumn
cfprBiosVfIntelVTForDirectedIOInstanceId = _CfprBiosVfIntelVTForDirectedIOInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 32, 1, 1),
    _CfprBiosVfIntelVTForDirectedIOInstanceId_Type()
)
cfprBiosVfIntelVTForDirectedIOInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfIntelVTForDirectedIOInstanceId.setStatus("current")
_CfprBiosVfIntelVTForDirectedIODn_Type = CfprManagedObjectDn
_CfprBiosVfIntelVTForDirectedIODn_Object = MibTableColumn
cfprBiosVfIntelVTForDirectedIODn = _CfprBiosVfIntelVTForDirectedIODn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 32, 1, 2),
    _CfprBiosVfIntelVTForDirectedIODn_Type()
)
cfprBiosVfIntelVTForDirectedIODn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfIntelVTForDirectedIODn.setStatus("current")
_CfprBiosVfIntelVTForDirectedIORn_Type = SnmpAdminString
_CfprBiosVfIntelVTForDirectedIORn_Object = MibTableColumn
cfprBiosVfIntelVTForDirectedIORn = _CfprBiosVfIntelVTForDirectedIORn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 32, 1, 3),
    _CfprBiosVfIntelVTForDirectedIORn_Type()
)
cfprBiosVfIntelVTForDirectedIORn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfIntelVTForDirectedIORn.setStatus("current")
_CfprBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport_Type = CfprBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport
_CfprBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport_Object = MibTableColumn
cfprBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport = _CfprBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 32, 1, 4),
    _CfprBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport_Type()
)
cfprBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport.setStatus("current")
_CfprBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport_Type = CfprBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport
_CfprBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport_Object = MibTableColumn
cfprBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport = _CfprBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 32, 1, 5),
    _CfprBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport_Type()
)
cfprBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport.setStatus("current")
_CfprBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping_Type = CfprBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping
_CfprBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping_Object = MibTableColumn
cfprBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping = _CfprBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 32, 1, 6),
    _CfprBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping_Type()
)
cfprBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping.setStatus("current")
_CfprBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport_Type = CfprBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport
_CfprBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport_Object = MibTableColumn
cfprBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport = _CfprBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 32, 1, 7),
    _CfprBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport_Type()
)
cfprBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport.setStatus("current")
_CfprBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO_Type = CfprBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO
_CfprBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO_Object = MibTableColumn
cfprBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO = _CfprBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 32, 1, 8),
    _CfprBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO_Type()
)
cfprBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO.setStatus("current")
_CfprBiosVfIntelVTForDirectedIOSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfIntelVTForDirectedIOSupportedByDefault_Object = MibTableColumn
cfprBiosVfIntelVTForDirectedIOSupportedByDefault = _CfprBiosVfIntelVTForDirectedIOSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 32, 1, 9),
    _CfprBiosVfIntelVTForDirectedIOSupportedByDefault_Type()
)
cfprBiosVfIntelVTForDirectedIOSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfIntelVTForDirectedIOSupportedByDefault.setStatus("current")
_CfprBiosVfIntelVirtualizationTechnologyTable_Object = MibTable
cfprBiosVfIntelVirtualizationTechnologyTable = _CfprBiosVfIntelVirtualizationTechnologyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 33)
)
if mibBuilder.loadTexts:
    cfprBiosVfIntelVirtualizationTechnologyTable.setStatus("current")
_CfprBiosVfIntelVirtualizationTechnologyEntry_Object = MibTableRow
cfprBiosVfIntelVirtualizationTechnologyEntry = _CfprBiosVfIntelVirtualizationTechnologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 33, 1)
)
cfprBiosVfIntelVirtualizationTechnologyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfIntelVirtualizationTechnologyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfIntelVirtualizationTechnologyEntry.setStatus("current")
_CfprBiosVfIntelVirtualizationTechnologyInstanceId_Type = CfprManagedObjectId
_CfprBiosVfIntelVirtualizationTechnologyInstanceId_Object = MibTableColumn
cfprBiosVfIntelVirtualizationTechnologyInstanceId = _CfprBiosVfIntelVirtualizationTechnologyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 33, 1, 1),
    _CfprBiosVfIntelVirtualizationTechnologyInstanceId_Type()
)
cfprBiosVfIntelVirtualizationTechnologyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfIntelVirtualizationTechnologyInstanceId.setStatus("current")
_CfprBiosVfIntelVirtualizationTechnologyDn_Type = CfprManagedObjectDn
_CfprBiosVfIntelVirtualizationTechnologyDn_Object = MibTableColumn
cfprBiosVfIntelVirtualizationTechnologyDn = _CfprBiosVfIntelVirtualizationTechnologyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 33, 1, 2),
    _CfprBiosVfIntelVirtualizationTechnologyDn_Type()
)
cfprBiosVfIntelVirtualizationTechnologyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfIntelVirtualizationTechnologyDn.setStatus("current")
_CfprBiosVfIntelVirtualizationTechnologyRn_Type = SnmpAdminString
_CfprBiosVfIntelVirtualizationTechnologyRn_Object = MibTableColumn
cfprBiosVfIntelVirtualizationTechnologyRn = _CfprBiosVfIntelVirtualizationTechnologyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 33, 1, 3),
    _CfprBiosVfIntelVirtualizationTechnologyRn_Type()
)
cfprBiosVfIntelVirtualizationTechnologyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfIntelVirtualizationTechnologyRn.setStatus("current")
_CfprBiosVfIntelVirtualizationTechnologyVpIntelVirtualizationTechnology_Type = CfprBiosVfIntelVirtualizationTechnologyVpIntelVirtTechnology
_CfprBiosVfIntelVirtualizationTechnologyVpIntelVirtualizationTechnology_Object = MibTableColumn
cfprBiosVfIntelVirtualizationTechnologyVpIntelVirtualizationTechnology = _CfprBiosVfIntelVirtualizationTechnologyVpIntelVirtualizationTechnology_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 33, 1, 4),
    _CfprBiosVfIntelVirtualizationTechnologyVpIntelVirtualizationTechnology_Type()
)
cfprBiosVfIntelVirtualizationTechnologyVpIntelVirtualizationTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfIntelVirtualizationTechnologyVpIntelVirtualizationTechnology.setStatus("current")
_CfprBiosVfIntelVirtualizationTechnologySupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfIntelVirtualizationTechnologySupportedByDefault_Object = MibTableColumn
cfprBiosVfIntelVirtualizationTechnologySupportedByDefault = _CfprBiosVfIntelVirtualizationTechnologySupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 33, 1, 5),
    _CfprBiosVfIntelVirtualizationTechnologySupportedByDefault_Type()
)
cfprBiosVfIntelVirtualizationTechnologySupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfIntelVirtualizationTechnologySupportedByDefault.setStatus("current")
_CfprBiosVfInterleaveConfigurationTable_Object = MibTable
cfprBiosVfInterleaveConfigurationTable = _CfprBiosVfInterleaveConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 34)
)
if mibBuilder.loadTexts:
    cfprBiosVfInterleaveConfigurationTable.setStatus("current")
_CfprBiosVfInterleaveConfigurationEntry_Object = MibTableRow
cfprBiosVfInterleaveConfigurationEntry = _CfprBiosVfInterleaveConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 34, 1)
)
cfprBiosVfInterleaveConfigurationEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfInterleaveConfigurationInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfInterleaveConfigurationEntry.setStatus("current")
_CfprBiosVfInterleaveConfigurationInstanceId_Type = CfprManagedObjectId
_CfprBiosVfInterleaveConfigurationInstanceId_Object = MibTableColumn
cfprBiosVfInterleaveConfigurationInstanceId = _CfprBiosVfInterleaveConfigurationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 34, 1, 1),
    _CfprBiosVfInterleaveConfigurationInstanceId_Type()
)
cfprBiosVfInterleaveConfigurationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfInterleaveConfigurationInstanceId.setStatus("current")
_CfprBiosVfInterleaveConfigurationDn_Type = CfprManagedObjectDn
_CfprBiosVfInterleaveConfigurationDn_Object = MibTableColumn
cfprBiosVfInterleaveConfigurationDn = _CfprBiosVfInterleaveConfigurationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 34, 1, 2),
    _CfprBiosVfInterleaveConfigurationDn_Type()
)
cfprBiosVfInterleaveConfigurationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfInterleaveConfigurationDn.setStatus("current")
_CfprBiosVfInterleaveConfigurationRn_Type = SnmpAdminString
_CfprBiosVfInterleaveConfigurationRn_Object = MibTableColumn
cfprBiosVfInterleaveConfigurationRn = _CfprBiosVfInterleaveConfigurationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 34, 1, 3),
    _CfprBiosVfInterleaveConfigurationRn_Type()
)
cfprBiosVfInterleaveConfigurationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfInterleaveConfigurationRn.setStatus("current")
_CfprBiosVfInterleaveConfigurationVpChannelInterleaving_Type = CfprBiosVfInterleaveConfigurationVpChannelInterleaving
_CfprBiosVfInterleaveConfigurationVpChannelInterleaving_Object = MibTableColumn
cfprBiosVfInterleaveConfigurationVpChannelInterleaving = _CfprBiosVfInterleaveConfigurationVpChannelInterleaving_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 34, 1, 4),
    _CfprBiosVfInterleaveConfigurationVpChannelInterleaving_Type()
)
cfprBiosVfInterleaveConfigurationVpChannelInterleaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfInterleaveConfigurationVpChannelInterleaving.setStatus("current")
_CfprBiosVfInterleaveConfigurationVpMemoryInterleaving_Type = CfprBiosVfInterleaveConfigurationVpMemoryInterleaving
_CfprBiosVfInterleaveConfigurationVpMemoryInterleaving_Object = MibTableColumn
cfprBiosVfInterleaveConfigurationVpMemoryInterleaving = _CfprBiosVfInterleaveConfigurationVpMemoryInterleaving_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 34, 1, 5),
    _CfprBiosVfInterleaveConfigurationVpMemoryInterleaving_Type()
)
cfprBiosVfInterleaveConfigurationVpMemoryInterleaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfInterleaveConfigurationVpMemoryInterleaving.setStatus("current")
_CfprBiosVfInterleaveConfigurationVpRankInterleaving_Type = CfprBiosVfInterleaveConfigurationVpRankInterleaving
_CfprBiosVfInterleaveConfigurationVpRankInterleaving_Object = MibTableColumn
cfprBiosVfInterleaveConfigurationVpRankInterleaving = _CfprBiosVfInterleaveConfigurationVpRankInterleaving_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 34, 1, 6),
    _CfprBiosVfInterleaveConfigurationVpRankInterleaving_Type()
)
cfprBiosVfInterleaveConfigurationVpRankInterleaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfInterleaveConfigurationVpRankInterleaving.setStatus("current")
_CfprBiosVfInterleaveConfigurationSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfInterleaveConfigurationSupportedByDefault_Object = MibTableColumn
cfprBiosVfInterleaveConfigurationSupportedByDefault = _CfprBiosVfInterleaveConfigurationSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 34, 1, 7),
    _CfprBiosVfInterleaveConfigurationSupportedByDefault_Type()
)
cfprBiosVfInterleaveConfigurationSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfInterleaveConfigurationSupportedByDefault.setStatus("current")
_CfprBiosVfLocalX2ApicTable_Object = MibTable
cfprBiosVfLocalX2ApicTable = _CfprBiosVfLocalX2ApicTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 35)
)
if mibBuilder.loadTexts:
    cfprBiosVfLocalX2ApicTable.setStatus("current")
_CfprBiosVfLocalX2ApicEntry_Object = MibTableRow
cfprBiosVfLocalX2ApicEntry = _CfprBiosVfLocalX2ApicEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 35, 1)
)
cfprBiosVfLocalX2ApicEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfLocalX2ApicInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfLocalX2ApicEntry.setStatus("current")
_CfprBiosVfLocalX2ApicInstanceId_Type = CfprManagedObjectId
_CfprBiosVfLocalX2ApicInstanceId_Object = MibTableColumn
cfprBiosVfLocalX2ApicInstanceId = _CfprBiosVfLocalX2ApicInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 35, 1, 1),
    _CfprBiosVfLocalX2ApicInstanceId_Type()
)
cfprBiosVfLocalX2ApicInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfLocalX2ApicInstanceId.setStatus("current")
_CfprBiosVfLocalX2ApicDn_Type = CfprManagedObjectDn
_CfprBiosVfLocalX2ApicDn_Object = MibTableColumn
cfprBiosVfLocalX2ApicDn = _CfprBiosVfLocalX2ApicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 35, 1, 2),
    _CfprBiosVfLocalX2ApicDn_Type()
)
cfprBiosVfLocalX2ApicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfLocalX2ApicDn.setStatus("current")
_CfprBiosVfLocalX2ApicRn_Type = SnmpAdminString
_CfprBiosVfLocalX2ApicRn_Object = MibTableColumn
cfprBiosVfLocalX2ApicRn = _CfprBiosVfLocalX2ApicRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 35, 1, 3),
    _CfprBiosVfLocalX2ApicRn_Type()
)
cfprBiosVfLocalX2ApicRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfLocalX2ApicRn.setStatus("current")
_CfprBiosVfLocalX2ApicVpLocalX2Apic_Type = CfprBiosVfLocalX2ApicVpLocalX2Apic
_CfprBiosVfLocalX2ApicVpLocalX2Apic_Object = MibTableColumn
cfprBiosVfLocalX2ApicVpLocalX2Apic = _CfprBiosVfLocalX2ApicVpLocalX2Apic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 35, 1, 4),
    _CfprBiosVfLocalX2ApicVpLocalX2Apic_Type()
)
cfprBiosVfLocalX2ApicVpLocalX2Apic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfLocalX2ApicVpLocalX2Apic.setStatus("current")
_CfprBiosVfLocalX2ApicSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfLocalX2ApicSupportedByDefault_Object = MibTableColumn
cfprBiosVfLocalX2ApicSupportedByDefault = _CfprBiosVfLocalX2ApicSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 35, 1, 5),
    _CfprBiosVfLocalX2ApicSupportedByDefault_Type()
)
cfprBiosVfLocalX2ApicSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfLocalX2ApicSupportedByDefault.setStatus("current")
_CfprBiosVfLvDIMMSupportTable_Object = MibTable
cfprBiosVfLvDIMMSupportTable = _CfprBiosVfLvDIMMSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 36)
)
if mibBuilder.loadTexts:
    cfprBiosVfLvDIMMSupportTable.setStatus("current")
_CfprBiosVfLvDIMMSupportEntry_Object = MibTableRow
cfprBiosVfLvDIMMSupportEntry = _CfprBiosVfLvDIMMSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 36, 1)
)
cfprBiosVfLvDIMMSupportEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfLvDIMMSupportInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfLvDIMMSupportEntry.setStatus("current")
_CfprBiosVfLvDIMMSupportInstanceId_Type = CfprManagedObjectId
_CfprBiosVfLvDIMMSupportInstanceId_Object = MibTableColumn
cfprBiosVfLvDIMMSupportInstanceId = _CfprBiosVfLvDIMMSupportInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 36, 1, 1),
    _CfprBiosVfLvDIMMSupportInstanceId_Type()
)
cfprBiosVfLvDIMMSupportInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfLvDIMMSupportInstanceId.setStatus("current")
_CfprBiosVfLvDIMMSupportDn_Type = CfprManagedObjectDn
_CfprBiosVfLvDIMMSupportDn_Object = MibTableColumn
cfprBiosVfLvDIMMSupportDn = _CfprBiosVfLvDIMMSupportDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 36, 1, 2),
    _CfprBiosVfLvDIMMSupportDn_Type()
)
cfprBiosVfLvDIMMSupportDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfLvDIMMSupportDn.setStatus("current")
_CfprBiosVfLvDIMMSupportRn_Type = SnmpAdminString
_CfprBiosVfLvDIMMSupportRn_Object = MibTableColumn
cfprBiosVfLvDIMMSupportRn = _CfprBiosVfLvDIMMSupportRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 36, 1, 3),
    _CfprBiosVfLvDIMMSupportRn_Type()
)
cfprBiosVfLvDIMMSupportRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfLvDIMMSupportRn.setStatus("current")
_CfprBiosVfLvDIMMSupportVpLvDDRMode_Type = CfprBiosVfLvDIMMSupportVpLvDDRMode
_CfprBiosVfLvDIMMSupportVpLvDDRMode_Object = MibTableColumn
cfprBiosVfLvDIMMSupportVpLvDDRMode = _CfprBiosVfLvDIMMSupportVpLvDDRMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 36, 1, 4),
    _CfprBiosVfLvDIMMSupportVpLvDDRMode_Type()
)
cfprBiosVfLvDIMMSupportVpLvDDRMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfLvDIMMSupportVpLvDDRMode.setStatus("current")
_CfprBiosVfLvDIMMSupportSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfLvDIMMSupportSupportedByDefault_Object = MibTableColumn
cfprBiosVfLvDIMMSupportSupportedByDefault = _CfprBiosVfLvDIMMSupportSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 36, 1, 5),
    _CfprBiosVfLvDIMMSupportSupportedByDefault_Type()
)
cfprBiosVfLvDIMMSupportSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfLvDIMMSupportSupportedByDefault.setStatus("current")
_CfprBiosVfMaxVariableMTRRSettingTable_Object = MibTable
cfprBiosVfMaxVariableMTRRSettingTable = _CfprBiosVfMaxVariableMTRRSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 37)
)
if mibBuilder.loadTexts:
    cfprBiosVfMaxVariableMTRRSettingTable.setStatus("current")
_CfprBiosVfMaxVariableMTRRSettingEntry_Object = MibTableRow
cfprBiosVfMaxVariableMTRRSettingEntry = _CfprBiosVfMaxVariableMTRRSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 37, 1)
)
cfprBiosVfMaxVariableMTRRSettingEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfMaxVariableMTRRSettingInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfMaxVariableMTRRSettingEntry.setStatus("current")
_CfprBiosVfMaxVariableMTRRSettingInstanceId_Type = CfprManagedObjectId
_CfprBiosVfMaxVariableMTRRSettingInstanceId_Object = MibTableColumn
cfprBiosVfMaxVariableMTRRSettingInstanceId = _CfprBiosVfMaxVariableMTRRSettingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 37, 1, 1),
    _CfprBiosVfMaxVariableMTRRSettingInstanceId_Type()
)
cfprBiosVfMaxVariableMTRRSettingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfMaxVariableMTRRSettingInstanceId.setStatus("current")
_CfprBiosVfMaxVariableMTRRSettingDn_Type = CfprManagedObjectDn
_CfprBiosVfMaxVariableMTRRSettingDn_Object = MibTableColumn
cfprBiosVfMaxVariableMTRRSettingDn = _CfprBiosVfMaxVariableMTRRSettingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 37, 1, 2),
    _CfprBiosVfMaxVariableMTRRSettingDn_Type()
)
cfprBiosVfMaxVariableMTRRSettingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfMaxVariableMTRRSettingDn.setStatus("current")
_CfprBiosVfMaxVariableMTRRSettingRn_Type = SnmpAdminString
_CfprBiosVfMaxVariableMTRRSettingRn_Object = MibTableColumn
cfprBiosVfMaxVariableMTRRSettingRn = _CfprBiosVfMaxVariableMTRRSettingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 37, 1, 3),
    _CfprBiosVfMaxVariableMTRRSettingRn_Type()
)
cfprBiosVfMaxVariableMTRRSettingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfMaxVariableMTRRSettingRn.setStatus("current")
_CfprBiosVfMaxVariableMTRRSettingVpProcessorMtrr_Type = CfprBiosVfMaxVariableMTRRSettingVpProcessorMtrr
_CfprBiosVfMaxVariableMTRRSettingVpProcessorMtrr_Object = MibTableColumn
cfprBiosVfMaxVariableMTRRSettingVpProcessorMtrr = _CfprBiosVfMaxVariableMTRRSettingVpProcessorMtrr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 37, 1, 4),
    _CfprBiosVfMaxVariableMTRRSettingVpProcessorMtrr_Type()
)
cfprBiosVfMaxVariableMTRRSettingVpProcessorMtrr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfMaxVariableMTRRSettingVpProcessorMtrr.setStatus("current")
_CfprBiosVfMaxVariableMTRRSettingSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfMaxVariableMTRRSettingSupportedByDefault_Object = MibTableColumn
cfprBiosVfMaxVariableMTRRSettingSupportedByDefault = _CfprBiosVfMaxVariableMTRRSettingSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 37, 1, 5),
    _CfprBiosVfMaxVariableMTRRSettingSupportedByDefault_Type()
)
cfprBiosVfMaxVariableMTRRSettingSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfMaxVariableMTRRSettingSupportedByDefault.setStatus("current")
_CfprBiosVfMaximumMemoryBelow4GBTable_Object = MibTable
cfprBiosVfMaximumMemoryBelow4GBTable = _CfprBiosVfMaximumMemoryBelow4GBTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 38)
)
if mibBuilder.loadTexts:
    cfprBiosVfMaximumMemoryBelow4GBTable.setStatus("current")
_CfprBiosVfMaximumMemoryBelow4GBEntry_Object = MibTableRow
cfprBiosVfMaximumMemoryBelow4GBEntry = _CfprBiosVfMaximumMemoryBelow4GBEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 38, 1)
)
cfprBiosVfMaximumMemoryBelow4GBEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfMaximumMemoryBelow4GBInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfMaximumMemoryBelow4GBEntry.setStatus("current")
_CfprBiosVfMaximumMemoryBelow4GBInstanceId_Type = CfprManagedObjectId
_CfprBiosVfMaximumMemoryBelow4GBInstanceId_Object = MibTableColumn
cfprBiosVfMaximumMemoryBelow4GBInstanceId = _CfprBiosVfMaximumMemoryBelow4GBInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 38, 1, 1),
    _CfprBiosVfMaximumMemoryBelow4GBInstanceId_Type()
)
cfprBiosVfMaximumMemoryBelow4GBInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfMaximumMemoryBelow4GBInstanceId.setStatus("current")
_CfprBiosVfMaximumMemoryBelow4GBDn_Type = CfprManagedObjectDn
_CfprBiosVfMaximumMemoryBelow4GBDn_Object = MibTableColumn
cfprBiosVfMaximumMemoryBelow4GBDn = _CfprBiosVfMaximumMemoryBelow4GBDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 38, 1, 2),
    _CfprBiosVfMaximumMemoryBelow4GBDn_Type()
)
cfprBiosVfMaximumMemoryBelow4GBDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfMaximumMemoryBelow4GBDn.setStatus("current")
_CfprBiosVfMaximumMemoryBelow4GBRn_Type = SnmpAdminString
_CfprBiosVfMaximumMemoryBelow4GBRn_Object = MibTableColumn
cfprBiosVfMaximumMemoryBelow4GBRn = _CfprBiosVfMaximumMemoryBelow4GBRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 38, 1, 3),
    _CfprBiosVfMaximumMemoryBelow4GBRn_Type()
)
cfprBiosVfMaximumMemoryBelow4GBRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfMaximumMemoryBelow4GBRn.setStatus("current")
_CfprBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB_Type = CfprBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB
_CfprBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB_Object = MibTableColumn
cfprBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB = _CfprBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 38, 1, 4),
    _CfprBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB_Type()
)
cfprBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB.setStatus("current")
_CfprBiosVfMaximumMemoryBelow4GBSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfMaximumMemoryBelow4GBSupportedByDefault_Object = MibTableColumn
cfprBiosVfMaximumMemoryBelow4GBSupportedByDefault = _CfprBiosVfMaximumMemoryBelow4GBSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 38, 1, 5),
    _CfprBiosVfMaximumMemoryBelow4GBSupportedByDefault_Type()
)
cfprBiosVfMaximumMemoryBelow4GBSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfMaximumMemoryBelow4GBSupportedByDefault.setStatus("current")
_CfprBiosVfMemoryMappedIOAbove4GBTable_Object = MibTable
cfprBiosVfMemoryMappedIOAbove4GBTable = _CfprBiosVfMemoryMappedIOAbove4GBTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 39)
)
if mibBuilder.loadTexts:
    cfprBiosVfMemoryMappedIOAbove4GBTable.setStatus("current")
_CfprBiosVfMemoryMappedIOAbove4GBEntry_Object = MibTableRow
cfprBiosVfMemoryMappedIOAbove4GBEntry = _CfprBiosVfMemoryMappedIOAbove4GBEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 39, 1)
)
cfprBiosVfMemoryMappedIOAbove4GBEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfMemoryMappedIOAbove4GBInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfMemoryMappedIOAbove4GBEntry.setStatus("current")
_CfprBiosVfMemoryMappedIOAbove4GBInstanceId_Type = CfprManagedObjectId
_CfprBiosVfMemoryMappedIOAbove4GBInstanceId_Object = MibTableColumn
cfprBiosVfMemoryMappedIOAbove4GBInstanceId = _CfprBiosVfMemoryMappedIOAbove4GBInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 39, 1, 1),
    _CfprBiosVfMemoryMappedIOAbove4GBInstanceId_Type()
)
cfprBiosVfMemoryMappedIOAbove4GBInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfMemoryMappedIOAbove4GBInstanceId.setStatus("current")
_CfprBiosVfMemoryMappedIOAbove4GBDn_Type = CfprManagedObjectDn
_CfprBiosVfMemoryMappedIOAbove4GBDn_Object = MibTableColumn
cfprBiosVfMemoryMappedIOAbove4GBDn = _CfprBiosVfMemoryMappedIOAbove4GBDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 39, 1, 2),
    _CfprBiosVfMemoryMappedIOAbove4GBDn_Type()
)
cfprBiosVfMemoryMappedIOAbove4GBDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfMemoryMappedIOAbove4GBDn.setStatus("current")
_CfprBiosVfMemoryMappedIOAbove4GBRn_Type = SnmpAdminString
_CfprBiosVfMemoryMappedIOAbove4GBRn_Object = MibTableColumn
cfprBiosVfMemoryMappedIOAbove4GBRn = _CfprBiosVfMemoryMappedIOAbove4GBRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 39, 1, 3),
    _CfprBiosVfMemoryMappedIOAbove4GBRn_Type()
)
cfprBiosVfMemoryMappedIOAbove4GBRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfMemoryMappedIOAbove4GBRn.setStatus("current")
_CfprBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB_Type = CfprBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB
_CfprBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB_Object = MibTableColumn
cfprBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB = _CfprBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 39, 1, 4),
    _CfprBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB_Type()
)
cfprBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB.setStatus("current")
_CfprBiosVfMemoryMappedIOAbove4GBSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfMemoryMappedIOAbove4GBSupportedByDefault_Object = MibTableColumn
cfprBiosVfMemoryMappedIOAbove4GBSupportedByDefault = _CfprBiosVfMemoryMappedIOAbove4GBSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 39, 1, 5),
    _CfprBiosVfMemoryMappedIOAbove4GBSupportedByDefault_Type()
)
cfprBiosVfMemoryMappedIOAbove4GBSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfMemoryMappedIOAbove4GBSupportedByDefault.setStatus("current")
_CfprBiosVfMirroringModeTable_Object = MibTable
cfprBiosVfMirroringModeTable = _CfprBiosVfMirroringModeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 40)
)
if mibBuilder.loadTexts:
    cfprBiosVfMirroringModeTable.setStatus("current")
_CfprBiosVfMirroringModeEntry_Object = MibTableRow
cfprBiosVfMirroringModeEntry = _CfprBiosVfMirroringModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 40, 1)
)
cfprBiosVfMirroringModeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfMirroringModeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfMirroringModeEntry.setStatus("current")
_CfprBiosVfMirroringModeInstanceId_Type = CfprManagedObjectId
_CfprBiosVfMirroringModeInstanceId_Object = MibTableColumn
cfprBiosVfMirroringModeInstanceId = _CfprBiosVfMirroringModeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 40, 1, 1),
    _CfprBiosVfMirroringModeInstanceId_Type()
)
cfprBiosVfMirroringModeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfMirroringModeInstanceId.setStatus("current")
_CfprBiosVfMirroringModeDn_Type = CfprManagedObjectDn
_CfprBiosVfMirroringModeDn_Object = MibTableColumn
cfprBiosVfMirroringModeDn = _CfprBiosVfMirroringModeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 40, 1, 2),
    _CfprBiosVfMirroringModeDn_Type()
)
cfprBiosVfMirroringModeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfMirroringModeDn.setStatus("current")
_CfprBiosVfMirroringModeRn_Type = SnmpAdminString
_CfprBiosVfMirroringModeRn_Object = MibTableColumn
cfprBiosVfMirroringModeRn = _CfprBiosVfMirroringModeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 40, 1, 3),
    _CfprBiosVfMirroringModeRn_Type()
)
cfprBiosVfMirroringModeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfMirroringModeRn.setStatus("current")
_CfprBiosVfMirroringModeVpMirroringMode_Type = CfprBiosVfMirroringModeVpMirroringMode
_CfprBiosVfMirroringModeVpMirroringMode_Object = MibTableColumn
cfprBiosVfMirroringModeVpMirroringMode = _CfprBiosVfMirroringModeVpMirroringMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 40, 1, 4),
    _CfprBiosVfMirroringModeVpMirroringMode_Type()
)
cfprBiosVfMirroringModeVpMirroringMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfMirroringModeVpMirroringMode.setStatus("current")
_CfprBiosVfMirroringModeSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfMirroringModeSupportedByDefault_Object = MibTableColumn
cfprBiosVfMirroringModeSupportedByDefault = _CfprBiosVfMirroringModeSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 40, 1, 5),
    _CfprBiosVfMirroringModeSupportedByDefault_Type()
)
cfprBiosVfMirroringModeSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfMirroringModeSupportedByDefault.setStatus("current")
_CfprBiosVfNUMAOptimizedTable_Object = MibTable
cfprBiosVfNUMAOptimizedTable = _CfprBiosVfNUMAOptimizedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 41)
)
if mibBuilder.loadTexts:
    cfprBiosVfNUMAOptimizedTable.setStatus("current")
_CfprBiosVfNUMAOptimizedEntry_Object = MibTableRow
cfprBiosVfNUMAOptimizedEntry = _CfprBiosVfNUMAOptimizedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 41, 1)
)
cfprBiosVfNUMAOptimizedEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfNUMAOptimizedInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfNUMAOptimizedEntry.setStatus("current")
_CfprBiosVfNUMAOptimizedInstanceId_Type = CfprManagedObjectId
_CfprBiosVfNUMAOptimizedInstanceId_Object = MibTableColumn
cfprBiosVfNUMAOptimizedInstanceId = _CfprBiosVfNUMAOptimizedInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 41, 1, 1),
    _CfprBiosVfNUMAOptimizedInstanceId_Type()
)
cfprBiosVfNUMAOptimizedInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfNUMAOptimizedInstanceId.setStatus("current")
_CfprBiosVfNUMAOptimizedDn_Type = CfprManagedObjectDn
_CfprBiosVfNUMAOptimizedDn_Object = MibTableColumn
cfprBiosVfNUMAOptimizedDn = _CfprBiosVfNUMAOptimizedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 41, 1, 2),
    _CfprBiosVfNUMAOptimizedDn_Type()
)
cfprBiosVfNUMAOptimizedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfNUMAOptimizedDn.setStatus("current")
_CfprBiosVfNUMAOptimizedRn_Type = SnmpAdminString
_CfprBiosVfNUMAOptimizedRn_Object = MibTableColumn
cfprBiosVfNUMAOptimizedRn = _CfprBiosVfNUMAOptimizedRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 41, 1, 3),
    _CfprBiosVfNUMAOptimizedRn_Type()
)
cfprBiosVfNUMAOptimizedRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfNUMAOptimizedRn.setStatus("current")
_CfprBiosVfNUMAOptimizedVpNUMAOptimized_Type = CfprBiosVfNUMAOptimizedVpNUMAOptimized
_CfprBiosVfNUMAOptimizedVpNUMAOptimized_Object = MibTableColumn
cfprBiosVfNUMAOptimizedVpNUMAOptimized = _CfprBiosVfNUMAOptimizedVpNUMAOptimized_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 41, 1, 4),
    _CfprBiosVfNUMAOptimizedVpNUMAOptimized_Type()
)
cfprBiosVfNUMAOptimizedVpNUMAOptimized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfNUMAOptimizedVpNUMAOptimized.setStatus("current")
_CfprBiosVfNUMAOptimizedSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfNUMAOptimizedSupportedByDefault_Object = MibTableColumn
cfprBiosVfNUMAOptimizedSupportedByDefault = _CfprBiosVfNUMAOptimizedSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 41, 1, 5),
    _CfprBiosVfNUMAOptimizedSupportedByDefault_Type()
)
cfprBiosVfNUMAOptimizedSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfNUMAOptimizedSupportedByDefault.setStatus("current")
_CfprBiosVfOSBootWatchdogTimerTable_Object = MibTable
cfprBiosVfOSBootWatchdogTimerTable = _CfprBiosVfOSBootWatchdogTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 42)
)
if mibBuilder.loadTexts:
    cfprBiosVfOSBootWatchdogTimerTable.setStatus("current")
_CfprBiosVfOSBootWatchdogTimerEntry_Object = MibTableRow
cfprBiosVfOSBootWatchdogTimerEntry = _CfprBiosVfOSBootWatchdogTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 42, 1)
)
cfprBiosVfOSBootWatchdogTimerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfOSBootWatchdogTimerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfOSBootWatchdogTimerEntry.setStatus("current")
_CfprBiosVfOSBootWatchdogTimerInstanceId_Type = CfprManagedObjectId
_CfprBiosVfOSBootWatchdogTimerInstanceId_Object = MibTableColumn
cfprBiosVfOSBootWatchdogTimerInstanceId = _CfprBiosVfOSBootWatchdogTimerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 42, 1, 1),
    _CfprBiosVfOSBootWatchdogTimerInstanceId_Type()
)
cfprBiosVfOSBootWatchdogTimerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfOSBootWatchdogTimerInstanceId.setStatus("current")
_CfprBiosVfOSBootWatchdogTimerDn_Type = CfprManagedObjectDn
_CfprBiosVfOSBootWatchdogTimerDn_Object = MibTableColumn
cfprBiosVfOSBootWatchdogTimerDn = _CfprBiosVfOSBootWatchdogTimerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 42, 1, 2),
    _CfprBiosVfOSBootWatchdogTimerDn_Type()
)
cfprBiosVfOSBootWatchdogTimerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOSBootWatchdogTimerDn.setStatus("current")
_CfprBiosVfOSBootWatchdogTimerRn_Type = SnmpAdminString
_CfprBiosVfOSBootWatchdogTimerRn_Object = MibTableColumn
cfprBiosVfOSBootWatchdogTimerRn = _CfprBiosVfOSBootWatchdogTimerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 42, 1, 3),
    _CfprBiosVfOSBootWatchdogTimerRn_Type()
)
cfprBiosVfOSBootWatchdogTimerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOSBootWatchdogTimerRn.setStatus("current")
_CfprBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer_Type = CfprBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer
_CfprBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer_Object = MibTableColumn
cfprBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer = _CfprBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 42, 1, 4),
    _CfprBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer_Type()
)
cfprBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer.setStatus("current")
_CfprBiosVfOSBootWatchdogTimerSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfOSBootWatchdogTimerSupportedByDefault_Object = MibTableColumn
cfprBiosVfOSBootWatchdogTimerSupportedByDefault = _CfprBiosVfOSBootWatchdogTimerSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 42, 1, 5),
    _CfprBiosVfOSBootWatchdogTimerSupportedByDefault_Type()
)
cfprBiosVfOSBootWatchdogTimerSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOSBootWatchdogTimerSupportedByDefault.setStatus("current")
_CfprBiosVfOSBootWatchdogTimerPolicyTable_Object = MibTable
cfprBiosVfOSBootWatchdogTimerPolicyTable = _CfprBiosVfOSBootWatchdogTimerPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 43)
)
if mibBuilder.loadTexts:
    cfprBiosVfOSBootWatchdogTimerPolicyTable.setStatus("current")
_CfprBiosVfOSBootWatchdogTimerPolicyEntry_Object = MibTableRow
cfprBiosVfOSBootWatchdogTimerPolicyEntry = _CfprBiosVfOSBootWatchdogTimerPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 43, 1)
)
cfprBiosVfOSBootWatchdogTimerPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfOSBootWatchdogTimerPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfOSBootWatchdogTimerPolicyEntry.setStatus("current")
_CfprBiosVfOSBootWatchdogTimerPolicyInstanceId_Type = CfprManagedObjectId
_CfprBiosVfOSBootWatchdogTimerPolicyInstanceId_Object = MibTableColumn
cfprBiosVfOSBootWatchdogTimerPolicyInstanceId = _CfprBiosVfOSBootWatchdogTimerPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 43, 1, 1),
    _CfprBiosVfOSBootWatchdogTimerPolicyInstanceId_Type()
)
cfprBiosVfOSBootWatchdogTimerPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfOSBootWatchdogTimerPolicyInstanceId.setStatus("current")
_CfprBiosVfOSBootWatchdogTimerPolicyDn_Type = CfprManagedObjectDn
_CfprBiosVfOSBootWatchdogTimerPolicyDn_Object = MibTableColumn
cfprBiosVfOSBootWatchdogTimerPolicyDn = _CfprBiosVfOSBootWatchdogTimerPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 43, 1, 2),
    _CfprBiosVfOSBootWatchdogTimerPolicyDn_Type()
)
cfprBiosVfOSBootWatchdogTimerPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOSBootWatchdogTimerPolicyDn.setStatus("current")
_CfprBiosVfOSBootWatchdogTimerPolicyRn_Type = SnmpAdminString
_CfprBiosVfOSBootWatchdogTimerPolicyRn_Object = MibTableColumn
cfprBiosVfOSBootWatchdogTimerPolicyRn = _CfprBiosVfOSBootWatchdogTimerPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 43, 1, 3),
    _CfprBiosVfOSBootWatchdogTimerPolicyRn_Type()
)
cfprBiosVfOSBootWatchdogTimerPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOSBootWatchdogTimerPolicyRn.setStatus("current")
_CfprBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy_Type = CfprBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy
_CfprBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy_Object = MibTableColumn
cfprBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy = _CfprBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 43, 1, 4),
    _CfprBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy_Type()
)
cfprBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy.setStatus("current")
_CfprBiosVfOSBootWatchdogTimerPolicySupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfOSBootWatchdogTimerPolicySupportedByDefault_Object = MibTableColumn
cfprBiosVfOSBootWatchdogTimerPolicySupportedByDefault = _CfprBiosVfOSBootWatchdogTimerPolicySupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 43, 1, 5),
    _CfprBiosVfOSBootWatchdogTimerPolicySupportedByDefault_Type()
)
cfprBiosVfOSBootWatchdogTimerPolicySupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOSBootWatchdogTimerPolicySupportedByDefault.setStatus("current")
_CfprBiosVfOSBootWatchdogTimerTimeoutTable_Object = MibTable
cfprBiosVfOSBootWatchdogTimerTimeoutTable = _CfprBiosVfOSBootWatchdogTimerTimeoutTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 44)
)
if mibBuilder.loadTexts:
    cfprBiosVfOSBootWatchdogTimerTimeoutTable.setStatus("current")
_CfprBiosVfOSBootWatchdogTimerTimeoutEntry_Object = MibTableRow
cfprBiosVfOSBootWatchdogTimerTimeoutEntry = _CfprBiosVfOSBootWatchdogTimerTimeoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 44, 1)
)
cfprBiosVfOSBootWatchdogTimerTimeoutEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfOSBootWatchdogTimerTimeoutInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfOSBootWatchdogTimerTimeoutEntry.setStatus("current")
_CfprBiosVfOSBootWatchdogTimerTimeoutInstanceId_Type = CfprManagedObjectId
_CfprBiosVfOSBootWatchdogTimerTimeoutInstanceId_Object = MibTableColumn
cfprBiosVfOSBootWatchdogTimerTimeoutInstanceId = _CfprBiosVfOSBootWatchdogTimerTimeoutInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 44, 1, 1),
    _CfprBiosVfOSBootWatchdogTimerTimeoutInstanceId_Type()
)
cfprBiosVfOSBootWatchdogTimerTimeoutInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfOSBootWatchdogTimerTimeoutInstanceId.setStatus("current")
_CfprBiosVfOSBootWatchdogTimerTimeoutDn_Type = CfprManagedObjectDn
_CfprBiosVfOSBootWatchdogTimerTimeoutDn_Object = MibTableColumn
cfprBiosVfOSBootWatchdogTimerTimeoutDn = _CfprBiosVfOSBootWatchdogTimerTimeoutDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 44, 1, 2),
    _CfprBiosVfOSBootWatchdogTimerTimeoutDn_Type()
)
cfprBiosVfOSBootWatchdogTimerTimeoutDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOSBootWatchdogTimerTimeoutDn.setStatus("current")
_CfprBiosVfOSBootWatchdogTimerTimeoutRn_Type = SnmpAdminString
_CfprBiosVfOSBootWatchdogTimerTimeoutRn_Object = MibTableColumn
cfprBiosVfOSBootWatchdogTimerTimeoutRn = _CfprBiosVfOSBootWatchdogTimerTimeoutRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 44, 1, 3),
    _CfprBiosVfOSBootWatchdogTimerTimeoutRn_Type()
)
cfprBiosVfOSBootWatchdogTimerTimeoutRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOSBootWatchdogTimerTimeoutRn.setStatus("current")
_CfprBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout_Type = CfprBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout
_CfprBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout_Object = MibTableColumn
cfprBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout = _CfprBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 44, 1, 4),
    _CfprBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout_Type()
)
cfprBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout.setStatus("current")
_CfprBiosVfOSBootWatchdogTimerTimeoutSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfOSBootWatchdogTimerTimeoutSupportedByDefault_Object = MibTableColumn
cfprBiosVfOSBootWatchdogTimerTimeoutSupportedByDefault = _CfprBiosVfOSBootWatchdogTimerTimeoutSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 44, 1, 5),
    _CfprBiosVfOSBootWatchdogTimerTimeoutSupportedByDefault_Type()
)
cfprBiosVfOSBootWatchdogTimerTimeoutSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOSBootWatchdogTimerTimeoutSupportedByDefault.setStatus("current")
_CfprBiosVfOnboardSATAControllerTable_Object = MibTable
cfprBiosVfOnboardSATAControllerTable = _CfprBiosVfOnboardSATAControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 45)
)
if mibBuilder.loadTexts:
    cfprBiosVfOnboardSATAControllerTable.setStatus("current")
_CfprBiosVfOnboardSATAControllerEntry_Object = MibTableRow
cfprBiosVfOnboardSATAControllerEntry = _CfprBiosVfOnboardSATAControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 45, 1)
)
cfprBiosVfOnboardSATAControllerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfOnboardSATAControllerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfOnboardSATAControllerEntry.setStatus("current")
_CfprBiosVfOnboardSATAControllerInstanceId_Type = CfprManagedObjectId
_CfprBiosVfOnboardSATAControllerInstanceId_Object = MibTableColumn
cfprBiosVfOnboardSATAControllerInstanceId = _CfprBiosVfOnboardSATAControllerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 45, 1, 1),
    _CfprBiosVfOnboardSATAControllerInstanceId_Type()
)
cfprBiosVfOnboardSATAControllerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfOnboardSATAControllerInstanceId.setStatus("current")
_CfprBiosVfOnboardSATAControllerDn_Type = CfprManagedObjectDn
_CfprBiosVfOnboardSATAControllerDn_Object = MibTableColumn
cfprBiosVfOnboardSATAControllerDn = _CfprBiosVfOnboardSATAControllerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 45, 1, 2),
    _CfprBiosVfOnboardSATAControllerDn_Type()
)
cfprBiosVfOnboardSATAControllerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOnboardSATAControllerDn.setStatus("current")
_CfprBiosVfOnboardSATAControllerRn_Type = SnmpAdminString
_CfprBiosVfOnboardSATAControllerRn_Object = MibTableColumn
cfprBiosVfOnboardSATAControllerRn = _CfprBiosVfOnboardSATAControllerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 45, 1, 3),
    _CfprBiosVfOnboardSATAControllerRn_Type()
)
cfprBiosVfOnboardSATAControllerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOnboardSATAControllerRn.setStatus("current")
_CfprBiosVfOnboardSATAControllerVpOnboardSATAController_Type = CfprBiosVfOnboardSATAControllerVpOnboardSATAController
_CfprBiosVfOnboardSATAControllerVpOnboardSATAController_Object = MibTableColumn
cfprBiosVfOnboardSATAControllerVpOnboardSATAController = _CfprBiosVfOnboardSATAControllerVpOnboardSATAController_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 45, 1, 4),
    _CfprBiosVfOnboardSATAControllerVpOnboardSATAController_Type()
)
cfprBiosVfOnboardSATAControllerVpOnboardSATAController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOnboardSATAControllerVpOnboardSATAController.setStatus("current")
_CfprBiosVfOnboardSATAControllerVpSATAMode_Type = CfprBiosVfOnboardSATAControllerVpSATAMode
_CfprBiosVfOnboardSATAControllerVpSATAMode_Object = MibTableColumn
cfprBiosVfOnboardSATAControllerVpSATAMode = _CfprBiosVfOnboardSATAControllerVpSATAMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 45, 1, 5),
    _CfprBiosVfOnboardSATAControllerVpSATAMode_Type()
)
cfprBiosVfOnboardSATAControllerVpSATAMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOnboardSATAControllerVpSATAMode.setStatus("current")
_CfprBiosVfOnboardSATAControllerSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfOnboardSATAControllerSupportedByDefault_Object = MibTableColumn
cfprBiosVfOnboardSATAControllerSupportedByDefault = _CfprBiosVfOnboardSATAControllerSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 45, 1, 6),
    _CfprBiosVfOnboardSATAControllerSupportedByDefault_Type()
)
cfprBiosVfOnboardSATAControllerSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOnboardSATAControllerSupportedByDefault.setStatus("current")
_CfprBiosVfOnboardStorageTable_Object = MibTable
cfprBiosVfOnboardStorageTable = _CfprBiosVfOnboardStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 46)
)
if mibBuilder.loadTexts:
    cfprBiosVfOnboardStorageTable.setStatus("current")
_CfprBiosVfOnboardStorageEntry_Object = MibTableRow
cfprBiosVfOnboardStorageEntry = _CfprBiosVfOnboardStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 46, 1)
)
cfprBiosVfOnboardStorageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfOnboardStorageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfOnboardStorageEntry.setStatus("current")
_CfprBiosVfOnboardStorageInstanceId_Type = CfprManagedObjectId
_CfprBiosVfOnboardStorageInstanceId_Object = MibTableColumn
cfprBiosVfOnboardStorageInstanceId = _CfprBiosVfOnboardStorageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 46, 1, 1),
    _CfprBiosVfOnboardStorageInstanceId_Type()
)
cfprBiosVfOnboardStorageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfOnboardStorageInstanceId.setStatus("current")
_CfprBiosVfOnboardStorageDn_Type = CfprManagedObjectDn
_CfprBiosVfOnboardStorageDn_Object = MibTableColumn
cfprBiosVfOnboardStorageDn = _CfprBiosVfOnboardStorageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 46, 1, 2),
    _CfprBiosVfOnboardStorageDn_Type()
)
cfprBiosVfOnboardStorageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOnboardStorageDn.setStatus("current")
_CfprBiosVfOnboardStorageRn_Type = SnmpAdminString
_CfprBiosVfOnboardStorageRn_Object = MibTableColumn
cfprBiosVfOnboardStorageRn = _CfprBiosVfOnboardStorageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 46, 1, 3),
    _CfprBiosVfOnboardStorageRn_Type()
)
cfprBiosVfOnboardStorageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOnboardStorageRn.setStatus("current")
_CfprBiosVfOnboardStorageVpOnboardSCUStorageSupport_Type = CfprBiosVfOnboardStorageVpOnboardSCUStorageSupport
_CfprBiosVfOnboardStorageVpOnboardSCUStorageSupport_Object = MibTableColumn
cfprBiosVfOnboardStorageVpOnboardSCUStorageSupport = _CfprBiosVfOnboardStorageVpOnboardSCUStorageSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 46, 1, 4),
    _CfprBiosVfOnboardStorageVpOnboardSCUStorageSupport_Type()
)
cfprBiosVfOnboardStorageVpOnboardSCUStorageSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOnboardStorageVpOnboardSCUStorageSupport.setStatus("current")
_CfprBiosVfOnboardStorageSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfOnboardStorageSupportedByDefault_Object = MibTableColumn
cfprBiosVfOnboardStorageSupportedByDefault = _CfprBiosVfOnboardStorageSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 46, 1, 5),
    _CfprBiosVfOnboardStorageSupportedByDefault_Type()
)
cfprBiosVfOnboardStorageSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOnboardStorageSupportedByDefault.setStatus("current")
_CfprBiosVfOptionROMEnableTable_Object = MibTable
cfprBiosVfOptionROMEnableTable = _CfprBiosVfOptionROMEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 47)
)
if mibBuilder.loadTexts:
    cfprBiosVfOptionROMEnableTable.setStatus("current")
_CfprBiosVfOptionROMEnableEntry_Object = MibTableRow
cfprBiosVfOptionROMEnableEntry = _CfprBiosVfOptionROMEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 47, 1)
)
cfprBiosVfOptionROMEnableEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfOptionROMEnableInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfOptionROMEnableEntry.setStatus("current")
_CfprBiosVfOptionROMEnableInstanceId_Type = CfprManagedObjectId
_CfprBiosVfOptionROMEnableInstanceId_Object = MibTableColumn
cfprBiosVfOptionROMEnableInstanceId = _CfprBiosVfOptionROMEnableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 47, 1, 1),
    _CfprBiosVfOptionROMEnableInstanceId_Type()
)
cfprBiosVfOptionROMEnableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfOptionROMEnableInstanceId.setStatus("current")
_CfprBiosVfOptionROMEnableDn_Type = CfprManagedObjectDn
_CfprBiosVfOptionROMEnableDn_Object = MibTableColumn
cfprBiosVfOptionROMEnableDn = _CfprBiosVfOptionROMEnableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 47, 1, 2),
    _CfprBiosVfOptionROMEnableDn_Type()
)
cfprBiosVfOptionROMEnableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOptionROMEnableDn.setStatus("current")
_CfprBiosVfOptionROMEnableRn_Type = SnmpAdminString
_CfprBiosVfOptionROMEnableRn_Object = MibTableColumn
cfprBiosVfOptionROMEnableRn = _CfprBiosVfOptionROMEnableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 47, 1, 3),
    _CfprBiosVfOptionROMEnableRn_Type()
)
cfprBiosVfOptionROMEnableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOptionROMEnableRn.setStatus("current")
_CfprBiosVfOptionROMEnableVpState_Type = CfprBiosVfOptionROMEnableVpState
_CfprBiosVfOptionROMEnableVpState_Object = MibTableColumn
cfprBiosVfOptionROMEnableVpState = _CfprBiosVfOptionROMEnableVpState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 47, 1, 4),
    _CfprBiosVfOptionROMEnableVpState_Type()
)
cfprBiosVfOptionROMEnableVpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOptionROMEnableVpState.setStatus("current")
_CfprBiosVfOptionROMEnableSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfOptionROMEnableSupportedByDefault_Object = MibTableColumn
cfprBiosVfOptionROMEnableSupportedByDefault = _CfprBiosVfOptionROMEnableSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 47, 1, 5),
    _CfprBiosVfOptionROMEnableSupportedByDefault_Type()
)
cfprBiosVfOptionROMEnableSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOptionROMEnableSupportedByDefault.setStatus("current")
_CfprBiosVfOptionROMLoadTable_Object = MibTable
cfprBiosVfOptionROMLoadTable = _CfprBiosVfOptionROMLoadTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 48)
)
if mibBuilder.loadTexts:
    cfprBiosVfOptionROMLoadTable.setStatus("current")
_CfprBiosVfOptionROMLoadEntry_Object = MibTableRow
cfprBiosVfOptionROMLoadEntry = _CfprBiosVfOptionROMLoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 48, 1)
)
cfprBiosVfOptionROMLoadEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfOptionROMLoadInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfOptionROMLoadEntry.setStatus("current")
_CfprBiosVfOptionROMLoadInstanceId_Type = CfprManagedObjectId
_CfprBiosVfOptionROMLoadInstanceId_Object = MibTableColumn
cfprBiosVfOptionROMLoadInstanceId = _CfprBiosVfOptionROMLoadInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 48, 1, 1),
    _CfprBiosVfOptionROMLoadInstanceId_Type()
)
cfprBiosVfOptionROMLoadInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfOptionROMLoadInstanceId.setStatus("current")
_CfprBiosVfOptionROMLoadDn_Type = CfprManagedObjectDn
_CfprBiosVfOptionROMLoadDn_Object = MibTableColumn
cfprBiosVfOptionROMLoadDn = _CfprBiosVfOptionROMLoadDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 48, 1, 2),
    _CfprBiosVfOptionROMLoadDn_Type()
)
cfprBiosVfOptionROMLoadDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOptionROMLoadDn.setStatus("current")
_CfprBiosVfOptionROMLoadRn_Type = SnmpAdminString
_CfprBiosVfOptionROMLoadRn_Object = MibTableColumn
cfprBiosVfOptionROMLoadRn = _CfprBiosVfOptionROMLoadRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 48, 1, 3),
    _CfprBiosVfOptionROMLoadRn_Type()
)
cfprBiosVfOptionROMLoadRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOptionROMLoadRn.setStatus("current")
_CfprBiosVfOptionROMLoadVpLoad_Type = CfprBiosVfOptionROMLoadVpLoad
_CfprBiosVfOptionROMLoadVpLoad_Object = MibTableColumn
cfprBiosVfOptionROMLoadVpLoad = _CfprBiosVfOptionROMLoadVpLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 48, 1, 4),
    _CfprBiosVfOptionROMLoadVpLoad_Type()
)
cfprBiosVfOptionROMLoadVpLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOptionROMLoadVpLoad.setStatus("current")
_CfprBiosVfOptionROMLoadSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfOptionROMLoadSupportedByDefault_Object = MibTableColumn
cfprBiosVfOptionROMLoadSupportedByDefault = _CfprBiosVfOptionROMLoadSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 48, 1, 5),
    _CfprBiosVfOptionROMLoadSupportedByDefault_Type()
)
cfprBiosVfOptionROMLoadSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfOptionROMLoadSupportedByDefault.setStatus("current")
_CfprBiosVfPCISlotLinkSpeedTable_Object = MibTable
cfprBiosVfPCISlotLinkSpeedTable = _CfprBiosVfPCISlotLinkSpeedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 49)
)
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotLinkSpeedTable.setStatus("current")
_CfprBiosVfPCISlotLinkSpeedEntry_Object = MibTableRow
cfprBiosVfPCISlotLinkSpeedEntry = _CfprBiosVfPCISlotLinkSpeedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 49, 1)
)
cfprBiosVfPCISlotLinkSpeedEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfPCISlotLinkSpeedInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotLinkSpeedEntry.setStatus("current")
_CfprBiosVfPCISlotLinkSpeedInstanceId_Type = CfprManagedObjectId
_CfprBiosVfPCISlotLinkSpeedInstanceId_Object = MibTableColumn
cfprBiosVfPCISlotLinkSpeedInstanceId = _CfprBiosVfPCISlotLinkSpeedInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 49, 1, 1),
    _CfprBiosVfPCISlotLinkSpeedInstanceId_Type()
)
cfprBiosVfPCISlotLinkSpeedInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotLinkSpeedInstanceId.setStatus("current")
_CfprBiosVfPCISlotLinkSpeedDn_Type = CfprManagedObjectDn
_CfprBiosVfPCISlotLinkSpeedDn_Object = MibTableColumn
cfprBiosVfPCISlotLinkSpeedDn = _CfprBiosVfPCISlotLinkSpeedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 49, 1, 2),
    _CfprBiosVfPCISlotLinkSpeedDn_Type()
)
cfprBiosVfPCISlotLinkSpeedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotLinkSpeedDn.setStatus("current")
_CfprBiosVfPCISlotLinkSpeedRn_Type = SnmpAdminString
_CfprBiosVfPCISlotLinkSpeedRn_Object = MibTableColumn
cfprBiosVfPCISlotLinkSpeedRn = _CfprBiosVfPCISlotLinkSpeedRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 49, 1, 3),
    _CfprBiosVfPCISlotLinkSpeedRn_Type()
)
cfprBiosVfPCISlotLinkSpeedRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotLinkSpeedRn.setStatus("current")
_CfprBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed_Type = CfprBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed
_CfprBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed_Object = MibTableColumn
cfprBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed = _CfprBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 49, 1, 4),
    _CfprBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed_Type()
)
cfprBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed.setStatus("current")
_CfprBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed_Type = CfprBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed
_CfprBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed_Object = MibTableColumn
cfprBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed = _CfprBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 49, 1, 5),
    _CfprBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed_Type()
)
cfprBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed.setStatus("current")
_CfprBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed_Type = CfprBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed
_CfprBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed_Object = MibTableColumn
cfprBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed = _CfprBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 49, 1, 6),
    _CfprBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed_Type()
)
cfprBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed.setStatus("current")
_CfprBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed_Type = CfprBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed
_CfprBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed_Object = MibTableColumn
cfprBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed = _CfprBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 49, 1, 7),
    _CfprBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed_Type()
)
cfprBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed.setStatus("current")
_CfprBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed_Type = CfprBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed
_CfprBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed_Object = MibTableColumn
cfprBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed = _CfprBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 49, 1, 8),
    _CfprBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed_Type()
)
cfprBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed.setStatus("current")
_CfprBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed_Type = CfprBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed
_CfprBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed_Object = MibTableColumn
cfprBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed = _CfprBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 49, 1, 9),
    _CfprBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed_Type()
)
cfprBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed.setStatus("current")
_CfprBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed_Type = CfprBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed
_CfprBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed_Object = MibTableColumn
cfprBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed = _CfprBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 49, 1, 10),
    _CfprBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed_Type()
)
cfprBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed.setStatus("current")
_CfprBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed_Type = CfprBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed
_CfprBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed_Object = MibTableColumn
cfprBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed = _CfprBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 49, 1, 11),
    _CfprBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed_Type()
)
cfprBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed.setStatus("current")
_CfprBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed_Type = CfprBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed
_CfprBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed_Object = MibTableColumn
cfprBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed = _CfprBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 49, 1, 12),
    _CfprBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed_Type()
)
cfprBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed.setStatus("current")
_CfprBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed_Type = CfprBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed
_CfprBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed_Object = MibTableColumn
cfprBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed = _CfprBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 49, 1, 13),
    _CfprBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed_Type()
)
cfprBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed.setStatus("current")
_CfprBiosVfPCISlotLinkSpeedSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfPCISlotLinkSpeedSupportedByDefault_Object = MibTableColumn
cfprBiosVfPCISlotLinkSpeedSupportedByDefault = _CfprBiosVfPCISlotLinkSpeedSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 49, 1, 14),
    _CfprBiosVfPCISlotLinkSpeedSupportedByDefault_Type()
)
cfprBiosVfPCISlotLinkSpeedSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotLinkSpeedSupportedByDefault.setStatus("current")
_CfprBiosVfPCISlotOptionROMEnableTable_Object = MibTable
cfprBiosVfPCISlotOptionROMEnableTable = _CfprBiosVfPCISlotOptionROMEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 50)
)
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotOptionROMEnableTable.setStatus("current")
_CfprBiosVfPCISlotOptionROMEnableEntry_Object = MibTableRow
cfprBiosVfPCISlotOptionROMEnableEntry = _CfprBiosVfPCISlotOptionROMEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 50, 1)
)
cfprBiosVfPCISlotOptionROMEnableEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfPCISlotOptionROMEnableInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotOptionROMEnableEntry.setStatus("current")
_CfprBiosVfPCISlotOptionROMEnableInstanceId_Type = CfprManagedObjectId
_CfprBiosVfPCISlotOptionROMEnableInstanceId_Object = MibTableColumn
cfprBiosVfPCISlotOptionROMEnableInstanceId = _CfprBiosVfPCISlotOptionROMEnableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 50, 1, 1),
    _CfprBiosVfPCISlotOptionROMEnableInstanceId_Type()
)
cfprBiosVfPCISlotOptionROMEnableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotOptionROMEnableInstanceId.setStatus("current")
_CfprBiosVfPCISlotOptionROMEnableDn_Type = CfprManagedObjectDn
_CfprBiosVfPCISlotOptionROMEnableDn_Object = MibTableColumn
cfprBiosVfPCISlotOptionROMEnableDn = _CfprBiosVfPCISlotOptionROMEnableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 50, 1, 2),
    _CfprBiosVfPCISlotOptionROMEnableDn_Type()
)
cfprBiosVfPCISlotOptionROMEnableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotOptionROMEnableDn.setStatus("current")
_CfprBiosVfPCISlotOptionROMEnableRn_Type = SnmpAdminString
_CfprBiosVfPCISlotOptionROMEnableRn_Object = MibTableColumn
cfprBiosVfPCISlotOptionROMEnableRn = _CfprBiosVfPCISlotOptionROMEnableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 50, 1, 3),
    _CfprBiosVfPCISlotOptionROMEnableRn_Type()
)
cfprBiosVfPCISlotOptionROMEnableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotOptionROMEnableRn.setStatus("current")
_CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM_Type = CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM
_CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM_Object = MibTableColumn
cfprBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM = _CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 50, 1, 4),
    _CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM_Type()
)
cfprBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM.setStatus("current")
_CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM_Type = CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM
_CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM_Object = MibTableColumn
cfprBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM = _CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 50, 1, 5),
    _CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM_Type()
)
cfprBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM.setStatus("current")
_CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM_Type = CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM
_CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM_Object = MibTableColumn
cfprBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM = _CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 50, 1, 6),
    _CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM_Type()
)
cfprBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM.setStatus("current")
_CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM_Type = CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM
_CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM_Object = MibTableColumn
cfprBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM = _CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 50, 1, 7),
    _CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM_Type()
)
cfprBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM.setStatus("current")
_CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM_Type = CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM
_CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM_Object = MibTableColumn
cfprBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM = _CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 50, 1, 8),
    _CfprBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM_Type()
)
cfprBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM.setStatus("current")
_CfprBiosVfPCISlotOptionROMEnableVpSlot10State_Type = CfprBiosVfPCISlotOptionROMEnableVpSlot10State
_CfprBiosVfPCISlotOptionROMEnableVpSlot10State_Object = MibTableColumn
cfprBiosVfPCISlotOptionROMEnableVpSlot10State = _CfprBiosVfPCISlotOptionROMEnableVpSlot10State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 50, 1, 9),
    _CfprBiosVfPCISlotOptionROMEnableVpSlot10State_Type()
)
cfprBiosVfPCISlotOptionROMEnableVpSlot10State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotOptionROMEnableVpSlot10State.setStatus("current")
_CfprBiosVfPCISlotOptionROMEnableVpSlot1State_Type = CfprBiosVfPCISlotOptionROMEnableVpSlot1State
_CfprBiosVfPCISlotOptionROMEnableVpSlot1State_Object = MibTableColumn
cfprBiosVfPCISlotOptionROMEnableVpSlot1State = _CfprBiosVfPCISlotOptionROMEnableVpSlot1State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 50, 1, 10),
    _CfprBiosVfPCISlotOptionROMEnableVpSlot1State_Type()
)
cfprBiosVfPCISlotOptionROMEnableVpSlot1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotOptionROMEnableVpSlot1State.setStatus("current")
_CfprBiosVfPCISlotOptionROMEnableVpSlot2State_Type = CfprBiosVfPCISlotOptionROMEnableVpSlot2State
_CfprBiosVfPCISlotOptionROMEnableVpSlot2State_Object = MibTableColumn
cfprBiosVfPCISlotOptionROMEnableVpSlot2State = _CfprBiosVfPCISlotOptionROMEnableVpSlot2State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 50, 1, 11),
    _CfprBiosVfPCISlotOptionROMEnableVpSlot2State_Type()
)
cfprBiosVfPCISlotOptionROMEnableVpSlot2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotOptionROMEnableVpSlot2State.setStatus("current")
_CfprBiosVfPCISlotOptionROMEnableVpSlot3State_Type = CfprBiosVfPCISlotOptionROMEnableVpSlot3State
_CfprBiosVfPCISlotOptionROMEnableVpSlot3State_Object = MibTableColumn
cfprBiosVfPCISlotOptionROMEnableVpSlot3State = _CfprBiosVfPCISlotOptionROMEnableVpSlot3State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 50, 1, 12),
    _CfprBiosVfPCISlotOptionROMEnableVpSlot3State_Type()
)
cfprBiosVfPCISlotOptionROMEnableVpSlot3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotOptionROMEnableVpSlot3State.setStatus("current")
_CfprBiosVfPCISlotOptionROMEnableVpSlot4State_Type = CfprBiosVfPCISlotOptionROMEnableVpSlot4State
_CfprBiosVfPCISlotOptionROMEnableVpSlot4State_Object = MibTableColumn
cfprBiosVfPCISlotOptionROMEnableVpSlot4State = _CfprBiosVfPCISlotOptionROMEnableVpSlot4State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 50, 1, 13),
    _CfprBiosVfPCISlotOptionROMEnableVpSlot4State_Type()
)
cfprBiosVfPCISlotOptionROMEnableVpSlot4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotOptionROMEnableVpSlot4State.setStatus("current")
_CfprBiosVfPCISlotOptionROMEnableVpSlot5State_Type = CfprBiosVfPCISlotOptionROMEnableVpSlot5State
_CfprBiosVfPCISlotOptionROMEnableVpSlot5State_Object = MibTableColumn
cfprBiosVfPCISlotOptionROMEnableVpSlot5State = _CfprBiosVfPCISlotOptionROMEnableVpSlot5State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 50, 1, 14),
    _CfprBiosVfPCISlotOptionROMEnableVpSlot5State_Type()
)
cfprBiosVfPCISlotOptionROMEnableVpSlot5State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotOptionROMEnableVpSlot5State.setStatus("current")
_CfprBiosVfPCISlotOptionROMEnableVpSlot6State_Type = CfprBiosVfPCISlotOptionROMEnableVpSlot6State
_CfprBiosVfPCISlotOptionROMEnableVpSlot6State_Object = MibTableColumn
cfprBiosVfPCISlotOptionROMEnableVpSlot6State = _CfprBiosVfPCISlotOptionROMEnableVpSlot6State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 50, 1, 15),
    _CfprBiosVfPCISlotOptionROMEnableVpSlot6State_Type()
)
cfprBiosVfPCISlotOptionROMEnableVpSlot6State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotOptionROMEnableVpSlot6State.setStatus("current")
_CfprBiosVfPCISlotOptionROMEnableVpSlot7State_Type = CfprBiosVfPCISlotOptionROMEnableVpSlot7State
_CfprBiosVfPCISlotOptionROMEnableVpSlot7State_Object = MibTableColumn
cfprBiosVfPCISlotOptionROMEnableVpSlot7State = _CfprBiosVfPCISlotOptionROMEnableVpSlot7State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 50, 1, 16),
    _CfprBiosVfPCISlotOptionROMEnableVpSlot7State_Type()
)
cfprBiosVfPCISlotOptionROMEnableVpSlot7State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotOptionROMEnableVpSlot7State.setStatus("current")
_CfprBiosVfPCISlotOptionROMEnableVpSlot8State_Type = CfprBiosVfPCISlotOptionROMEnableVpSlot8State
_CfprBiosVfPCISlotOptionROMEnableVpSlot8State_Object = MibTableColumn
cfprBiosVfPCISlotOptionROMEnableVpSlot8State = _CfprBiosVfPCISlotOptionROMEnableVpSlot8State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 50, 1, 17),
    _CfprBiosVfPCISlotOptionROMEnableVpSlot8State_Type()
)
cfprBiosVfPCISlotOptionROMEnableVpSlot8State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotOptionROMEnableVpSlot8State.setStatus("current")
_CfprBiosVfPCISlotOptionROMEnableVpSlot9State_Type = CfprBiosVfPCISlotOptionROMEnableVpSlot9State
_CfprBiosVfPCISlotOptionROMEnableVpSlot9State_Object = MibTableColumn
cfprBiosVfPCISlotOptionROMEnableVpSlot9State = _CfprBiosVfPCISlotOptionROMEnableVpSlot9State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 50, 1, 18),
    _CfprBiosVfPCISlotOptionROMEnableVpSlot9State_Type()
)
cfprBiosVfPCISlotOptionROMEnableVpSlot9State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotOptionROMEnableVpSlot9State.setStatus("current")
_CfprBiosVfPCISlotOptionROMEnableVpSlotMezzState_Type = CfprBiosVfPCISlotOptionROMEnableVpSlotMezzState
_CfprBiosVfPCISlotOptionROMEnableVpSlotMezzState_Object = MibTableColumn
cfprBiosVfPCISlotOptionROMEnableVpSlotMezzState = _CfprBiosVfPCISlotOptionROMEnableVpSlotMezzState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 50, 1, 19),
    _CfprBiosVfPCISlotOptionROMEnableVpSlotMezzState_Type()
)
cfprBiosVfPCISlotOptionROMEnableVpSlotMezzState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotOptionROMEnableVpSlotMezzState.setStatus("current")
_CfprBiosVfPCISlotOptionROMEnableSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfPCISlotOptionROMEnableSupportedByDefault_Object = MibTableColumn
cfprBiosVfPCISlotOptionROMEnableSupportedByDefault = _CfprBiosVfPCISlotOptionROMEnableSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 50, 1, 20),
    _CfprBiosVfPCISlotOptionROMEnableSupportedByDefault_Type()
)
cfprBiosVfPCISlotOptionROMEnableSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPCISlotOptionROMEnableSupportedByDefault.setStatus("current")
_CfprBiosVfPOSTErrorPauseTable_Object = MibTable
cfprBiosVfPOSTErrorPauseTable = _CfprBiosVfPOSTErrorPauseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 51)
)
if mibBuilder.loadTexts:
    cfprBiosVfPOSTErrorPauseTable.setStatus("current")
_CfprBiosVfPOSTErrorPauseEntry_Object = MibTableRow
cfprBiosVfPOSTErrorPauseEntry = _CfprBiosVfPOSTErrorPauseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 51, 1)
)
cfprBiosVfPOSTErrorPauseEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfPOSTErrorPauseInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfPOSTErrorPauseEntry.setStatus("current")
_CfprBiosVfPOSTErrorPauseInstanceId_Type = CfprManagedObjectId
_CfprBiosVfPOSTErrorPauseInstanceId_Object = MibTableColumn
cfprBiosVfPOSTErrorPauseInstanceId = _CfprBiosVfPOSTErrorPauseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 51, 1, 1),
    _CfprBiosVfPOSTErrorPauseInstanceId_Type()
)
cfprBiosVfPOSTErrorPauseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfPOSTErrorPauseInstanceId.setStatus("current")
_CfprBiosVfPOSTErrorPauseDn_Type = CfprManagedObjectDn
_CfprBiosVfPOSTErrorPauseDn_Object = MibTableColumn
cfprBiosVfPOSTErrorPauseDn = _CfprBiosVfPOSTErrorPauseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 51, 1, 2),
    _CfprBiosVfPOSTErrorPauseDn_Type()
)
cfprBiosVfPOSTErrorPauseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPOSTErrorPauseDn.setStatus("current")
_CfprBiosVfPOSTErrorPauseRn_Type = SnmpAdminString
_CfprBiosVfPOSTErrorPauseRn_Object = MibTableColumn
cfprBiosVfPOSTErrorPauseRn = _CfprBiosVfPOSTErrorPauseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 51, 1, 3),
    _CfprBiosVfPOSTErrorPauseRn_Type()
)
cfprBiosVfPOSTErrorPauseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPOSTErrorPauseRn.setStatus("current")
_CfprBiosVfPOSTErrorPauseVpPOSTErrorPause_Type = CfprBiosVfPOSTErrorPauseVpPOSTErrorPause
_CfprBiosVfPOSTErrorPauseVpPOSTErrorPause_Object = MibTableColumn
cfprBiosVfPOSTErrorPauseVpPOSTErrorPause = _CfprBiosVfPOSTErrorPauseVpPOSTErrorPause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 51, 1, 4),
    _CfprBiosVfPOSTErrorPauseVpPOSTErrorPause_Type()
)
cfprBiosVfPOSTErrorPauseVpPOSTErrorPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPOSTErrorPauseVpPOSTErrorPause.setStatus("current")
_CfprBiosVfPOSTErrorPauseSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfPOSTErrorPauseSupportedByDefault_Object = MibTableColumn
cfprBiosVfPOSTErrorPauseSupportedByDefault = _CfprBiosVfPOSTErrorPauseSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 51, 1, 5),
    _CfprBiosVfPOSTErrorPauseSupportedByDefault_Type()
)
cfprBiosVfPOSTErrorPauseSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPOSTErrorPauseSupportedByDefault.setStatus("current")
_CfprBiosVfPSTATECoordinationTable_Object = MibTable
cfprBiosVfPSTATECoordinationTable = _CfprBiosVfPSTATECoordinationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 52)
)
if mibBuilder.loadTexts:
    cfprBiosVfPSTATECoordinationTable.setStatus("current")
_CfprBiosVfPSTATECoordinationEntry_Object = MibTableRow
cfprBiosVfPSTATECoordinationEntry = _CfprBiosVfPSTATECoordinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 52, 1)
)
cfprBiosVfPSTATECoordinationEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfPSTATECoordinationInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfPSTATECoordinationEntry.setStatus("current")
_CfprBiosVfPSTATECoordinationInstanceId_Type = CfprManagedObjectId
_CfprBiosVfPSTATECoordinationInstanceId_Object = MibTableColumn
cfprBiosVfPSTATECoordinationInstanceId = _CfprBiosVfPSTATECoordinationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 52, 1, 1),
    _CfprBiosVfPSTATECoordinationInstanceId_Type()
)
cfprBiosVfPSTATECoordinationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfPSTATECoordinationInstanceId.setStatus("current")
_CfprBiosVfPSTATECoordinationDn_Type = CfprManagedObjectDn
_CfprBiosVfPSTATECoordinationDn_Object = MibTableColumn
cfprBiosVfPSTATECoordinationDn = _CfprBiosVfPSTATECoordinationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 52, 1, 2),
    _CfprBiosVfPSTATECoordinationDn_Type()
)
cfprBiosVfPSTATECoordinationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPSTATECoordinationDn.setStatus("current")
_CfprBiosVfPSTATECoordinationRn_Type = SnmpAdminString
_CfprBiosVfPSTATECoordinationRn_Object = MibTableColumn
cfprBiosVfPSTATECoordinationRn = _CfprBiosVfPSTATECoordinationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 52, 1, 3),
    _CfprBiosVfPSTATECoordinationRn_Type()
)
cfprBiosVfPSTATECoordinationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPSTATECoordinationRn.setStatus("current")
_CfprBiosVfPSTATECoordinationVpPSTATECoordination_Type = CfprBiosVfPSTATECoordinationVpPSTATECoordination
_CfprBiosVfPSTATECoordinationVpPSTATECoordination_Object = MibTableColumn
cfprBiosVfPSTATECoordinationVpPSTATECoordination = _CfprBiosVfPSTATECoordinationVpPSTATECoordination_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 52, 1, 4),
    _CfprBiosVfPSTATECoordinationVpPSTATECoordination_Type()
)
cfprBiosVfPSTATECoordinationVpPSTATECoordination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPSTATECoordinationVpPSTATECoordination.setStatus("current")
_CfprBiosVfPSTATECoordinationSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfPSTATECoordinationSupportedByDefault_Object = MibTableColumn
cfprBiosVfPSTATECoordinationSupportedByDefault = _CfprBiosVfPSTATECoordinationSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 52, 1, 5),
    _CfprBiosVfPSTATECoordinationSupportedByDefault_Type()
)
cfprBiosVfPSTATECoordinationSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPSTATECoordinationSupportedByDefault.setStatus("current")
_CfprBiosVfPackageCStateLimitTable_Object = MibTable
cfprBiosVfPackageCStateLimitTable = _CfprBiosVfPackageCStateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 53)
)
if mibBuilder.loadTexts:
    cfprBiosVfPackageCStateLimitTable.setStatus("current")
_CfprBiosVfPackageCStateLimitEntry_Object = MibTableRow
cfprBiosVfPackageCStateLimitEntry = _CfprBiosVfPackageCStateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 53, 1)
)
cfprBiosVfPackageCStateLimitEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfPackageCStateLimitInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfPackageCStateLimitEntry.setStatus("current")
_CfprBiosVfPackageCStateLimitInstanceId_Type = CfprManagedObjectId
_CfprBiosVfPackageCStateLimitInstanceId_Object = MibTableColumn
cfprBiosVfPackageCStateLimitInstanceId = _CfprBiosVfPackageCStateLimitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 53, 1, 1),
    _CfprBiosVfPackageCStateLimitInstanceId_Type()
)
cfprBiosVfPackageCStateLimitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfPackageCStateLimitInstanceId.setStatus("current")
_CfprBiosVfPackageCStateLimitDn_Type = CfprManagedObjectDn
_CfprBiosVfPackageCStateLimitDn_Object = MibTableColumn
cfprBiosVfPackageCStateLimitDn = _CfprBiosVfPackageCStateLimitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 53, 1, 2),
    _CfprBiosVfPackageCStateLimitDn_Type()
)
cfprBiosVfPackageCStateLimitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPackageCStateLimitDn.setStatus("current")
_CfprBiosVfPackageCStateLimitRn_Type = SnmpAdminString
_CfprBiosVfPackageCStateLimitRn_Object = MibTableColumn
cfprBiosVfPackageCStateLimitRn = _CfprBiosVfPackageCStateLimitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 53, 1, 3),
    _CfprBiosVfPackageCStateLimitRn_Type()
)
cfprBiosVfPackageCStateLimitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPackageCStateLimitRn.setStatus("current")
_CfprBiosVfPackageCStateLimitVpPackageCStateLimit_Type = CfprBiosVfPackageCStateLimitVpPackageCStateLimit
_CfprBiosVfPackageCStateLimitVpPackageCStateLimit_Object = MibTableColumn
cfprBiosVfPackageCStateLimitVpPackageCStateLimit = _CfprBiosVfPackageCStateLimitVpPackageCStateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 53, 1, 4),
    _CfprBiosVfPackageCStateLimitVpPackageCStateLimit_Type()
)
cfprBiosVfPackageCStateLimitVpPackageCStateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPackageCStateLimitVpPackageCStateLimit.setStatus("current")
_CfprBiosVfPackageCStateLimitSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfPackageCStateLimitSupportedByDefault_Object = MibTableColumn
cfprBiosVfPackageCStateLimitSupportedByDefault = _CfprBiosVfPackageCStateLimitSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 53, 1, 5),
    _CfprBiosVfPackageCStateLimitSupportedByDefault_Type()
)
cfprBiosVfPackageCStateLimitSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfPackageCStateLimitSupportedByDefault.setStatus("current")
_CfprBiosVfProcessorC1ETable_Object = MibTable
cfprBiosVfProcessorC1ETable = _CfprBiosVfProcessorC1ETable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 54)
)
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC1ETable.setStatus("current")
_CfprBiosVfProcessorC1EEntry_Object = MibTableRow
cfprBiosVfProcessorC1EEntry = _CfprBiosVfProcessorC1EEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 54, 1)
)
cfprBiosVfProcessorC1EEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfProcessorC1EInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC1EEntry.setStatus("current")
_CfprBiosVfProcessorC1EInstanceId_Type = CfprManagedObjectId
_CfprBiosVfProcessorC1EInstanceId_Object = MibTableColumn
cfprBiosVfProcessorC1EInstanceId = _CfprBiosVfProcessorC1EInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 54, 1, 1),
    _CfprBiosVfProcessorC1EInstanceId_Type()
)
cfprBiosVfProcessorC1EInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC1EInstanceId.setStatus("current")
_CfprBiosVfProcessorC1EDn_Type = CfprManagedObjectDn
_CfprBiosVfProcessorC1EDn_Object = MibTableColumn
cfprBiosVfProcessorC1EDn = _CfprBiosVfProcessorC1EDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 54, 1, 2),
    _CfprBiosVfProcessorC1EDn_Type()
)
cfprBiosVfProcessorC1EDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC1EDn.setStatus("current")
_CfprBiosVfProcessorC1ERn_Type = SnmpAdminString
_CfprBiosVfProcessorC1ERn_Object = MibTableColumn
cfprBiosVfProcessorC1ERn = _CfprBiosVfProcessorC1ERn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 54, 1, 3),
    _CfprBiosVfProcessorC1ERn_Type()
)
cfprBiosVfProcessorC1ERn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC1ERn.setStatus("current")
_CfprBiosVfProcessorC1EVpProcessorC1E_Type = CfprBiosVfProcessorC1EVpProcessorC1E
_CfprBiosVfProcessorC1EVpProcessorC1E_Object = MibTableColumn
cfprBiosVfProcessorC1EVpProcessorC1E = _CfprBiosVfProcessorC1EVpProcessorC1E_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 54, 1, 4),
    _CfprBiosVfProcessorC1EVpProcessorC1E_Type()
)
cfprBiosVfProcessorC1EVpProcessorC1E.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC1EVpProcessorC1E.setStatus("current")
_CfprBiosVfProcessorC1ESupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfProcessorC1ESupportedByDefault_Object = MibTableColumn
cfprBiosVfProcessorC1ESupportedByDefault = _CfprBiosVfProcessorC1ESupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 54, 1, 5),
    _CfprBiosVfProcessorC1ESupportedByDefault_Type()
)
cfprBiosVfProcessorC1ESupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC1ESupportedByDefault.setStatus("current")
_CfprBiosVfProcessorC3ReportTable_Object = MibTable
cfprBiosVfProcessorC3ReportTable = _CfprBiosVfProcessorC3ReportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 55)
)
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC3ReportTable.setStatus("current")
_CfprBiosVfProcessorC3ReportEntry_Object = MibTableRow
cfprBiosVfProcessorC3ReportEntry = _CfprBiosVfProcessorC3ReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 55, 1)
)
cfprBiosVfProcessorC3ReportEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfProcessorC3ReportInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC3ReportEntry.setStatus("current")
_CfprBiosVfProcessorC3ReportInstanceId_Type = CfprManagedObjectId
_CfprBiosVfProcessorC3ReportInstanceId_Object = MibTableColumn
cfprBiosVfProcessorC3ReportInstanceId = _CfprBiosVfProcessorC3ReportInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 55, 1, 1),
    _CfprBiosVfProcessorC3ReportInstanceId_Type()
)
cfprBiosVfProcessorC3ReportInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC3ReportInstanceId.setStatus("current")
_CfprBiosVfProcessorC3ReportDn_Type = CfprManagedObjectDn
_CfprBiosVfProcessorC3ReportDn_Object = MibTableColumn
cfprBiosVfProcessorC3ReportDn = _CfprBiosVfProcessorC3ReportDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 55, 1, 2),
    _CfprBiosVfProcessorC3ReportDn_Type()
)
cfprBiosVfProcessorC3ReportDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC3ReportDn.setStatus("current")
_CfprBiosVfProcessorC3ReportRn_Type = SnmpAdminString
_CfprBiosVfProcessorC3ReportRn_Object = MibTableColumn
cfprBiosVfProcessorC3ReportRn = _CfprBiosVfProcessorC3ReportRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 55, 1, 3),
    _CfprBiosVfProcessorC3ReportRn_Type()
)
cfprBiosVfProcessorC3ReportRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC3ReportRn.setStatus("current")
_CfprBiosVfProcessorC3ReportVpProcessorC3Report_Type = CfprBiosVfProcessorC3ReportVpProcessorC3Report
_CfprBiosVfProcessorC3ReportVpProcessorC3Report_Object = MibTableColumn
cfprBiosVfProcessorC3ReportVpProcessorC3Report = _CfprBiosVfProcessorC3ReportVpProcessorC3Report_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 55, 1, 4),
    _CfprBiosVfProcessorC3ReportVpProcessorC3Report_Type()
)
cfprBiosVfProcessorC3ReportVpProcessorC3Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC3ReportVpProcessorC3Report.setStatus("current")
_CfprBiosVfProcessorC3ReportSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfProcessorC3ReportSupportedByDefault_Object = MibTableColumn
cfprBiosVfProcessorC3ReportSupportedByDefault = _CfprBiosVfProcessorC3ReportSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 55, 1, 5),
    _CfprBiosVfProcessorC3ReportSupportedByDefault_Type()
)
cfprBiosVfProcessorC3ReportSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC3ReportSupportedByDefault.setStatus("current")
_CfprBiosVfProcessorC6ReportTable_Object = MibTable
cfprBiosVfProcessorC6ReportTable = _CfprBiosVfProcessorC6ReportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 56)
)
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC6ReportTable.setStatus("current")
_CfprBiosVfProcessorC6ReportEntry_Object = MibTableRow
cfprBiosVfProcessorC6ReportEntry = _CfprBiosVfProcessorC6ReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 56, 1)
)
cfprBiosVfProcessorC6ReportEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfProcessorC6ReportInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC6ReportEntry.setStatus("current")
_CfprBiosVfProcessorC6ReportInstanceId_Type = CfprManagedObjectId
_CfprBiosVfProcessorC6ReportInstanceId_Object = MibTableColumn
cfprBiosVfProcessorC6ReportInstanceId = _CfprBiosVfProcessorC6ReportInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 56, 1, 1),
    _CfprBiosVfProcessorC6ReportInstanceId_Type()
)
cfprBiosVfProcessorC6ReportInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC6ReportInstanceId.setStatus("current")
_CfprBiosVfProcessorC6ReportDn_Type = CfprManagedObjectDn
_CfprBiosVfProcessorC6ReportDn_Object = MibTableColumn
cfprBiosVfProcessorC6ReportDn = _CfprBiosVfProcessorC6ReportDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 56, 1, 2),
    _CfprBiosVfProcessorC6ReportDn_Type()
)
cfprBiosVfProcessorC6ReportDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC6ReportDn.setStatus("current")
_CfprBiosVfProcessorC6ReportRn_Type = SnmpAdminString
_CfprBiosVfProcessorC6ReportRn_Object = MibTableColumn
cfprBiosVfProcessorC6ReportRn = _CfprBiosVfProcessorC6ReportRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 56, 1, 3),
    _CfprBiosVfProcessorC6ReportRn_Type()
)
cfprBiosVfProcessorC6ReportRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC6ReportRn.setStatus("current")
_CfprBiosVfProcessorC6ReportVpProcessorC6Report_Type = CfprBiosVfProcessorC6ReportVpProcessorC6Report
_CfprBiosVfProcessorC6ReportVpProcessorC6Report_Object = MibTableColumn
cfprBiosVfProcessorC6ReportVpProcessorC6Report = _CfprBiosVfProcessorC6ReportVpProcessorC6Report_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 56, 1, 4),
    _CfprBiosVfProcessorC6ReportVpProcessorC6Report_Type()
)
cfprBiosVfProcessorC6ReportVpProcessorC6Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC6ReportVpProcessorC6Report.setStatus("current")
_CfprBiosVfProcessorC6ReportSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfProcessorC6ReportSupportedByDefault_Object = MibTableColumn
cfprBiosVfProcessorC6ReportSupportedByDefault = _CfprBiosVfProcessorC6ReportSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 56, 1, 5),
    _CfprBiosVfProcessorC6ReportSupportedByDefault_Type()
)
cfprBiosVfProcessorC6ReportSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC6ReportSupportedByDefault.setStatus("current")
_CfprBiosVfProcessorC7ReportTable_Object = MibTable
cfprBiosVfProcessorC7ReportTable = _CfprBiosVfProcessorC7ReportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 57)
)
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC7ReportTable.setStatus("current")
_CfprBiosVfProcessorC7ReportEntry_Object = MibTableRow
cfprBiosVfProcessorC7ReportEntry = _CfprBiosVfProcessorC7ReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 57, 1)
)
cfprBiosVfProcessorC7ReportEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfProcessorC7ReportInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC7ReportEntry.setStatus("current")
_CfprBiosVfProcessorC7ReportInstanceId_Type = CfprManagedObjectId
_CfprBiosVfProcessorC7ReportInstanceId_Object = MibTableColumn
cfprBiosVfProcessorC7ReportInstanceId = _CfprBiosVfProcessorC7ReportInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 57, 1, 1),
    _CfprBiosVfProcessorC7ReportInstanceId_Type()
)
cfprBiosVfProcessorC7ReportInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC7ReportInstanceId.setStatus("current")
_CfprBiosVfProcessorC7ReportDn_Type = CfprManagedObjectDn
_CfprBiosVfProcessorC7ReportDn_Object = MibTableColumn
cfprBiosVfProcessorC7ReportDn = _CfprBiosVfProcessorC7ReportDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 57, 1, 2),
    _CfprBiosVfProcessorC7ReportDn_Type()
)
cfprBiosVfProcessorC7ReportDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC7ReportDn.setStatus("current")
_CfprBiosVfProcessorC7ReportRn_Type = SnmpAdminString
_CfprBiosVfProcessorC7ReportRn_Object = MibTableColumn
cfprBiosVfProcessorC7ReportRn = _CfprBiosVfProcessorC7ReportRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 57, 1, 3),
    _CfprBiosVfProcessorC7ReportRn_Type()
)
cfprBiosVfProcessorC7ReportRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC7ReportRn.setStatus("current")
_CfprBiosVfProcessorC7ReportVpProcessorC7Report_Type = CfprBiosVfProcessorC7ReportVpProcessorC7Report
_CfprBiosVfProcessorC7ReportVpProcessorC7Report_Object = MibTableColumn
cfprBiosVfProcessorC7ReportVpProcessorC7Report = _CfprBiosVfProcessorC7ReportVpProcessorC7Report_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 57, 1, 4),
    _CfprBiosVfProcessorC7ReportVpProcessorC7Report_Type()
)
cfprBiosVfProcessorC7ReportVpProcessorC7Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC7ReportVpProcessorC7Report.setStatus("current")
_CfprBiosVfProcessorC7ReportSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfProcessorC7ReportSupportedByDefault_Object = MibTableColumn
cfprBiosVfProcessorC7ReportSupportedByDefault = _CfprBiosVfProcessorC7ReportSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 57, 1, 5),
    _CfprBiosVfProcessorC7ReportSupportedByDefault_Type()
)
cfprBiosVfProcessorC7ReportSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorC7ReportSupportedByDefault.setStatus("current")
_CfprBiosVfProcessorCStateTable_Object = MibTable
cfprBiosVfProcessorCStateTable = _CfprBiosVfProcessorCStateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 58)
)
if mibBuilder.loadTexts:
    cfprBiosVfProcessorCStateTable.setStatus("current")
_CfprBiosVfProcessorCStateEntry_Object = MibTableRow
cfprBiosVfProcessorCStateEntry = _CfprBiosVfProcessorCStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 58, 1)
)
cfprBiosVfProcessorCStateEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfProcessorCStateInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfProcessorCStateEntry.setStatus("current")
_CfprBiosVfProcessorCStateInstanceId_Type = CfprManagedObjectId
_CfprBiosVfProcessorCStateInstanceId_Object = MibTableColumn
cfprBiosVfProcessorCStateInstanceId = _CfprBiosVfProcessorCStateInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 58, 1, 1),
    _CfprBiosVfProcessorCStateInstanceId_Type()
)
cfprBiosVfProcessorCStateInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorCStateInstanceId.setStatus("current")
_CfprBiosVfProcessorCStateDn_Type = CfprManagedObjectDn
_CfprBiosVfProcessorCStateDn_Object = MibTableColumn
cfprBiosVfProcessorCStateDn = _CfprBiosVfProcessorCStateDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 58, 1, 2),
    _CfprBiosVfProcessorCStateDn_Type()
)
cfprBiosVfProcessorCStateDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorCStateDn.setStatus("current")
_CfprBiosVfProcessorCStateRn_Type = SnmpAdminString
_CfprBiosVfProcessorCStateRn_Object = MibTableColumn
cfprBiosVfProcessorCStateRn = _CfprBiosVfProcessorCStateRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 58, 1, 3),
    _CfprBiosVfProcessorCStateRn_Type()
)
cfprBiosVfProcessorCStateRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorCStateRn.setStatus("current")
_CfprBiosVfProcessorCStateVpProcessorCState_Type = CfprBiosVfProcessorCStateVpProcessorCState
_CfprBiosVfProcessorCStateVpProcessorCState_Object = MibTableColumn
cfprBiosVfProcessorCStateVpProcessorCState = _CfprBiosVfProcessorCStateVpProcessorCState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 58, 1, 4),
    _CfprBiosVfProcessorCStateVpProcessorCState_Type()
)
cfprBiosVfProcessorCStateVpProcessorCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorCStateVpProcessorCState.setStatus("current")
_CfprBiosVfProcessorCStateSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfProcessorCStateSupportedByDefault_Object = MibTableColumn
cfprBiosVfProcessorCStateSupportedByDefault = _CfprBiosVfProcessorCStateSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 58, 1, 5),
    _CfprBiosVfProcessorCStateSupportedByDefault_Type()
)
cfprBiosVfProcessorCStateSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorCStateSupportedByDefault.setStatus("current")
_CfprBiosVfProcessorEnergyConfigurationTable_Object = MibTable
cfprBiosVfProcessorEnergyConfigurationTable = _CfprBiosVfProcessorEnergyConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 59)
)
if mibBuilder.loadTexts:
    cfprBiosVfProcessorEnergyConfigurationTable.setStatus("current")
_CfprBiosVfProcessorEnergyConfigurationEntry_Object = MibTableRow
cfprBiosVfProcessorEnergyConfigurationEntry = _CfprBiosVfProcessorEnergyConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 59, 1)
)
cfprBiosVfProcessorEnergyConfigurationEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfProcessorEnergyConfigurationInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfProcessorEnergyConfigurationEntry.setStatus("current")
_CfprBiosVfProcessorEnergyConfigurationInstanceId_Type = CfprManagedObjectId
_CfprBiosVfProcessorEnergyConfigurationInstanceId_Object = MibTableColumn
cfprBiosVfProcessorEnergyConfigurationInstanceId = _CfprBiosVfProcessorEnergyConfigurationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 59, 1, 1),
    _CfprBiosVfProcessorEnergyConfigurationInstanceId_Type()
)
cfprBiosVfProcessorEnergyConfigurationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorEnergyConfigurationInstanceId.setStatus("current")
_CfprBiosVfProcessorEnergyConfigurationDn_Type = CfprManagedObjectDn
_CfprBiosVfProcessorEnergyConfigurationDn_Object = MibTableColumn
cfprBiosVfProcessorEnergyConfigurationDn = _CfprBiosVfProcessorEnergyConfigurationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 59, 1, 2),
    _CfprBiosVfProcessorEnergyConfigurationDn_Type()
)
cfprBiosVfProcessorEnergyConfigurationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorEnergyConfigurationDn.setStatus("current")
_CfprBiosVfProcessorEnergyConfigurationRn_Type = SnmpAdminString
_CfprBiosVfProcessorEnergyConfigurationRn_Object = MibTableColumn
cfprBiosVfProcessorEnergyConfigurationRn = _CfprBiosVfProcessorEnergyConfigurationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 59, 1, 3),
    _CfprBiosVfProcessorEnergyConfigurationRn_Type()
)
cfprBiosVfProcessorEnergyConfigurationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorEnergyConfigurationRn.setStatus("current")
_CfprBiosVfProcessorEnergyConfigurationVpEnergyPerformance_Type = CfprBiosVfProcessorEnergyConfigurationVpEnergyPerformance
_CfprBiosVfProcessorEnergyConfigurationVpEnergyPerformance_Object = MibTableColumn
cfprBiosVfProcessorEnergyConfigurationVpEnergyPerformance = _CfprBiosVfProcessorEnergyConfigurationVpEnergyPerformance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 59, 1, 4),
    _CfprBiosVfProcessorEnergyConfigurationVpEnergyPerformance_Type()
)
cfprBiosVfProcessorEnergyConfigurationVpEnergyPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorEnergyConfigurationVpEnergyPerformance.setStatus("current")
_CfprBiosVfProcessorEnergyConfigurationVpPowerTechnology_Type = CfprBiosVfProcessorEnergyConfigurationVpPowerTechnology
_CfprBiosVfProcessorEnergyConfigurationVpPowerTechnology_Object = MibTableColumn
cfprBiosVfProcessorEnergyConfigurationVpPowerTechnology = _CfprBiosVfProcessorEnergyConfigurationVpPowerTechnology_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 59, 1, 5),
    _CfprBiosVfProcessorEnergyConfigurationVpPowerTechnology_Type()
)
cfprBiosVfProcessorEnergyConfigurationVpPowerTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorEnergyConfigurationVpPowerTechnology.setStatus("current")
_CfprBiosVfProcessorEnergyConfigurationSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfProcessorEnergyConfigurationSupportedByDefault_Object = MibTableColumn
cfprBiosVfProcessorEnergyConfigurationSupportedByDefault = _CfprBiosVfProcessorEnergyConfigurationSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 59, 1, 6),
    _CfprBiosVfProcessorEnergyConfigurationSupportedByDefault_Type()
)
cfprBiosVfProcessorEnergyConfigurationSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorEnergyConfigurationSupportedByDefault.setStatus("current")
_CfprBiosVfProcessorPrefetchConfigTable_Object = MibTable
cfprBiosVfProcessorPrefetchConfigTable = _CfprBiosVfProcessorPrefetchConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 60)
)
if mibBuilder.loadTexts:
    cfprBiosVfProcessorPrefetchConfigTable.setStatus("current")
_CfprBiosVfProcessorPrefetchConfigEntry_Object = MibTableRow
cfprBiosVfProcessorPrefetchConfigEntry = _CfprBiosVfProcessorPrefetchConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 60, 1)
)
cfprBiosVfProcessorPrefetchConfigEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfProcessorPrefetchConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfProcessorPrefetchConfigEntry.setStatus("current")
_CfprBiosVfProcessorPrefetchConfigInstanceId_Type = CfprManagedObjectId
_CfprBiosVfProcessorPrefetchConfigInstanceId_Object = MibTableColumn
cfprBiosVfProcessorPrefetchConfigInstanceId = _CfprBiosVfProcessorPrefetchConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 60, 1, 1),
    _CfprBiosVfProcessorPrefetchConfigInstanceId_Type()
)
cfprBiosVfProcessorPrefetchConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorPrefetchConfigInstanceId.setStatus("current")
_CfprBiosVfProcessorPrefetchConfigDn_Type = CfprManagedObjectDn
_CfprBiosVfProcessorPrefetchConfigDn_Object = MibTableColumn
cfprBiosVfProcessorPrefetchConfigDn = _CfprBiosVfProcessorPrefetchConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 60, 1, 2),
    _CfprBiosVfProcessorPrefetchConfigDn_Type()
)
cfprBiosVfProcessorPrefetchConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorPrefetchConfigDn.setStatus("current")
_CfprBiosVfProcessorPrefetchConfigRn_Type = SnmpAdminString
_CfprBiosVfProcessorPrefetchConfigRn_Object = MibTableColumn
cfprBiosVfProcessorPrefetchConfigRn = _CfprBiosVfProcessorPrefetchConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 60, 1, 3),
    _CfprBiosVfProcessorPrefetchConfigRn_Type()
)
cfprBiosVfProcessorPrefetchConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorPrefetchConfigRn.setStatus("current")
_CfprBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher_Type = CfprBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher
_CfprBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher_Object = MibTableColumn
cfprBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher = _CfprBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 60, 1, 4),
    _CfprBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher_Type()
)
cfprBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher.setStatus("current")
_CfprBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher_Type = CfprBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher
_CfprBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher_Object = MibTableColumn
cfprBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher = _CfprBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 60, 1, 5),
    _CfprBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher_Type()
)
cfprBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher.setStatus("current")
_CfprBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch_Type = CfprBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch
_CfprBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch_Object = MibTableColumn
cfprBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch = _CfprBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 60, 1, 6),
    _CfprBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch_Type()
)
cfprBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch.setStatus("current")
_CfprBiosVfProcessorPrefetchConfigVpHardwarePrefetcher_Type = CfprBiosVfProcessorPrefetchConfigVpHardwarePrefetcher
_CfprBiosVfProcessorPrefetchConfigVpHardwarePrefetcher_Object = MibTableColumn
cfprBiosVfProcessorPrefetchConfigVpHardwarePrefetcher = _CfprBiosVfProcessorPrefetchConfigVpHardwarePrefetcher_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 60, 1, 7),
    _CfprBiosVfProcessorPrefetchConfigVpHardwarePrefetcher_Type()
)
cfprBiosVfProcessorPrefetchConfigVpHardwarePrefetcher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorPrefetchConfigVpHardwarePrefetcher.setStatus("current")
_CfprBiosVfProcessorPrefetchConfigSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfProcessorPrefetchConfigSupportedByDefault_Object = MibTableColumn
cfprBiosVfProcessorPrefetchConfigSupportedByDefault = _CfprBiosVfProcessorPrefetchConfigSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 60, 1, 8),
    _CfprBiosVfProcessorPrefetchConfigSupportedByDefault_Type()
)
cfprBiosVfProcessorPrefetchConfigSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfProcessorPrefetchConfigSupportedByDefault.setStatus("current")
_CfprBiosVfQPILinkFrequencySelectTable_Object = MibTable
cfprBiosVfQPILinkFrequencySelectTable = _CfprBiosVfQPILinkFrequencySelectTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 61)
)
if mibBuilder.loadTexts:
    cfprBiosVfQPILinkFrequencySelectTable.setStatus("current")
_CfprBiosVfQPILinkFrequencySelectEntry_Object = MibTableRow
cfprBiosVfQPILinkFrequencySelectEntry = _CfprBiosVfQPILinkFrequencySelectEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 61, 1)
)
cfprBiosVfQPILinkFrequencySelectEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfQPILinkFrequencySelectInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfQPILinkFrequencySelectEntry.setStatus("current")
_CfprBiosVfQPILinkFrequencySelectInstanceId_Type = CfprManagedObjectId
_CfprBiosVfQPILinkFrequencySelectInstanceId_Object = MibTableColumn
cfprBiosVfQPILinkFrequencySelectInstanceId = _CfprBiosVfQPILinkFrequencySelectInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 61, 1, 1),
    _CfprBiosVfQPILinkFrequencySelectInstanceId_Type()
)
cfprBiosVfQPILinkFrequencySelectInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfQPILinkFrequencySelectInstanceId.setStatus("current")
_CfprBiosVfQPILinkFrequencySelectDn_Type = CfprManagedObjectDn
_CfprBiosVfQPILinkFrequencySelectDn_Object = MibTableColumn
cfprBiosVfQPILinkFrequencySelectDn = _CfprBiosVfQPILinkFrequencySelectDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 61, 1, 2),
    _CfprBiosVfQPILinkFrequencySelectDn_Type()
)
cfprBiosVfQPILinkFrequencySelectDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfQPILinkFrequencySelectDn.setStatus("current")
_CfprBiosVfQPILinkFrequencySelectRn_Type = SnmpAdminString
_CfprBiosVfQPILinkFrequencySelectRn_Object = MibTableColumn
cfprBiosVfQPILinkFrequencySelectRn = _CfprBiosVfQPILinkFrequencySelectRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 61, 1, 3),
    _CfprBiosVfQPILinkFrequencySelectRn_Type()
)
cfprBiosVfQPILinkFrequencySelectRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfQPILinkFrequencySelectRn.setStatus("current")
_CfprBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect_Type = CfprBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect
_CfprBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect_Object = MibTableColumn
cfprBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect = _CfprBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 61, 1, 4),
    _CfprBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect_Type()
)
cfprBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect.setStatus("current")
_CfprBiosVfQPILinkFrequencySelectSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfQPILinkFrequencySelectSupportedByDefault_Object = MibTableColumn
cfprBiosVfQPILinkFrequencySelectSupportedByDefault = _CfprBiosVfQPILinkFrequencySelectSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 61, 1, 5),
    _CfprBiosVfQPILinkFrequencySelectSupportedByDefault_Type()
)
cfprBiosVfQPILinkFrequencySelectSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfQPILinkFrequencySelectSupportedByDefault.setStatus("current")
_CfprBiosVfQuietBootTable_Object = MibTable
cfprBiosVfQuietBootTable = _CfprBiosVfQuietBootTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 62)
)
if mibBuilder.loadTexts:
    cfprBiosVfQuietBootTable.setStatus("current")
_CfprBiosVfQuietBootEntry_Object = MibTableRow
cfprBiosVfQuietBootEntry = _CfprBiosVfQuietBootEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 62, 1)
)
cfprBiosVfQuietBootEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfQuietBootInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfQuietBootEntry.setStatus("current")
_CfprBiosVfQuietBootInstanceId_Type = CfprManagedObjectId
_CfprBiosVfQuietBootInstanceId_Object = MibTableColumn
cfprBiosVfQuietBootInstanceId = _CfprBiosVfQuietBootInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 62, 1, 1),
    _CfprBiosVfQuietBootInstanceId_Type()
)
cfprBiosVfQuietBootInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfQuietBootInstanceId.setStatus("current")
_CfprBiosVfQuietBootDn_Type = CfprManagedObjectDn
_CfprBiosVfQuietBootDn_Object = MibTableColumn
cfprBiosVfQuietBootDn = _CfprBiosVfQuietBootDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 62, 1, 2),
    _CfprBiosVfQuietBootDn_Type()
)
cfprBiosVfQuietBootDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfQuietBootDn.setStatus("current")
_CfprBiosVfQuietBootRn_Type = SnmpAdminString
_CfprBiosVfQuietBootRn_Object = MibTableColumn
cfprBiosVfQuietBootRn = _CfprBiosVfQuietBootRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 62, 1, 3),
    _CfprBiosVfQuietBootRn_Type()
)
cfprBiosVfQuietBootRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfQuietBootRn.setStatus("current")
_CfprBiosVfQuietBootVpQuietBoot_Type = CfprBiosVfQuietBootVpQuietBoot
_CfprBiosVfQuietBootVpQuietBoot_Object = MibTableColumn
cfprBiosVfQuietBootVpQuietBoot = _CfprBiosVfQuietBootVpQuietBoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 62, 1, 4),
    _CfprBiosVfQuietBootVpQuietBoot_Type()
)
cfprBiosVfQuietBootVpQuietBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfQuietBootVpQuietBoot.setStatus("current")
_CfprBiosVfQuietBootSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfQuietBootSupportedByDefault_Object = MibTableColumn
cfprBiosVfQuietBootSupportedByDefault = _CfprBiosVfQuietBootSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 62, 1, 5),
    _CfprBiosVfQuietBootSupportedByDefault_Type()
)
cfprBiosVfQuietBootSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfQuietBootSupportedByDefault.setStatus("current")
_CfprBiosVfResumeOnACPowerLossTable_Object = MibTable
cfprBiosVfResumeOnACPowerLossTable = _CfprBiosVfResumeOnACPowerLossTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 63)
)
if mibBuilder.loadTexts:
    cfprBiosVfResumeOnACPowerLossTable.setStatus("current")
_CfprBiosVfResumeOnACPowerLossEntry_Object = MibTableRow
cfprBiosVfResumeOnACPowerLossEntry = _CfprBiosVfResumeOnACPowerLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 63, 1)
)
cfprBiosVfResumeOnACPowerLossEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfResumeOnACPowerLossInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfResumeOnACPowerLossEntry.setStatus("current")
_CfprBiosVfResumeOnACPowerLossInstanceId_Type = CfprManagedObjectId
_CfprBiosVfResumeOnACPowerLossInstanceId_Object = MibTableColumn
cfprBiosVfResumeOnACPowerLossInstanceId = _CfprBiosVfResumeOnACPowerLossInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 63, 1, 1),
    _CfprBiosVfResumeOnACPowerLossInstanceId_Type()
)
cfprBiosVfResumeOnACPowerLossInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfResumeOnACPowerLossInstanceId.setStatus("current")
_CfprBiosVfResumeOnACPowerLossDn_Type = CfprManagedObjectDn
_CfprBiosVfResumeOnACPowerLossDn_Object = MibTableColumn
cfprBiosVfResumeOnACPowerLossDn = _CfprBiosVfResumeOnACPowerLossDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 63, 1, 2),
    _CfprBiosVfResumeOnACPowerLossDn_Type()
)
cfprBiosVfResumeOnACPowerLossDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfResumeOnACPowerLossDn.setStatus("current")
_CfprBiosVfResumeOnACPowerLossRn_Type = SnmpAdminString
_CfprBiosVfResumeOnACPowerLossRn_Object = MibTableColumn
cfprBiosVfResumeOnACPowerLossRn = _CfprBiosVfResumeOnACPowerLossRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 63, 1, 3),
    _CfprBiosVfResumeOnACPowerLossRn_Type()
)
cfprBiosVfResumeOnACPowerLossRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfResumeOnACPowerLossRn.setStatus("current")
_CfprBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss_Type = CfprBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss
_CfprBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss_Object = MibTableColumn
cfprBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss = _CfprBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 63, 1, 4),
    _CfprBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss_Type()
)
cfprBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss.setStatus("current")
_CfprBiosVfResumeOnACPowerLossSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfResumeOnACPowerLossSupportedByDefault_Object = MibTableColumn
cfprBiosVfResumeOnACPowerLossSupportedByDefault = _CfprBiosVfResumeOnACPowerLossSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 63, 1, 5),
    _CfprBiosVfResumeOnACPowerLossSupportedByDefault_Type()
)
cfprBiosVfResumeOnACPowerLossSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfResumeOnACPowerLossSupportedByDefault.setStatus("current")
_CfprBiosVfScrubPoliciesTable_Object = MibTable
cfprBiosVfScrubPoliciesTable = _CfprBiosVfScrubPoliciesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 64)
)
if mibBuilder.loadTexts:
    cfprBiosVfScrubPoliciesTable.setStatus("current")
_CfprBiosVfScrubPoliciesEntry_Object = MibTableRow
cfprBiosVfScrubPoliciesEntry = _CfprBiosVfScrubPoliciesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 64, 1)
)
cfprBiosVfScrubPoliciesEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfScrubPoliciesInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfScrubPoliciesEntry.setStatus("current")
_CfprBiosVfScrubPoliciesInstanceId_Type = CfprManagedObjectId
_CfprBiosVfScrubPoliciesInstanceId_Object = MibTableColumn
cfprBiosVfScrubPoliciesInstanceId = _CfprBiosVfScrubPoliciesInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 64, 1, 1),
    _CfprBiosVfScrubPoliciesInstanceId_Type()
)
cfprBiosVfScrubPoliciesInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfScrubPoliciesInstanceId.setStatus("current")
_CfprBiosVfScrubPoliciesDn_Type = CfprManagedObjectDn
_CfprBiosVfScrubPoliciesDn_Object = MibTableColumn
cfprBiosVfScrubPoliciesDn = _CfprBiosVfScrubPoliciesDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 64, 1, 2),
    _CfprBiosVfScrubPoliciesDn_Type()
)
cfprBiosVfScrubPoliciesDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfScrubPoliciesDn.setStatus("current")
_CfprBiosVfScrubPoliciesRn_Type = SnmpAdminString
_CfprBiosVfScrubPoliciesRn_Object = MibTableColumn
cfprBiosVfScrubPoliciesRn = _CfprBiosVfScrubPoliciesRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 64, 1, 3),
    _CfprBiosVfScrubPoliciesRn_Type()
)
cfprBiosVfScrubPoliciesRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfScrubPoliciesRn.setStatus("current")
_CfprBiosVfScrubPoliciesVpDemandScrub_Type = CfprBiosVfScrubPoliciesVpDemandScrub
_CfprBiosVfScrubPoliciesVpDemandScrub_Object = MibTableColumn
cfprBiosVfScrubPoliciesVpDemandScrub = _CfprBiosVfScrubPoliciesVpDemandScrub_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 64, 1, 4),
    _CfprBiosVfScrubPoliciesVpDemandScrub_Type()
)
cfprBiosVfScrubPoliciesVpDemandScrub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfScrubPoliciesVpDemandScrub.setStatus("current")
_CfprBiosVfScrubPoliciesVpPatrolScrub_Type = CfprBiosVfScrubPoliciesVpPatrolScrub
_CfprBiosVfScrubPoliciesVpPatrolScrub_Object = MibTableColumn
cfprBiosVfScrubPoliciesVpPatrolScrub = _CfprBiosVfScrubPoliciesVpPatrolScrub_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 64, 1, 5),
    _CfprBiosVfScrubPoliciesVpPatrolScrub_Type()
)
cfprBiosVfScrubPoliciesVpPatrolScrub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfScrubPoliciesVpPatrolScrub.setStatus("current")
_CfprBiosVfScrubPoliciesSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfScrubPoliciesSupportedByDefault_Object = MibTableColumn
cfprBiosVfScrubPoliciesSupportedByDefault = _CfprBiosVfScrubPoliciesSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 64, 1, 6),
    _CfprBiosVfScrubPoliciesSupportedByDefault_Type()
)
cfprBiosVfScrubPoliciesSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfScrubPoliciesSupportedByDefault.setStatus("current")
_CfprBiosVfSelectMemoryRASConfigurationTable_Object = MibTable
cfprBiosVfSelectMemoryRASConfigurationTable = _CfprBiosVfSelectMemoryRASConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 65)
)
if mibBuilder.loadTexts:
    cfprBiosVfSelectMemoryRASConfigurationTable.setStatus("current")
_CfprBiosVfSelectMemoryRASConfigurationEntry_Object = MibTableRow
cfprBiosVfSelectMemoryRASConfigurationEntry = _CfprBiosVfSelectMemoryRASConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 65, 1)
)
cfprBiosVfSelectMemoryRASConfigurationEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfSelectMemoryRASConfigurationInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfSelectMemoryRASConfigurationEntry.setStatus("current")
_CfprBiosVfSelectMemoryRASConfigurationInstanceId_Type = CfprManagedObjectId
_CfprBiosVfSelectMemoryRASConfigurationInstanceId_Object = MibTableColumn
cfprBiosVfSelectMemoryRASConfigurationInstanceId = _CfprBiosVfSelectMemoryRASConfigurationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 65, 1, 1),
    _CfprBiosVfSelectMemoryRASConfigurationInstanceId_Type()
)
cfprBiosVfSelectMemoryRASConfigurationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfSelectMemoryRASConfigurationInstanceId.setStatus("current")
_CfprBiosVfSelectMemoryRASConfigurationDn_Type = CfprManagedObjectDn
_CfprBiosVfSelectMemoryRASConfigurationDn_Object = MibTableColumn
cfprBiosVfSelectMemoryRASConfigurationDn = _CfprBiosVfSelectMemoryRASConfigurationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 65, 1, 2),
    _CfprBiosVfSelectMemoryRASConfigurationDn_Type()
)
cfprBiosVfSelectMemoryRASConfigurationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfSelectMemoryRASConfigurationDn.setStatus("current")
_CfprBiosVfSelectMemoryRASConfigurationRn_Type = SnmpAdminString
_CfprBiosVfSelectMemoryRASConfigurationRn_Object = MibTableColumn
cfprBiosVfSelectMemoryRASConfigurationRn = _CfprBiosVfSelectMemoryRASConfigurationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 65, 1, 3),
    _CfprBiosVfSelectMemoryRASConfigurationRn_Type()
)
cfprBiosVfSelectMemoryRASConfigurationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfSelectMemoryRASConfigurationRn.setStatus("current")
_CfprBiosVfSelectMemoryRASConfigurationVpSelectMemoryRASConfiguration_Type = CfprBiosVfSelectMemoryRASConfigurationVpSelectMemoryRASConf
_CfprBiosVfSelectMemoryRASConfigurationVpSelectMemoryRASConfiguration_Object = MibTableColumn
cfprBiosVfSelectMemoryRASConfigurationVpSelectMemoryRASConfiguration = _CfprBiosVfSelectMemoryRASConfigurationVpSelectMemoryRASConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 65, 1, 4),
    _CfprBiosVfSelectMemoryRASConfigurationVpSelectMemoryRASConfiguration_Type()
)
cfprBiosVfSelectMemoryRASConfigurationVpSelectMemoryRASConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfSelectMemoryRASConfigurationVpSelectMemoryRASConfiguration.setStatus("current")
_CfprBiosVfSelectMemoryRASConfigurationSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfSelectMemoryRASConfigurationSupportedByDefault_Object = MibTableColumn
cfprBiosVfSelectMemoryRASConfigurationSupportedByDefault = _CfprBiosVfSelectMemoryRASConfigurationSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 65, 1, 5),
    _CfprBiosVfSelectMemoryRASConfigurationSupportedByDefault_Type()
)
cfprBiosVfSelectMemoryRASConfigurationSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfSelectMemoryRASConfigurationSupportedByDefault.setStatus("current")
_CfprBiosVfSerialPortAEnableTable_Object = MibTable
cfprBiosVfSerialPortAEnableTable = _CfprBiosVfSerialPortAEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 66)
)
if mibBuilder.loadTexts:
    cfprBiosVfSerialPortAEnableTable.setStatus("current")
_CfprBiosVfSerialPortAEnableEntry_Object = MibTableRow
cfprBiosVfSerialPortAEnableEntry = _CfprBiosVfSerialPortAEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 66, 1)
)
cfprBiosVfSerialPortAEnableEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfSerialPortAEnableInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfSerialPortAEnableEntry.setStatus("current")
_CfprBiosVfSerialPortAEnableInstanceId_Type = CfprManagedObjectId
_CfprBiosVfSerialPortAEnableInstanceId_Object = MibTableColumn
cfprBiosVfSerialPortAEnableInstanceId = _CfprBiosVfSerialPortAEnableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 66, 1, 1),
    _CfprBiosVfSerialPortAEnableInstanceId_Type()
)
cfprBiosVfSerialPortAEnableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfSerialPortAEnableInstanceId.setStatus("current")
_CfprBiosVfSerialPortAEnableDn_Type = CfprManagedObjectDn
_CfprBiosVfSerialPortAEnableDn_Object = MibTableColumn
cfprBiosVfSerialPortAEnableDn = _CfprBiosVfSerialPortAEnableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 66, 1, 2),
    _CfprBiosVfSerialPortAEnableDn_Type()
)
cfprBiosVfSerialPortAEnableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfSerialPortAEnableDn.setStatus("current")
_CfprBiosVfSerialPortAEnableRn_Type = SnmpAdminString
_CfprBiosVfSerialPortAEnableRn_Object = MibTableColumn
cfprBiosVfSerialPortAEnableRn = _CfprBiosVfSerialPortAEnableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 66, 1, 3),
    _CfprBiosVfSerialPortAEnableRn_Type()
)
cfprBiosVfSerialPortAEnableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfSerialPortAEnableRn.setStatus("current")
_CfprBiosVfSerialPortAEnableVpSerialPortAEnable_Type = CfprBiosVfSerialPortAEnableVpSerialPortAEnable
_CfprBiosVfSerialPortAEnableVpSerialPortAEnable_Object = MibTableColumn
cfprBiosVfSerialPortAEnableVpSerialPortAEnable = _CfprBiosVfSerialPortAEnableVpSerialPortAEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 66, 1, 4),
    _CfprBiosVfSerialPortAEnableVpSerialPortAEnable_Type()
)
cfprBiosVfSerialPortAEnableVpSerialPortAEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfSerialPortAEnableVpSerialPortAEnable.setStatus("current")
_CfprBiosVfSerialPortAEnableSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfSerialPortAEnableSupportedByDefault_Object = MibTableColumn
cfprBiosVfSerialPortAEnableSupportedByDefault = _CfprBiosVfSerialPortAEnableSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 66, 1, 5),
    _CfprBiosVfSerialPortAEnableSupportedByDefault_Type()
)
cfprBiosVfSerialPortAEnableSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfSerialPortAEnableSupportedByDefault.setStatus("current")
_CfprBiosVfSparingModeTable_Object = MibTable
cfprBiosVfSparingModeTable = _CfprBiosVfSparingModeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 67)
)
if mibBuilder.loadTexts:
    cfprBiosVfSparingModeTable.setStatus("current")
_CfprBiosVfSparingModeEntry_Object = MibTableRow
cfprBiosVfSparingModeEntry = _CfprBiosVfSparingModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 67, 1)
)
cfprBiosVfSparingModeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfSparingModeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfSparingModeEntry.setStatus("current")
_CfprBiosVfSparingModeInstanceId_Type = CfprManagedObjectId
_CfprBiosVfSparingModeInstanceId_Object = MibTableColumn
cfprBiosVfSparingModeInstanceId = _CfprBiosVfSparingModeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 67, 1, 1),
    _CfprBiosVfSparingModeInstanceId_Type()
)
cfprBiosVfSparingModeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfSparingModeInstanceId.setStatus("current")
_CfprBiosVfSparingModeDn_Type = CfprManagedObjectDn
_CfprBiosVfSparingModeDn_Object = MibTableColumn
cfprBiosVfSparingModeDn = _CfprBiosVfSparingModeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 67, 1, 2),
    _CfprBiosVfSparingModeDn_Type()
)
cfprBiosVfSparingModeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfSparingModeDn.setStatus("current")
_CfprBiosVfSparingModeRn_Type = SnmpAdminString
_CfprBiosVfSparingModeRn_Object = MibTableColumn
cfprBiosVfSparingModeRn = _CfprBiosVfSparingModeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 67, 1, 3),
    _CfprBiosVfSparingModeRn_Type()
)
cfprBiosVfSparingModeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfSparingModeRn.setStatus("current")
_CfprBiosVfSparingModeVpSparingMode_Type = CfprBiosVfSparingModeVpSparingMode
_CfprBiosVfSparingModeVpSparingMode_Object = MibTableColumn
cfprBiosVfSparingModeVpSparingMode = _CfprBiosVfSparingModeVpSparingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 67, 1, 4),
    _CfprBiosVfSparingModeVpSparingMode_Type()
)
cfprBiosVfSparingModeVpSparingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfSparingModeVpSparingMode.setStatus("current")
_CfprBiosVfSparingModeSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfSparingModeSupportedByDefault_Object = MibTableColumn
cfprBiosVfSparingModeSupportedByDefault = _CfprBiosVfSparingModeSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 67, 1, 5),
    _CfprBiosVfSparingModeSupportedByDefault_Type()
)
cfprBiosVfSparingModeSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfSparingModeSupportedByDefault.setStatus("current")
_CfprBiosVfSriovConfigTable_Object = MibTable
cfprBiosVfSriovConfigTable = _CfprBiosVfSriovConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 68)
)
if mibBuilder.loadTexts:
    cfprBiosVfSriovConfigTable.setStatus("current")
_CfprBiosVfSriovConfigEntry_Object = MibTableRow
cfprBiosVfSriovConfigEntry = _CfprBiosVfSriovConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 68, 1)
)
cfprBiosVfSriovConfigEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfSriovConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfSriovConfigEntry.setStatus("current")
_CfprBiosVfSriovConfigInstanceId_Type = CfprManagedObjectId
_CfprBiosVfSriovConfigInstanceId_Object = MibTableColumn
cfprBiosVfSriovConfigInstanceId = _CfprBiosVfSriovConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 68, 1, 1),
    _CfprBiosVfSriovConfigInstanceId_Type()
)
cfprBiosVfSriovConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfSriovConfigInstanceId.setStatus("current")
_CfprBiosVfSriovConfigDn_Type = CfprManagedObjectDn
_CfprBiosVfSriovConfigDn_Object = MibTableColumn
cfprBiosVfSriovConfigDn = _CfprBiosVfSriovConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 68, 1, 2),
    _CfprBiosVfSriovConfigDn_Type()
)
cfprBiosVfSriovConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfSriovConfigDn.setStatus("current")
_CfprBiosVfSriovConfigRn_Type = SnmpAdminString
_CfprBiosVfSriovConfigRn_Object = MibTableColumn
cfprBiosVfSriovConfigRn = _CfprBiosVfSriovConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 68, 1, 3),
    _CfprBiosVfSriovConfigRn_Type()
)
cfprBiosVfSriovConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfSriovConfigRn.setStatus("current")
_CfprBiosVfSriovConfigVpSriov_Type = CfprBiosVfSriovConfigVpSriov
_CfprBiosVfSriovConfigVpSriov_Object = MibTableColumn
cfprBiosVfSriovConfigVpSriov = _CfprBiosVfSriovConfigVpSriov_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 68, 1, 4),
    _CfprBiosVfSriovConfigVpSriov_Type()
)
cfprBiosVfSriovConfigVpSriov.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfSriovConfigVpSriov.setStatus("current")
_CfprBiosVfSriovConfigSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfSriovConfigSupportedByDefault_Object = MibTableColumn
cfprBiosVfSriovConfigSupportedByDefault = _CfprBiosVfSriovConfigSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 68, 1, 5),
    _CfprBiosVfSriovConfigSupportedByDefault_Type()
)
cfprBiosVfSriovConfigSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfSriovConfigSupportedByDefault.setStatus("current")
_CfprBiosVfTPMSupportTable_Object = MibTable
cfprBiosVfTPMSupportTable = _CfprBiosVfTPMSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 69)
)
if mibBuilder.loadTexts:
    cfprBiosVfTPMSupportTable.setStatus("current")
_CfprBiosVfTPMSupportEntry_Object = MibTableRow
cfprBiosVfTPMSupportEntry = _CfprBiosVfTPMSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 69, 1)
)
cfprBiosVfTPMSupportEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfTPMSupportInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfTPMSupportEntry.setStatus("current")
_CfprBiosVfTPMSupportInstanceId_Type = CfprManagedObjectId
_CfprBiosVfTPMSupportInstanceId_Object = MibTableColumn
cfprBiosVfTPMSupportInstanceId = _CfprBiosVfTPMSupportInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 69, 1, 1),
    _CfprBiosVfTPMSupportInstanceId_Type()
)
cfprBiosVfTPMSupportInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfTPMSupportInstanceId.setStatus("current")
_CfprBiosVfTPMSupportDn_Type = CfprManagedObjectDn
_CfprBiosVfTPMSupportDn_Object = MibTableColumn
cfprBiosVfTPMSupportDn = _CfprBiosVfTPMSupportDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 69, 1, 2),
    _CfprBiosVfTPMSupportDn_Type()
)
cfprBiosVfTPMSupportDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfTPMSupportDn.setStatus("current")
_CfprBiosVfTPMSupportRn_Type = SnmpAdminString
_CfprBiosVfTPMSupportRn_Object = MibTableColumn
cfprBiosVfTPMSupportRn = _CfprBiosVfTPMSupportRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 69, 1, 3),
    _CfprBiosVfTPMSupportRn_Type()
)
cfprBiosVfTPMSupportRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfTPMSupportRn.setStatus("current")
_CfprBiosVfTPMSupportVpTPMSupport_Type = CfprBiosVfTPMSupportVpTPMSupport
_CfprBiosVfTPMSupportVpTPMSupport_Object = MibTableColumn
cfprBiosVfTPMSupportVpTPMSupport = _CfprBiosVfTPMSupportVpTPMSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 69, 1, 4),
    _CfprBiosVfTPMSupportVpTPMSupport_Type()
)
cfprBiosVfTPMSupportVpTPMSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfTPMSupportVpTPMSupport.setStatus("current")
_CfprBiosVfTPMSupportSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfTPMSupportSupportedByDefault_Object = MibTableColumn
cfprBiosVfTPMSupportSupportedByDefault = _CfprBiosVfTPMSupportSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 69, 1, 5),
    _CfprBiosVfTPMSupportSupportedByDefault_Type()
)
cfprBiosVfTPMSupportSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfTPMSupportSupportedByDefault.setStatus("current")
_CfprBiosVfFPRMBootModeControlTable_Object = MibTable
cfprBiosVfFPRMBootModeControlTable = _CfprBiosVfFPRMBootModeControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 70)
)
if mibBuilder.loadTexts:
    cfprBiosVfFPRMBootModeControlTable.setStatus("current")
_CfprBiosVfFPRMBootModeControlEntry_Object = MibTableRow
cfprBiosVfFPRMBootModeControlEntry = _CfprBiosVfFPRMBootModeControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 70, 1)
)
cfprBiosVfFPRMBootModeControlEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfFPRMBootModeControlInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfFPRMBootModeControlEntry.setStatus("current")
_CfprBiosVfFPRMBootModeControlInstanceId_Type = CfprManagedObjectId
_CfprBiosVfFPRMBootModeControlInstanceId_Object = MibTableColumn
cfprBiosVfFPRMBootModeControlInstanceId = _CfprBiosVfFPRMBootModeControlInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 70, 1, 1),
    _CfprBiosVfFPRMBootModeControlInstanceId_Type()
)
cfprBiosVfFPRMBootModeControlInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfFPRMBootModeControlInstanceId.setStatus("current")
_CfprBiosVfFPRMBootModeControlDn_Type = CfprManagedObjectDn
_CfprBiosVfFPRMBootModeControlDn_Object = MibTableColumn
cfprBiosVfFPRMBootModeControlDn = _CfprBiosVfFPRMBootModeControlDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 70, 1, 2),
    _CfprBiosVfFPRMBootModeControlDn_Type()
)
cfprBiosVfFPRMBootModeControlDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfFPRMBootModeControlDn.setStatus("current")
_CfprBiosVfFPRMBootModeControlRn_Type = SnmpAdminString
_CfprBiosVfFPRMBootModeControlRn_Object = MibTableColumn
cfprBiosVfFPRMBootModeControlRn = _CfprBiosVfFPRMBootModeControlRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 70, 1, 3),
    _CfprBiosVfFPRMBootModeControlRn_Type()
)
cfprBiosVfFPRMBootModeControlRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfFPRMBootModeControlRn.setStatus("current")
_CfprBiosVfFPRMBootModeControlVpUEFIBootMode_Type = CfprBiosVfFPRMBootModeControlVpUEFIBootMode
_CfprBiosVfFPRMBootModeControlVpUEFIBootMode_Object = MibTableColumn
cfprBiosVfFPRMBootModeControlVpUEFIBootMode = _CfprBiosVfFPRMBootModeControlVpUEFIBootMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 70, 1, 4),
    _CfprBiosVfFPRMBootModeControlVpUEFIBootMode_Type()
)
cfprBiosVfFPRMBootModeControlVpUEFIBootMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfFPRMBootModeControlVpUEFIBootMode.setStatus("current")
_CfprBiosVfFPRMBootModeControlSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfFPRMBootModeControlSupportedByDefault_Object = MibTableColumn
cfprBiosVfFPRMBootModeControlSupportedByDefault = _CfprBiosVfFPRMBootModeControlSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 70, 1, 5),
    _CfprBiosVfFPRMBootModeControlSupportedByDefault_Type()
)
cfprBiosVfFPRMBootModeControlSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfFPRMBootModeControlSupportedByDefault.setStatus("current")
_CfprBiosVfFPRMBootOrderRuleControlTable_Object = MibTable
cfprBiosVfFPRMBootOrderRuleControlTable = _CfprBiosVfFPRMBootOrderRuleControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 71)
)
if mibBuilder.loadTexts:
    cfprBiosVfFPRMBootOrderRuleControlTable.setStatus("current")
_CfprBiosVfFPRMBootOrderRuleControlEntry_Object = MibTableRow
cfprBiosVfFPRMBootOrderRuleControlEntry = _CfprBiosVfFPRMBootOrderRuleControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 71, 1)
)
cfprBiosVfFPRMBootOrderRuleControlEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfFPRMBootOrderRuleControlInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfFPRMBootOrderRuleControlEntry.setStatus("current")
_CfprBiosVfFPRMBootOrderRuleControlInstanceId_Type = CfprManagedObjectId
_CfprBiosVfFPRMBootOrderRuleControlInstanceId_Object = MibTableColumn
cfprBiosVfFPRMBootOrderRuleControlInstanceId = _CfprBiosVfFPRMBootOrderRuleControlInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 71, 1, 1),
    _CfprBiosVfFPRMBootOrderRuleControlInstanceId_Type()
)
cfprBiosVfFPRMBootOrderRuleControlInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfFPRMBootOrderRuleControlInstanceId.setStatus("current")
_CfprBiosVfFPRMBootOrderRuleControlDn_Type = CfprManagedObjectDn
_CfprBiosVfFPRMBootOrderRuleControlDn_Object = MibTableColumn
cfprBiosVfFPRMBootOrderRuleControlDn = _CfprBiosVfFPRMBootOrderRuleControlDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 71, 1, 2),
    _CfprBiosVfFPRMBootOrderRuleControlDn_Type()
)
cfprBiosVfFPRMBootOrderRuleControlDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfFPRMBootOrderRuleControlDn.setStatus("current")
_CfprBiosVfFPRMBootOrderRuleControlRn_Type = SnmpAdminString
_CfprBiosVfFPRMBootOrderRuleControlRn_Object = MibTableColumn
cfprBiosVfFPRMBootOrderRuleControlRn = _CfprBiosVfFPRMBootOrderRuleControlRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 71, 1, 3),
    _CfprBiosVfFPRMBootOrderRuleControlRn_Type()
)
cfprBiosVfFPRMBootOrderRuleControlRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfFPRMBootOrderRuleControlRn.setStatus("current")
_CfprBiosVfFPRMBootOrderRuleControlVpFPRMBootOrderRule_Type = CfprBiosVfFPRMBootOrderRuleControlVpFPRMBootOrderRule
_CfprBiosVfFPRMBootOrderRuleControlVpFPRMBootOrderRule_Object = MibTableColumn
cfprBiosVfFPRMBootOrderRuleControlVpFPRMBootOrderRule = _CfprBiosVfFPRMBootOrderRuleControlVpFPRMBootOrderRule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 71, 1, 4),
    _CfprBiosVfFPRMBootOrderRuleControlVpFPRMBootOrderRule_Type()
)
cfprBiosVfFPRMBootOrderRuleControlVpFPRMBootOrderRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfFPRMBootOrderRuleControlVpFPRMBootOrderRule.setStatus("current")
_CfprBiosVfFPRMBootOrderRuleControlSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfFPRMBootOrderRuleControlSupportedByDefault_Object = MibTableColumn
cfprBiosVfFPRMBootOrderRuleControlSupportedByDefault = _CfprBiosVfFPRMBootOrderRuleControlSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 71, 1, 5),
    _CfprBiosVfFPRMBootOrderRuleControlSupportedByDefault_Type()
)
cfprBiosVfFPRMBootOrderRuleControlSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfFPRMBootOrderRuleControlSupportedByDefault.setStatus("current")
_CfprBiosVfUEFIOSUseLegacyVideoTable_Object = MibTable
cfprBiosVfUEFIOSUseLegacyVideoTable = _CfprBiosVfUEFIOSUseLegacyVideoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 72)
)
if mibBuilder.loadTexts:
    cfprBiosVfUEFIOSUseLegacyVideoTable.setStatus("current")
_CfprBiosVfUEFIOSUseLegacyVideoEntry_Object = MibTableRow
cfprBiosVfUEFIOSUseLegacyVideoEntry = _CfprBiosVfUEFIOSUseLegacyVideoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 72, 1)
)
cfprBiosVfUEFIOSUseLegacyVideoEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfUEFIOSUseLegacyVideoInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfUEFIOSUseLegacyVideoEntry.setStatus("current")
_CfprBiosVfUEFIOSUseLegacyVideoInstanceId_Type = CfprManagedObjectId
_CfprBiosVfUEFIOSUseLegacyVideoInstanceId_Object = MibTableColumn
cfprBiosVfUEFIOSUseLegacyVideoInstanceId = _CfprBiosVfUEFIOSUseLegacyVideoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 72, 1, 1),
    _CfprBiosVfUEFIOSUseLegacyVideoInstanceId_Type()
)
cfprBiosVfUEFIOSUseLegacyVideoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfUEFIOSUseLegacyVideoInstanceId.setStatus("current")
_CfprBiosVfUEFIOSUseLegacyVideoDn_Type = CfprManagedObjectDn
_CfprBiosVfUEFIOSUseLegacyVideoDn_Object = MibTableColumn
cfprBiosVfUEFIOSUseLegacyVideoDn = _CfprBiosVfUEFIOSUseLegacyVideoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 72, 1, 2),
    _CfprBiosVfUEFIOSUseLegacyVideoDn_Type()
)
cfprBiosVfUEFIOSUseLegacyVideoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUEFIOSUseLegacyVideoDn.setStatus("current")
_CfprBiosVfUEFIOSUseLegacyVideoRn_Type = SnmpAdminString
_CfprBiosVfUEFIOSUseLegacyVideoRn_Object = MibTableColumn
cfprBiosVfUEFIOSUseLegacyVideoRn = _CfprBiosVfUEFIOSUseLegacyVideoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 72, 1, 3),
    _CfprBiosVfUEFIOSUseLegacyVideoRn_Type()
)
cfprBiosVfUEFIOSUseLegacyVideoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUEFIOSUseLegacyVideoRn.setStatus("current")
_CfprBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo_Type = CfprBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo
_CfprBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo_Object = MibTableColumn
cfprBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo = _CfprBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 72, 1, 4),
    _CfprBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo_Type()
)
cfprBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo.setStatus("current")
_CfprBiosVfUEFIOSUseLegacyVideoSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfUEFIOSUseLegacyVideoSupportedByDefault_Object = MibTableColumn
cfprBiosVfUEFIOSUseLegacyVideoSupportedByDefault = _CfprBiosVfUEFIOSUseLegacyVideoSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 72, 1, 5),
    _CfprBiosVfUEFIOSUseLegacyVideoSupportedByDefault_Type()
)
cfprBiosVfUEFIOSUseLegacyVideoSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUEFIOSUseLegacyVideoSupportedByDefault.setStatus("current")
_CfprBiosVfUSBBootConfigTable_Object = MibTable
cfprBiosVfUSBBootConfigTable = _CfprBiosVfUSBBootConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 73)
)
if mibBuilder.loadTexts:
    cfprBiosVfUSBBootConfigTable.setStatus("current")
_CfprBiosVfUSBBootConfigEntry_Object = MibTableRow
cfprBiosVfUSBBootConfigEntry = _CfprBiosVfUSBBootConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 73, 1)
)
cfprBiosVfUSBBootConfigEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfUSBBootConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfUSBBootConfigEntry.setStatus("current")
_CfprBiosVfUSBBootConfigInstanceId_Type = CfprManagedObjectId
_CfprBiosVfUSBBootConfigInstanceId_Object = MibTableColumn
cfprBiosVfUSBBootConfigInstanceId = _CfprBiosVfUSBBootConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 73, 1, 1),
    _CfprBiosVfUSBBootConfigInstanceId_Type()
)
cfprBiosVfUSBBootConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfUSBBootConfigInstanceId.setStatus("current")
_CfprBiosVfUSBBootConfigDn_Type = CfprManagedObjectDn
_CfprBiosVfUSBBootConfigDn_Object = MibTableColumn
cfprBiosVfUSBBootConfigDn = _CfprBiosVfUSBBootConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 73, 1, 2),
    _CfprBiosVfUSBBootConfigDn_Type()
)
cfprBiosVfUSBBootConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBBootConfigDn.setStatus("current")
_CfprBiosVfUSBBootConfigRn_Type = SnmpAdminString
_CfprBiosVfUSBBootConfigRn_Object = MibTableColumn
cfprBiosVfUSBBootConfigRn = _CfprBiosVfUSBBootConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 73, 1, 3),
    _CfprBiosVfUSBBootConfigRn_Type()
)
cfprBiosVfUSBBootConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBBootConfigRn.setStatus("current")
_CfprBiosVfUSBBootConfigVpLegacyUSBSupport_Type = CfprBiosVfUSBBootConfigVpLegacyUSBSupport
_CfprBiosVfUSBBootConfigVpLegacyUSBSupport_Object = MibTableColumn
cfprBiosVfUSBBootConfigVpLegacyUSBSupport = _CfprBiosVfUSBBootConfigVpLegacyUSBSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 73, 1, 4),
    _CfprBiosVfUSBBootConfigVpLegacyUSBSupport_Type()
)
cfprBiosVfUSBBootConfigVpLegacyUSBSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBBootConfigVpLegacyUSBSupport.setStatus("current")
_CfprBiosVfUSBBootConfigVpMakeDeviceNonBootable_Type = CfprBiosVfUSBBootConfigVpMakeDeviceNonBootable
_CfprBiosVfUSBBootConfigVpMakeDeviceNonBootable_Object = MibTableColumn
cfprBiosVfUSBBootConfigVpMakeDeviceNonBootable = _CfprBiosVfUSBBootConfigVpMakeDeviceNonBootable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 73, 1, 5),
    _CfprBiosVfUSBBootConfigVpMakeDeviceNonBootable_Type()
)
cfprBiosVfUSBBootConfigVpMakeDeviceNonBootable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBBootConfigVpMakeDeviceNonBootable.setStatus("current")
_CfprBiosVfUSBBootConfigSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfUSBBootConfigSupportedByDefault_Object = MibTableColumn
cfprBiosVfUSBBootConfigSupportedByDefault = _CfprBiosVfUSBBootConfigSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 73, 1, 6),
    _CfprBiosVfUSBBootConfigSupportedByDefault_Type()
)
cfprBiosVfUSBBootConfigSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBBootConfigSupportedByDefault.setStatus("current")
_CfprBiosVfUSBConfigurationTable_Object = MibTable
cfprBiosVfUSBConfigurationTable = _CfprBiosVfUSBConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 74)
)
if mibBuilder.loadTexts:
    cfprBiosVfUSBConfigurationTable.setStatus("current")
_CfprBiosVfUSBConfigurationEntry_Object = MibTableRow
cfprBiosVfUSBConfigurationEntry = _CfprBiosVfUSBConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 74, 1)
)
cfprBiosVfUSBConfigurationEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfUSBConfigurationInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfUSBConfigurationEntry.setStatus("current")
_CfprBiosVfUSBConfigurationInstanceId_Type = CfprManagedObjectId
_CfprBiosVfUSBConfigurationInstanceId_Object = MibTableColumn
cfprBiosVfUSBConfigurationInstanceId = _CfprBiosVfUSBConfigurationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 74, 1, 1),
    _CfprBiosVfUSBConfigurationInstanceId_Type()
)
cfprBiosVfUSBConfigurationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfUSBConfigurationInstanceId.setStatus("current")
_CfprBiosVfUSBConfigurationDn_Type = CfprManagedObjectDn
_CfprBiosVfUSBConfigurationDn_Object = MibTableColumn
cfprBiosVfUSBConfigurationDn = _CfprBiosVfUSBConfigurationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 74, 1, 2),
    _CfprBiosVfUSBConfigurationDn_Type()
)
cfprBiosVfUSBConfigurationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBConfigurationDn.setStatus("current")
_CfprBiosVfUSBConfigurationRn_Type = SnmpAdminString
_CfprBiosVfUSBConfigurationRn_Object = MibTableColumn
cfprBiosVfUSBConfigurationRn = _CfprBiosVfUSBConfigurationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 74, 1, 3),
    _CfprBiosVfUSBConfigurationRn_Type()
)
cfprBiosVfUSBConfigurationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBConfigurationRn.setStatus("current")
_CfprBiosVfUSBConfigurationVpLegacyUSBSupport_Type = CfprBiosVfUSBConfigurationVpLegacyUSBSupport
_CfprBiosVfUSBConfigurationVpLegacyUSBSupport_Object = MibTableColumn
cfprBiosVfUSBConfigurationVpLegacyUSBSupport = _CfprBiosVfUSBConfigurationVpLegacyUSBSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 74, 1, 4),
    _CfprBiosVfUSBConfigurationVpLegacyUSBSupport_Type()
)
cfprBiosVfUSBConfigurationVpLegacyUSBSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBConfigurationVpLegacyUSBSupport.setStatus("current")
_CfprBiosVfUSBConfigurationVpXHCIMode_Type = CfprBiosVfUSBConfigurationVpXHCIMode
_CfprBiosVfUSBConfigurationVpXHCIMode_Object = MibTableColumn
cfprBiosVfUSBConfigurationVpXHCIMode = _CfprBiosVfUSBConfigurationVpXHCIMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 74, 1, 5),
    _CfprBiosVfUSBConfigurationVpXHCIMode_Type()
)
cfprBiosVfUSBConfigurationVpXHCIMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBConfigurationVpXHCIMode.setStatus("current")
_CfprBiosVfUSBConfigurationSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfUSBConfigurationSupportedByDefault_Object = MibTableColumn
cfprBiosVfUSBConfigurationSupportedByDefault = _CfprBiosVfUSBConfigurationSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 74, 1, 6),
    _CfprBiosVfUSBConfigurationSupportedByDefault_Type()
)
cfprBiosVfUSBConfigurationSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBConfigurationSupportedByDefault.setStatus("current")
_CfprBiosVfUSBFrontPanelAccessLockTable_Object = MibTable
cfprBiosVfUSBFrontPanelAccessLockTable = _CfprBiosVfUSBFrontPanelAccessLockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 75)
)
if mibBuilder.loadTexts:
    cfprBiosVfUSBFrontPanelAccessLockTable.setStatus("current")
_CfprBiosVfUSBFrontPanelAccessLockEntry_Object = MibTableRow
cfprBiosVfUSBFrontPanelAccessLockEntry = _CfprBiosVfUSBFrontPanelAccessLockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 75, 1)
)
cfprBiosVfUSBFrontPanelAccessLockEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfUSBFrontPanelAccessLockInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfUSBFrontPanelAccessLockEntry.setStatus("current")
_CfprBiosVfUSBFrontPanelAccessLockInstanceId_Type = CfprManagedObjectId
_CfprBiosVfUSBFrontPanelAccessLockInstanceId_Object = MibTableColumn
cfprBiosVfUSBFrontPanelAccessLockInstanceId = _CfprBiosVfUSBFrontPanelAccessLockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 75, 1, 1),
    _CfprBiosVfUSBFrontPanelAccessLockInstanceId_Type()
)
cfprBiosVfUSBFrontPanelAccessLockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfUSBFrontPanelAccessLockInstanceId.setStatus("current")
_CfprBiosVfUSBFrontPanelAccessLockDn_Type = CfprManagedObjectDn
_CfprBiosVfUSBFrontPanelAccessLockDn_Object = MibTableColumn
cfprBiosVfUSBFrontPanelAccessLockDn = _CfprBiosVfUSBFrontPanelAccessLockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 75, 1, 2),
    _CfprBiosVfUSBFrontPanelAccessLockDn_Type()
)
cfprBiosVfUSBFrontPanelAccessLockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBFrontPanelAccessLockDn.setStatus("current")
_CfprBiosVfUSBFrontPanelAccessLockRn_Type = SnmpAdminString
_CfprBiosVfUSBFrontPanelAccessLockRn_Object = MibTableColumn
cfprBiosVfUSBFrontPanelAccessLockRn = _CfprBiosVfUSBFrontPanelAccessLockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 75, 1, 3),
    _CfprBiosVfUSBFrontPanelAccessLockRn_Type()
)
cfprBiosVfUSBFrontPanelAccessLockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBFrontPanelAccessLockRn.setStatus("current")
_CfprBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock_Type = CfprBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock
_CfprBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock_Object = MibTableColumn
cfprBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock = _CfprBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 75, 1, 4),
    _CfprBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock_Type()
)
cfprBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock.setStatus("current")
_CfprBiosVfUSBFrontPanelAccessLockSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfUSBFrontPanelAccessLockSupportedByDefault_Object = MibTableColumn
cfprBiosVfUSBFrontPanelAccessLockSupportedByDefault = _CfprBiosVfUSBFrontPanelAccessLockSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 75, 1, 5),
    _CfprBiosVfUSBFrontPanelAccessLockSupportedByDefault_Type()
)
cfprBiosVfUSBFrontPanelAccessLockSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBFrontPanelAccessLockSupportedByDefault.setStatus("current")
_CfprBiosVfUSBPortConfigurationTable_Object = MibTable
cfprBiosVfUSBPortConfigurationTable = _CfprBiosVfUSBPortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 76)
)
if mibBuilder.loadTexts:
    cfprBiosVfUSBPortConfigurationTable.setStatus("current")
_CfprBiosVfUSBPortConfigurationEntry_Object = MibTableRow
cfprBiosVfUSBPortConfigurationEntry = _CfprBiosVfUSBPortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 76, 1)
)
cfprBiosVfUSBPortConfigurationEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfUSBPortConfigurationInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfUSBPortConfigurationEntry.setStatus("current")
_CfprBiosVfUSBPortConfigurationInstanceId_Type = CfprManagedObjectId
_CfprBiosVfUSBPortConfigurationInstanceId_Object = MibTableColumn
cfprBiosVfUSBPortConfigurationInstanceId = _CfprBiosVfUSBPortConfigurationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 76, 1, 1),
    _CfprBiosVfUSBPortConfigurationInstanceId_Type()
)
cfprBiosVfUSBPortConfigurationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfUSBPortConfigurationInstanceId.setStatus("current")
_CfprBiosVfUSBPortConfigurationDn_Type = CfprManagedObjectDn
_CfprBiosVfUSBPortConfigurationDn_Object = MibTableColumn
cfprBiosVfUSBPortConfigurationDn = _CfprBiosVfUSBPortConfigurationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 76, 1, 2),
    _CfprBiosVfUSBPortConfigurationDn_Type()
)
cfprBiosVfUSBPortConfigurationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBPortConfigurationDn.setStatus("current")
_CfprBiosVfUSBPortConfigurationRn_Type = SnmpAdminString
_CfprBiosVfUSBPortConfigurationRn_Object = MibTableColumn
cfprBiosVfUSBPortConfigurationRn = _CfprBiosVfUSBPortConfigurationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 76, 1, 3),
    _CfprBiosVfUSBPortConfigurationRn_Type()
)
cfprBiosVfUSBPortConfigurationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBPortConfigurationRn.setStatus("current")
_CfprBiosVfUSBPortConfigurationVpPort6064Emulation_Type = CfprBiosVfUSBPortConfigurationVpPort6064Emulation
_CfprBiosVfUSBPortConfigurationVpPort6064Emulation_Object = MibTableColumn
cfprBiosVfUSBPortConfigurationVpPort6064Emulation = _CfprBiosVfUSBPortConfigurationVpPort6064Emulation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 76, 1, 4),
    _CfprBiosVfUSBPortConfigurationVpPort6064Emulation_Type()
)
cfprBiosVfUSBPortConfigurationVpPort6064Emulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBPortConfigurationVpPort6064Emulation.setStatus("current")
_CfprBiosVfUSBPortConfigurationVpUSBPortFront_Type = CfprBiosVfUSBPortConfigurationVpUSBPortFront
_CfprBiosVfUSBPortConfigurationVpUSBPortFront_Object = MibTableColumn
cfprBiosVfUSBPortConfigurationVpUSBPortFront = _CfprBiosVfUSBPortConfigurationVpUSBPortFront_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 76, 1, 5),
    _CfprBiosVfUSBPortConfigurationVpUSBPortFront_Type()
)
cfprBiosVfUSBPortConfigurationVpUSBPortFront.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBPortConfigurationVpUSBPortFront.setStatus("current")
_CfprBiosVfUSBPortConfigurationVpUSBPortInternal_Type = CfprBiosVfUSBPortConfigurationVpUSBPortInternal
_CfprBiosVfUSBPortConfigurationVpUSBPortInternal_Object = MibTableColumn
cfprBiosVfUSBPortConfigurationVpUSBPortInternal = _CfprBiosVfUSBPortConfigurationVpUSBPortInternal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 76, 1, 6),
    _CfprBiosVfUSBPortConfigurationVpUSBPortInternal_Type()
)
cfprBiosVfUSBPortConfigurationVpUSBPortInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBPortConfigurationVpUSBPortInternal.setStatus("current")
_CfprBiosVfUSBPortConfigurationVpUSBPortKVM_Type = CfprBiosVfUSBPortConfigurationVpUSBPortKVM
_CfprBiosVfUSBPortConfigurationVpUSBPortKVM_Object = MibTableColumn
cfprBiosVfUSBPortConfigurationVpUSBPortKVM = _CfprBiosVfUSBPortConfigurationVpUSBPortKVM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 76, 1, 7),
    _CfprBiosVfUSBPortConfigurationVpUSBPortKVM_Type()
)
cfprBiosVfUSBPortConfigurationVpUSBPortKVM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBPortConfigurationVpUSBPortKVM.setStatus("current")
_CfprBiosVfUSBPortConfigurationVpUSBPortRear_Type = CfprBiosVfUSBPortConfigurationVpUSBPortRear
_CfprBiosVfUSBPortConfigurationVpUSBPortRear_Object = MibTableColumn
cfprBiosVfUSBPortConfigurationVpUSBPortRear = _CfprBiosVfUSBPortConfigurationVpUSBPortRear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 76, 1, 8),
    _CfprBiosVfUSBPortConfigurationVpUSBPortRear_Type()
)
cfprBiosVfUSBPortConfigurationVpUSBPortRear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBPortConfigurationVpUSBPortRear.setStatus("current")
_CfprBiosVfUSBPortConfigurationVpUSBPortSDCard_Type = CfprBiosVfUSBPortConfigurationVpUSBPortSDCard
_CfprBiosVfUSBPortConfigurationVpUSBPortSDCard_Object = MibTableColumn
cfprBiosVfUSBPortConfigurationVpUSBPortSDCard = _CfprBiosVfUSBPortConfigurationVpUSBPortSDCard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 76, 1, 9),
    _CfprBiosVfUSBPortConfigurationVpUSBPortSDCard_Type()
)
cfprBiosVfUSBPortConfigurationVpUSBPortSDCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBPortConfigurationVpUSBPortSDCard.setStatus("current")
_CfprBiosVfUSBPortConfigurationVpUSBPortVMedia_Type = CfprBiosVfUSBPortConfigurationVpUSBPortVMedia
_CfprBiosVfUSBPortConfigurationVpUSBPortVMedia_Object = MibTableColumn
cfprBiosVfUSBPortConfigurationVpUSBPortVMedia = _CfprBiosVfUSBPortConfigurationVpUSBPortVMedia_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 76, 1, 10),
    _CfprBiosVfUSBPortConfigurationVpUSBPortVMedia_Type()
)
cfprBiosVfUSBPortConfigurationVpUSBPortVMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBPortConfigurationVpUSBPortVMedia.setStatus("current")
_CfprBiosVfUSBPortConfigurationSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfUSBPortConfigurationSupportedByDefault_Object = MibTableColumn
cfprBiosVfUSBPortConfigurationSupportedByDefault = _CfprBiosVfUSBPortConfigurationSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 76, 1, 11),
    _CfprBiosVfUSBPortConfigurationSupportedByDefault_Type()
)
cfprBiosVfUSBPortConfigurationSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBPortConfigurationSupportedByDefault.setStatus("current")
_CfprBiosVfUSBSystemIdlePowerOptimizingSettingTable_Object = MibTable
cfprBiosVfUSBSystemIdlePowerOptimizingSettingTable = _CfprBiosVfUSBSystemIdlePowerOptimizingSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 77)
)
if mibBuilder.loadTexts:
    cfprBiosVfUSBSystemIdlePowerOptimizingSettingTable.setStatus("current")
_CfprBiosVfUSBSystemIdlePowerOptimizingSettingEntry_Object = MibTableRow
cfprBiosVfUSBSystemIdlePowerOptimizingSettingEntry = _CfprBiosVfUSBSystemIdlePowerOptimizingSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 77, 1)
)
cfprBiosVfUSBSystemIdlePowerOptimizingSettingEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfUSBSystemIdlePowerOptimizingSettingEntry.setStatus("current")
_CfprBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId_Type = CfprManagedObjectId
_CfprBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId_Object = MibTableColumn
cfprBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId = _CfprBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 77, 1, 1),
    _CfprBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId_Type()
)
cfprBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId.setStatus("current")
_CfprBiosVfUSBSystemIdlePowerOptimizingSettingDn_Type = CfprManagedObjectDn
_CfprBiosVfUSBSystemIdlePowerOptimizingSettingDn_Object = MibTableColumn
cfprBiosVfUSBSystemIdlePowerOptimizingSettingDn = _CfprBiosVfUSBSystemIdlePowerOptimizingSettingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 77, 1, 2),
    _CfprBiosVfUSBSystemIdlePowerOptimizingSettingDn_Type()
)
cfprBiosVfUSBSystemIdlePowerOptimizingSettingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBSystemIdlePowerOptimizingSettingDn.setStatus("current")
_CfprBiosVfUSBSystemIdlePowerOptimizingSettingRn_Type = SnmpAdminString
_CfprBiosVfUSBSystemIdlePowerOptimizingSettingRn_Object = MibTableColumn
cfprBiosVfUSBSystemIdlePowerOptimizingSettingRn = _CfprBiosVfUSBSystemIdlePowerOptimizingSettingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 77, 1, 3),
    _CfprBiosVfUSBSystemIdlePowerOptimizingSettingRn_Type()
)
cfprBiosVfUSBSystemIdlePowerOptimizingSettingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBSystemIdlePowerOptimizingSettingRn.setStatus("current")
_CfprBiosVfUSBSystemIdlePowerOptimizingSettingVpUSBIdlePowerOptimizing_Type = CfprBiosVfUSBSysIdlePowerOptimizingSettingVpUSBIdlePowerOptimize
_CfprBiosVfUSBSystemIdlePowerOptimizingSettingVpUSBIdlePowerOptimizing_Object = MibTableColumn
cfprBiosVfUSBSystemIdlePowerOptimizingSettingVpUSBIdlePowerOptimizing = _CfprBiosVfUSBSystemIdlePowerOptimizingSettingVpUSBIdlePowerOptimizing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 77, 1, 4),
    _CfprBiosVfUSBSystemIdlePowerOptimizingSettingVpUSBIdlePowerOptimizing_Type()
)
cfprBiosVfUSBSystemIdlePowerOptimizingSettingVpUSBIdlePowerOptimizing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBSystemIdlePowerOptimizingSettingVpUSBIdlePowerOptimizing.setStatus("current")
_CfprBiosVfUSBSystemIdlePowerOptimizingSettingSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfUSBSystemIdlePowerOptimizingSettingSupportedByDefault_Object = MibTableColumn
cfprBiosVfUSBSystemIdlePowerOptimizingSettingSupportedByDefault = _CfprBiosVfUSBSystemIdlePowerOptimizingSettingSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 77, 1, 5),
    _CfprBiosVfUSBSystemIdlePowerOptimizingSettingSupportedByDefault_Type()
)
cfprBiosVfUSBSystemIdlePowerOptimizingSettingSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfUSBSystemIdlePowerOptimizingSettingSupportedByDefault.setStatus("current")
_CfprBiosVfVGAPriorityTable_Object = MibTable
cfprBiosVfVGAPriorityTable = _CfprBiosVfVGAPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 78)
)
if mibBuilder.loadTexts:
    cfprBiosVfVGAPriorityTable.setStatus("current")
_CfprBiosVfVGAPriorityEntry_Object = MibTableRow
cfprBiosVfVGAPriorityEntry = _CfprBiosVfVGAPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 78, 1)
)
cfprBiosVfVGAPriorityEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosVfVGAPriorityInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosVfVGAPriorityEntry.setStatus("current")
_CfprBiosVfVGAPriorityInstanceId_Type = CfprManagedObjectId
_CfprBiosVfVGAPriorityInstanceId_Object = MibTableColumn
cfprBiosVfVGAPriorityInstanceId = _CfprBiosVfVGAPriorityInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 78, 1, 1),
    _CfprBiosVfVGAPriorityInstanceId_Type()
)
cfprBiosVfVGAPriorityInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosVfVGAPriorityInstanceId.setStatus("current")
_CfprBiosVfVGAPriorityDn_Type = CfprManagedObjectDn
_CfprBiosVfVGAPriorityDn_Object = MibTableColumn
cfprBiosVfVGAPriorityDn = _CfprBiosVfVGAPriorityDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 78, 1, 2),
    _CfprBiosVfVGAPriorityDn_Type()
)
cfprBiosVfVGAPriorityDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfVGAPriorityDn.setStatus("current")
_CfprBiosVfVGAPriorityRn_Type = SnmpAdminString
_CfprBiosVfVGAPriorityRn_Object = MibTableColumn
cfprBiosVfVGAPriorityRn = _CfprBiosVfVGAPriorityRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 78, 1, 3),
    _CfprBiosVfVGAPriorityRn_Type()
)
cfprBiosVfVGAPriorityRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfVGAPriorityRn.setStatus("current")
_CfprBiosVfVGAPriorityVpVGAPriority_Type = CfprBiosVfVGAPriorityVpVGAPriority
_CfprBiosVfVGAPriorityVpVGAPriority_Object = MibTableColumn
cfprBiosVfVGAPriorityVpVGAPriority = _CfprBiosVfVGAPriorityVpVGAPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 78, 1, 4),
    _CfprBiosVfVGAPriorityVpVGAPriority_Type()
)
cfprBiosVfVGAPriorityVpVGAPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfVGAPriorityVpVGAPriority.setStatus("current")
_CfprBiosVfVGAPrioritySupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosVfVGAPrioritySupportedByDefault_Object = MibTableColumn
cfprBiosVfVGAPrioritySupportedByDefault = _CfprBiosVfVGAPrioritySupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 78, 1, 5),
    _CfprBiosVfVGAPrioritySupportedByDefault_Type()
)
cfprBiosVfVGAPrioritySupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosVfVGAPrioritySupportedByDefault.setStatus("current")
_CfprBiosTokenFeatureGroupTable_Object = MibTable
cfprBiosTokenFeatureGroupTable = _CfprBiosTokenFeatureGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 79)
)
if mibBuilder.loadTexts:
    cfprBiosTokenFeatureGroupTable.setStatus("current")
_CfprBiosTokenFeatureGroupEntry_Object = MibTableRow
cfprBiosTokenFeatureGroupEntry = _CfprBiosTokenFeatureGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 79, 1)
)
cfprBiosTokenFeatureGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosTokenFeatureGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosTokenFeatureGroupEntry.setStatus("current")
_CfprBiosTokenFeatureGroupInstanceId_Type = CfprManagedObjectId
_CfprBiosTokenFeatureGroupInstanceId_Object = MibTableColumn
cfprBiosTokenFeatureGroupInstanceId = _CfprBiosTokenFeatureGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 79, 1, 1),
    _CfprBiosTokenFeatureGroupInstanceId_Type()
)
cfprBiosTokenFeatureGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosTokenFeatureGroupInstanceId.setStatus("current")
_CfprBiosTokenFeatureGroupDn_Type = CfprManagedObjectDn
_CfprBiosTokenFeatureGroupDn_Object = MibTableColumn
cfprBiosTokenFeatureGroupDn = _CfprBiosTokenFeatureGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 79, 1, 2),
    _CfprBiosTokenFeatureGroupDn_Type()
)
cfprBiosTokenFeatureGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosTokenFeatureGroupDn.setStatus("current")
_CfprBiosTokenFeatureGroupRn_Type = SnmpAdminString
_CfprBiosTokenFeatureGroupRn_Object = MibTableColumn
cfprBiosTokenFeatureGroupRn = _CfprBiosTokenFeatureGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 79, 1, 3),
    _CfprBiosTokenFeatureGroupRn_Type()
)
cfprBiosTokenFeatureGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosTokenFeatureGroupRn.setStatus("current")
_CfprBiosTokenFeatureGroupName_Type = SnmpAdminString
_CfprBiosTokenFeatureGroupName_Object = MibTableColumn
cfprBiosTokenFeatureGroupName = _CfprBiosTokenFeatureGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 79, 1, 4),
    _CfprBiosTokenFeatureGroupName_Type()
)
cfprBiosTokenFeatureGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosTokenFeatureGroupName.setStatus("current")
_CfprBiosTokenFeatureGroupSupportedByDefault_Type = CfprBiosSupportedAction
_CfprBiosTokenFeatureGroupSupportedByDefault_Object = MibTableColumn
cfprBiosTokenFeatureGroupSupportedByDefault = _CfprBiosTokenFeatureGroupSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 79, 1, 5),
    _CfprBiosTokenFeatureGroupSupportedByDefault_Type()
)
cfprBiosTokenFeatureGroupSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosTokenFeatureGroupSupportedByDefault.setStatus("current")
_CfprBiosTokenParamTable_Object = MibTable
cfprBiosTokenParamTable = _CfprBiosTokenParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 80)
)
if mibBuilder.loadTexts:
    cfprBiosTokenParamTable.setStatus("current")
_CfprBiosTokenParamEntry_Object = MibTableRow
cfprBiosTokenParamEntry = _CfprBiosTokenParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 80, 1)
)
cfprBiosTokenParamEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosTokenParamInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosTokenParamEntry.setStatus("current")
_CfprBiosTokenParamInstanceId_Type = CfprManagedObjectId
_CfprBiosTokenParamInstanceId_Object = MibTableColumn
cfprBiosTokenParamInstanceId = _CfprBiosTokenParamInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 80, 1, 1),
    _CfprBiosTokenParamInstanceId_Type()
)
cfprBiosTokenParamInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosTokenParamInstanceId.setStatus("current")
_CfprBiosTokenParamDn_Type = CfprManagedObjectDn
_CfprBiosTokenParamDn_Object = MibTableColumn
cfprBiosTokenParamDn = _CfprBiosTokenParamDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 80, 1, 2),
    _CfprBiosTokenParamDn_Type()
)
cfprBiosTokenParamDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosTokenParamDn.setStatus("current")
_CfprBiosTokenParamRn_Type = SnmpAdminString
_CfprBiosTokenParamRn_Object = MibTableColumn
cfprBiosTokenParamRn = _CfprBiosTokenParamRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 80, 1, 3),
    _CfprBiosTokenParamRn_Type()
)
cfprBiosTokenParamRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosTokenParamRn.setStatus("current")
_CfprBiosTokenParamLegacyPropId_Type = SnmpAdminString
_CfprBiosTokenParamLegacyPropId_Object = MibTableColumn
cfprBiosTokenParamLegacyPropId = _CfprBiosTokenParamLegacyPropId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 80, 1, 4),
    _CfprBiosTokenParamLegacyPropId_Type()
)
cfprBiosTokenParamLegacyPropId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosTokenParamLegacyPropId.setStatus("current")
_CfprBiosTokenParamParamName_Type = SnmpAdminString
_CfprBiosTokenParamParamName_Object = MibTableColumn
cfprBiosTokenParamParamName = _CfprBiosTokenParamParamName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 80, 1, 5),
    _CfprBiosTokenParamParamName_Type()
)
cfprBiosTokenParamParamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosTokenParamParamName.setStatus("current")
_CfprBiosTokenParamTargetTokenName_Type = SnmpAdminString
_CfprBiosTokenParamTargetTokenName_Object = MibTableColumn
cfprBiosTokenParamTargetTokenName = _CfprBiosTokenParamTargetTokenName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 80, 1, 6),
    _CfprBiosTokenParamTargetTokenName_Type()
)
cfprBiosTokenParamTargetTokenName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosTokenParamTargetTokenName.setStatus("current")
_CfprBiosTokenParamUiGroupName_Type = SnmpAdminString
_CfprBiosTokenParamUiGroupName_Object = MibTableColumn
cfprBiosTokenParamUiGroupName = _CfprBiosTokenParamUiGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 80, 1, 7),
    _CfprBiosTokenParamUiGroupName_Type()
)
cfprBiosTokenParamUiGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosTokenParamUiGroupName.setStatus("current")
_CfprBiosTokenSettingsTable_Object = MibTable
cfprBiosTokenSettingsTable = _CfprBiosTokenSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 81)
)
if mibBuilder.loadTexts:
    cfprBiosTokenSettingsTable.setStatus("current")
_CfprBiosTokenSettingsEntry_Object = MibTableRow
cfprBiosTokenSettingsEntry = _CfprBiosTokenSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 81, 1)
)
cfprBiosTokenSettingsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BIOS-MIB", "cfprBiosTokenSettingsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBiosTokenSettingsEntry.setStatus("current")
_CfprBiosTokenSettingsInstanceId_Type = CfprManagedObjectId
_CfprBiosTokenSettingsInstanceId_Object = MibTableColumn
cfprBiosTokenSettingsInstanceId = _CfprBiosTokenSettingsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 81, 1, 1),
    _CfprBiosTokenSettingsInstanceId_Type()
)
cfprBiosTokenSettingsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBiosTokenSettingsInstanceId.setStatus("current")
_CfprBiosTokenSettingsDn_Type = CfprManagedObjectDn
_CfprBiosTokenSettingsDn_Object = MibTableColumn
cfprBiosTokenSettingsDn = _CfprBiosTokenSettingsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 81, 1, 2),
    _CfprBiosTokenSettingsDn_Type()
)
cfprBiosTokenSettingsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosTokenSettingsDn.setStatus("current")
_CfprBiosTokenSettingsRn_Type = SnmpAdminString
_CfprBiosTokenSettingsRn_Object = MibTableColumn
cfprBiosTokenSettingsRn = _CfprBiosTokenSettingsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 81, 1, 3),
    _CfprBiosTokenSettingsRn_Type()
)
cfprBiosTokenSettingsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosTokenSettingsRn.setStatus("current")
_CfprBiosTokenSettingsBiosRetSettingName_Type = SnmpAdminString
_CfprBiosTokenSettingsBiosRetSettingName_Object = MibTableColumn
cfprBiosTokenSettingsBiosRetSettingName = _CfprBiosTokenSettingsBiosRetSettingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 81, 1, 4),
    _CfprBiosTokenSettingsBiosRetSettingName_Type()
)
cfprBiosTokenSettingsBiosRetSettingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosTokenSettingsBiosRetSettingName.setStatus("current")
_CfprBiosTokenSettingsIsAssigned_Type = TruthValue
_CfprBiosTokenSettingsIsAssigned_Object = MibTableColumn
cfprBiosTokenSettingsIsAssigned = _CfprBiosTokenSettingsIsAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 81, 1, 5),
    _CfprBiosTokenSettingsIsAssigned_Type()
)
cfprBiosTokenSettingsIsAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosTokenSettingsIsAssigned.setStatus("current")
_CfprBiosTokenSettingsLegacyPropVal_Type = SnmpAdminString
_CfprBiosTokenSettingsLegacyPropVal_Object = MibTableColumn
cfprBiosTokenSettingsLegacyPropVal = _CfprBiosTokenSettingsLegacyPropVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 81, 1, 6),
    _CfprBiosTokenSettingsLegacyPropVal_Type()
)
cfprBiosTokenSettingsLegacyPropVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosTokenSettingsLegacyPropVal.setStatus("current")
_CfprBiosTokenSettingsSettingsMoRn_Type = SnmpAdminString
_CfprBiosTokenSettingsSettingsMoRn_Object = MibTableColumn
cfprBiosTokenSettingsSettingsMoRn = _CfprBiosTokenSettingsSettingsMoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 81, 1, 7),
    _CfprBiosTokenSettingsSettingsMoRn_Type()
)
cfprBiosTokenSettingsSettingsMoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosTokenSettingsSettingsMoRn.setStatus("current")
_CfprBiosTokenSettingsTargetTokenValue_Type = SnmpAdminString
_CfprBiosTokenSettingsTargetTokenValue_Object = MibTableColumn
cfprBiosTokenSettingsTargetTokenValue = _CfprBiosTokenSettingsTargetTokenValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 5, 81, 1, 8),
    _CfprBiosTokenSettingsTargetTokenValue_Type()
)
cfprBiosTokenSettingsTargetTokenValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBiosTokenSettingsTargetTokenValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-BIOS-MIB",
    **{"cfprBiosObjects": cfprBiosObjects,
       "cfprBiosBOTTable": cfprBiosBOTTable,
       "cfprBiosBOTEntry": cfprBiosBOTEntry,
       "cfprBiosBOTInstanceId": cfprBiosBOTInstanceId,
       "cfprBiosBOTDn": cfprBiosBOTDn,
       "cfprBiosBOTRn": cfprBiosBOTRn,
       "cfprBiosBOTLastUpdate": cfprBiosBOTLastUpdate,
       "cfprBiosBootDevTable": cfprBiosBootDevTable,
       "cfprBiosBootDevEntry": cfprBiosBootDevEntry,
       "cfprBiosBootDevInstanceId": cfprBiosBootDevInstanceId,
       "cfprBiosBootDevDn": cfprBiosBootDevDn,
       "cfprBiosBootDevRn": cfprBiosBootDevRn,
       "cfprBiosBootDevDescr": cfprBiosBootDevDescr,
       "cfprBiosBootDevDeviceName": cfprBiosBootDevDeviceName,
       "cfprBiosBootDevErrValue": cfprBiosBootDevErrValue,
       "cfprBiosBootDevOrder": cfprBiosBootDevOrder,
       "cfprBiosBootDevGrpTable": cfprBiosBootDevGrpTable,
       "cfprBiosBootDevGrpEntry": cfprBiosBootDevGrpEntry,
       "cfprBiosBootDevGrpInstanceId": cfprBiosBootDevGrpInstanceId,
       "cfprBiosBootDevGrpDn": cfprBiosBootDevGrpDn,
       "cfprBiosBootDevGrpRn": cfprBiosBootDevGrpRn,
       "cfprBiosBootDevGrpDescr": cfprBiosBootDevGrpDescr,
       "cfprBiosBootDevGrpDeviceName": cfprBiosBootDevGrpDeviceName,
       "cfprBiosBootDevGrpErrVal": cfprBiosBootDevGrpErrVal,
       "cfprBiosBootDevGrpOrder": cfprBiosBootDevGrpOrder,
       "cfprBiosBootDevGrpType": cfprBiosBootDevGrpType,
       "cfprBiosFeatureRefTable": cfprBiosFeatureRefTable,
       "cfprBiosFeatureRefEntry": cfprBiosFeatureRefEntry,
       "cfprBiosFeatureRefInstanceId": cfprBiosFeatureRefInstanceId,
       "cfprBiosFeatureRefDn": cfprBiosFeatureRefDn,
       "cfprBiosFeatureRefRn": cfprBiosFeatureRefRn,
       "cfprBiosFeatureRefFtrMoClassName": cfprBiosFeatureRefFtrMoClassName,
       "cfprBiosFeatureRefIsSupported": cfprBiosFeatureRefIsSupported,
       "cfprBiosFeatureRefName": cfprBiosFeatureRefName,
       "cfprBiosParameterRefTable": cfprBiosParameterRefTable,
       "cfprBiosParameterRefEntry": cfprBiosParameterRefEntry,
       "cfprBiosParameterRefInstanceId": cfprBiosParameterRefInstanceId,
       "cfprBiosParameterRefDn": cfprBiosParameterRefDn,
       "cfprBiosParameterRefRn": cfprBiosParameterRefRn,
       "cfprBiosParameterRefIsSupported": cfprBiosParameterRefIsSupported,
       "cfprBiosParameterRefName": cfprBiosParameterRefName,
       "cfprBiosParameterRefPropertyName": cfprBiosParameterRefPropertyName,
       "cfprBiosRefTable": cfprBiosRefTable,
       "cfprBiosRefEntry": cfprBiosRefEntry,
       "cfprBiosRefInstanceId": cfprBiosRefInstanceId,
       "cfprBiosRefDn": cfprBiosRefDn,
       "cfprBiosRefRn": cfprBiosRefRn,
       "cfprBiosRefIsSupported": cfprBiosRefIsSupported,
       "cfprBiosSettingRefTable": cfprBiosSettingRefTable,
       "cfprBiosSettingRefEntry": cfprBiosSettingRefEntry,
       "cfprBiosSettingRefInstanceId": cfprBiosSettingRefInstanceId,
       "cfprBiosSettingRefDn": cfprBiosSettingRefDn,
       "cfprBiosSettingRefRn": cfprBiosSettingRefRn,
       "cfprBiosSettingRefConstantName": cfprBiosSettingRefConstantName,
       "cfprBiosSettingRefIsDefault": cfprBiosSettingRefIsDefault,
       "cfprBiosSettingRefIsSupported": cfprBiosSettingRefIsSupported,
       "cfprBiosSettingRefName": cfprBiosSettingRefName,
       "cfprBiosSettingsTable": cfprBiosSettingsTable,
       "cfprBiosSettingsEntry": cfprBiosSettingsEntry,
       "cfprBiosSettingsInstanceId": cfprBiosSettingsInstanceId,
       "cfprBiosSettingsDn": cfprBiosSettingsDn,
       "cfprBiosSettingsRn": cfprBiosSettingsRn,
       "cfprBiosUnitTable": cfprBiosUnitTable,
       "cfprBiosUnitEntry": cfprBiosUnitEntry,
       "cfprBiosUnitInstanceId": cfprBiosUnitInstanceId,
       "cfprBiosUnitDn": cfprBiosUnitDn,
       "cfprBiosUnitRn": cfprBiosUnitRn,
       "cfprBiosUnitInitSeq": cfprBiosUnitInitSeq,
       "cfprBiosUnitInitTs": cfprBiosUnitInitTs,
       "cfprBiosUnitModel": cfprBiosUnitModel,
       "cfprBiosUnitRevision": cfprBiosUnitRevision,
       "cfprBiosUnitSerial": cfprBiosUnitSerial,
       "cfprBiosUnitVendor": cfprBiosUnitVendor,
       "cfprBiosVIdentityParamsTable": cfprBiosVIdentityParamsTable,
       "cfprBiosVIdentityParamsEntry": cfprBiosVIdentityParamsEntry,
       "cfprBiosVIdentityParamsInstanceId": cfprBiosVIdentityParamsInstanceId,
       "cfprBiosVIdentityParamsDn": cfprBiosVIdentityParamsDn,
       "cfprBiosVIdentityParamsRn": cfprBiosVIdentityParamsRn,
       "cfprBiosVIdentityParamsLsServerName": cfprBiosVIdentityParamsLsServerName,
       "cfprBiosVIdentityParamsLsServerTmplName": cfprBiosVIdentityParamsLsServerTmplName,
       "cfprBiosVIdentityParamsSysName": cfprBiosVIdentityParamsSysName,
       "cfprBiosVProfileTable": cfprBiosVProfileTable,
       "cfprBiosVProfileEntry": cfprBiosVProfileEntry,
       "cfprBiosVProfileInstanceId": cfprBiosVProfileInstanceId,
       "cfprBiosVProfileDn": cfprBiosVProfileDn,
       "cfprBiosVProfileRn": cfprBiosVProfileRn,
       "cfprBiosVProfileDescr": cfprBiosVProfileDescr,
       "cfprBiosVProfileIntId": cfprBiosVProfileIntId,
       "cfprBiosVProfileName": cfprBiosVProfileName,
       "cfprBiosVProfilePolicyLevel": cfprBiosVProfilePolicyLevel,
       "cfprBiosVProfilePolicyOwner": cfprBiosVProfilePolicyOwner,
       "cfprBiosVProfileRebootOnUpdate": cfprBiosVProfileRebootOnUpdate,
       "cfprBiosVfACPI10SupportTable": cfprBiosVfACPI10SupportTable,
       "cfprBiosVfACPI10SupportEntry": cfprBiosVfACPI10SupportEntry,
       "cfprBiosVfACPI10SupportInstanceId": cfprBiosVfACPI10SupportInstanceId,
       "cfprBiosVfACPI10SupportDn": cfprBiosVfACPI10SupportDn,
       "cfprBiosVfACPI10SupportRn": cfprBiosVfACPI10SupportRn,
       "cfprBiosVfACPI10SupportVpACPI10Support": cfprBiosVfACPI10SupportVpACPI10Support,
       "cfprBiosVfACPI10SupportSupportedByDefault": cfprBiosVfACPI10SupportSupportedByDefault,
       "cfprBiosVfAllUSBDevicesTable": cfprBiosVfAllUSBDevicesTable,
       "cfprBiosVfAllUSBDevicesEntry": cfprBiosVfAllUSBDevicesEntry,
       "cfprBiosVfAllUSBDevicesInstanceId": cfprBiosVfAllUSBDevicesInstanceId,
       "cfprBiosVfAllUSBDevicesDn": cfprBiosVfAllUSBDevicesDn,
       "cfprBiosVfAllUSBDevicesRn": cfprBiosVfAllUSBDevicesRn,
       "cfprBiosVfAllUSBDevicesVpAllUSBDevices": cfprBiosVfAllUSBDevicesVpAllUSBDevices,
       "cfprBiosVfAllUSBDevicesSupportedByDefault": cfprBiosVfAllUSBDevicesSupportedByDefault,
       "cfprBiosVfAltitudeTable": cfprBiosVfAltitudeTable,
       "cfprBiosVfAltitudeEntry": cfprBiosVfAltitudeEntry,
       "cfprBiosVfAltitudeInstanceId": cfprBiosVfAltitudeInstanceId,
       "cfprBiosVfAltitudeDn": cfprBiosVfAltitudeDn,
       "cfprBiosVfAltitudeRn": cfprBiosVfAltitudeRn,
       "cfprBiosVfAltitudeVpAltitude": cfprBiosVfAltitudeVpAltitude,
       "cfprBiosVfAltitudeSupportedByDefault": cfprBiosVfAltitudeSupportedByDefault,
       "cfprBiosVfAssertNMIOnPERRTable": cfprBiosVfAssertNMIOnPERRTable,
       "cfprBiosVfAssertNMIOnPERREntry": cfprBiosVfAssertNMIOnPERREntry,
       "cfprBiosVfAssertNMIOnPERRInstanceId": cfprBiosVfAssertNMIOnPERRInstanceId,
       "cfprBiosVfAssertNMIOnPERRDn": cfprBiosVfAssertNMIOnPERRDn,
       "cfprBiosVfAssertNMIOnPERRRn": cfprBiosVfAssertNMIOnPERRRn,
       "cfprBiosVfAssertNMIOnPERRVpAssertNMIOnPERR": cfprBiosVfAssertNMIOnPERRVpAssertNMIOnPERR,
       "cfprBiosVfAssertNMIOnPERRSupportedByDefault": cfprBiosVfAssertNMIOnPERRSupportedByDefault,
       "cfprBiosVfAssertNMIOnSERRTable": cfprBiosVfAssertNMIOnSERRTable,
       "cfprBiosVfAssertNMIOnSERREntry": cfprBiosVfAssertNMIOnSERREntry,
       "cfprBiosVfAssertNMIOnSERRInstanceId": cfprBiosVfAssertNMIOnSERRInstanceId,
       "cfprBiosVfAssertNMIOnSERRDn": cfprBiosVfAssertNMIOnSERRDn,
       "cfprBiosVfAssertNMIOnSERRRn": cfprBiosVfAssertNMIOnSERRRn,
       "cfprBiosVfAssertNMIOnSERRVpAssertNMIOnSERR": cfprBiosVfAssertNMIOnSERRVpAssertNMIOnSERR,
       "cfprBiosVfAssertNMIOnSERRSupportedByDefault": cfprBiosVfAssertNMIOnSERRSupportedByDefault,
       "cfprBiosVfBootOptionRetryTable": cfprBiosVfBootOptionRetryTable,
       "cfprBiosVfBootOptionRetryEntry": cfprBiosVfBootOptionRetryEntry,
       "cfprBiosVfBootOptionRetryInstanceId": cfprBiosVfBootOptionRetryInstanceId,
       "cfprBiosVfBootOptionRetryDn": cfprBiosVfBootOptionRetryDn,
       "cfprBiosVfBootOptionRetryRn": cfprBiosVfBootOptionRetryRn,
       "cfprBiosVfBootOptionRetryVpBootOptionRetry": cfprBiosVfBootOptionRetryVpBootOptionRetry,
       "cfprBiosVfBootOptionRetrySupportedByDefault": cfprBiosVfBootOptionRetrySupportedByDefault,
       "cfprBiosVfCPUPerformanceTable": cfprBiosVfCPUPerformanceTable,
       "cfprBiosVfCPUPerformanceEntry": cfprBiosVfCPUPerformanceEntry,
       "cfprBiosVfCPUPerformanceInstanceId": cfprBiosVfCPUPerformanceInstanceId,
       "cfprBiosVfCPUPerformanceDn": cfprBiosVfCPUPerformanceDn,
       "cfprBiosVfCPUPerformanceRn": cfprBiosVfCPUPerformanceRn,
       "cfprBiosVfCPUPerformanceVpCPUPerformance": cfprBiosVfCPUPerformanceVpCPUPerformance,
       "cfprBiosVfCPUPerformanceSupportedByDefault": cfprBiosVfCPUPerformanceSupportedByDefault,
       "cfprBiosVfConsoleRedirectionTable": cfprBiosVfConsoleRedirectionTable,
       "cfprBiosVfConsoleRedirectionEntry": cfprBiosVfConsoleRedirectionEntry,
       "cfprBiosVfConsoleRedirectionInstanceId": cfprBiosVfConsoleRedirectionInstanceId,
       "cfprBiosVfConsoleRedirectionDn": cfprBiosVfConsoleRedirectionDn,
       "cfprBiosVfConsoleRedirectionRn": cfprBiosVfConsoleRedirectionRn,
       "cfprBiosVfConsoleRedirectionVpBaudRate": cfprBiosVfConsoleRedirectionVpBaudRate,
       "cfprBiosVfConsoleRedirectionVpConsoleRedirection": cfprBiosVfConsoleRedirectionVpConsoleRedirection,
       "cfprBiosVfConsoleRedirectionVpFlowControl": cfprBiosVfConsoleRedirectionVpFlowControl,
       "cfprBiosVfConsoleRedirectionVpLegacyOSRedirection": cfprBiosVfConsoleRedirectionVpLegacyOSRedirection,
       "cfprBiosVfConsoleRedirectionVpPuttyKeyPad": cfprBiosVfConsoleRedirectionVpPuttyKeyPad,
       "cfprBiosVfConsoleRedirectionVpTerminalType": cfprBiosVfConsoleRedirectionVpTerminalType,
       "cfprBiosVfConsoleRedirectionSupportedByDefault": cfprBiosVfConsoleRedirectionSupportedByDefault,
       "cfprBiosVfCoreMultiProcessingTable": cfprBiosVfCoreMultiProcessingTable,
       "cfprBiosVfCoreMultiProcessingEntry": cfprBiosVfCoreMultiProcessingEntry,
       "cfprBiosVfCoreMultiProcessingInstanceId": cfprBiosVfCoreMultiProcessingInstanceId,
       "cfprBiosVfCoreMultiProcessingDn": cfprBiosVfCoreMultiProcessingDn,
       "cfprBiosVfCoreMultiProcessingRn": cfprBiosVfCoreMultiProcessingRn,
       "cfprBiosVfCoreMultiProcessingVpCoreMultiProcessing": cfprBiosVfCoreMultiProcessingVpCoreMultiProcessing,
       "cfprBiosVfCoreMultiProcessingSupportedByDefault": cfprBiosVfCoreMultiProcessingSupportedByDefault,
       "cfprBiosVfDRAMClockThrottlingTable": cfprBiosVfDRAMClockThrottlingTable,
       "cfprBiosVfDRAMClockThrottlingEntry": cfprBiosVfDRAMClockThrottlingEntry,
       "cfprBiosVfDRAMClockThrottlingInstanceId": cfprBiosVfDRAMClockThrottlingInstanceId,
       "cfprBiosVfDRAMClockThrottlingDn": cfprBiosVfDRAMClockThrottlingDn,
       "cfprBiosVfDRAMClockThrottlingRn": cfprBiosVfDRAMClockThrottlingRn,
       "cfprBiosVfDRAMClockThrottlingVpDRAMClockThrottling": cfprBiosVfDRAMClockThrottlingVpDRAMClockThrottling,
       "cfprBiosVfDRAMClockThrottlingSupportedByDefault": cfprBiosVfDRAMClockThrottlingSupportedByDefault,
       "cfprBiosVfDirectCacheAccessTable": cfprBiosVfDirectCacheAccessTable,
       "cfprBiosVfDirectCacheAccessEntry": cfprBiosVfDirectCacheAccessEntry,
       "cfprBiosVfDirectCacheAccessInstanceId": cfprBiosVfDirectCacheAccessInstanceId,
       "cfprBiosVfDirectCacheAccessDn": cfprBiosVfDirectCacheAccessDn,
       "cfprBiosVfDirectCacheAccessRn": cfprBiosVfDirectCacheAccessRn,
       "cfprBiosVfDirectCacheAccessVpDirectCacheAccess": cfprBiosVfDirectCacheAccessVpDirectCacheAccess,
       "cfprBiosVfDirectCacheAccessSupportedByDefault": cfprBiosVfDirectCacheAccessSupportedByDefault,
       "cfprBiosVfDramRefreshRateTable": cfprBiosVfDramRefreshRateTable,
       "cfprBiosVfDramRefreshRateEntry": cfprBiosVfDramRefreshRateEntry,
       "cfprBiosVfDramRefreshRateInstanceId": cfprBiosVfDramRefreshRateInstanceId,
       "cfprBiosVfDramRefreshRateDn": cfprBiosVfDramRefreshRateDn,
       "cfprBiosVfDramRefreshRateRn": cfprBiosVfDramRefreshRateRn,
       "cfprBiosVfDramRefreshRateVpDramRefreshRate": cfprBiosVfDramRefreshRateVpDramRefreshRate,
       "cfprBiosVfDramRefreshRateSupportedByDefault": cfprBiosVfDramRefreshRateSupportedByDefault,
       "cfprBiosVfEnhancedIntelSpeedStepTechTable": cfprBiosVfEnhancedIntelSpeedStepTechTable,
       "cfprBiosVfEnhancedIntelSpeedStepTechEntry": cfprBiosVfEnhancedIntelSpeedStepTechEntry,
       "cfprBiosVfEnhancedIntelSpeedStepTechInstanceId": cfprBiosVfEnhancedIntelSpeedStepTechInstanceId,
       "cfprBiosVfEnhancedIntelSpeedStepTechDn": cfprBiosVfEnhancedIntelSpeedStepTechDn,
       "cfprBiosVfEnhancedIntelSpeedStepTechRn": cfprBiosVfEnhancedIntelSpeedStepTechRn,
       "cfprBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech": cfprBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech,
       "cfprBiosVfEnhancedIntelSpeedStepTechSupportedByDefault": cfprBiosVfEnhancedIntelSpeedStepTechSupportedByDefault,
       "cfprBiosVfExecuteDisableBitTable": cfprBiosVfExecuteDisableBitTable,
       "cfprBiosVfExecuteDisableBitEntry": cfprBiosVfExecuteDisableBitEntry,
       "cfprBiosVfExecuteDisableBitInstanceId": cfprBiosVfExecuteDisableBitInstanceId,
       "cfprBiosVfExecuteDisableBitDn": cfprBiosVfExecuteDisableBitDn,
       "cfprBiosVfExecuteDisableBitRn": cfprBiosVfExecuteDisableBitRn,
       "cfprBiosVfExecuteDisableBitVpExecuteDisableBit": cfprBiosVfExecuteDisableBitVpExecuteDisableBit,
       "cfprBiosVfExecuteDisableBitSupportedByDefault": cfprBiosVfExecuteDisableBitSupportedByDefault,
       "cfprBiosVfFRB2TimerTable": cfprBiosVfFRB2TimerTable,
       "cfprBiosVfFRB2TimerEntry": cfprBiosVfFRB2TimerEntry,
       "cfprBiosVfFRB2TimerInstanceId": cfprBiosVfFRB2TimerInstanceId,
       "cfprBiosVfFRB2TimerDn": cfprBiosVfFRB2TimerDn,
       "cfprBiosVfFRB2TimerRn": cfprBiosVfFRB2TimerRn,
       "cfprBiosVfFRB2TimerVpFRB2Timer": cfprBiosVfFRB2TimerVpFRB2Timer,
       "cfprBiosVfFRB2TimerSupportedByDefault": cfprBiosVfFRB2TimerSupportedByDefault,
       "cfprBiosVfFrequencyFloorOverrideTable": cfprBiosVfFrequencyFloorOverrideTable,
       "cfprBiosVfFrequencyFloorOverrideEntry": cfprBiosVfFrequencyFloorOverrideEntry,
       "cfprBiosVfFrequencyFloorOverrideInstanceId": cfprBiosVfFrequencyFloorOverrideInstanceId,
       "cfprBiosVfFrequencyFloorOverrideDn": cfprBiosVfFrequencyFloorOverrideDn,
       "cfprBiosVfFrequencyFloorOverrideRn": cfprBiosVfFrequencyFloorOverrideRn,
       "cfprBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride": cfprBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride,
       "cfprBiosVfFrequencyFloorOverrideSupportedByDefault": cfprBiosVfFrequencyFloorOverrideSupportedByDefault,
       "cfprBiosVfFrontPanelLockoutTable": cfprBiosVfFrontPanelLockoutTable,
       "cfprBiosVfFrontPanelLockoutEntry": cfprBiosVfFrontPanelLockoutEntry,
       "cfprBiosVfFrontPanelLockoutInstanceId": cfprBiosVfFrontPanelLockoutInstanceId,
       "cfprBiosVfFrontPanelLockoutDn": cfprBiosVfFrontPanelLockoutDn,
       "cfprBiosVfFrontPanelLockoutRn": cfprBiosVfFrontPanelLockoutRn,
       "cfprBiosVfFrontPanelLockoutVpFrontPanelLockout": cfprBiosVfFrontPanelLockoutVpFrontPanelLockout,
       "cfprBiosVfFrontPanelLockoutSupportedByDefault": cfprBiosVfFrontPanelLockoutSupportedByDefault,
       "cfprBiosVfIntelEntrySASRAIDModuleTable": cfprBiosVfIntelEntrySASRAIDModuleTable,
       "cfprBiosVfIntelEntrySASRAIDModuleEntry": cfprBiosVfIntelEntrySASRAIDModuleEntry,
       "cfprBiosVfIntelEntrySASRAIDModuleInstanceId": cfprBiosVfIntelEntrySASRAIDModuleInstanceId,
       "cfprBiosVfIntelEntrySASRAIDModuleDn": cfprBiosVfIntelEntrySASRAIDModuleDn,
       "cfprBiosVfIntelEntrySASRAIDModuleRn": cfprBiosVfIntelEntrySASRAIDModuleRn,
       "cfprBiosVfIntelEntrySASRAIDModuleVpSASRAID": cfprBiosVfIntelEntrySASRAIDModuleVpSASRAID,
       "cfprBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule": cfprBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule,
       "cfprBiosVfIntelEntrySASRAIDModuleSupportedByDefault": cfprBiosVfIntelEntrySASRAIDModuleSupportedByDefault,
       "cfprBiosVfIntelHyperThreadingTechTable": cfprBiosVfIntelHyperThreadingTechTable,
       "cfprBiosVfIntelHyperThreadingTechEntry": cfprBiosVfIntelHyperThreadingTechEntry,
       "cfprBiosVfIntelHyperThreadingTechInstanceId": cfprBiosVfIntelHyperThreadingTechInstanceId,
       "cfprBiosVfIntelHyperThreadingTechDn": cfprBiosVfIntelHyperThreadingTechDn,
       "cfprBiosVfIntelHyperThreadingTechRn": cfprBiosVfIntelHyperThreadingTechRn,
       "cfprBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech": cfprBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech,
       "cfprBiosVfIntelHyperThreadingTechSupportedByDefault": cfprBiosVfIntelHyperThreadingTechSupportedByDefault,
       "cfprBiosVfIntelTurboBoostTechTable": cfprBiosVfIntelTurboBoostTechTable,
       "cfprBiosVfIntelTurboBoostTechEntry": cfprBiosVfIntelTurboBoostTechEntry,
       "cfprBiosVfIntelTurboBoostTechInstanceId": cfprBiosVfIntelTurboBoostTechInstanceId,
       "cfprBiosVfIntelTurboBoostTechDn": cfprBiosVfIntelTurboBoostTechDn,
       "cfprBiosVfIntelTurboBoostTechRn": cfprBiosVfIntelTurboBoostTechRn,
       "cfprBiosVfIntelTurboBoostTechVpIntelTurboBoostTech": cfprBiosVfIntelTurboBoostTechVpIntelTurboBoostTech,
       "cfprBiosVfIntelTurboBoostTechSupportedByDefault": cfprBiosVfIntelTurboBoostTechSupportedByDefault,
       "cfprBiosVfIntelVTForDirectedIOTable": cfprBiosVfIntelVTForDirectedIOTable,
       "cfprBiosVfIntelVTForDirectedIOEntry": cfprBiosVfIntelVTForDirectedIOEntry,
       "cfprBiosVfIntelVTForDirectedIOInstanceId": cfprBiosVfIntelVTForDirectedIOInstanceId,
       "cfprBiosVfIntelVTForDirectedIODn": cfprBiosVfIntelVTForDirectedIODn,
       "cfprBiosVfIntelVTForDirectedIORn": cfprBiosVfIntelVTForDirectedIORn,
       "cfprBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport": cfprBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport,
       "cfprBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport": cfprBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport,
       "cfprBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping": cfprBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping,
       "cfprBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport": cfprBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport,
       "cfprBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO": cfprBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO,
       "cfprBiosVfIntelVTForDirectedIOSupportedByDefault": cfprBiosVfIntelVTForDirectedIOSupportedByDefault,
       "cfprBiosVfIntelVirtualizationTechnologyTable": cfprBiosVfIntelVirtualizationTechnologyTable,
       "cfprBiosVfIntelVirtualizationTechnologyEntry": cfprBiosVfIntelVirtualizationTechnologyEntry,
       "cfprBiosVfIntelVirtualizationTechnologyInstanceId": cfprBiosVfIntelVirtualizationTechnologyInstanceId,
       "cfprBiosVfIntelVirtualizationTechnologyDn": cfprBiosVfIntelVirtualizationTechnologyDn,
       "cfprBiosVfIntelVirtualizationTechnologyRn": cfprBiosVfIntelVirtualizationTechnologyRn,
       "cfprBiosVfIntelVirtualizationTechnologyVpIntelVirtualizationTechnology": cfprBiosVfIntelVirtualizationTechnologyVpIntelVirtualizationTechnology,
       "cfprBiosVfIntelVirtualizationTechnologySupportedByDefault": cfprBiosVfIntelVirtualizationTechnologySupportedByDefault,
       "cfprBiosVfInterleaveConfigurationTable": cfprBiosVfInterleaveConfigurationTable,
       "cfprBiosVfInterleaveConfigurationEntry": cfprBiosVfInterleaveConfigurationEntry,
       "cfprBiosVfInterleaveConfigurationInstanceId": cfprBiosVfInterleaveConfigurationInstanceId,
       "cfprBiosVfInterleaveConfigurationDn": cfprBiosVfInterleaveConfigurationDn,
       "cfprBiosVfInterleaveConfigurationRn": cfprBiosVfInterleaveConfigurationRn,
       "cfprBiosVfInterleaveConfigurationVpChannelInterleaving": cfprBiosVfInterleaveConfigurationVpChannelInterleaving,
       "cfprBiosVfInterleaveConfigurationVpMemoryInterleaving": cfprBiosVfInterleaveConfigurationVpMemoryInterleaving,
       "cfprBiosVfInterleaveConfigurationVpRankInterleaving": cfprBiosVfInterleaveConfigurationVpRankInterleaving,
       "cfprBiosVfInterleaveConfigurationSupportedByDefault": cfprBiosVfInterleaveConfigurationSupportedByDefault,
       "cfprBiosVfLocalX2ApicTable": cfprBiosVfLocalX2ApicTable,
       "cfprBiosVfLocalX2ApicEntry": cfprBiosVfLocalX2ApicEntry,
       "cfprBiosVfLocalX2ApicInstanceId": cfprBiosVfLocalX2ApicInstanceId,
       "cfprBiosVfLocalX2ApicDn": cfprBiosVfLocalX2ApicDn,
       "cfprBiosVfLocalX2ApicRn": cfprBiosVfLocalX2ApicRn,
       "cfprBiosVfLocalX2ApicVpLocalX2Apic": cfprBiosVfLocalX2ApicVpLocalX2Apic,
       "cfprBiosVfLocalX2ApicSupportedByDefault": cfprBiosVfLocalX2ApicSupportedByDefault,
       "cfprBiosVfLvDIMMSupportTable": cfprBiosVfLvDIMMSupportTable,
       "cfprBiosVfLvDIMMSupportEntry": cfprBiosVfLvDIMMSupportEntry,
       "cfprBiosVfLvDIMMSupportInstanceId": cfprBiosVfLvDIMMSupportInstanceId,
       "cfprBiosVfLvDIMMSupportDn": cfprBiosVfLvDIMMSupportDn,
       "cfprBiosVfLvDIMMSupportRn": cfprBiosVfLvDIMMSupportRn,
       "cfprBiosVfLvDIMMSupportVpLvDDRMode": cfprBiosVfLvDIMMSupportVpLvDDRMode,
       "cfprBiosVfLvDIMMSupportSupportedByDefault": cfprBiosVfLvDIMMSupportSupportedByDefault,
       "cfprBiosVfMaxVariableMTRRSettingTable": cfprBiosVfMaxVariableMTRRSettingTable,
       "cfprBiosVfMaxVariableMTRRSettingEntry": cfprBiosVfMaxVariableMTRRSettingEntry,
       "cfprBiosVfMaxVariableMTRRSettingInstanceId": cfprBiosVfMaxVariableMTRRSettingInstanceId,
       "cfprBiosVfMaxVariableMTRRSettingDn": cfprBiosVfMaxVariableMTRRSettingDn,
       "cfprBiosVfMaxVariableMTRRSettingRn": cfprBiosVfMaxVariableMTRRSettingRn,
       "cfprBiosVfMaxVariableMTRRSettingVpProcessorMtrr": cfprBiosVfMaxVariableMTRRSettingVpProcessorMtrr,
       "cfprBiosVfMaxVariableMTRRSettingSupportedByDefault": cfprBiosVfMaxVariableMTRRSettingSupportedByDefault,
       "cfprBiosVfMaximumMemoryBelow4GBTable": cfprBiosVfMaximumMemoryBelow4GBTable,
       "cfprBiosVfMaximumMemoryBelow4GBEntry": cfprBiosVfMaximumMemoryBelow4GBEntry,
       "cfprBiosVfMaximumMemoryBelow4GBInstanceId": cfprBiosVfMaximumMemoryBelow4GBInstanceId,
       "cfprBiosVfMaximumMemoryBelow4GBDn": cfprBiosVfMaximumMemoryBelow4GBDn,
       "cfprBiosVfMaximumMemoryBelow4GBRn": cfprBiosVfMaximumMemoryBelow4GBRn,
       "cfprBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB": cfprBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB,
       "cfprBiosVfMaximumMemoryBelow4GBSupportedByDefault": cfprBiosVfMaximumMemoryBelow4GBSupportedByDefault,
       "cfprBiosVfMemoryMappedIOAbove4GBTable": cfprBiosVfMemoryMappedIOAbove4GBTable,
       "cfprBiosVfMemoryMappedIOAbove4GBEntry": cfprBiosVfMemoryMappedIOAbove4GBEntry,
       "cfprBiosVfMemoryMappedIOAbove4GBInstanceId": cfprBiosVfMemoryMappedIOAbove4GBInstanceId,
       "cfprBiosVfMemoryMappedIOAbove4GBDn": cfprBiosVfMemoryMappedIOAbove4GBDn,
       "cfprBiosVfMemoryMappedIOAbove4GBRn": cfprBiosVfMemoryMappedIOAbove4GBRn,
       "cfprBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB": cfprBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB,
       "cfprBiosVfMemoryMappedIOAbove4GBSupportedByDefault": cfprBiosVfMemoryMappedIOAbove4GBSupportedByDefault,
       "cfprBiosVfMirroringModeTable": cfprBiosVfMirroringModeTable,
       "cfprBiosVfMirroringModeEntry": cfprBiosVfMirroringModeEntry,
       "cfprBiosVfMirroringModeInstanceId": cfprBiosVfMirroringModeInstanceId,
       "cfprBiosVfMirroringModeDn": cfprBiosVfMirroringModeDn,
       "cfprBiosVfMirroringModeRn": cfprBiosVfMirroringModeRn,
       "cfprBiosVfMirroringModeVpMirroringMode": cfprBiosVfMirroringModeVpMirroringMode,
       "cfprBiosVfMirroringModeSupportedByDefault": cfprBiosVfMirroringModeSupportedByDefault,
       "cfprBiosVfNUMAOptimizedTable": cfprBiosVfNUMAOptimizedTable,
       "cfprBiosVfNUMAOptimizedEntry": cfprBiosVfNUMAOptimizedEntry,
       "cfprBiosVfNUMAOptimizedInstanceId": cfprBiosVfNUMAOptimizedInstanceId,
       "cfprBiosVfNUMAOptimizedDn": cfprBiosVfNUMAOptimizedDn,
       "cfprBiosVfNUMAOptimizedRn": cfprBiosVfNUMAOptimizedRn,
       "cfprBiosVfNUMAOptimizedVpNUMAOptimized": cfprBiosVfNUMAOptimizedVpNUMAOptimized,
       "cfprBiosVfNUMAOptimizedSupportedByDefault": cfprBiosVfNUMAOptimizedSupportedByDefault,
       "cfprBiosVfOSBootWatchdogTimerTable": cfprBiosVfOSBootWatchdogTimerTable,
       "cfprBiosVfOSBootWatchdogTimerEntry": cfprBiosVfOSBootWatchdogTimerEntry,
       "cfprBiosVfOSBootWatchdogTimerInstanceId": cfprBiosVfOSBootWatchdogTimerInstanceId,
       "cfprBiosVfOSBootWatchdogTimerDn": cfprBiosVfOSBootWatchdogTimerDn,
       "cfprBiosVfOSBootWatchdogTimerRn": cfprBiosVfOSBootWatchdogTimerRn,
       "cfprBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer": cfprBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer,
       "cfprBiosVfOSBootWatchdogTimerSupportedByDefault": cfprBiosVfOSBootWatchdogTimerSupportedByDefault,
       "cfprBiosVfOSBootWatchdogTimerPolicyTable": cfprBiosVfOSBootWatchdogTimerPolicyTable,
       "cfprBiosVfOSBootWatchdogTimerPolicyEntry": cfprBiosVfOSBootWatchdogTimerPolicyEntry,
       "cfprBiosVfOSBootWatchdogTimerPolicyInstanceId": cfprBiosVfOSBootWatchdogTimerPolicyInstanceId,
       "cfprBiosVfOSBootWatchdogTimerPolicyDn": cfprBiosVfOSBootWatchdogTimerPolicyDn,
       "cfprBiosVfOSBootWatchdogTimerPolicyRn": cfprBiosVfOSBootWatchdogTimerPolicyRn,
       "cfprBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy": cfprBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy,
       "cfprBiosVfOSBootWatchdogTimerPolicySupportedByDefault": cfprBiosVfOSBootWatchdogTimerPolicySupportedByDefault,
       "cfprBiosVfOSBootWatchdogTimerTimeoutTable": cfprBiosVfOSBootWatchdogTimerTimeoutTable,
       "cfprBiosVfOSBootWatchdogTimerTimeoutEntry": cfprBiosVfOSBootWatchdogTimerTimeoutEntry,
       "cfprBiosVfOSBootWatchdogTimerTimeoutInstanceId": cfprBiosVfOSBootWatchdogTimerTimeoutInstanceId,
       "cfprBiosVfOSBootWatchdogTimerTimeoutDn": cfprBiosVfOSBootWatchdogTimerTimeoutDn,
       "cfprBiosVfOSBootWatchdogTimerTimeoutRn": cfprBiosVfOSBootWatchdogTimerTimeoutRn,
       "cfprBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout": cfprBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout,
       "cfprBiosVfOSBootWatchdogTimerTimeoutSupportedByDefault": cfprBiosVfOSBootWatchdogTimerTimeoutSupportedByDefault,
       "cfprBiosVfOnboardSATAControllerTable": cfprBiosVfOnboardSATAControllerTable,
       "cfprBiosVfOnboardSATAControllerEntry": cfprBiosVfOnboardSATAControllerEntry,
       "cfprBiosVfOnboardSATAControllerInstanceId": cfprBiosVfOnboardSATAControllerInstanceId,
       "cfprBiosVfOnboardSATAControllerDn": cfprBiosVfOnboardSATAControllerDn,
       "cfprBiosVfOnboardSATAControllerRn": cfprBiosVfOnboardSATAControllerRn,
       "cfprBiosVfOnboardSATAControllerVpOnboardSATAController": cfprBiosVfOnboardSATAControllerVpOnboardSATAController,
       "cfprBiosVfOnboardSATAControllerVpSATAMode": cfprBiosVfOnboardSATAControllerVpSATAMode,
       "cfprBiosVfOnboardSATAControllerSupportedByDefault": cfprBiosVfOnboardSATAControllerSupportedByDefault,
       "cfprBiosVfOnboardStorageTable": cfprBiosVfOnboardStorageTable,
       "cfprBiosVfOnboardStorageEntry": cfprBiosVfOnboardStorageEntry,
       "cfprBiosVfOnboardStorageInstanceId": cfprBiosVfOnboardStorageInstanceId,
       "cfprBiosVfOnboardStorageDn": cfprBiosVfOnboardStorageDn,
       "cfprBiosVfOnboardStorageRn": cfprBiosVfOnboardStorageRn,
       "cfprBiosVfOnboardStorageVpOnboardSCUStorageSupport": cfprBiosVfOnboardStorageVpOnboardSCUStorageSupport,
       "cfprBiosVfOnboardStorageSupportedByDefault": cfprBiosVfOnboardStorageSupportedByDefault,
       "cfprBiosVfOptionROMEnableTable": cfprBiosVfOptionROMEnableTable,
       "cfprBiosVfOptionROMEnableEntry": cfprBiosVfOptionROMEnableEntry,
       "cfprBiosVfOptionROMEnableInstanceId": cfprBiosVfOptionROMEnableInstanceId,
       "cfprBiosVfOptionROMEnableDn": cfprBiosVfOptionROMEnableDn,
       "cfprBiosVfOptionROMEnableRn": cfprBiosVfOptionROMEnableRn,
       "cfprBiosVfOptionROMEnableVpState": cfprBiosVfOptionROMEnableVpState,
       "cfprBiosVfOptionROMEnableSupportedByDefault": cfprBiosVfOptionROMEnableSupportedByDefault,
       "cfprBiosVfOptionROMLoadTable": cfprBiosVfOptionROMLoadTable,
       "cfprBiosVfOptionROMLoadEntry": cfprBiosVfOptionROMLoadEntry,
       "cfprBiosVfOptionROMLoadInstanceId": cfprBiosVfOptionROMLoadInstanceId,
       "cfprBiosVfOptionROMLoadDn": cfprBiosVfOptionROMLoadDn,
       "cfprBiosVfOptionROMLoadRn": cfprBiosVfOptionROMLoadRn,
       "cfprBiosVfOptionROMLoadVpLoad": cfprBiosVfOptionROMLoadVpLoad,
       "cfprBiosVfOptionROMLoadSupportedByDefault": cfprBiosVfOptionROMLoadSupportedByDefault,
       "cfprBiosVfPCISlotLinkSpeedTable": cfprBiosVfPCISlotLinkSpeedTable,
       "cfprBiosVfPCISlotLinkSpeedEntry": cfprBiosVfPCISlotLinkSpeedEntry,
       "cfprBiosVfPCISlotLinkSpeedInstanceId": cfprBiosVfPCISlotLinkSpeedInstanceId,
       "cfprBiosVfPCISlotLinkSpeedDn": cfprBiosVfPCISlotLinkSpeedDn,
       "cfprBiosVfPCISlotLinkSpeedRn": cfprBiosVfPCISlotLinkSpeedRn,
       "cfprBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed": cfprBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed,
       "cfprBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed": cfprBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed,
       "cfprBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed": cfprBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed,
       "cfprBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed": cfprBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed,
       "cfprBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed": cfprBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed,
       "cfprBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed": cfprBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed,
       "cfprBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed": cfprBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed,
       "cfprBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed": cfprBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed,
       "cfprBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed": cfprBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed,
       "cfprBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed": cfprBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed,
       "cfprBiosVfPCISlotLinkSpeedSupportedByDefault": cfprBiosVfPCISlotLinkSpeedSupportedByDefault,
       "cfprBiosVfPCISlotOptionROMEnableTable": cfprBiosVfPCISlotOptionROMEnableTable,
       "cfprBiosVfPCISlotOptionROMEnableEntry": cfprBiosVfPCISlotOptionROMEnableEntry,
       "cfprBiosVfPCISlotOptionROMEnableInstanceId": cfprBiosVfPCISlotOptionROMEnableInstanceId,
       "cfprBiosVfPCISlotOptionROMEnableDn": cfprBiosVfPCISlotOptionROMEnableDn,
       "cfprBiosVfPCISlotOptionROMEnableRn": cfprBiosVfPCISlotOptionROMEnableRn,
       "cfprBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM": cfprBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM,
       "cfprBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM": cfprBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM,
       "cfprBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM": cfprBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM,
       "cfprBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM": cfprBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM,
       "cfprBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM": cfprBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM,
       "cfprBiosVfPCISlotOptionROMEnableVpSlot10State": cfprBiosVfPCISlotOptionROMEnableVpSlot10State,
       "cfprBiosVfPCISlotOptionROMEnableVpSlot1State": cfprBiosVfPCISlotOptionROMEnableVpSlot1State,
       "cfprBiosVfPCISlotOptionROMEnableVpSlot2State": cfprBiosVfPCISlotOptionROMEnableVpSlot2State,
       "cfprBiosVfPCISlotOptionROMEnableVpSlot3State": cfprBiosVfPCISlotOptionROMEnableVpSlot3State,
       "cfprBiosVfPCISlotOptionROMEnableVpSlot4State": cfprBiosVfPCISlotOptionROMEnableVpSlot4State,
       "cfprBiosVfPCISlotOptionROMEnableVpSlot5State": cfprBiosVfPCISlotOptionROMEnableVpSlot5State,
       "cfprBiosVfPCISlotOptionROMEnableVpSlot6State": cfprBiosVfPCISlotOptionROMEnableVpSlot6State,
       "cfprBiosVfPCISlotOptionROMEnableVpSlot7State": cfprBiosVfPCISlotOptionROMEnableVpSlot7State,
       "cfprBiosVfPCISlotOptionROMEnableVpSlot8State": cfprBiosVfPCISlotOptionROMEnableVpSlot8State,
       "cfprBiosVfPCISlotOptionROMEnableVpSlot9State": cfprBiosVfPCISlotOptionROMEnableVpSlot9State,
       "cfprBiosVfPCISlotOptionROMEnableVpSlotMezzState": cfprBiosVfPCISlotOptionROMEnableVpSlotMezzState,
       "cfprBiosVfPCISlotOptionROMEnableSupportedByDefault": cfprBiosVfPCISlotOptionROMEnableSupportedByDefault,
       "cfprBiosVfPOSTErrorPauseTable": cfprBiosVfPOSTErrorPauseTable,
       "cfprBiosVfPOSTErrorPauseEntry": cfprBiosVfPOSTErrorPauseEntry,
       "cfprBiosVfPOSTErrorPauseInstanceId": cfprBiosVfPOSTErrorPauseInstanceId,
       "cfprBiosVfPOSTErrorPauseDn": cfprBiosVfPOSTErrorPauseDn,
       "cfprBiosVfPOSTErrorPauseRn": cfprBiosVfPOSTErrorPauseRn,
       "cfprBiosVfPOSTErrorPauseVpPOSTErrorPause": cfprBiosVfPOSTErrorPauseVpPOSTErrorPause,
       "cfprBiosVfPOSTErrorPauseSupportedByDefault": cfprBiosVfPOSTErrorPauseSupportedByDefault,
       "cfprBiosVfPSTATECoordinationTable": cfprBiosVfPSTATECoordinationTable,
       "cfprBiosVfPSTATECoordinationEntry": cfprBiosVfPSTATECoordinationEntry,
       "cfprBiosVfPSTATECoordinationInstanceId": cfprBiosVfPSTATECoordinationInstanceId,
       "cfprBiosVfPSTATECoordinationDn": cfprBiosVfPSTATECoordinationDn,
       "cfprBiosVfPSTATECoordinationRn": cfprBiosVfPSTATECoordinationRn,
       "cfprBiosVfPSTATECoordinationVpPSTATECoordination": cfprBiosVfPSTATECoordinationVpPSTATECoordination,
       "cfprBiosVfPSTATECoordinationSupportedByDefault": cfprBiosVfPSTATECoordinationSupportedByDefault,
       "cfprBiosVfPackageCStateLimitTable": cfprBiosVfPackageCStateLimitTable,
       "cfprBiosVfPackageCStateLimitEntry": cfprBiosVfPackageCStateLimitEntry,
       "cfprBiosVfPackageCStateLimitInstanceId": cfprBiosVfPackageCStateLimitInstanceId,
       "cfprBiosVfPackageCStateLimitDn": cfprBiosVfPackageCStateLimitDn,
       "cfprBiosVfPackageCStateLimitRn": cfprBiosVfPackageCStateLimitRn,
       "cfprBiosVfPackageCStateLimitVpPackageCStateLimit": cfprBiosVfPackageCStateLimitVpPackageCStateLimit,
       "cfprBiosVfPackageCStateLimitSupportedByDefault": cfprBiosVfPackageCStateLimitSupportedByDefault,
       "cfprBiosVfProcessorC1ETable": cfprBiosVfProcessorC1ETable,
       "cfprBiosVfProcessorC1EEntry": cfprBiosVfProcessorC1EEntry,
       "cfprBiosVfProcessorC1EInstanceId": cfprBiosVfProcessorC1EInstanceId,
       "cfprBiosVfProcessorC1EDn": cfprBiosVfProcessorC1EDn,
       "cfprBiosVfProcessorC1ERn": cfprBiosVfProcessorC1ERn,
       "cfprBiosVfProcessorC1EVpProcessorC1E": cfprBiosVfProcessorC1EVpProcessorC1E,
       "cfprBiosVfProcessorC1ESupportedByDefault": cfprBiosVfProcessorC1ESupportedByDefault,
       "cfprBiosVfProcessorC3ReportTable": cfprBiosVfProcessorC3ReportTable,
       "cfprBiosVfProcessorC3ReportEntry": cfprBiosVfProcessorC3ReportEntry,
       "cfprBiosVfProcessorC3ReportInstanceId": cfprBiosVfProcessorC3ReportInstanceId,
       "cfprBiosVfProcessorC3ReportDn": cfprBiosVfProcessorC3ReportDn,
       "cfprBiosVfProcessorC3ReportRn": cfprBiosVfProcessorC3ReportRn,
       "cfprBiosVfProcessorC3ReportVpProcessorC3Report": cfprBiosVfProcessorC3ReportVpProcessorC3Report,
       "cfprBiosVfProcessorC3ReportSupportedByDefault": cfprBiosVfProcessorC3ReportSupportedByDefault,
       "cfprBiosVfProcessorC6ReportTable": cfprBiosVfProcessorC6ReportTable,
       "cfprBiosVfProcessorC6ReportEntry": cfprBiosVfProcessorC6ReportEntry,
       "cfprBiosVfProcessorC6ReportInstanceId": cfprBiosVfProcessorC6ReportInstanceId,
       "cfprBiosVfProcessorC6ReportDn": cfprBiosVfProcessorC6ReportDn,
       "cfprBiosVfProcessorC6ReportRn": cfprBiosVfProcessorC6ReportRn,
       "cfprBiosVfProcessorC6ReportVpProcessorC6Report": cfprBiosVfProcessorC6ReportVpProcessorC6Report,
       "cfprBiosVfProcessorC6ReportSupportedByDefault": cfprBiosVfProcessorC6ReportSupportedByDefault,
       "cfprBiosVfProcessorC7ReportTable": cfprBiosVfProcessorC7ReportTable,
       "cfprBiosVfProcessorC7ReportEntry": cfprBiosVfProcessorC7ReportEntry,
       "cfprBiosVfProcessorC7ReportInstanceId": cfprBiosVfProcessorC7ReportInstanceId,
       "cfprBiosVfProcessorC7ReportDn": cfprBiosVfProcessorC7ReportDn,
       "cfprBiosVfProcessorC7ReportRn": cfprBiosVfProcessorC7ReportRn,
       "cfprBiosVfProcessorC7ReportVpProcessorC7Report": cfprBiosVfProcessorC7ReportVpProcessorC7Report,
       "cfprBiosVfProcessorC7ReportSupportedByDefault": cfprBiosVfProcessorC7ReportSupportedByDefault,
       "cfprBiosVfProcessorCStateTable": cfprBiosVfProcessorCStateTable,
       "cfprBiosVfProcessorCStateEntry": cfprBiosVfProcessorCStateEntry,
       "cfprBiosVfProcessorCStateInstanceId": cfprBiosVfProcessorCStateInstanceId,
       "cfprBiosVfProcessorCStateDn": cfprBiosVfProcessorCStateDn,
       "cfprBiosVfProcessorCStateRn": cfprBiosVfProcessorCStateRn,
       "cfprBiosVfProcessorCStateVpProcessorCState": cfprBiosVfProcessorCStateVpProcessorCState,
       "cfprBiosVfProcessorCStateSupportedByDefault": cfprBiosVfProcessorCStateSupportedByDefault,
       "cfprBiosVfProcessorEnergyConfigurationTable": cfprBiosVfProcessorEnergyConfigurationTable,
       "cfprBiosVfProcessorEnergyConfigurationEntry": cfprBiosVfProcessorEnergyConfigurationEntry,
       "cfprBiosVfProcessorEnergyConfigurationInstanceId": cfprBiosVfProcessorEnergyConfigurationInstanceId,
       "cfprBiosVfProcessorEnergyConfigurationDn": cfprBiosVfProcessorEnergyConfigurationDn,
       "cfprBiosVfProcessorEnergyConfigurationRn": cfprBiosVfProcessorEnergyConfigurationRn,
       "cfprBiosVfProcessorEnergyConfigurationVpEnergyPerformance": cfprBiosVfProcessorEnergyConfigurationVpEnergyPerformance,
       "cfprBiosVfProcessorEnergyConfigurationVpPowerTechnology": cfprBiosVfProcessorEnergyConfigurationVpPowerTechnology,
       "cfprBiosVfProcessorEnergyConfigurationSupportedByDefault": cfprBiosVfProcessorEnergyConfigurationSupportedByDefault,
       "cfprBiosVfProcessorPrefetchConfigTable": cfprBiosVfProcessorPrefetchConfigTable,
       "cfprBiosVfProcessorPrefetchConfigEntry": cfprBiosVfProcessorPrefetchConfigEntry,
       "cfprBiosVfProcessorPrefetchConfigInstanceId": cfprBiosVfProcessorPrefetchConfigInstanceId,
       "cfprBiosVfProcessorPrefetchConfigDn": cfprBiosVfProcessorPrefetchConfigDn,
       "cfprBiosVfProcessorPrefetchConfigRn": cfprBiosVfProcessorPrefetchConfigRn,
       "cfprBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher": cfprBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher,
       "cfprBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher": cfprBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher,
       "cfprBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch": cfprBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch,
       "cfprBiosVfProcessorPrefetchConfigVpHardwarePrefetcher": cfprBiosVfProcessorPrefetchConfigVpHardwarePrefetcher,
       "cfprBiosVfProcessorPrefetchConfigSupportedByDefault": cfprBiosVfProcessorPrefetchConfigSupportedByDefault,
       "cfprBiosVfQPILinkFrequencySelectTable": cfprBiosVfQPILinkFrequencySelectTable,
       "cfprBiosVfQPILinkFrequencySelectEntry": cfprBiosVfQPILinkFrequencySelectEntry,
       "cfprBiosVfQPILinkFrequencySelectInstanceId": cfprBiosVfQPILinkFrequencySelectInstanceId,
       "cfprBiosVfQPILinkFrequencySelectDn": cfprBiosVfQPILinkFrequencySelectDn,
       "cfprBiosVfQPILinkFrequencySelectRn": cfprBiosVfQPILinkFrequencySelectRn,
       "cfprBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect": cfprBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect,
       "cfprBiosVfQPILinkFrequencySelectSupportedByDefault": cfprBiosVfQPILinkFrequencySelectSupportedByDefault,
       "cfprBiosVfQuietBootTable": cfprBiosVfQuietBootTable,
       "cfprBiosVfQuietBootEntry": cfprBiosVfQuietBootEntry,
       "cfprBiosVfQuietBootInstanceId": cfprBiosVfQuietBootInstanceId,
       "cfprBiosVfQuietBootDn": cfprBiosVfQuietBootDn,
       "cfprBiosVfQuietBootRn": cfprBiosVfQuietBootRn,
       "cfprBiosVfQuietBootVpQuietBoot": cfprBiosVfQuietBootVpQuietBoot,
       "cfprBiosVfQuietBootSupportedByDefault": cfprBiosVfQuietBootSupportedByDefault,
       "cfprBiosVfResumeOnACPowerLossTable": cfprBiosVfResumeOnACPowerLossTable,
       "cfprBiosVfResumeOnACPowerLossEntry": cfprBiosVfResumeOnACPowerLossEntry,
       "cfprBiosVfResumeOnACPowerLossInstanceId": cfprBiosVfResumeOnACPowerLossInstanceId,
       "cfprBiosVfResumeOnACPowerLossDn": cfprBiosVfResumeOnACPowerLossDn,
       "cfprBiosVfResumeOnACPowerLossRn": cfprBiosVfResumeOnACPowerLossRn,
       "cfprBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss": cfprBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss,
       "cfprBiosVfResumeOnACPowerLossSupportedByDefault": cfprBiosVfResumeOnACPowerLossSupportedByDefault,
       "cfprBiosVfScrubPoliciesTable": cfprBiosVfScrubPoliciesTable,
       "cfprBiosVfScrubPoliciesEntry": cfprBiosVfScrubPoliciesEntry,
       "cfprBiosVfScrubPoliciesInstanceId": cfprBiosVfScrubPoliciesInstanceId,
       "cfprBiosVfScrubPoliciesDn": cfprBiosVfScrubPoliciesDn,
       "cfprBiosVfScrubPoliciesRn": cfprBiosVfScrubPoliciesRn,
       "cfprBiosVfScrubPoliciesVpDemandScrub": cfprBiosVfScrubPoliciesVpDemandScrub,
       "cfprBiosVfScrubPoliciesVpPatrolScrub": cfprBiosVfScrubPoliciesVpPatrolScrub,
       "cfprBiosVfScrubPoliciesSupportedByDefault": cfprBiosVfScrubPoliciesSupportedByDefault,
       "cfprBiosVfSelectMemoryRASConfigurationTable": cfprBiosVfSelectMemoryRASConfigurationTable,
       "cfprBiosVfSelectMemoryRASConfigurationEntry": cfprBiosVfSelectMemoryRASConfigurationEntry,
       "cfprBiosVfSelectMemoryRASConfigurationInstanceId": cfprBiosVfSelectMemoryRASConfigurationInstanceId,
       "cfprBiosVfSelectMemoryRASConfigurationDn": cfprBiosVfSelectMemoryRASConfigurationDn,
       "cfprBiosVfSelectMemoryRASConfigurationRn": cfprBiosVfSelectMemoryRASConfigurationRn,
       "cfprBiosVfSelectMemoryRASConfigurationVpSelectMemoryRASConfiguration": cfprBiosVfSelectMemoryRASConfigurationVpSelectMemoryRASConfiguration,
       "cfprBiosVfSelectMemoryRASConfigurationSupportedByDefault": cfprBiosVfSelectMemoryRASConfigurationSupportedByDefault,
       "cfprBiosVfSerialPortAEnableTable": cfprBiosVfSerialPortAEnableTable,
       "cfprBiosVfSerialPortAEnableEntry": cfprBiosVfSerialPortAEnableEntry,
       "cfprBiosVfSerialPortAEnableInstanceId": cfprBiosVfSerialPortAEnableInstanceId,
       "cfprBiosVfSerialPortAEnableDn": cfprBiosVfSerialPortAEnableDn,
       "cfprBiosVfSerialPortAEnableRn": cfprBiosVfSerialPortAEnableRn,
       "cfprBiosVfSerialPortAEnableVpSerialPortAEnable": cfprBiosVfSerialPortAEnableVpSerialPortAEnable,
       "cfprBiosVfSerialPortAEnableSupportedByDefault": cfprBiosVfSerialPortAEnableSupportedByDefault,
       "cfprBiosVfSparingModeTable": cfprBiosVfSparingModeTable,
       "cfprBiosVfSparingModeEntry": cfprBiosVfSparingModeEntry,
       "cfprBiosVfSparingModeInstanceId": cfprBiosVfSparingModeInstanceId,
       "cfprBiosVfSparingModeDn": cfprBiosVfSparingModeDn,
       "cfprBiosVfSparingModeRn": cfprBiosVfSparingModeRn,
       "cfprBiosVfSparingModeVpSparingMode": cfprBiosVfSparingModeVpSparingMode,
       "cfprBiosVfSparingModeSupportedByDefault": cfprBiosVfSparingModeSupportedByDefault,
       "cfprBiosVfSriovConfigTable": cfprBiosVfSriovConfigTable,
       "cfprBiosVfSriovConfigEntry": cfprBiosVfSriovConfigEntry,
       "cfprBiosVfSriovConfigInstanceId": cfprBiosVfSriovConfigInstanceId,
       "cfprBiosVfSriovConfigDn": cfprBiosVfSriovConfigDn,
       "cfprBiosVfSriovConfigRn": cfprBiosVfSriovConfigRn,
       "cfprBiosVfSriovConfigVpSriov": cfprBiosVfSriovConfigVpSriov,
       "cfprBiosVfSriovConfigSupportedByDefault": cfprBiosVfSriovConfigSupportedByDefault,
       "cfprBiosVfTPMSupportTable": cfprBiosVfTPMSupportTable,
       "cfprBiosVfTPMSupportEntry": cfprBiosVfTPMSupportEntry,
       "cfprBiosVfTPMSupportInstanceId": cfprBiosVfTPMSupportInstanceId,
       "cfprBiosVfTPMSupportDn": cfprBiosVfTPMSupportDn,
       "cfprBiosVfTPMSupportRn": cfprBiosVfTPMSupportRn,
       "cfprBiosVfTPMSupportVpTPMSupport": cfprBiosVfTPMSupportVpTPMSupport,
       "cfprBiosVfTPMSupportSupportedByDefault": cfprBiosVfTPMSupportSupportedByDefault,
       "cfprBiosVfFPRMBootModeControlTable": cfprBiosVfFPRMBootModeControlTable,
       "cfprBiosVfFPRMBootModeControlEntry": cfprBiosVfFPRMBootModeControlEntry,
       "cfprBiosVfFPRMBootModeControlInstanceId": cfprBiosVfFPRMBootModeControlInstanceId,
       "cfprBiosVfFPRMBootModeControlDn": cfprBiosVfFPRMBootModeControlDn,
       "cfprBiosVfFPRMBootModeControlRn": cfprBiosVfFPRMBootModeControlRn,
       "cfprBiosVfFPRMBootModeControlVpUEFIBootMode": cfprBiosVfFPRMBootModeControlVpUEFIBootMode,
       "cfprBiosVfFPRMBootModeControlSupportedByDefault": cfprBiosVfFPRMBootModeControlSupportedByDefault,
       "cfprBiosVfFPRMBootOrderRuleControlTable": cfprBiosVfFPRMBootOrderRuleControlTable,
       "cfprBiosVfFPRMBootOrderRuleControlEntry": cfprBiosVfFPRMBootOrderRuleControlEntry,
       "cfprBiosVfFPRMBootOrderRuleControlInstanceId": cfprBiosVfFPRMBootOrderRuleControlInstanceId,
       "cfprBiosVfFPRMBootOrderRuleControlDn": cfprBiosVfFPRMBootOrderRuleControlDn,
       "cfprBiosVfFPRMBootOrderRuleControlRn": cfprBiosVfFPRMBootOrderRuleControlRn,
       "cfprBiosVfFPRMBootOrderRuleControlVpFPRMBootOrderRule": cfprBiosVfFPRMBootOrderRuleControlVpFPRMBootOrderRule,
       "cfprBiosVfFPRMBootOrderRuleControlSupportedByDefault": cfprBiosVfFPRMBootOrderRuleControlSupportedByDefault,
       "cfprBiosVfUEFIOSUseLegacyVideoTable": cfprBiosVfUEFIOSUseLegacyVideoTable,
       "cfprBiosVfUEFIOSUseLegacyVideoEntry": cfprBiosVfUEFIOSUseLegacyVideoEntry,
       "cfprBiosVfUEFIOSUseLegacyVideoInstanceId": cfprBiosVfUEFIOSUseLegacyVideoInstanceId,
       "cfprBiosVfUEFIOSUseLegacyVideoDn": cfprBiosVfUEFIOSUseLegacyVideoDn,
       "cfprBiosVfUEFIOSUseLegacyVideoRn": cfprBiosVfUEFIOSUseLegacyVideoRn,
       "cfprBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo": cfprBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo,
       "cfprBiosVfUEFIOSUseLegacyVideoSupportedByDefault": cfprBiosVfUEFIOSUseLegacyVideoSupportedByDefault,
       "cfprBiosVfUSBBootConfigTable": cfprBiosVfUSBBootConfigTable,
       "cfprBiosVfUSBBootConfigEntry": cfprBiosVfUSBBootConfigEntry,
       "cfprBiosVfUSBBootConfigInstanceId": cfprBiosVfUSBBootConfigInstanceId,
       "cfprBiosVfUSBBootConfigDn": cfprBiosVfUSBBootConfigDn,
       "cfprBiosVfUSBBootConfigRn": cfprBiosVfUSBBootConfigRn,
       "cfprBiosVfUSBBootConfigVpLegacyUSBSupport": cfprBiosVfUSBBootConfigVpLegacyUSBSupport,
       "cfprBiosVfUSBBootConfigVpMakeDeviceNonBootable": cfprBiosVfUSBBootConfigVpMakeDeviceNonBootable,
       "cfprBiosVfUSBBootConfigSupportedByDefault": cfprBiosVfUSBBootConfigSupportedByDefault,
       "cfprBiosVfUSBConfigurationTable": cfprBiosVfUSBConfigurationTable,
       "cfprBiosVfUSBConfigurationEntry": cfprBiosVfUSBConfigurationEntry,
       "cfprBiosVfUSBConfigurationInstanceId": cfprBiosVfUSBConfigurationInstanceId,
       "cfprBiosVfUSBConfigurationDn": cfprBiosVfUSBConfigurationDn,
       "cfprBiosVfUSBConfigurationRn": cfprBiosVfUSBConfigurationRn,
       "cfprBiosVfUSBConfigurationVpLegacyUSBSupport": cfprBiosVfUSBConfigurationVpLegacyUSBSupport,
       "cfprBiosVfUSBConfigurationVpXHCIMode": cfprBiosVfUSBConfigurationVpXHCIMode,
       "cfprBiosVfUSBConfigurationSupportedByDefault": cfprBiosVfUSBConfigurationSupportedByDefault,
       "cfprBiosVfUSBFrontPanelAccessLockTable": cfprBiosVfUSBFrontPanelAccessLockTable,
       "cfprBiosVfUSBFrontPanelAccessLockEntry": cfprBiosVfUSBFrontPanelAccessLockEntry,
       "cfprBiosVfUSBFrontPanelAccessLockInstanceId": cfprBiosVfUSBFrontPanelAccessLockInstanceId,
       "cfprBiosVfUSBFrontPanelAccessLockDn": cfprBiosVfUSBFrontPanelAccessLockDn,
       "cfprBiosVfUSBFrontPanelAccessLockRn": cfprBiosVfUSBFrontPanelAccessLockRn,
       "cfprBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock": cfprBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock,
       "cfprBiosVfUSBFrontPanelAccessLockSupportedByDefault": cfprBiosVfUSBFrontPanelAccessLockSupportedByDefault,
       "cfprBiosVfUSBPortConfigurationTable": cfprBiosVfUSBPortConfigurationTable,
       "cfprBiosVfUSBPortConfigurationEntry": cfprBiosVfUSBPortConfigurationEntry,
       "cfprBiosVfUSBPortConfigurationInstanceId": cfprBiosVfUSBPortConfigurationInstanceId,
       "cfprBiosVfUSBPortConfigurationDn": cfprBiosVfUSBPortConfigurationDn,
       "cfprBiosVfUSBPortConfigurationRn": cfprBiosVfUSBPortConfigurationRn,
       "cfprBiosVfUSBPortConfigurationVpPort6064Emulation": cfprBiosVfUSBPortConfigurationVpPort6064Emulation,
       "cfprBiosVfUSBPortConfigurationVpUSBPortFront": cfprBiosVfUSBPortConfigurationVpUSBPortFront,
       "cfprBiosVfUSBPortConfigurationVpUSBPortInternal": cfprBiosVfUSBPortConfigurationVpUSBPortInternal,
       "cfprBiosVfUSBPortConfigurationVpUSBPortKVM": cfprBiosVfUSBPortConfigurationVpUSBPortKVM,
       "cfprBiosVfUSBPortConfigurationVpUSBPortRear": cfprBiosVfUSBPortConfigurationVpUSBPortRear,
       "cfprBiosVfUSBPortConfigurationVpUSBPortSDCard": cfprBiosVfUSBPortConfigurationVpUSBPortSDCard,
       "cfprBiosVfUSBPortConfigurationVpUSBPortVMedia": cfprBiosVfUSBPortConfigurationVpUSBPortVMedia,
       "cfprBiosVfUSBPortConfigurationSupportedByDefault": cfprBiosVfUSBPortConfigurationSupportedByDefault,
       "cfprBiosVfUSBSystemIdlePowerOptimizingSettingTable": cfprBiosVfUSBSystemIdlePowerOptimizingSettingTable,
       "cfprBiosVfUSBSystemIdlePowerOptimizingSettingEntry": cfprBiosVfUSBSystemIdlePowerOptimizingSettingEntry,
       "cfprBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId": cfprBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId,
       "cfprBiosVfUSBSystemIdlePowerOptimizingSettingDn": cfprBiosVfUSBSystemIdlePowerOptimizingSettingDn,
       "cfprBiosVfUSBSystemIdlePowerOptimizingSettingRn": cfprBiosVfUSBSystemIdlePowerOptimizingSettingRn,
       "cfprBiosVfUSBSystemIdlePowerOptimizingSettingVpUSBIdlePowerOptimizing": cfprBiosVfUSBSystemIdlePowerOptimizingSettingVpUSBIdlePowerOptimizing,
       "cfprBiosVfUSBSystemIdlePowerOptimizingSettingSupportedByDefault": cfprBiosVfUSBSystemIdlePowerOptimizingSettingSupportedByDefault,
       "cfprBiosVfVGAPriorityTable": cfprBiosVfVGAPriorityTable,
       "cfprBiosVfVGAPriorityEntry": cfprBiosVfVGAPriorityEntry,
       "cfprBiosVfVGAPriorityInstanceId": cfprBiosVfVGAPriorityInstanceId,
       "cfprBiosVfVGAPriorityDn": cfprBiosVfVGAPriorityDn,
       "cfprBiosVfVGAPriorityRn": cfprBiosVfVGAPriorityRn,
       "cfprBiosVfVGAPriorityVpVGAPriority": cfprBiosVfVGAPriorityVpVGAPriority,
       "cfprBiosVfVGAPrioritySupportedByDefault": cfprBiosVfVGAPrioritySupportedByDefault,
       "cfprBiosTokenFeatureGroupTable": cfprBiosTokenFeatureGroupTable,
       "cfprBiosTokenFeatureGroupEntry": cfprBiosTokenFeatureGroupEntry,
       "cfprBiosTokenFeatureGroupInstanceId": cfprBiosTokenFeatureGroupInstanceId,
       "cfprBiosTokenFeatureGroupDn": cfprBiosTokenFeatureGroupDn,
       "cfprBiosTokenFeatureGroupRn": cfprBiosTokenFeatureGroupRn,
       "cfprBiosTokenFeatureGroupName": cfprBiosTokenFeatureGroupName,
       "cfprBiosTokenFeatureGroupSupportedByDefault": cfprBiosTokenFeatureGroupSupportedByDefault,
       "cfprBiosTokenParamTable": cfprBiosTokenParamTable,
       "cfprBiosTokenParamEntry": cfprBiosTokenParamEntry,
       "cfprBiosTokenParamInstanceId": cfprBiosTokenParamInstanceId,
       "cfprBiosTokenParamDn": cfprBiosTokenParamDn,
       "cfprBiosTokenParamRn": cfprBiosTokenParamRn,
       "cfprBiosTokenParamLegacyPropId": cfprBiosTokenParamLegacyPropId,
       "cfprBiosTokenParamParamName": cfprBiosTokenParamParamName,
       "cfprBiosTokenParamTargetTokenName": cfprBiosTokenParamTargetTokenName,
       "cfprBiosTokenParamUiGroupName": cfprBiosTokenParamUiGroupName,
       "cfprBiosTokenSettingsTable": cfprBiosTokenSettingsTable,
       "cfprBiosTokenSettingsEntry": cfprBiosTokenSettingsEntry,
       "cfprBiosTokenSettingsInstanceId": cfprBiosTokenSettingsInstanceId,
       "cfprBiosTokenSettingsDn": cfprBiosTokenSettingsDn,
       "cfprBiosTokenSettingsRn": cfprBiosTokenSettingsRn,
       "cfprBiosTokenSettingsBiosRetSettingName": cfprBiosTokenSettingsBiosRetSettingName,
       "cfprBiosTokenSettingsIsAssigned": cfprBiosTokenSettingsIsAssigned,
       "cfprBiosTokenSettingsLegacyPropVal": cfprBiosTokenSettingsLegacyPropVal,
       "cfprBiosTokenSettingsSettingsMoRn": cfprBiosTokenSettingsSettingsMoRn,
       "cfprBiosTokenSettingsTargetTokenValue": cfprBiosTokenSettingsTargetTokenValue}
)
