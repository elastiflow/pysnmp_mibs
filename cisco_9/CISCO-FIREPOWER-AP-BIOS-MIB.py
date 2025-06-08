# SNMP MIB module (CISCO-FIREPOWER-AP-BIOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-BIOS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:15:13 2025
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

(CfprApManagedObjectDn,
 CfprApManagedObjectId,
 ciscoFirepowerApMIBObjects) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-MIB",
    "CfprApManagedObjectDn",
    "CfprApManagedObjectId",
    "ciscoFirepowerApMIBObjects")

(CfprApBiosBootDevErrorCode,
 CfprApBiosBootDevGrpType,
 CfprApBiosBootDevOrder,
 CfprApBiosDefaultAction,
 CfprApBiosSupportedAction,
 CfprApBiosVfACPI10SupportVpACPI10Support,
 CfprApBiosVfAllUSBDevicesVpAllUSBDevices,
 CfprApBiosVfAltitudeVpAltitude,
 CfprApBiosVfAssertNMIOnPERRVpAssertNMIOnPERR,
 CfprApBiosVfAssertNMIOnSERRVpAssertNMIOnSERR,
 CfprApBiosVfBootOptionRetryVpBootOptionRetry,
 CfprApBiosVfCPUPerformanceVpCPUPerformance,
 CfprApBiosVfConsoleRedirectionVpBaudRate,
 CfprApBiosVfConsoleRedirectionVpConsoleRedirection,
 CfprApBiosVfConsoleRedirectionVpFlowControl,
 CfprApBiosVfConsoleRedirectionVpLegacyOSRedirection,
 CfprApBiosVfConsoleRedirectionVpPuttyKeyPad,
 CfprApBiosVfConsoleRedirectionVpTerminalType,
 CfprApBiosVfCoreMultiProcessingVpCoreMultiProcessing,
 CfprApBiosVfDRAMClockThrottlingVpDRAMClockThrottling,
 CfprApBiosVfDirectCacheAccessVpDirectCacheAccess,
 CfprApBiosVfDramRefreshRateVpDramRefreshRate,
 CfprApBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech,
 CfprApBiosVfExecuteDisableBitVpExecuteDisableBit,
 CfprApBiosVfFRB2TimerVpFRB2Timer,
 CfprApBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride,
 CfprApBiosVfFrontPanelLockoutVpFrontPanelLockout,
 CfprApBiosVfIntelEntrySASRAIDModuleVpSASRAID,
 CfprApBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule,
 CfprApBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech,
 CfprApBiosVfIntelTurboBoostTechVpIntelTurboBoostTech,
 CfprApBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport,
 CfprApBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport,
 CfprApBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping,
 CfprApBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport,
 CfprApBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO,
 CfprApBiosVfIntelVirtualizationTechnologyVpIntelVirtTechnology,
 CfprApBiosVfInterleaveConfigurationVpChannelInterleaving,
 CfprApBiosVfInterleaveConfigurationVpMemoryInterleaving,
 CfprApBiosVfInterleaveConfigurationVpRankInterleaving,
 CfprApBiosVfLocalX2ApicVpLocalX2Apic,
 CfprApBiosVfLvDIMMSupportVpLvDDRMode,
 CfprApBiosVfMaxVariableMTRRSettingVpProcessorMtrr,
 CfprApBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB,
 CfprApBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB,
 CfprApBiosVfMirroringModeVpMirroringMode,
 CfprApBiosVfNUMAOptimizedVpNUMAOptimized,
 CfprApBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy,
 CfprApBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout,
 CfprApBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer,
 CfprApBiosVfOnboardSATAControllerVpOnboardSATAController,
 CfprApBiosVfOnboardSATAControllerVpSATAMode,
 CfprApBiosVfOnboardStorageVpOnboardSCUStorageSupport,
 CfprApBiosVfOptionROMEnableVpState,
 CfprApBiosVfOptionROMLoadVpLoad,
 CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed,
 CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed,
 CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed,
 CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed,
 CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed,
 CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed,
 CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed,
 CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed,
 CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed,
 CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed,
 CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM,
 CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM,
 CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM,
 CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM,
 CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM,
 CfprApBiosVfPCISlotOptionROMEnableVpSlot10State,
 CfprApBiosVfPCISlotOptionROMEnableVpSlot1State,
 CfprApBiosVfPCISlotOptionROMEnableVpSlot2State,
 CfprApBiosVfPCISlotOptionROMEnableVpSlot3State,
 CfprApBiosVfPCISlotOptionROMEnableVpSlot4State,
 CfprApBiosVfPCISlotOptionROMEnableVpSlot5State,
 CfprApBiosVfPCISlotOptionROMEnableVpSlot6State,
 CfprApBiosVfPCISlotOptionROMEnableVpSlot7State,
 CfprApBiosVfPCISlotOptionROMEnableVpSlot8State,
 CfprApBiosVfPCISlotOptionROMEnableVpSlot9State,
 CfprApBiosVfPCISlotOptionROMEnableVpSlotMezzState,
 CfprApBiosVfPOSTErrorPauseVpPOSTErrorPause,
 CfprApBiosVfPSTATECoordinationVpPSTATECoordination,
 CfprApBiosVfPackageCStateLimitVpPackageCStateLimit,
 CfprApBiosVfProcessorC1EVpProcessorC1E,
 CfprApBiosVfProcessorC3ReportVpProcessorC3Report,
 CfprApBiosVfProcessorC6ReportVpProcessorC6Report,
 CfprApBiosVfProcessorC7ReportVpProcessorC7Report,
 CfprApBiosVfProcessorCStateVpProcessorCState,
 CfprApBiosVfProcessorEnergyConfigurationVpEnergyPerformance,
 CfprApBiosVfProcessorEnergyConfigurationVpPowerTechnology,
 CfprApBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher,
 CfprApBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher,
 CfprApBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch,
 CfprApBiosVfProcessorPrefetchConfigVpHardwarePrefetcher,
 CfprApBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect,
 CfprApBiosVfQuietBootVpQuietBoot,
 CfprApBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss,
 CfprApBiosVfScrubPoliciesVpDemandScrub,
 CfprApBiosVfScrubPoliciesVpPatrolScrub,
 CfprApBiosVfSelectMemoryRASConfigurationVpSelectMemoryRASConf,
 CfprApBiosVfSerialPortAEnableVpSerialPortAEnable,
 CfprApBiosVfSparingModeVpSparingMode,
 CfprApBiosVfSriovConfigVpSriov,
 CfprApBiosVfTPMSupportVpTPMSupport,
 CfprApBiosVfUCSMBootModeControlVpUEFIBootMode,
 CfprApBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule,
 CfprApBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo,
 CfprApBiosVfUSBBootConfigVpLegacyUSBSupport,
 CfprApBiosVfUSBBootConfigVpMakeDeviceNonBootable,
 CfprApBiosVfUSBConfigurationVpLegacyUSBSupport,
 CfprApBiosVfUSBConfigurationVpXHCIMode,
 CfprApBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock,
 CfprApBiosVfUSBPortConfigurationVpPort6064Emulation,
 CfprApBiosVfUSBPortConfigurationVpUSBPortFront,
 CfprApBiosVfUSBPortConfigurationVpUSBPortInternal,
 CfprApBiosVfUSBPortConfigurationVpUSBPortKVM,
 CfprApBiosVfUSBPortConfigurationVpUSBPortRear,
 CfprApBiosVfUSBPortConfigurationVpUSBPortSDCard,
 CfprApBiosVfUSBPortConfigurationVpUSBPortVMedia,
 CfprApBiosVfUSBSysIdlePowerOptimizingSettingVpUSBIdlePowerOptimize,
 CfprApBiosVfVGAPriorityVpVGAPriority,
 CfprApPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApBiosBootDevErrorCode",
    "CfprApBiosBootDevGrpType",
    "CfprApBiosBootDevOrder",
    "CfprApBiosDefaultAction",
    "CfprApBiosSupportedAction",
    "CfprApBiosVfACPI10SupportVpACPI10Support",
    "CfprApBiosVfAllUSBDevicesVpAllUSBDevices",
    "CfprApBiosVfAltitudeVpAltitude",
    "CfprApBiosVfAssertNMIOnPERRVpAssertNMIOnPERR",
    "CfprApBiosVfAssertNMIOnSERRVpAssertNMIOnSERR",
    "CfprApBiosVfBootOptionRetryVpBootOptionRetry",
    "CfprApBiosVfCPUPerformanceVpCPUPerformance",
    "CfprApBiosVfConsoleRedirectionVpBaudRate",
    "CfprApBiosVfConsoleRedirectionVpConsoleRedirection",
    "CfprApBiosVfConsoleRedirectionVpFlowControl",
    "CfprApBiosVfConsoleRedirectionVpLegacyOSRedirection",
    "CfprApBiosVfConsoleRedirectionVpPuttyKeyPad",
    "CfprApBiosVfConsoleRedirectionVpTerminalType",
    "CfprApBiosVfCoreMultiProcessingVpCoreMultiProcessing",
    "CfprApBiosVfDRAMClockThrottlingVpDRAMClockThrottling",
    "CfprApBiosVfDirectCacheAccessVpDirectCacheAccess",
    "CfprApBiosVfDramRefreshRateVpDramRefreshRate",
    "CfprApBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech",
    "CfprApBiosVfExecuteDisableBitVpExecuteDisableBit",
    "CfprApBiosVfFRB2TimerVpFRB2Timer",
    "CfprApBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride",
    "CfprApBiosVfFrontPanelLockoutVpFrontPanelLockout",
    "CfprApBiosVfIntelEntrySASRAIDModuleVpSASRAID",
    "CfprApBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule",
    "CfprApBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech",
    "CfprApBiosVfIntelTurboBoostTechVpIntelTurboBoostTech",
    "CfprApBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport",
    "CfprApBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport",
    "CfprApBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping",
    "CfprApBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport",
    "CfprApBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO",
    "CfprApBiosVfIntelVirtualizationTechnologyVpIntelVirtTechnology",
    "CfprApBiosVfInterleaveConfigurationVpChannelInterleaving",
    "CfprApBiosVfInterleaveConfigurationVpMemoryInterleaving",
    "CfprApBiosVfInterleaveConfigurationVpRankInterleaving",
    "CfprApBiosVfLocalX2ApicVpLocalX2Apic",
    "CfprApBiosVfLvDIMMSupportVpLvDDRMode",
    "CfprApBiosVfMaxVariableMTRRSettingVpProcessorMtrr",
    "CfprApBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB",
    "CfprApBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB",
    "CfprApBiosVfMirroringModeVpMirroringMode",
    "CfprApBiosVfNUMAOptimizedVpNUMAOptimized",
    "CfprApBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy",
    "CfprApBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout",
    "CfprApBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer",
    "CfprApBiosVfOnboardSATAControllerVpOnboardSATAController",
    "CfprApBiosVfOnboardSATAControllerVpSATAMode",
    "CfprApBiosVfOnboardStorageVpOnboardSCUStorageSupport",
    "CfprApBiosVfOptionROMEnableVpState",
    "CfprApBiosVfOptionROMLoadVpLoad",
    "CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed",
    "CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed",
    "CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed",
    "CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed",
    "CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed",
    "CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed",
    "CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed",
    "CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed",
    "CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed",
    "CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed",
    "CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM",
    "CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM",
    "CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM",
    "CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM",
    "CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM",
    "CfprApBiosVfPCISlotOptionROMEnableVpSlot10State",
    "CfprApBiosVfPCISlotOptionROMEnableVpSlot1State",
    "CfprApBiosVfPCISlotOptionROMEnableVpSlot2State",
    "CfprApBiosVfPCISlotOptionROMEnableVpSlot3State",
    "CfprApBiosVfPCISlotOptionROMEnableVpSlot4State",
    "CfprApBiosVfPCISlotOptionROMEnableVpSlot5State",
    "CfprApBiosVfPCISlotOptionROMEnableVpSlot6State",
    "CfprApBiosVfPCISlotOptionROMEnableVpSlot7State",
    "CfprApBiosVfPCISlotOptionROMEnableVpSlot8State",
    "CfprApBiosVfPCISlotOptionROMEnableVpSlot9State",
    "CfprApBiosVfPCISlotOptionROMEnableVpSlotMezzState",
    "CfprApBiosVfPOSTErrorPauseVpPOSTErrorPause",
    "CfprApBiosVfPSTATECoordinationVpPSTATECoordination",
    "CfprApBiosVfPackageCStateLimitVpPackageCStateLimit",
    "CfprApBiosVfProcessorC1EVpProcessorC1E",
    "CfprApBiosVfProcessorC3ReportVpProcessorC3Report",
    "CfprApBiosVfProcessorC6ReportVpProcessorC6Report",
    "CfprApBiosVfProcessorC7ReportVpProcessorC7Report",
    "CfprApBiosVfProcessorCStateVpProcessorCState",
    "CfprApBiosVfProcessorEnergyConfigurationVpEnergyPerformance",
    "CfprApBiosVfProcessorEnergyConfigurationVpPowerTechnology",
    "CfprApBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher",
    "CfprApBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher",
    "CfprApBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch",
    "CfprApBiosVfProcessorPrefetchConfigVpHardwarePrefetcher",
    "CfprApBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect",
    "CfprApBiosVfQuietBootVpQuietBoot",
    "CfprApBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss",
    "CfprApBiosVfScrubPoliciesVpDemandScrub",
    "CfprApBiosVfScrubPoliciesVpPatrolScrub",
    "CfprApBiosVfSelectMemoryRASConfigurationVpSelectMemoryRASConf",
    "CfprApBiosVfSerialPortAEnableVpSerialPortAEnable",
    "CfprApBiosVfSparingModeVpSparingMode",
    "CfprApBiosVfSriovConfigVpSriov",
    "CfprApBiosVfTPMSupportVpTPMSupport",
    "CfprApBiosVfUCSMBootModeControlVpUEFIBootMode",
    "CfprApBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule",
    "CfprApBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo",
    "CfprApBiosVfUSBBootConfigVpLegacyUSBSupport",
    "CfprApBiosVfUSBBootConfigVpMakeDeviceNonBootable",
    "CfprApBiosVfUSBConfigurationVpLegacyUSBSupport",
    "CfprApBiosVfUSBConfigurationVpXHCIMode",
    "CfprApBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock",
    "CfprApBiosVfUSBPortConfigurationVpPort6064Emulation",
    "CfprApBiosVfUSBPortConfigurationVpUSBPortFront",
    "CfprApBiosVfUSBPortConfigurationVpUSBPortInternal",
    "CfprApBiosVfUSBPortConfigurationVpUSBPortKVM",
    "CfprApBiosVfUSBPortConfigurationVpUSBPortRear",
    "CfprApBiosVfUSBPortConfigurationVpUSBPortSDCard",
    "CfprApBiosVfUSBPortConfigurationVpUSBPortVMedia",
    "CfprApBiosVfUSBSysIdlePowerOptimizingSettingVpUSBIdlePowerOptimize",
    "CfprApBiosVfVGAPriorityVpVGAPriority",
    "CfprApPolicyPolicyOwner")

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

cfprApBiosObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApBiosBOTTable_Object = MibTable
cfprApBiosBOTTable = _CfprApBiosBOTTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cfprApBiosBOTTable.setStatus("current")
_CfprApBiosBOTEntry_Object = MibTableRow
cfprApBiosBOTEntry = _CfprApBiosBOTEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 1, 1)
)
cfprApBiosBOTEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosBOTInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosBOTEntry.setStatus("current")
_CfprApBiosBOTInstanceId_Type = CfprApManagedObjectId
_CfprApBiosBOTInstanceId_Object = MibTableColumn
cfprApBiosBOTInstanceId = _CfprApBiosBOTInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 1, 1, 1),
    _CfprApBiosBOTInstanceId_Type()
)
cfprApBiosBOTInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosBOTInstanceId.setStatus("current")
_CfprApBiosBOTDn_Type = CfprApManagedObjectDn
_CfprApBiosBOTDn_Object = MibTableColumn
cfprApBiosBOTDn = _CfprApBiosBOTDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 1, 1, 2),
    _CfprApBiosBOTDn_Type()
)
cfprApBiosBOTDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosBOTDn.setStatus("current")
_CfprApBiosBOTRn_Type = SnmpAdminString
_CfprApBiosBOTRn_Object = MibTableColumn
cfprApBiosBOTRn = _CfprApBiosBOTRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 1, 1, 3),
    _CfprApBiosBOTRn_Type()
)
cfprApBiosBOTRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosBOTRn.setStatus("current")
_CfprApBiosBOTLastUpdate_Type = DateAndTime
_CfprApBiosBOTLastUpdate_Object = MibTableColumn
cfprApBiosBOTLastUpdate = _CfprApBiosBOTLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 1, 1, 4),
    _CfprApBiosBOTLastUpdate_Type()
)
cfprApBiosBOTLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosBOTLastUpdate.setStatus("current")
_CfprApBiosBootDevTable_Object = MibTable
cfprApBiosBootDevTable = _CfprApBiosBootDevTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cfprApBiosBootDevTable.setStatus("current")
_CfprApBiosBootDevEntry_Object = MibTableRow
cfprApBiosBootDevEntry = _CfprApBiosBootDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 2, 1)
)
cfprApBiosBootDevEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosBootDevInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosBootDevEntry.setStatus("current")
_CfprApBiosBootDevInstanceId_Type = CfprApManagedObjectId
_CfprApBiosBootDevInstanceId_Object = MibTableColumn
cfprApBiosBootDevInstanceId = _CfprApBiosBootDevInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 2, 1, 1),
    _CfprApBiosBootDevInstanceId_Type()
)
cfprApBiosBootDevInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosBootDevInstanceId.setStatus("current")
_CfprApBiosBootDevDn_Type = CfprApManagedObjectDn
_CfprApBiosBootDevDn_Object = MibTableColumn
cfprApBiosBootDevDn = _CfprApBiosBootDevDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 2, 1, 2),
    _CfprApBiosBootDevDn_Type()
)
cfprApBiosBootDevDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosBootDevDn.setStatus("current")
_CfprApBiosBootDevRn_Type = SnmpAdminString
_CfprApBiosBootDevRn_Object = MibTableColumn
cfprApBiosBootDevRn = _CfprApBiosBootDevRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 2, 1, 3),
    _CfprApBiosBootDevRn_Type()
)
cfprApBiosBootDevRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosBootDevRn.setStatus("current")
_CfprApBiosBootDevDescr_Type = SnmpAdminString
_CfprApBiosBootDevDescr_Object = MibTableColumn
cfprApBiosBootDevDescr = _CfprApBiosBootDevDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 2, 1, 4),
    _CfprApBiosBootDevDescr_Type()
)
cfprApBiosBootDevDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosBootDevDescr.setStatus("current")
_CfprApBiosBootDevDeviceName_Type = SnmpAdminString
_CfprApBiosBootDevDeviceName_Object = MibTableColumn
cfprApBiosBootDevDeviceName = _CfprApBiosBootDevDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 2, 1, 5),
    _CfprApBiosBootDevDeviceName_Type()
)
cfprApBiosBootDevDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosBootDevDeviceName.setStatus("current")
_CfprApBiosBootDevErrValue_Type = CfprApBiosBootDevErrorCode
_CfprApBiosBootDevErrValue_Object = MibTableColumn
cfprApBiosBootDevErrValue = _CfprApBiosBootDevErrValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 2, 1, 6),
    _CfprApBiosBootDevErrValue_Type()
)
cfprApBiosBootDevErrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosBootDevErrValue.setStatus("current")
_CfprApBiosBootDevOrder_Type = CfprApBiosBootDevOrder
_CfprApBiosBootDevOrder_Object = MibTableColumn
cfprApBiosBootDevOrder = _CfprApBiosBootDevOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 2, 1, 7),
    _CfprApBiosBootDevOrder_Type()
)
cfprApBiosBootDevOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosBootDevOrder.setStatus("current")
_CfprApBiosBootDevGrpTable_Object = MibTable
cfprApBiosBootDevGrpTable = _CfprApBiosBootDevGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 3)
)
if mibBuilder.loadTexts:
    cfprApBiosBootDevGrpTable.setStatus("current")
_CfprApBiosBootDevGrpEntry_Object = MibTableRow
cfprApBiosBootDevGrpEntry = _CfprApBiosBootDevGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 3, 1)
)
cfprApBiosBootDevGrpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosBootDevGrpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosBootDevGrpEntry.setStatus("current")
_CfprApBiosBootDevGrpInstanceId_Type = CfprApManagedObjectId
_CfprApBiosBootDevGrpInstanceId_Object = MibTableColumn
cfprApBiosBootDevGrpInstanceId = _CfprApBiosBootDevGrpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 3, 1, 1),
    _CfprApBiosBootDevGrpInstanceId_Type()
)
cfprApBiosBootDevGrpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosBootDevGrpInstanceId.setStatus("current")
_CfprApBiosBootDevGrpDn_Type = CfprApManagedObjectDn
_CfprApBiosBootDevGrpDn_Object = MibTableColumn
cfprApBiosBootDevGrpDn = _CfprApBiosBootDevGrpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 3, 1, 2),
    _CfprApBiosBootDevGrpDn_Type()
)
cfprApBiosBootDevGrpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosBootDevGrpDn.setStatus("current")
_CfprApBiosBootDevGrpRn_Type = SnmpAdminString
_CfprApBiosBootDevGrpRn_Object = MibTableColumn
cfprApBiosBootDevGrpRn = _CfprApBiosBootDevGrpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 3, 1, 3),
    _CfprApBiosBootDevGrpRn_Type()
)
cfprApBiosBootDevGrpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosBootDevGrpRn.setStatus("current")
_CfprApBiosBootDevGrpDescr_Type = SnmpAdminString
_CfprApBiosBootDevGrpDescr_Object = MibTableColumn
cfprApBiosBootDevGrpDescr = _CfprApBiosBootDevGrpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 3, 1, 4),
    _CfprApBiosBootDevGrpDescr_Type()
)
cfprApBiosBootDevGrpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosBootDevGrpDescr.setStatus("current")
_CfprApBiosBootDevGrpDeviceName_Type = SnmpAdminString
_CfprApBiosBootDevGrpDeviceName_Object = MibTableColumn
cfprApBiosBootDevGrpDeviceName = _CfprApBiosBootDevGrpDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 3, 1, 5),
    _CfprApBiosBootDevGrpDeviceName_Type()
)
cfprApBiosBootDevGrpDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosBootDevGrpDeviceName.setStatus("current")
_CfprApBiosBootDevGrpErrVal_Type = CfprApBiosBootDevErrorCode
_CfprApBiosBootDevGrpErrVal_Object = MibTableColumn
cfprApBiosBootDevGrpErrVal = _CfprApBiosBootDevGrpErrVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 3, 1, 6),
    _CfprApBiosBootDevGrpErrVal_Type()
)
cfprApBiosBootDevGrpErrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosBootDevGrpErrVal.setStatus("current")
_CfprApBiosBootDevGrpOrder_Type = CfprApBiosBootDevOrder
_CfprApBiosBootDevGrpOrder_Object = MibTableColumn
cfprApBiosBootDevGrpOrder = _CfprApBiosBootDevGrpOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 3, 1, 7),
    _CfprApBiosBootDevGrpOrder_Type()
)
cfprApBiosBootDevGrpOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosBootDevGrpOrder.setStatus("current")
_CfprApBiosBootDevGrpType_Type = CfprApBiosBootDevGrpType
_CfprApBiosBootDevGrpType_Object = MibTableColumn
cfprApBiosBootDevGrpType = _CfprApBiosBootDevGrpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 3, 1, 8),
    _CfprApBiosBootDevGrpType_Type()
)
cfprApBiosBootDevGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosBootDevGrpType.setStatus("current")
_CfprApBiosFeatureRefTable_Object = MibTable
cfprApBiosFeatureRefTable = _CfprApBiosFeatureRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 4)
)
if mibBuilder.loadTexts:
    cfprApBiosFeatureRefTable.setStatus("current")
_CfprApBiosFeatureRefEntry_Object = MibTableRow
cfprApBiosFeatureRefEntry = _CfprApBiosFeatureRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 4, 1)
)
cfprApBiosFeatureRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosFeatureRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosFeatureRefEntry.setStatus("current")
_CfprApBiosFeatureRefInstanceId_Type = CfprApManagedObjectId
_CfprApBiosFeatureRefInstanceId_Object = MibTableColumn
cfprApBiosFeatureRefInstanceId = _CfprApBiosFeatureRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 4, 1, 1),
    _CfprApBiosFeatureRefInstanceId_Type()
)
cfprApBiosFeatureRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosFeatureRefInstanceId.setStatus("current")
_CfprApBiosFeatureRefDn_Type = CfprApManagedObjectDn
_CfprApBiosFeatureRefDn_Object = MibTableColumn
cfprApBiosFeatureRefDn = _CfprApBiosFeatureRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 4, 1, 2),
    _CfprApBiosFeatureRefDn_Type()
)
cfprApBiosFeatureRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosFeatureRefDn.setStatus("current")
_CfprApBiosFeatureRefRn_Type = SnmpAdminString
_CfprApBiosFeatureRefRn_Object = MibTableColumn
cfprApBiosFeatureRefRn = _CfprApBiosFeatureRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 4, 1, 3),
    _CfprApBiosFeatureRefRn_Type()
)
cfprApBiosFeatureRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosFeatureRefRn.setStatus("current")
_CfprApBiosFeatureRefFtrMoClassName_Type = SnmpAdminString
_CfprApBiosFeatureRefFtrMoClassName_Object = MibTableColumn
cfprApBiosFeatureRefFtrMoClassName = _CfprApBiosFeatureRefFtrMoClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 4, 1, 4),
    _CfprApBiosFeatureRefFtrMoClassName_Type()
)
cfprApBiosFeatureRefFtrMoClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosFeatureRefFtrMoClassName.setStatus("current")
_CfprApBiosFeatureRefIsSupported_Type = CfprApBiosSupportedAction
_CfprApBiosFeatureRefIsSupported_Object = MibTableColumn
cfprApBiosFeatureRefIsSupported = _CfprApBiosFeatureRefIsSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 4, 1, 5),
    _CfprApBiosFeatureRefIsSupported_Type()
)
cfprApBiosFeatureRefIsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosFeatureRefIsSupported.setStatus("current")
_CfprApBiosFeatureRefName_Type = SnmpAdminString
_CfprApBiosFeatureRefName_Object = MibTableColumn
cfprApBiosFeatureRefName = _CfprApBiosFeatureRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 4, 1, 6),
    _CfprApBiosFeatureRefName_Type()
)
cfprApBiosFeatureRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosFeatureRefName.setStatus("current")
_CfprApBiosParameterRefTable_Object = MibTable
cfprApBiosParameterRefTable = _CfprApBiosParameterRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 5)
)
if mibBuilder.loadTexts:
    cfprApBiosParameterRefTable.setStatus("current")
_CfprApBiosParameterRefEntry_Object = MibTableRow
cfprApBiosParameterRefEntry = _CfprApBiosParameterRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 5, 1)
)
cfprApBiosParameterRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosParameterRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosParameterRefEntry.setStatus("current")
_CfprApBiosParameterRefInstanceId_Type = CfprApManagedObjectId
_CfprApBiosParameterRefInstanceId_Object = MibTableColumn
cfprApBiosParameterRefInstanceId = _CfprApBiosParameterRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 5, 1, 1),
    _CfprApBiosParameterRefInstanceId_Type()
)
cfprApBiosParameterRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosParameterRefInstanceId.setStatus("current")
_CfprApBiosParameterRefDn_Type = CfprApManagedObjectDn
_CfprApBiosParameterRefDn_Object = MibTableColumn
cfprApBiosParameterRefDn = _CfprApBiosParameterRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 5, 1, 2),
    _CfprApBiosParameterRefDn_Type()
)
cfprApBiosParameterRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosParameterRefDn.setStatus("current")
_CfprApBiosParameterRefRn_Type = SnmpAdminString
_CfprApBiosParameterRefRn_Object = MibTableColumn
cfprApBiosParameterRefRn = _CfprApBiosParameterRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 5, 1, 3),
    _CfprApBiosParameterRefRn_Type()
)
cfprApBiosParameterRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosParameterRefRn.setStatus("current")
_CfprApBiosParameterRefIsSupported_Type = CfprApBiosSupportedAction
_CfprApBiosParameterRefIsSupported_Object = MibTableColumn
cfprApBiosParameterRefIsSupported = _CfprApBiosParameterRefIsSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 5, 1, 4),
    _CfprApBiosParameterRefIsSupported_Type()
)
cfprApBiosParameterRefIsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosParameterRefIsSupported.setStatus("current")
_CfprApBiosParameterRefName_Type = SnmpAdminString
_CfprApBiosParameterRefName_Object = MibTableColumn
cfprApBiosParameterRefName = _CfprApBiosParameterRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 5, 1, 5),
    _CfprApBiosParameterRefName_Type()
)
cfprApBiosParameterRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosParameterRefName.setStatus("current")
_CfprApBiosParameterRefPropertyName_Type = SnmpAdminString
_CfprApBiosParameterRefPropertyName_Object = MibTableColumn
cfprApBiosParameterRefPropertyName = _CfprApBiosParameterRefPropertyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 5, 1, 6),
    _CfprApBiosParameterRefPropertyName_Type()
)
cfprApBiosParameterRefPropertyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosParameterRefPropertyName.setStatus("current")
_CfprApBiosRefTable_Object = MibTable
cfprApBiosRefTable = _CfprApBiosRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 6)
)
if mibBuilder.loadTexts:
    cfprApBiosRefTable.setStatus("current")
_CfprApBiosRefEntry_Object = MibTableRow
cfprApBiosRefEntry = _CfprApBiosRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 6, 1)
)
cfprApBiosRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosRefEntry.setStatus("current")
_CfprApBiosRefInstanceId_Type = CfprApManagedObjectId
_CfprApBiosRefInstanceId_Object = MibTableColumn
cfprApBiosRefInstanceId = _CfprApBiosRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 6, 1, 1),
    _CfprApBiosRefInstanceId_Type()
)
cfprApBiosRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosRefInstanceId.setStatus("current")
_CfprApBiosRefDn_Type = CfprApManagedObjectDn
_CfprApBiosRefDn_Object = MibTableColumn
cfprApBiosRefDn = _CfprApBiosRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 6, 1, 2),
    _CfprApBiosRefDn_Type()
)
cfprApBiosRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosRefDn.setStatus("current")
_CfprApBiosRefRn_Type = SnmpAdminString
_CfprApBiosRefRn_Object = MibTableColumn
cfprApBiosRefRn = _CfprApBiosRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 6, 1, 3),
    _CfprApBiosRefRn_Type()
)
cfprApBiosRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosRefRn.setStatus("current")
_CfprApBiosRefIsSupported_Type = CfprApBiosSupportedAction
_CfprApBiosRefIsSupported_Object = MibTableColumn
cfprApBiosRefIsSupported = _CfprApBiosRefIsSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 6, 1, 4),
    _CfprApBiosRefIsSupported_Type()
)
cfprApBiosRefIsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosRefIsSupported.setStatus("current")
_CfprApBiosSettingRefTable_Object = MibTable
cfprApBiosSettingRefTable = _CfprApBiosSettingRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 7)
)
if mibBuilder.loadTexts:
    cfprApBiosSettingRefTable.setStatus("current")
_CfprApBiosSettingRefEntry_Object = MibTableRow
cfprApBiosSettingRefEntry = _CfprApBiosSettingRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 7, 1)
)
cfprApBiosSettingRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosSettingRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosSettingRefEntry.setStatus("current")
_CfprApBiosSettingRefInstanceId_Type = CfprApManagedObjectId
_CfprApBiosSettingRefInstanceId_Object = MibTableColumn
cfprApBiosSettingRefInstanceId = _CfprApBiosSettingRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 7, 1, 1),
    _CfprApBiosSettingRefInstanceId_Type()
)
cfprApBiosSettingRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosSettingRefInstanceId.setStatus("current")
_CfprApBiosSettingRefDn_Type = CfprApManagedObjectDn
_CfprApBiosSettingRefDn_Object = MibTableColumn
cfprApBiosSettingRefDn = _CfprApBiosSettingRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 7, 1, 2),
    _CfprApBiosSettingRefDn_Type()
)
cfprApBiosSettingRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosSettingRefDn.setStatus("current")
_CfprApBiosSettingRefRn_Type = SnmpAdminString
_CfprApBiosSettingRefRn_Object = MibTableColumn
cfprApBiosSettingRefRn = _CfprApBiosSettingRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 7, 1, 3),
    _CfprApBiosSettingRefRn_Type()
)
cfprApBiosSettingRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosSettingRefRn.setStatus("current")
_CfprApBiosSettingRefConstantName_Type = SnmpAdminString
_CfprApBiosSettingRefConstantName_Object = MibTableColumn
cfprApBiosSettingRefConstantName = _CfprApBiosSettingRefConstantName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 7, 1, 4),
    _CfprApBiosSettingRefConstantName_Type()
)
cfprApBiosSettingRefConstantName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosSettingRefConstantName.setStatus("current")
_CfprApBiosSettingRefIsDefault_Type = CfprApBiosDefaultAction
_CfprApBiosSettingRefIsDefault_Object = MibTableColumn
cfprApBiosSettingRefIsDefault = _CfprApBiosSettingRefIsDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 7, 1, 5),
    _CfprApBiosSettingRefIsDefault_Type()
)
cfprApBiosSettingRefIsDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosSettingRefIsDefault.setStatus("current")
_CfprApBiosSettingRefIsSupported_Type = CfprApBiosSupportedAction
_CfprApBiosSettingRefIsSupported_Object = MibTableColumn
cfprApBiosSettingRefIsSupported = _CfprApBiosSettingRefIsSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 7, 1, 6),
    _CfprApBiosSettingRefIsSupported_Type()
)
cfprApBiosSettingRefIsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosSettingRefIsSupported.setStatus("current")
_CfprApBiosSettingRefName_Type = SnmpAdminString
_CfprApBiosSettingRefName_Object = MibTableColumn
cfprApBiosSettingRefName = _CfprApBiosSettingRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 7, 1, 7),
    _CfprApBiosSettingRefName_Type()
)
cfprApBiosSettingRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosSettingRefName.setStatus("current")
_CfprApBiosSettingsTable_Object = MibTable
cfprApBiosSettingsTable = _CfprApBiosSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 8)
)
if mibBuilder.loadTexts:
    cfprApBiosSettingsTable.setStatus("current")
_CfprApBiosSettingsEntry_Object = MibTableRow
cfprApBiosSettingsEntry = _CfprApBiosSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 8, 1)
)
cfprApBiosSettingsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosSettingsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosSettingsEntry.setStatus("current")
_CfprApBiosSettingsInstanceId_Type = CfprApManagedObjectId
_CfprApBiosSettingsInstanceId_Object = MibTableColumn
cfprApBiosSettingsInstanceId = _CfprApBiosSettingsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 8, 1, 1),
    _CfprApBiosSettingsInstanceId_Type()
)
cfprApBiosSettingsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosSettingsInstanceId.setStatus("current")
_CfprApBiosSettingsDn_Type = CfprApManagedObjectDn
_CfprApBiosSettingsDn_Object = MibTableColumn
cfprApBiosSettingsDn = _CfprApBiosSettingsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 8, 1, 2),
    _CfprApBiosSettingsDn_Type()
)
cfprApBiosSettingsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosSettingsDn.setStatus("current")
_CfprApBiosSettingsRn_Type = SnmpAdminString
_CfprApBiosSettingsRn_Object = MibTableColumn
cfprApBiosSettingsRn = _CfprApBiosSettingsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 8, 1, 3),
    _CfprApBiosSettingsRn_Type()
)
cfprApBiosSettingsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosSettingsRn.setStatus("current")
_CfprApBiosUnitTable_Object = MibTable
cfprApBiosUnitTable = _CfprApBiosUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 9)
)
if mibBuilder.loadTexts:
    cfprApBiosUnitTable.setStatus("current")
_CfprApBiosUnitEntry_Object = MibTableRow
cfprApBiosUnitEntry = _CfprApBiosUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 9, 1)
)
cfprApBiosUnitEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosUnitInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosUnitEntry.setStatus("current")
_CfprApBiosUnitInstanceId_Type = CfprApManagedObjectId
_CfprApBiosUnitInstanceId_Object = MibTableColumn
cfprApBiosUnitInstanceId = _CfprApBiosUnitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 9, 1, 1),
    _CfprApBiosUnitInstanceId_Type()
)
cfprApBiosUnitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosUnitInstanceId.setStatus("current")
_CfprApBiosUnitDn_Type = CfprApManagedObjectDn
_CfprApBiosUnitDn_Object = MibTableColumn
cfprApBiosUnitDn = _CfprApBiosUnitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 9, 1, 2),
    _CfprApBiosUnitDn_Type()
)
cfprApBiosUnitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosUnitDn.setStatus("current")
_CfprApBiosUnitRn_Type = SnmpAdminString
_CfprApBiosUnitRn_Object = MibTableColumn
cfprApBiosUnitRn = _CfprApBiosUnitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 9, 1, 3),
    _CfprApBiosUnitRn_Type()
)
cfprApBiosUnitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosUnitRn.setStatus("current")
_CfprApBiosUnitInitSeq_Type = SnmpAdminString
_CfprApBiosUnitInitSeq_Object = MibTableColumn
cfprApBiosUnitInitSeq = _CfprApBiosUnitInitSeq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 9, 1, 4),
    _CfprApBiosUnitInitSeq_Type()
)
cfprApBiosUnitInitSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosUnitInitSeq.setStatus("current")
_CfprApBiosUnitInitTs_Type = DateAndTime
_CfprApBiosUnitInitTs_Object = MibTableColumn
cfprApBiosUnitInitTs = _CfprApBiosUnitInitTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 9, 1, 5),
    _CfprApBiosUnitInitTs_Type()
)
cfprApBiosUnitInitTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosUnitInitTs.setStatus("current")
_CfprApBiosUnitModel_Type = SnmpAdminString
_CfprApBiosUnitModel_Object = MibTableColumn
cfprApBiosUnitModel = _CfprApBiosUnitModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 9, 1, 6),
    _CfprApBiosUnitModel_Type()
)
cfprApBiosUnitModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosUnitModel.setStatus("current")
_CfprApBiosUnitRevision_Type = SnmpAdminString
_CfprApBiosUnitRevision_Object = MibTableColumn
cfprApBiosUnitRevision = _CfprApBiosUnitRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 9, 1, 7),
    _CfprApBiosUnitRevision_Type()
)
cfprApBiosUnitRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosUnitRevision.setStatus("current")
_CfprApBiosUnitSerial_Type = SnmpAdminString
_CfprApBiosUnitSerial_Object = MibTableColumn
cfprApBiosUnitSerial = _CfprApBiosUnitSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 9, 1, 8),
    _CfprApBiosUnitSerial_Type()
)
cfprApBiosUnitSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosUnitSerial.setStatus("current")
_CfprApBiosUnitVendor_Type = SnmpAdminString
_CfprApBiosUnitVendor_Object = MibTableColumn
cfprApBiosUnitVendor = _CfprApBiosUnitVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 9, 1, 9),
    _CfprApBiosUnitVendor_Type()
)
cfprApBiosUnitVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosUnitVendor.setStatus("current")
_CfprApBiosVIdentityParamsTable_Object = MibTable
cfprApBiosVIdentityParamsTable = _CfprApBiosVIdentityParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 10)
)
if mibBuilder.loadTexts:
    cfprApBiosVIdentityParamsTable.setStatus("current")
_CfprApBiosVIdentityParamsEntry_Object = MibTableRow
cfprApBiosVIdentityParamsEntry = _CfprApBiosVIdentityParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 10, 1)
)
cfprApBiosVIdentityParamsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVIdentityParamsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVIdentityParamsEntry.setStatus("current")
_CfprApBiosVIdentityParamsInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVIdentityParamsInstanceId_Object = MibTableColumn
cfprApBiosVIdentityParamsInstanceId = _CfprApBiosVIdentityParamsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 10, 1, 1),
    _CfprApBiosVIdentityParamsInstanceId_Type()
)
cfprApBiosVIdentityParamsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVIdentityParamsInstanceId.setStatus("current")
_CfprApBiosVIdentityParamsDn_Type = CfprApManagedObjectDn
_CfprApBiosVIdentityParamsDn_Object = MibTableColumn
cfprApBiosVIdentityParamsDn = _CfprApBiosVIdentityParamsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 10, 1, 2),
    _CfprApBiosVIdentityParamsDn_Type()
)
cfprApBiosVIdentityParamsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVIdentityParamsDn.setStatus("current")
_CfprApBiosVIdentityParamsRn_Type = SnmpAdminString
_CfprApBiosVIdentityParamsRn_Object = MibTableColumn
cfprApBiosVIdentityParamsRn = _CfprApBiosVIdentityParamsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 10, 1, 3),
    _CfprApBiosVIdentityParamsRn_Type()
)
cfprApBiosVIdentityParamsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVIdentityParamsRn.setStatus("current")
_CfprApBiosVIdentityParamsLsServerName_Type = SnmpAdminString
_CfprApBiosVIdentityParamsLsServerName_Object = MibTableColumn
cfprApBiosVIdentityParamsLsServerName = _CfprApBiosVIdentityParamsLsServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 10, 1, 4),
    _CfprApBiosVIdentityParamsLsServerName_Type()
)
cfprApBiosVIdentityParamsLsServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVIdentityParamsLsServerName.setStatus("current")
_CfprApBiosVIdentityParamsLsServerTmplName_Type = SnmpAdminString
_CfprApBiosVIdentityParamsLsServerTmplName_Object = MibTableColumn
cfprApBiosVIdentityParamsLsServerTmplName = _CfprApBiosVIdentityParamsLsServerTmplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 10, 1, 5),
    _CfprApBiosVIdentityParamsLsServerTmplName_Type()
)
cfprApBiosVIdentityParamsLsServerTmplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVIdentityParamsLsServerTmplName.setStatus("current")
_CfprApBiosVIdentityParamsSysName_Type = SnmpAdminString
_CfprApBiosVIdentityParamsSysName_Object = MibTableColumn
cfprApBiosVIdentityParamsSysName = _CfprApBiosVIdentityParamsSysName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 10, 1, 6),
    _CfprApBiosVIdentityParamsSysName_Type()
)
cfprApBiosVIdentityParamsSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVIdentityParamsSysName.setStatus("current")
_CfprApBiosVProfileTable_Object = MibTable
cfprApBiosVProfileTable = _CfprApBiosVProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 11)
)
if mibBuilder.loadTexts:
    cfprApBiosVProfileTable.setStatus("current")
_CfprApBiosVProfileEntry_Object = MibTableRow
cfprApBiosVProfileEntry = _CfprApBiosVProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 11, 1)
)
cfprApBiosVProfileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVProfileEntry.setStatus("current")
_CfprApBiosVProfileInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVProfileInstanceId_Object = MibTableColumn
cfprApBiosVProfileInstanceId = _CfprApBiosVProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 11, 1, 1),
    _CfprApBiosVProfileInstanceId_Type()
)
cfprApBiosVProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVProfileInstanceId.setStatus("current")
_CfprApBiosVProfileDn_Type = CfprApManagedObjectDn
_CfprApBiosVProfileDn_Object = MibTableColumn
cfprApBiosVProfileDn = _CfprApBiosVProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 11, 1, 2),
    _CfprApBiosVProfileDn_Type()
)
cfprApBiosVProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVProfileDn.setStatus("current")
_CfprApBiosVProfileRn_Type = SnmpAdminString
_CfprApBiosVProfileRn_Object = MibTableColumn
cfprApBiosVProfileRn = _CfprApBiosVProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 11, 1, 3),
    _CfprApBiosVProfileRn_Type()
)
cfprApBiosVProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVProfileRn.setStatus("current")
_CfprApBiosVProfileDescr_Type = SnmpAdminString
_CfprApBiosVProfileDescr_Object = MibTableColumn
cfprApBiosVProfileDescr = _CfprApBiosVProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 11, 1, 4),
    _CfprApBiosVProfileDescr_Type()
)
cfprApBiosVProfileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVProfileDescr.setStatus("current")
_CfprApBiosVProfileIntId_Type = SnmpAdminString
_CfprApBiosVProfileIntId_Object = MibTableColumn
cfprApBiosVProfileIntId = _CfprApBiosVProfileIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 11, 1, 5),
    _CfprApBiosVProfileIntId_Type()
)
cfprApBiosVProfileIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVProfileIntId.setStatus("current")
_CfprApBiosVProfileName_Type = SnmpAdminString
_CfprApBiosVProfileName_Object = MibTableColumn
cfprApBiosVProfileName = _CfprApBiosVProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 11, 1, 6),
    _CfprApBiosVProfileName_Type()
)
cfprApBiosVProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVProfileName.setStatus("current")
_CfprApBiosVProfilePolicyLevel_Type = Gauge32
_CfprApBiosVProfilePolicyLevel_Object = MibTableColumn
cfprApBiosVProfilePolicyLevel = _CfprApBiosVProfilePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 11, 1, 7),
    _CfprApBiosVProfilePolicyLevel_Type()
)
cfprApBiosVProfilePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVProfilePolicyLevel.setStatus("current")
_CfprApBiosVProfilePolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApBiosVProfilePolicyOwner_Object = MibTableColumn
cfprApBiosVProfilePolicyOwner = _CfprApBiosVProfilePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 11, 1, 8),
    _CfprApBiosVProfilePolicyOwner_Type()
)
cfprApBiosVProfilePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVProfilePolicyOwner.setStatus("current")
_CfprApBiosVProfileRebootOnUpdate_Type = TruthValue
_CfprApBiosVProfileRebootOnUpdate_Object = MibTableColumn
cfprApBiosVProfileRebootOnUpdate = _CfprApBiosVProfileRebootOnUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 11, 1, 9),
    _CfprApBiosVProfileRebootOnUpdate_Type()
)
cfprApBiosVProfileRebootOnUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVProfileRebootOnUpdate.setStatus("current")
_CfprApBiosVfACPI10SupportTable_Object = MibTable
cfprApBiosVfACPI10SupportTable = _CfprApBiosVfACPI10SupportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 12)
)
if mibBuilder.loadTexts:
    cfprApBiosVfACPI10SupportTable.setStatus("current")
_CfprApBiosVfACPI10SupportEntry_Object = MibTableRow
cfprApBiosVfACPI10SupportEntry = _CfprApBiosVfACPI10SupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 12, 1)
)
cfprApBiosVfACPI10SupportEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfACPI10SupportInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfACPI10SupportEntry.setStatus("current")
_CfprApBiosVfACPI10SupportInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfACPI10SupportInstanceId_Object = MibTableColumn
cfprApBiosVfACPI10SupportInstanceId = _CfprApBiosVfACPI10SupportInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 12, 1, 1),
    _CfprApBiosVfACPI10SupportInstanceId_Type()
)
cfprApBiosVfACPI10SupportInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfACPI10SupportInstanceId.setStatus("current")
_CfprApBiosVfACPI10SupportDn_Type = CfprApManagedObjectDn
_CfprApBiosVfACPI10SupportDn_Object = MibTableColumn
cfprApBiosVfACPI10SupportDn = _CfprApBiosVfACPI10SupportDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 12, 1, 2),
    _CfprApBiosVfACPI10SupportDn_Type()
)
cfprApBiosVfACPI10SupportDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfACPI10SupportDn.setStatus("current")
_CfprApBiosVfACPI10SupportRn_Type = SnmpAdminString
_CfprApBiosVfACPI10SupportRn_Object = MibTableColumn
cfprApBiosVfACPI10SupportRn = _CfprApBiosVfACPI10SupportRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 12, 1, 3),
    _CfprApBiosVfACPI10SupportRn_Type()
)
cfprApBiosVfACPI10SupportRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfACPI10SupportRn.setStatus("current")
_CfprApBiosVfACPI10SupportVpACPI10Support_Type = CfprApBiosVfACPI10SupportVpACPI10Support
_CfprApBiosVfACPI10SupportVpACPI10Support_Object = MibTableColumn
cfprApBiosVfACPI10SupportVpACPI10Support = _CfprApBiosVfACPI10SupportVpACPI10Support_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 12, 1, 4),
    _CfprApBiosVfACPI10SupportVpACPI10Support_Type()
)
cfprApBiosVfACPI10SupportVpACPI10Support.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfACPI10SupportVpACPI10Support.setStatus("current")
_CfprApBiosVfAllUSBDevicesTable_Object = MibTable
cfprApBiosVfAllUSBDevicesTable = _CfprApBiosVfAllUSBDevicesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 13)
)
if mibBuilder.loadTexts:
    cfprApBiosVfAllUSBDevicesTable.setStatus("current")
_CfprApBiosVfAllUSBDevicesEntry_Object = MibTableRow
cfprApBiosVfAllUSBDevicesEntry = _CfprApBiosVfAllUSBDevicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 13, 1)
)
cfprApBiosVfAllUSBDevicesEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfAllUSBDevicesInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfAllUSBDevicesEntry.setStatus("current")
_CfprApBiosVfAllUSBDevicesInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfAllUSBDevicesInstanceId_Object = MibTableColumn
cfprApBiosVfAllUSBDevicesInstanceId = _CfprApBiosVfAllUSBDevicesInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 13, 1, 1),
    _CfprApBiosVfAllUSBDevicesInstanceId_Type()
)
cfprApBiosVfAllUSBDevicesInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfAllUSBDevicesInstanceId.setStatus("current")
_CfprApBiosVfAllUSBDevicesDn_Type = CfprApManagedObjectDn
_CfprApBiosVfAllUSBDevicesDn_Object = MibTableColumn
cfprApBiosVfAllUSBDevicesDn = _CfprApBiosVfAllUSBDevicesDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 13, 1, 2),
    _CfprApBiosVfAllUSBDevicesDn_Type()
)
cfprApBiosVfAllUSBDevicesDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfAllUSBDevicesDn.setStatus("current")
_CfprApBiosVfAllUSBDevicesRn_Type = SnmpAdminString
_CfprApBiosVfAllUSBDevicesRn_Object = MibTableColumn
cfprApBiosVfAllUSBDevicesRn = _CfprApBiosVfAllUSBDevicesRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 13, 1, 3),
    _CfprApBiosVfAllUSBDevicesRn_Type()
)
cfprApBiosVfAllUSBDevicesRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfAllUSBDevicesRn.setStatus("current")
_CfprApBiosVfAllUSBDevicesVpAllUSBDevices_Type = CfprApBiosVfAllUSBDevicesVpAllUSBDevices
_CfprApBiosVfAllUSBDevicesVpAllUSBDevices_Object = MibTableColumn
cfprApBiosVfAllUSBDevicesVpAllUSBDevices = _CfprApBiosVfAllUSBDevicesVpAllUSBDevices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 13, 1, 4),
    _CfprApBiosVfAllUSBDevicesVpAllUSBDevices_Type()
)
cfprApBiosVfAllUSBDevicesVpAllUSBDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfAllUSBDevicesVpAllUSBDevices.setStatus("current")
_CfprApBiosVfAltitudeTable_Object = MibTable
cfprApBiosVfAltitudeTable = _CfprApBiosVfAltitudeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 14)
)
if mibBuilder.loadTexts:
    cfprApBiosVfAltitudeTable.setStatus("current")
_CfprApBiosVfAltitudeEntry_Object = MibTableRow
cfprApBiosVfAltitudeEntry = _CfprApBiosVfAltitudeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 14, 1)
)
cfprApBiosVfAltitudeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfAltitudeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfAltitudeEntry.setStatus("current")
_CfprApBiosVfAltitudeInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfAltitudeInstanceId_Object = MibTableColumn
cfprApBiosVfAltitudeInstanceId = _CfprApBiosVfAltitudeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 14, 1, 1),
    _CfprApBiosVfAltitudeInstanceId_Type()
)
cfprApBiosVfAltitudeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfAltitudeInstanceId.setStatus("current")
_CfprApBiosVfAltitudeDn_Type = CfprApManagedObjectDn
_CfprApBiosVfAltitudeDn_Object = MibTableColumn
cfprApBiosVfAltitudeDn = _CfprApBiosVfAltitudeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 14, 1, 2),
    _CfprApBiosVfAltitudeDn_Type()
)
cfprApBiosVfAltitudeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfAltitudeDn.setStatus("current")
_CfprApBiosVfAltitudeRn_Type = SnmpAdminString
_CfprApBiosVfAltitudeRn_Object = MibTableColumn
cfprApBiosVfAltitudeRn = _CfprApBiosVfAltitudeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 14, 1, 3),
    _CfprApBiosVfAltitudeRn_Type()
)
cfprApBiosVfAltitudeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfAltitudeRn.setStatus("current")
_CfprApBiosVfAltitudeVpAltitude_Type = CfprApBiosVfAltitudeVpAltitude
_CfprApBiosVfAltitudeVpAltitude_Object = MibTableColumn
cfprApBiosVfAltitudeVpAltitude = _CfprApBiosVfAltitudeVpAltitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 14, 1, 4),
    _CfprApBiosVfAltitudeVpAltitude_Type()
)
cfprApBiosVfAltitudeVpAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfAltitudeVpAltitude.setStatus("current")
_CfprApBiosVfAssertNMIOnPERRTable_Object = MibTable
cfprApBiosVfAssertNMIOnPERRTable = _CfprApBiosVfAssertNMIOnPERRTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 15)
)
if mibBuilder.loadTexts:
    cfprApBiosVfAssertNMIOnPERRTable.setStatus("current")
_CfprApBiosVfAssertNMIOnPERREntry_Object = MibTableRow
cfprApBiosVfAssertNMIOnPERREntry = _CfprApBiosVfAssertNMIOnPERREntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 15, 1)
)
cfprApBiosVfAssertNMIOnPERREntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfAssertNMIOnPERRInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfAssertNMIOnPERREntry.setStatus("current")
_CfprApBiosVfAssertNMIOnPERRInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfAssertNMIOnPERRInstanceId_Object = MibTableColumn
cfprApBiosVfAssertNMIOnPERRInstanceId = _CfprApBiosVfAssertNMIOnPERRInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 15, 1, 1),
    _CfprApBiosVfAssertNMIOnPERRInstanceId_Type()
)
cfprApBiosVfAssertNMIOnPERRInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfAssertNMIOnPERRInstanceId.setStatus("current")
_CfprApBiosVfAssertNMIOnPERRDn_Type = CfprApManagedObjectDn
_CfprApBiosVfAssertNMIOnPERRDn_Object = MibTableColumn
cfprApBiosVfAssertNMIOnPERRDn = _CfprApBiosVfAssertNMIOnPERRDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 15, 1, 2),
    _CfprApBiosVfAssertNMIOnPERRDn_Type()
)
cfprApBiosVfAssertNMIOnPERRDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfAssertNMIOnPERRDn.setStatus("current")
_CfprApBiosVfAssertNMIOnPERRRn_Type = SnmpAdminString
_CfprApBiosVfAssertNMIOnPERRRn_Object = MibTableColumn
cfprApBiosVfAssertNMIOnPERRRn = _CfprApBiosVfAssertNMIOnPERRRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 15, 1, 3),
    _CfprApBiosVfAssertNMIOnPERRRn_Type()
)
cfprApBiosVfAssertNMIOnPERRRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfAssertNMIOnPERRRn.setStatus("current")
_CfprApBiosVfAssertNMIOnPERRVpAssertNMIOnPERR_Type = CfprApBiosVfAssertNMIOnPERRVpAssertNMIOnPERR
_CfprApBiosVfAssertNMIOnPERRVpAssertNMIOnPERR_Object = MibTableColumn
cfprApBiosVfAssertNMIOnPERRVpAssertNMIOnPERR = _CfprApBiosVfAssertNMIOnPERRVpAssertNMIOnPERR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 15, 1, 4),
    _CfprApBiosVfAssertNMIOnPERRVpAssertNMIOnPERR_Type()
)
cfprApBiosVfAssertNMIOnPERRVpAssertNMIOnPERR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfAssertNMIOnPERRVpAssertNMIOnPERR.setStatus("current")
_CfprApBiosVfAssertNMIOnSERRTable_Object = MibTable
cfprApBiosVfAssertNMIOnSERRTable = _CfprApBiosVfAssertNMIOnSERRTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 16)
)
if mibBuilder.loadTexts:
    cfprApBiosVfAssertNMIOnSERRTable.setStatus("current")
_CfprApBiosVfAssertNMIOnSERREntry_Object = MibTableRow
cfprApBiosVfAssertNMIOnSERREntry = _CfprApBiosVfAssertNMIOnSERREntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 16, 1)
)
cfprApBiosVfAssertNMIOnSERREntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfAssertNMIOnSERRInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfAssertNMIOnSERREntry.setStatus("current")
_CfprApBiosVfAssertNMIOnSERRInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfAssertNMIOnSERRInstanceId_Object = MibTableColumn
cfprApBiosVfAssertNMIOnSERRInstanceId = _CfprApBiosVfAssertNMIOnSERRInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 16, 1, 1),
    _CfprApBiosVfAssertNMIOnSERRInstanceId_Type()
)
cfprApBiosVfAssertNMIOnSERRInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfAssertNMIOnSERRInstanceId.setStatus("current")
_CfprApBiosVfAssertNMIOnSERRDn_Type = CfprApManagedObjectDn
_CfprApBiosVfAssertNMIOnSERRDn_Object = MibTableColumn
cfprApBiosVfAssertNMIOnSERRDn = _CfprApBiosVfAssertNMIOnSERRDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 16, 1, 2),
    _CfprApBiosVfAssertNMIOnSERRDn_Type()
)
cfprApBiosVfAssertNMIOnSERRDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfAssertNMIOnSERRDn.setStatus("current")
_CfprApBiosVfAssertNMIOnSERRRn_Type = SnmpAdminString
_CfprApBiosVfAssertNMIOnSERRRn_Object = MibTableColumn
cfprApBiosVfAssertNMIOnSERRRn = _CfprApBiosVfAssertNMIOnSERRRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 16, 1, 3),
    _CfprApBiosVfAssertNMIOnSERRRn_Type()
)
cfprApBiosVfAssertNMIOnSERRRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfAssertNMIOnSERRRn.setStatus("current")
_CfprApBiosVfAssertNMIOnSERRVpAssertNMIOnSERR_Type = CfprApBiosVfAssertNMIOnSERRVpAssertNMIOnSERR
_CfprApBiosVfAssertNMIOnSERRVpAssertNMIOnSERR_Object = MibTableColumn
cfprApBiosVfAssertNMIOnSERRVpAssertNMIOnSERR = _CfprApBiosVfAssertNMIOnSERRVpAssertNMIOnSERR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 16, 1, 4),
    _CfprApBiosVfAssertNMIOnSERRVpAssertNMIOnSERR_Type()
)
cfprApBiosVfAssertNMIOnSERRVpAssertNMIOnSERR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfAssertNMIOnSERRVpAssertNMIOnSERR.setStatus("current")
_CfprApBiosVfBootOptionRetryTable_Object = MibTable
cfprApBiosVfBootOptionRetryTable = _CfprApBiosVfBootOptionRetryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 17)
)
if mibBuilder.loadTexts:
    cfprApBiosVfBootOptionRetryTable.setStatus("current")
_CfprApBiosVfBootOptionRetryEntry_Object = MibTableRow
cfprApBiosVfBootOptionRetryEntry = _CfprApBiosVfBootOptionRetryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 17, 1)
)
cfprApBiosVfBootOptionRetryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfBootOptionRetryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfBootOptionRetryEntry.setStatus("current")
_CfprApBiosVfBootOptionRetryInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfBootOptionRetryInstanceId_Object = MibTableColumn
cfprApBiosVfBootOptionRetryInstanceId = _CfprApBiosVfBootOptionRetryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 17, 1, 1),
    _CfprApBiosVfBootOptionRetryInstanceId_Type()
)
cfprApBiosVfBootOptionRetryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfBootOptionRetryInstanceId.setStatus("current")
_CfprApBiosVfBootOptionRetryDn_Type = CfprApManagedObjectDn
_CfprApBiosVfBootOptionRetryDn_Object = MibTableColumn
cfprApBiosVfBootOptionRetryDn = _CfprApBiosVfBootOptionRetryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 17, 1, 2),
    _CfprApBiosVfBootOptionRetryDn_Type()
)
cfprApBiosVfBootOptionRetryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfBootOptionRetryDn.setStatus("current")
_CfprApBiosVfBootOptionRetryRn_Type = SnmpAdminString
_CfprApBiosVfBootOptionRetryRn_Object = MibTableColumn
cfprApBiosVfBootOptionRetryRn = _CfprApBiosVfBootOptionRetryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 17, 1, 3),
    _CfprApBiosVfBootOptionRetryRn_Type()
)
cfprApBiosVfBootOptionRetryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfBootOptionRetryRn.setStatus("current")
_CfprApBiosVfBootOptionRetryVpBootOptionRetry_Type = CfprApBiosVfBootOptionRetryVpBootOptionRetry
_CfprApBiosVfBootOptionRetryVpBootOptionRetry_Object = MibTableColumn
cfprApBiosVfBootOptionRetryVpBootOptionRetry = _CfprApBiosVfBootOptionRetryVpBootOptionRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 17, 1, 4),
    _CfprApBiosVfBootOptionRetryVpBootOptionRetry_Type()
)
cfprApBiosVfBootOptionRetryVpBootOptionRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfBootOptionRetryVpBootOptionRetry.setStatus("current")
_CfprApBiosVfCPUPerformanceTable_Object = MibTable
cfprApBiosVfCPUPerformanceTable = _CfprApBiosVfCPUPerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 18)
)
if mibBuilder.loadTexts:
    cfprApBiosVfCPUPerformanceTable.setStatus("current")
_CfprApBiosVfCPUPerformanceEntry_Object = MibTableRow
cfprApBiosVfCPUPerformanceEntry = _CfprApBiosVfCPUPerformanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 18, 1)
)
cfprApBiosVfCPUPerformanceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfCPUPerformanceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfCPUPerformanceEntry.setStatus("current")
_CfprApBiosVfCPUPerformanceInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfCPUPerformanceInstanceId_Object = MibTableColumn
cfprApBiosVfCPUPerformanceInstanceId = _CfprApBiosVfCPUPerformanceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 18, 1, 1),
    _CfprApBiosVfCPUPerformanceInstanceId_Type()
)
cfprApBiosVfCPUPerformanceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfCPUPerformanceInstanceId.setStatus("current")
_CfprApBiosVfCPUPerformanceDn_Type = CfprApManagedObjectDn
_CfprApBiosVfCPUPerformanceDn_Object = MibTableColumn
cfprApBiosVfCPUPerformanceDn = _CfprApBiosVfCPUPerformanceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 18, 1, 2),
    _CfprApBiosVfCPUPerformanceDn_Type()
)
cfprApBiosVfCPUPerformanceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfCPUPerformanceDn.setStatus("current")
_CfprApBiosVfCPUPerformanceRn_Type = SnmpAdminString
_CfprApBiosVfCPUPerformanceRn_Object = MibTableColumn
cfprApBiosVfCPUPerformanceRn = _CfprApBiosVfCPUPerformanceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 18, 1, 3),
    _CfprApBiosVfCPUPerformanceRn_Type()
)
cfprApBiosVfCPUPerformanceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfCPUPerformanceRn.setStatus("current")
_CfprApBiosVfCPUPerformanceVpCPUPerformance_Type = CfprApBiosVfCPUPerformanceVpCPUPerformance
_CfprApBiosVfCPUPerformanceVpCPUPerformance_Object = MibTableColumn
cfprApBiosVfCPUPerformanceVpCPUPerformance = _CfprApBiosVfCPUPerformanceVpCPUPerformance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 18, 1, 4),
    _CfprApBiosVfCPUPerformanceVpCPUPerformance_Type()
)
cfprApBiosVfCPUPerformanceVpCPUPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfCPUPerformanceVpCPUPerformance.setStatus("current")
_CfprApBiosVfConsoleRedirectionTable_Object = MibTable
cfprApBiosVfConsoleRedirectionTable = _CfprApBiosVfConsoleRedirectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 19)
)
if mibBuilder.loadTexts:
    cfprApBiosVfConsoleRedirectionTable.setStatus("current")
_CfprApBiosVfConsoleRedirectionEntry_Object = MibTableRow
cfprApBiosVfConsoleRedirectionEntry = _CfprApBiosVfConsoleRedirectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 19, 1)
)
cfprApBiosVfConsoleRedirectionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfConsoleRedirectionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfConsoleRedirectionEntry.setStatus("current")
_CfprApBiosVfConsoleRedirectionInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfConsoleRedirectionInstanceId_Object = MibTableColumn
cfprApBiosVfConsoleRedirectionInstanceId = _CfprApBiosVfConsoleRedirectionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 19, 1, 1),
    _CfprApBiosVfConsoleRedirectionInstanceId_Type()
)
cfprApBiosVfConsoleRedirectionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfConsoleRedirectionInstanceId.setStatus("current")
_CfprApBiosVfConsoleRedirectionDn_Type = CfprApManagedObjectDn
_CfprApBiosVfConsoleRedirectionDn_Object = MibTableColumn
cfprApBiosVfConsoleRedirectionDn = _CfprApBiosVfConsoleRedirectionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 19, 1, 2),
    _CfprApBiosVfConsoleRedirectionDn_Type()
)
cfprApBiosVfConsoleRedirectionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfConsoleRedirectionDn.setStatus("current")
_CfprApBiosVfConsoleRedirectionRn_Type = SnmpAdminString
_CfprApBiosVfConsoleRedirectionRn_Object = MibTableColumn
cfprApBiosVfConsoleRedirectionRn = _CfprApBiosVfConsoleRedirectionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 19, 1, 3),
    _CfprApBiosVfConsoleRedirectionRn_Type()
)
cfprApBiosVfConsoleRedirectionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfConsoleRedirectionRn.setStatus("current")
_CfprApBiosVfConsoleRedirectionVpBaudRate_Type = CfprApBiosVfConsoleRedirectionVpBaudRate
_CfprApBiosVfConsoleRedirectionVpBaudRate_Object = MibTableColumn
cfprApBiosVfConsoleRedirectionVpBaudRate = _CfprApBiosVfConsoleRedirectionVpBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 19, 1, 4),
    _CfprApBiosVfConsoleRedirectionVpBaudRate_Type()
)
cfprApBiosVfConsoleRedirectionVpBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfConsoleRedirectionVpBaudRate.setStatus("current")
_CfprApBiosVfConsoleRedirectionVpConsoleRedirection_Type = CfprApBiosVfConsoleRedirectionVpConsoleRedirection
_CfprApBiosVfConsoleRedirectionVpConsoleRedirection_Object = MibTableColumn
cfprApBiosVfConsoleRedirectionVpConsoleRedirection = _CfprApBiosVfConsoleRedirectionVpConsoleRedirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 19, 1, 5),
    _CfprApBiosVfConsoleRedirectionVpConsoleRedirection_Type()
)
cfprApBiosVfConsoleRedirectionVpConsoleRedirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfConsoleRedirectionVpConsoleRedirection.setStatus("current")
_CfprApBiosVfConsoleRedirectionVpFlowControl_Type = CfprApBiosVfConsoleRedirectionVpFlowControl
_CfprApBiosVfConsoleRedirectionVpFlowControl_Object = MibTableColumn
cfprApBiosVfConsoleRedirectionVpFlowControl = _CfprApBiosVfConsoleRedirectionVpFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 19, 1, 6),
    _CfprApBiosVfConsoleRedirectionVpFlowControl_Type()
)
cfprApBiosVfConsoleRedirectionVpFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfConsoleRedirectionVpFlowControl.setStatus("current")
_CfprApBiosVfConsoleRedirectionVpLegacyOSRedirection_Type = CfprApBiosVfConsoleRedirectionVpLegacyOSRedirection
_CfprApBiosVfConsoleRedirectionVpLegacyOSRedirection_Object = MibTableColumn
cfprApBiosVfConsoleRedirectionVpLegacyOSRedirection = _CfprApBiosVfConsoleRedirectionVpLegacyOSRedirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 19, 1, 7),
    _CfprApBiosVfConsoleRedirectionVpLegacyOSRedirection_Type()
)
cfprApBiosVfConsoleRedirectionVpLegacyOSRedirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfConsoleRedirectionVpLegacyOSRedirection.setStatus("current")
_CfprApBiosVfConsoleRedirectionVpPuttyKeyPad_Type = CfprApBiosVfConsoleRedirectionVpPuttyKeyPad
_CfprApBiosVfConsoleRedirectionVpPuttyKeyPad_Object = MibTableColumn
cfprApBiosVfConsoleRedirectionVpPuttyKeyPad = _CfprApBiosVfConsoleRedirectionVpPuttyKeyPad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 19, 1, 8),
    _CfprApBiosVfConsoleRedirectionVpPuttyKeyPad_Type()
)
cfprApBiosVfConsoleRedirectionVpPuttyKeyPad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfConsoleRedirectionVpPuttyKeyPad.setStatus("current")
_CfprApBiosVfConsoleRedirectionVpTerminalType_Type = CfprApBiosVfConsoleRedirectionVpTerminalType
_CfprApBiosVfConsoleRedirectionVpTerminalType_Object = MibTableColumn
cfprApBiosVfConsoleRedirectionVpTerminalType = _CfprApBiosVfConsoleRedirectionVpTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 19, 1, 9),
    _CfprApBiosVfConsoleRedirectionVpTerminalType_Type()
)
cfprApBiosVfConsoleRedirectionVpTerminalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfConsoleRedirectionVpTerminalType.setStatus("current")
_CfprApBiosVfCoreMultiProcessingTable_Object = MibTable
cfprApBiosVfCoreMultiProcessingTable = _CfprApBiosVfCoreMultiProcessingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 20)
)
if mibBuilder.loadTexts:
    cfprApBiosVfCoreMultiProcessingTable.setStatus("current")
_CfprApBiosVfCoreMultiProcessingEntry_Object = MibTableRow
cfprApBiosVfCoreMultiProcessingEntry = _CfprApBiosVfCoreMultiProcessingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 20, 1)
)
cfprApBiosVfCoreMultiProcessingEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfCoreMultiProcessingInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfCoreMultiProcessingEntry.setStatus("current")
_CfprApBiosVfCoreMultiProcessingInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfCoreMultiProcessingInstanceId_Object = MibTableColumn
cfprApBiosVfCoreMultiProcessingInstanceId = _CfprApBiosVfCoreMultiProcessingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 20, 1, 1),
    _CfprApBiosVfCoreMultiProcessingInstanceId_Type()
)
cfprApBiosVfCoreMultiProcessingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfCoreMultiProcessingInstanceId.setStatus("current")
_CfprApBiosVfCoreMultiProcessingDn_Type = CfprApManagedObjectDn
_CfprApBiosVfCoreMultiProcessingDn_Object = MibTableColumn
cfprApBiosVfCoreMultiProcessingDn = _CfprApBiosVfCoreMultiProcessingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 20, 1, 2),
    _CfprApBiosVfCoreMultiProcessingDn_Type()
)
cfprApBiosVfCoreMultiProcessingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfCoreMultiProcessingDn.setStatus("current")
_CfprApBiosVfCoreMultiProcessingRn_Type = SnmpAdminString
_CfprApBiosVfCoreMultiProcessingRn_Object = MibTableColumn
cfprApBiosVfCoreMultiProcessingRn = _CfprApBiosVfCoreMultiProcessingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 20, 1, 3),
    _CfprApBiosVfCoreMultiProcessingRn_Type()
)
cfprApBiosVfCoreMultiProcessingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfCoreMultiProcessingRn.setStatus("current")
_CfprApBiosVfCoreMultiProcessingVpCoreMultiProcessing_Type = CfprApBiosVfCoreMultiProcessingVpCoreMultiProcessing
_CfprApBiosVfCoreMultiProcessingVpCoreMultiProcessing_Object = MibTableColumn
cfprApBiosVfCoreMultiProcessingVpCoreMultiProcessing = _CfprApBiosVfCoreMultiProcessingVpCoreMultiProcessing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 20, 1, 4),
    _CfprApBiosVfCoreMultiProcessingVpCoreMultiProcessing_Type()
)
cfprApBiosVfCoreMultiProcessingVpCoreMultiProcessing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfCoreMultiProcessingVpCoreMultiProcessing.setStatus("current")
_CfprApBiosVfDRAMClockThrottlingTable_Object = MibTable
cfprApBiosVfDRAMClockThrottlingTable = _CfprApBiosVfDRAMClockThrottlingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 21)
)
if mibBuilder.loadTexts:
    cfprApBiosVfDRAMClockThrottlingTable.setStatus("current")
_CfprApBiosVfDRAMClockThrottlingEntry_Object = MibTableRow
cfprApBiosVfDRAMClockThrottlingEntry = _CfprApBiosVfDRAMClockThrottlingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 21, 1)
)
cfprApBiosVfDRAMClockThrottlingEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfDRAMClockThrottlingInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfDRAMClockThrottlingEntry.setStatus("current")
_CfprApBiosVfDRAMClockThrottlingInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfDRAMClockThrottlingInstanceId_Object = MibTableColumn
cfprApBiosVfDRAMClockThrottlingInstanceId = _CfprApBiosVfDRAMClockThrottlingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 21, 1, 1),
    _CfprApBiosVfDRAMClockThrottlingInstanceId_Type()
)
cfprApBiosVfDRAMClockThrottlingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfDRAMClockThrottlingInstanceId.setStatus("current")
_CfprApBiosVfDRAMClockThrottlingDn_Type = CfprApManagedObjectDn
_CfprApBiosVfDRAMClockThrottlingDn_Object = MibTableColumn
cfprApBiosVfDRAMClockThrottlingDn = _CfprApBiosVfDRAMClockThrottlingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 21, 1, 2),
    _CfprApBiosVfDRAMClockThrottlingDn_Type()
)
cfprApBiosVfDRAMClockThrottlingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfDRAMClockThrottlingDn.setStatus("current")
_CfprApBiosVfDRAMClockThrottlingRn_Type = SnmpAdminString
_CfprApBiosVfDRAMClockThrottlingRn_Object = MibTableColumn
cfprApBiosVfDRAMClockThrottlingRn = _CfprApBiosVfDRAMClockThrottlingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 21, 1, 3),
    _CfprApBiosVfDRAMClockThrottlingRn_Type()
)
cfprApBiosVfDRAMClockThrottlingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfDRAMClockThrottlingRn.setStatus("current")
_CfprApBiosVfDRAMClockThrottlingVpDRAMClockThrottling_Type = CfprApBiosVfDRAMClockThrottlingVpDRAMClockThrottling
_CfprApBiosVfDRAMClockThrottlingVpDRAMClockThrottling_Object = MibTableColumn
cfprApBiosVfDRAMClockThrottlingVpDRAMClockThrottling = _CfprApBiosVfDRAMClockThrottlingVpDRAMClockThrottling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 21, 1, 4),
    _CfprApBiosVfDRAMClockThrottlingVpDRAMClockThrottling_Type()
)
cfprApBiosVfDRAMClockThrottlingVpDRAMClockThrottling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfDRAMClockThrottlingVpDRAMClockThrottling.setStatus("current")
_CfprApBiosVfDirectCacheAccessTable_Object = MibTable
cfprApBiosVfDirectCacheAccessTable = _CfprApBiosVfDirectCacheAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 22)
)
if mibBuilder.loadTexts:
    cfprApBiosVfDirectCacheAccessTable.setStatus("current")
_CfprApBiosVfDirectCacheAccessEntry_Object = MibTableRow
cfprApBiosVfDirectCacheAccessEntry = _CfprApBiosVfDirectCacheAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 22, 1)
)
cfprApBiosVfDirectCacheAccessEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfDirectCacheAccessInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfDirectCacheAccessEntry.setStatus("current")
_CfprApBiosVfDirectCacheAccessInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfDirectCacheAccessInstanceId_Object = MibTableColumn
cfprApBiosVfDirectCacheAccessInstanceId = _CfprApBiosVfDirectCacheAccessInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 22, 1, 1),
    _CfprApBiosVfDirectCacheAccessInstanceId_Type()
)
cfprApBiosVfDirectCacheAccessInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfDirectCacheAccessInstanceId.setStatus("current")
_CfprApBiosVfDirectCacheAccessDn_Type = CfprApManagedObjectDn
_CfprApBiosVfDirectCacheAccessDn_Object = MibTableColumn
cfprApBiosVfDirectCacheAccessDn = _CfprApBiosVfDirectCacheAccessDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 22, 1, 2),
    _CfprApBiosVfDirectCacheAccessDn_Type()
)
cfprApBiosVfDirectCacheAccessDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfDirectCacheAccessDn.setStatus("current")
_CfprApBiosVfDirectCacheAccessRn_Type = SnmpAdminString
_CfprApBiosVfDirectCacheAccessRn_Object = MibTableColumn
cfprApBiosVfDirectCacheAccessRn = _CfprApBiosVfDirectCacheAccessRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 22, 1, 3),
    _CfprApBiosVfDirectCacheAccessRn_Type()
)
cfprApBiosVfDirectCacheAccessRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfDirectCacheAccessRn.setStatus("current")
_CfprApBiosVfDirectCacheAccessVpDirectCacheAccess_Type = CfprApBiosVfDirectCacheAccessVpDirectCacheAccess
_CfprApBiosVfDirectCacheAccessVpDirectCacheAccess_Object = MibTableColumn
cfprApBiosVfDirectCacheAccessVpDirectCacheAccess = _CfprApBiosVfDirectCacheAccessVpDirectCacheAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 22, 1, 4),
    _CfprApBiosVfDirectCacheAccessVpDirectCacheAccess_Type()
)
cfprApBiosVfDirectCacheAccessVpDirectCacheAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfDirectCacheAccessVpDirectCacheAccess.setStatus("current")
_CfprApBiosVfDramRefreshRateTable_Object = MibTable
cfprApBiosVfDramRefreshRateTable = _CfprApBiosVfDramRefreshRateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 23)
)
if mibBuilder.loadTexts:
    cfprApBiosVfDramRefreshRateTable.setStatus("current")
_CfprApBiosVfDramRefreshRateEntry_Object = MibTableRow
cfprApBiosVfDramRefreshRateEntry = _CfprApBiosVfDramRefreshRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 23, 1)
)
cfprApBiosVfDramRefreshRateEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfDramRefreshRateInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfDramRefreshRateEntry.setStatus("current")
_CfprApBiosVfDramRefreshRateInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfDramRefreshRateInstanceId_Object = MibTableColumn
cfprApBiosVfDramRefreshRateInstanceId = _CfprApBiosVfDramRefreshRateInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 23, 1, 1),
    _CfprApBiosVfDramRefreshRateInstanceId_Type()
)
cfprApBiosVfDramRefreshRateInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfDramRefreshRateInstanceId.setStatus("current")
_CfprApBiosVfDramRefreshRateDn_Type = CfprApManagedObjectDn
_CfprApBiosVfDramRefreshRateDn_Object = MibTableColumn
cfprApBiosVfDramRefreshRateDn = _CfprApBiosVfDramRefreshRateDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 23, 1, 2),
    _CfprApBiosVfDramRefreshRateDn_Type()
)
cfprApBiosVfDramRefreshRateDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfDramRefreshRateDn.setStatus("current")
_CfprApBiosVfDramRefreshRateRn_Type = SnmpAdminString
_CfprApBiosVfDramRefreshRateRn_Object = MibTableColumn
cfprApBiosVfDramRefreshRateRn = _CfprApBiosVfDramRefreshRateRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 23, 1, 3),
    _CfprApBiosVfDramRefreshRateRn_Type()
)
cfprApBiosVfDramRefreshRateRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfDramRefreshRateRn.setStatus("current")
_CfprApBiosVfDramRefreshRateVpDramRefreshRate_Type = CfprApBiosVfDramRefreshRateVpDramRefreshRate
_CfprApBiosVfDramRefreshRateVpDramRefreshRate_Object = MibTableColumn
cfprApBiosVfDramRefreshRateVpDramRefreshRate = _CfprApBiosVfDramRefreshRateVpDramRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 23, 1, 4),
    _CfprApBiosVfDramRefreshRateVpDramRefreshRate_Type()
)
cfprApBiosVfDramRefreshRateVpDramRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfDramRefreshRateVpDramRefreshRate.setStatus("current")
_CfprApBiosVfEnhancedIntelSpeedStepTechTable_Object = MibTable
cfprApBiosVfEnhancedIntelSpeedStepTechTable = _CfprApBiosVfEnhancedIntelSpeedStepTechTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 24)
)
if mibBuilder.loadTexts:
    cfprApBiosVfEnhancedIntelSpeedStepTechTable.setStatus("current")
_CfprApBiosVfEnhancedIntelSpeedStepTechEntry_Object = MibTableRow
cfprApBiosVfEnhancedIntelSpeedStepTechEntry = _CfprApBiosVfEnhancedIntelSpeedStepTechEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 24, 1)
)
cfprApBiosVfEnhancedIntelSpeedStepTechEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfEnhancedIntelSpeedStepTechInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfEnhancedIntelSpeedStepTechEntry.setStatus("current")
_CfprApBiosVfEnhancedIntelSpeedStepTechInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfEnhancedIntelSpeedStepTechInstanceId_Object = MibTableColumn
cfprApBiosVfEnhancedIntelSpeedStepTechInstanceId = _CfprApBiosVfEnhancedIntelSpeedStepTechInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 24, 1, 1),
    _CfprApBiosVfEnhancedIntelSpeedStepTechInstanceId_Type()
)
cfprApBiosVfEnhancedIntelSpeedStepTechInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfEnhancedIntelSpeedStepTechInstanceId.setStatus("current")
_CfprApBiosVfEnhancedIntelSpeedStepTechDn_Type = CfprApManagedObjectDn
_CfprApBiosVfEnhancedIntelSpeedStepTechDn_Object = MibTableColumn
cfprApBiosVfEnhancedIntelSpeedStepTechDn = _CfprApBiosVfEnhancedIntelSpeedStepTechDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 24, 1, 2),
    _CfprApBiosVfEnhancedIntelSpeedStepTechDn_Type()
)
cfprApBiosVfEnhancedIntelSpeedStepTechDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfEnhancedIntelSpeedStepTechDn.setStatus("current")
_CfprApBiosVfEnhancedIntelSpeedStepTechRn_Type = SnmpAdminString
_CfprApBiosVfEnhancedIntelSpeedStepTechRn_Object = MibTableColumn
cfprApBiosVfEnhancedIntelSpeedStepTechRn = _CfprApBiosVfEnhancedIntelSpeedStepTechRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 24, 1, 3),
    _CfprApBiosVfEnhancedIntelSpeedStepTechRn_Type()
)
cfprApBiosVfEnhancedIntelSpeedStepTechRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfEnhancedIntelSpeedStepTechRn.setStatus("current")
_CfprApBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech_Type = CfprApBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech
_CfprApBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech_Object = MibTableColumn
cfprApBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech = _CfprApBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 24, 1, 4),
    _CfprApBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech_Type()
)
cfprApBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech.setStatus("current")
_CfprApBiosVfExecuteDisableBitTable_Object = MibTable
cfprApBiosVfExecuteDisableBitTable = _CfprApBiosVfExecuteDisableBitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 25)
)
if mibBuilder.loadTexts:
    cfprApBiosVfExecuteDisableBitTable.setStatus("current")
_CfprApBiosVfExecuteDisableBitEntry_Object = MibTableRow
cfprApBiosVfExecuteDisableBitEntry = _CfprApBiosVfExecuteDisableBitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 25, 1)
)
cfprApBiosVfExecuteDisableBitEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfExecuteDisableBitInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfExecuteDisableBitEntry.setStatus("current")
_CfprApBiosVfExecuteDisableBitInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfExecuteDisableBitInstanceId_Object = MibTableColumn
cfprApBiosVfExecuteDisableBitInstanceId = _CfprApBiosVfExecuteDisableBitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 25, 1, 1),
    _CfprApBiosVfExecuteDisableBitInstanceId_Type()
)
cfprApBiosVfExecuteDisableBitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfExecuteDisableBitInstanceId.setStatus("current")
_CfprApBiosVfExecuteDisableBitDn_Type = CfprApManagedObjectDn
_CfprApBiosVfExecuteDisableBitDn_Object = MibTableColumn
cfprApBiosVfExecuteDisableBitDn = _CfprApBiosVfExecuteDisableBitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 25, 1, 2),
    _CfprApBiosVfExecuteDisableBitDn_Type()
)
cfprApBiosVfExecuteDisableBitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfExecuteDisableBitDn.setStatus("current")
_CfprApBiosVfExecuteDisableBitRn_Type = SnmpAdminString
_CfprApBiosVfExecuteDisableBitRn_Object = MibTableColumn
cfprApBiosVfExecuteDisableBitRn = _CfprApBiosVfExecuteDisableBitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 25, 1, 3),
    _CfprApBiosVfExecuteDisableBitRn_Type()
)
cfprApBiosVfExecuteDisableBitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfExecuteDisableBitRn.setStatus("current")
_CfprApBiosVfExecuteDisableBitVpExecuteDisableBit_Type = CfprApBiosVfExecuteDisableBitVpExecuteDisableBit
_CfprApBiosVfExecuteDisableBitVpExecuteDisableBit_Object = MibTableColumn
cfprApBiosVfExecuteDisableBitVpExecuteDisableBit = _CfprApBiosVfExecuteDisableBitVpExecuteDisableBit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 25, 1, 4),
    _CfprApBiosVfExecuteDisableBitVpExecuteDisableBit_Type()
)
cfprApBiosVfExecuteDisableBitVpExecuteDisableBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfExecuteDisableBitVpExecuteDisableBit.setStatus("current")
_CfprApBiosVfFRB2TimerTable_Object = MibTable
cfprApBiosVfFRB2TimerTable = _CfprApBiosVfFRB2TimerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 26)
)
if mibBuilder.loadTexts:
    cfprApBiosVfFRB2TimerTable.setStatus("current")
_CfprApBiosVfFRB2TimerEntry_Object = MibTableRow
cfprApBiosVfFRB2TimerEntry = _CfprApBiosVfFRB2TimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 26, 1)
)
cfprApBiosVfFRB2TimerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfFRB2TimerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfFRB2TimerEntry.setStatus("current")
_CfprApBiosVfFRB2TimerInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfFRB2TimerInstanceId_Object = MibTableColumn
cfprApBiosVfFRB2TimerInstanceId = _CfprApBiosVfFRB2TimerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 26, 1, 1),
    _CfprApBiosVfFRB2TimerInstanceId_Type()
)
cfprApBiosVfFRB2TimerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfFRB2TimerInstanceId.setStatus("current")
_CfprApBiosVfFRB2TimerDn_Type = CfprApManagedObjectDn
_CfprApBiosVfFRB2TimerDn_Object = MibTableColumn
cfprApBiosVfFRB2TimerDn = _CfprApBiosVfFRB2TimerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 26, 1, 2),
    _CfprApBiosVfFRB2TimerDn_Type()
)
cfprApBiosVfFRB2TimerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfFRB2TimerDn.setStatus("current")
_CfprApBiosVfFRB2TimerRn_Type = SnmpAdminString
_CfprApBiosVfFRB2TimerRn_Object = MibTableColumn
cfprApBiosVfFRB2TimerRn = _CfprApBiosVfFRB2TimerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 26, 1, 3),
    _CfprApBiosVfFRB2TimerRn_Type()
)
cfprApBiosVfFRB2TimerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfFRB2TimerRn.setStatus("current")
_CfprApBiosVfFRB2TimerVpFRB2Timer_Type = CfprApBiosVfFRB2TimerVpFRB2Timer
_CfprApBiosVfFRB2TimerVpFRB2Timer_Object = MibTableColumn
cfprApBiosVfFRB2TimerVpFRB2Timer = _CfprApBiosVfFRB2TimerVpFRB2Timer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 26, 1, 4),
    _CfprApBiosVfFRB2TimerVpFRB2Timer_Type()
)
cfprApBiosVfFRB2TimerVpFRB2Timer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfFRB2TimerVpFRB2Timer.setStatus("current")
_CfprApBiosVfFrequencyFloorOverrideTable_Object = MibTable
cfprApBiosVfFrequencyFloorOverrideTable = _CfprApBiosVfFrequencyFloorOverrideTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 27)
)
if mibBuilder.loadTexts:
    cfprApBiosVfFrequencyFloorOverrideTable.setStatus("current")
_CfprApBiosVfFrequencyFloorOverrideEntry_Object = MibTableRow
cfprApBiosVfFrequencyFloorOverrideEntry = _CfprApBiosVfFrequencyFloorOverrideEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 27, 1)
)
cfprApBiosVfFrequencyFloorOverrideEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfFrequencyFloorOverrideInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfFrequencyFloorOverrideEntry.setStatus("current")
_CfprApBiosVfFrequencyFloorOverrideInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfFrequencyFloorOverrideInstanceId_Object = MibTableColumn
cfprApBiosVfFrequencyFloorOverrideInstanceId = _CfprApBiosVfFrequencyFloorOverrideInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 27, 1, 1),
    _CfprApBiosVfFrequencyFloorOverrideInstanceId_Type()
)
cfprApBiosVfFrequencyFloorOverrideInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfFrequencyFloorOverrideInstanceId.setStatus("current")
_CfprApBiosVfFrequencyFloorOverrideDn_Type = CfprApManagedObjectDn
_CfprApBiosVfFrequencyFloorOverrideDn_Object = MibTableColumn
cfprApBiosVfFrequencyFloorOverrideDn = _CfprApBiosVfFrequencyFloorOverrideDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 27, 1, 2),
    _CfprApBiosVfFrequencyFloorOverrideDn_Type()
)
cfprApBiosVfFrequencyFloorOverrideDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfFrequencyFloorOverrideDn.setStatus("current")
_CfprApBiosVfFrequencyFloorOverrideRn_Type = SnmpAdminString
_CfprApBiosVfFrequencyFloorOverrideRn_Object = MibTableColumn
cfprApBiosVfFrequencyFloorOverrideRn = _CfprApBiosVfFrequencyFloorOverrideRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 27, 1, 3),
    _CfprApBiosVfFrequencyFloorOverrideRn_Type()
)
cfprApBiosVfFrequencyFloorOverrideRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfFrequencyFloorOverrideRn.setStatus("current")
_CfprApBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride_Type = CfprApBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride
_CfprApBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride_Object = MibTableColumn
cfprApBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride = _CfprApBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 27, 1, 4),
    _CfprApBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride_Type()
)
cfprApBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride.setStatus("current")
_CfprApBiosVfFrontPanelLockoutTable_Object = MibTable
cfprApBiosVfFrontPanelLockoutTable = _CfprApBiosVfFrontPanelLockoutTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 28)
)
if mibBuilder.loadTexts:
    cfprApBiosVfFrontPanelLockoutTable.setStatus("current")
_CfprApBiosVfFrontPanelLockoutEntry_Object = MibTableRow
cfprApBiosVfFrontPanelLockoutEntry = _CfprApBiosVfFrontPanelLockoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 28, 1)
)
cfprApBiosVfFrontPanelLockoutEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfFrontPanelLockoutInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfFrontPanelLockoutEntry.setStatus("current")
_CfprApBiosVfFrontPanelLockoutInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfFrontPanelLockoutInstanceId_Object = MibTableColumn
cfprApBiosVfFrontPanelLockoutInstanceId = _CfprApBiosVfFrontPanelLockoutInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 28, 1, 1),
    _CfprApBiosVfFrontPanelLockoutInstanceId_Type()
)
cfprApBiosVfFrontPanelLockoutInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfFrontPanelLockoutInstanceId.setStatus("current")
_CfprApBiosVfFrontPanelLockoutDn_Type = CfprApManagedObjectDn
_CfprApBiosVfFrontPanelLockoutDn_Object = MibTableColumn
cfprApBiosVfFrontPanelLockoutDn = _CfprApBiosVfFrontPanelLockoutDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 28, 1, 2),
    _CfprApBiosVfFrontPanelLockoutDn_Type()
)
cfprApBiosVfFrontPanelLockoutDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfFrontPanelLockoutDn.setStatus("current")
_CfprApBiosVfFrontPanelLockoutRn_Type = SnmpAdminString
_CfprApBiosVfFrontPanelLockoutRn_Object = MibTableColumn
cfprApBiosVfFrontPanelLockoutRn = _CfprApBiosVfFrontPanelLockoutRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 28, 1, 3),
    _CfprApBiosVfFrontPanelLockoutRn_Type()
)
cfprApBiosVfFrontPanelLockoutRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfFrontPanelLockoutRn.setStatus("current")
_CfprApBiosVfFrontPanelLockoutVpFrontPanelLockout_Type = CfprApBiosVfFrontPanelLockoutVpFrontPanelLockout
_CfprApBiosVfFrontPanelLockoutVpFrontPanelLockout_Object = MibTableColumn
cfprApBiosVfFrontPanelLockoutVpFrontPanelLockout = _CfprApBiosVfFrontPanelLockoutVpFrontPanelLockout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 28, 1, 4),
    _CfprApBiosVfFrontPanelLockoutVpFrontPanelLockout_Type()
)
cfprApBiosVfFrontPanelLockoutVpFrontPanelLockout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfFrontPanelLockoutVpFrontPanelLockout.setStatus("current")
_CfprApBiosVfIntelEntrySASRAIDModuleTable_Object = MibTable
cfprApBiosVfIntelEntrySASRAIDModuleTable = _CfprApBiosVfIntelEntrySASRAIDModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 29)
)
if mibBuilder.loadTexts:
    cfprApBiosVfIntelEntrySASRAIDModuleTable.setStatus("current")
_CfprApBiosVfIntelEntrySASRAIDModuleEntry_Object = MibTableRow
cfprApBiosVfIntelEntrySASRAIDModuleEntry = _CfprApBiosVfIntelEntrySASRAIDModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 29, 1)
)
cfprApBiosVfIntelEntrySASRAIDModuleEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfIntelEntrySASRAIDModuleInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfIntelEntrySASRAIDModuleEntry.setStatus("current")
_CfprApBiosVfIntelEntrySASRAIDModuleInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfIntelEntrySASRAIDModuleInstanceId_Object = MibTableColumn
cfprApBiosVfIntelEntrySASRAIDModuleInstanceId = _CfprApBiosVfIntelEntrySASRAIDModuleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 29, 1, 1),
    _CfprApBiosVfIntelEntrySASRAIDModuleInstanceId_Type()
)
cfprApBiosVfIntelEntrySASRAIDModuleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfIntelEntrySASRAIDModuleInstanceId.setStatus("current")
_CfprApBiosVfIntelEntrySASRAIDModuleDn_Type = CfprApManagedObjectDn
_CfprApBiosVfIntelEntrySASRAIDModuleDn_Object = MibTableColumn
cfprApBiosVfIntelEntrySASRAIDModuleDn = _CfprApBiosVfIntelEntrySASRAIDModuleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 29, 1, 2),
    _CfprApBiosVfIntelEntrySASRAIDModuleDn_Type()
)
cfprApBiosVfIntelEntrySASRAIDModuleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfIntelEntrySASRAIDModuleDn.setStatus("current")
_CfprApBiosVfIntelEntrySASRAIDModuleRn_Type = SnmpAdminString
_CfprApBiosVfIntelEntrySASRAIDModuleRn_Object = MibTableColumn
cfprApBiosVfIntelEntrySASRAIDModuleRn = _CfprApBiosVfIntelEntrySASRAIDModuleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 29, 1, 3),
    _CfprApBiosVfIntelEntrySASRAIDModuleRn_Type()
)
cfprApBiosVfIntelEntrySASRAIDModuleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfIntelEntrySASRAIDModuleRn.setStatus("current")
_CfprApBiosVfIntelEntrySASRAIDModuleVpSASRAID_Type = CfprApBiosVfIntelEntrySASRAIDModuleVpSASRAID
_CfprApBiosVfIntelEntrySASRAIDModuleVpSASRAID_Object = MibTableColumn
cfprApBiosVfIntelEntrySASRAIDModuleVpSASRAID = _CfprApBiosVfIntelEntrySASRAIDModuleVpSASRAID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 29, 1, 4),
    _CfprApBiosVfIntelEntrySASRAIDModuleVpSASRAID_Type()
)
cfprApBiosVfIntelEntrySASRAIDModuleVpSASRAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfIntelEntrySASRAIDModuleVpSASRAID.setStatus("current")
_CfprApBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule_Type = CfprApBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule
_CfprApBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule_Object = MibTableColumn
cfprApBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule = _CfprApBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 29, 1, 5),
    _CfprApBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule_Type()
)
cfprApBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule.setStatus("current")
_CfprApBiosVfIntelHyperThreadingTechTable_Object = MibTable
cfprApBiosVfIntelHyperThreadingTechTable = _CfprApBiosVfIntelHyperThreadingTechTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 30)
)
if mibBuilder.loadTexts:
    cfprApBiosVfIntelHyperThreadingTechTable.setStatus("current")
_CfprApBiosVfIntelHyperThreadingTechEntry_Object = MibTableRow
cfprApBiosVfIntelHyperThreadingTechEntry = _CfprApBiosVfIntelHyperThreadingTechEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 30, 1)
)
cfprApBiosVfIntelHyperThreadingTechEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfIntelHyperThreadingTechInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfIntelHyperThreadingTechEntry.setStatus("current")
_CfprApBiosVfIntelHyperThreadingTechInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfIntelHyperThreadingTechInstanceId_Object = MibTableColumn
cfprApBiosVfIntelHyperThreadingTechInstanceId = _CfprApBiosVfIntelHyperThreadingTechInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 30, 1, 1),
    _CfprApBiosVfIntelHyperThreadingTechInstanceId_Type()
)
cfprApBiosVfIntelHyperThreadingTechInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfIntelHyperThreadingTechInstanceId.setStatus("current")
_CfprApBiosVfIntelHyperThreadingTechDn_Type = CfprApManagedObjectDn
_CfprApBiosVfIntelHyperThreadingTechDn_Object = MibTableColumn
cfprApBiosVfIntelHyperThreadingTechDn = _CfprApBiosVfIntelHyperThreadingTechDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 30, 1, 2),
    _CfprApBiosVfIntelHyperThreadingTechDn_Type()
)
cfprApBiosVfIntelHyperThreadingTechDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfIntelHyperThreadingTechDn.setStatus("current")
_CfprApBiosVfIntelHyperThreadingTechRn_Type = SnmpAdminString
_CfprApBiosVfIntelHyperThreadingTechRn_Object = MibTableColumn
cfprApBiosVfIntelHyperThreadingTechRn = _CfprApBiosVfIntelHyperThreadingTechRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 30, 1, 3),
    _CfprApBiosVfIntelHyperThreadingTechRn_Type()
)
cfprApBiosVfIntelHyperThreadingTechRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfIntelHyperThreadingTechRn.setStatus("current")
_CfprApBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech_Type = CfprApBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech
_CfprApBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech_Object = MibTableColumn
cfprApBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech = _CfprApBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 30, 1, 4),
    _CfprApBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech_Type()
)
cfprApBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech.setStatus("current")
_CfprApBiosVfIntelTurboBoostTechTable_Object = MibTable
cfprApBiosVfIntelTurboBoostTechTable = _CfprApBiosVfIntelTurboBoostTechTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 31)
)
if mibBuilder.loadTexts:
    cfprApBiosVfIntelTurboBoostTechTable.setStatus("current")
_CfprApBiosVfIntelTurboBoostTechEntry_Object = MibTableRow
cfprApBiosVfIntelTurboBoostTechEntry = _CfprApBiosVfIntelTurboBoostTechEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 31, 1)
)
cfprApBiosVfIntelTurboBoostTechEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfIntelTurboBoostTechInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfIntelTurboBoostTechEntry.setStatus("current")
_CfprApBiosVfIntelTurboBoostTechInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfIntelTurboBoostTechInstanceId_Object = MibTableColumn
cfprApBiosVfIntelTurboBoostTechInstanceId = _CfprApBiosVfIntelTurboBoostTechInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 31, 1, 1),
    _CfprApBiosVfIntelTurboBoostTechInstanceId_Type()
)
cfprApBiosVfIntelTurboBoostTechInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfIntelTurboBoostTechInstanceId.setStatus("current")
_CfprApBiosVfIntelTurboBoostTechDn_Type = CfprApManagedObjectDn
_CfprApBiosVfIntelTurboBoostTechDn_Object = MibTableColumn
cfprApBiosVfIntelTurboBoostTechDn = _CfprApBiosVfIntelTurboBoostTechDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 31, 1, 2),
    _CfprApBiosVfIntelTurboBoostTechDn_Type()
)
cfprApBiosVfIntelTurboBoostTechDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfIntelTurboBoostTechDn.setStatus("current")
_CfprApBiosVfIntelTurboBoostTechRn_Type = SnmpAdminString
_CfprApBiosVfIntelTurboBoostTechRn_Object = MibTableColumn
cfprApBiosVfIntelTurboBoostTechRn = _CfprApBiosVfIntelTurboBoostTechRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 31, 1, 3),
    _CfprApBiosVfIntelTurboBoostTechRn_Type()
)
cfprApBiosVfIntelTurboBoostTechRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfIntelTurboBoostTechRn.setStatus("current")
_CfprApBiosVfIntelTurboBoostTechVpIntelTurboBoostTech_Type = CfprApBiosVfIntelTurboBoostTechVpIntelTurboBoostTech
_CfprApBiosVfIntelTurboBoostTechVpIntelTurboBoostTech_Object = MibTableColumn
cfprApBiosVfIntelTurboBoostTechVpIntelTurboBoostTech = _CfprApBiosVfIntelTurboBoostTechVpIntelTurboBoostTech_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 31, 1, 4),
    _CfprApBiosVfIntelTurboBoostTechVpIntelTurboBoostTech_Type()
)
cfprApBiosVfIntelTurboBoostTechVpIntelTurboBoostTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfIntelTurboBoostTechVpIntelTurboBoostTech.setStatus("current")
_CfprApBiosVfIntelVTForDirectedIOTable_Object = MibTable
cfprApBiosVfIntelVTForDirectedIOTable = _CfprApBiosVfIntelVTForDirectedIOTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 32)
)
if mibBuilder.loadTexts:
    cfprApBiosVfIntelVTForDirectedIOTable.setStatus("current")
_CfprApBiosVfIntelVTForDirectedIOEntry_Object = MibTableRow
cfprApBiosVfIntelVTForDirectedIOEntry = _CfprApBiosVfIntelVTForDirectedIOEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 32, 1)
)
cfprApBiosVfIntelVTForDirectedIOEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfIntelVTForDirectedIOInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfIntelVTForDirectedIOEntry.setStatus("current")
_CfprApBiosVfIntelVTForDirectedIOInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfIntelVTForDirectedIOInstanceId_Object = MibTableColumn
cfprApBiosVfIntelVTForDirectedIOInstanceId = _CfprApBiosVfIntelVTForDirectedIOInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 32, 1, 1),
    _CfprApBiosVfIntelVTForDirectedIOInstanceId_Type()
)
cfprApBiosVfIntelVTForDirectedIOInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfIntelVTForDirectedIOInstanceId.setStatus("current")
_CfprApBiosVfIntelVTForDirectedIODn_Type = CfprApManagedObjectDn
_CfprApBiosVfIntelVTForDirectedIODn_Object = MibTableColumn
cfprApBiosVfIntelVTForDirectedIODn = _CfprApBiosVfIntelVTForDirectedIODn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 32, 1, 2),
    _CfprApBiosVfIntelVTForDirectedIODn_Type()
)
cfprApBiosVfIntelVTForDirectedIODn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfIntelVTForDirectedIODn.setStatus("current")
_CfprApBiosVfIntelVTForDirectedIORn_Type = SnmpAdminString
_CfprApBiosVfIntelVTForDirectedIORn_Object = MibTableColumn
cfprApBiosVfIntelVTForDirectedIORn = _CfprApBiosVfIntelVTForDirectedIORn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 32, 1, 3),
    _CfprApBiosVfIntelVTForDirectedIORn_Type()
)
cfprApBiosVfIntelVTForDirectedIORn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfIntelVTForDirectedIORn.setStatus("current")
_CfprApBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport_Type = CfprApBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport
_CfprApBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport_Object = MibTableColumn
cfprApBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport = _CfprApBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 32, 1, 4),
    _CfprApBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport_Type()
)
cfprApBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport.setStatus("current")
_CfprApBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport_Type = CfprApBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport
_CfprApBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport_Object = MibTableColumn
cfprApBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport = _CfprApBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 32, 1, 5),
    _CfprApBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport_Type()
)
cfprApBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport.setStatus("current")
_CfprApBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping_Type = CfprApBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping
_CfprApBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping_Object = MibTableColumn
cfprApBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping = _CfprApBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 32, 1, 6),
    _CfprApBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping_Type()
)
cfprApBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping.setStatus("current")
_CfprApBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport_Type = CfprApBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport
_CfprApBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport_Object = MibTableColumn
cfprApBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport = _CfprApBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 32, 1, 7),
    _CfprApBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport_Type()
)
cfprApBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport.setStatus("current")
_CfprApBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO_Type = CfprApBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO
_CfprApBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO_Object = MibTableColumn
cfprApBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO = _CfprApBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 32, 1, 8),
    _CfprApBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO_Type()
)
cfprApBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO.setStatus("current")
_CfprApBiosVfIntelVirtualizationTechnologyTable_Object = MibTable
cfprApBiosVfIntelVirtualizationTechnologyTable = _CfprApBiosVfIntelVirtualizationTechnologyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 33)
)
if mibBuilder.loadTexts:
    cfprApBiosVfIntelVirtualizationTechnologyTable.setStatus("current")
_CfprApBiosVfIntelVirtualizationTechnologyEntry_Object = MibTableRow
cfprApBiosVfIntelVirtualizationTechnologyEntry = _CfprApBiosVfIntelVirtualizationTechnologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 33, 1)
)
cfprApBiosVfIntelVirtualizationTechnologyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfIntelVirtualizationTechnologyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfIntelVirtualizationTechnologyEntry.setStatus("current")
_CfprApBiosVfIntelVirtualizationTechnologyInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfIntelVirtualizationTechnologyInstanceId_Object = MibTableColumn
cfprApBiosVfIntelVirtualizationTechnologyInstanceId = _CfprApBiosVfIntelVirtualizationTechnologyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 33, 1, 1),
    _CfprApBiosVfIntelVirtualizationTechnologyInstanceId_Type()
)
cfprApBiosVfIntelVirtualizationTechnologyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfIntelVirtualizationTechnologyInstanceId.setStatus("current")
_CfprApBiosVfIntelVirtualizationTechnologyDn_Type = CfprApManagedObjectDn
_CfprApBiosVfIntelVirtualizationTechnologyDn_Object = MibTableColumn
cfprApBiosVfIntelVirtualizationTechnologyDn = _CfprApBiosVfIntelVirtualizationTechnologyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 33, 1, 2),
    _CfprApBiosVfIntelVirtualizationTechnologyDn_Type()
)
cfprApBiosVfIntelVirtualizationTechnologyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfIntelVirtualizationTechnologyDn.setStatus("current")
_CfprApBiosVfIntelVirtualizationTechnologyRn_Type = SnmpAdminString
_CfprApBiosVfIntelVirtualizationTechnologyRn_Object = MibTableColumn
cfprApBiosVfIntelVirtualizationTechnologyRn = _CfprApBiosVfIntelVirtualizationTechnologyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 33, 1, 3),
    _CfprApBiosVfIntelVirtualizationTechnologyRn_Type()
)
cfprApBiosVfIntelVirtualizationTechnologyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfIntelVirtualizationTechnologyRn.setStatus("current")
_CfprApBiosVfIntelVirtualizationTechnologyVpIntelVirtualizationTechnology_Type = CfprApBiosVfIntelVirtualizationTechnologyVpIntelVirtTechnology
_CfprApBiosVfIntelVirtualizationTechnologyVpIntelVirtualizationTechnology_Object = MibTableColumn
cfprApBiosVfIntelVirtualizationTechnologyVpIntelVirtualizationTechnology = _CfprApBiosVfIntelVirtualizationTechnologyVpIntelVirtualizationTechnology_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 33, 1, 4),
    _CfprApBiosVfIntelVirtualizationTechnologyVpIntelVirtualizationTechnology_Type()
)
cfprApBiosVfIntelVirtualizationTechnologyVpIntelVirtualizationTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfIntelVirtualizationTechnologyVpIntelVirtualizationTechnology.setStatus("current")
_CfprApBiosVfInterleaveConfigurationTable_Object = MibTable
cfprApBiosVfInterleaveConfigurationTable = _CfprApBiosVfInterleaveConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 34)
)
if mibBuilder.loadTexts:
    cfprApBiosVfInterleaveConfigurationTable.setStatus("current")
_CfprApBiosVfInterleaveConfigurationEntry_Object = MibTableRow
cfprApBiosVfInterleaveConfigurationEntry = _CfprApBiosVfInterleaveConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 34, 1)
)
cfprApBiosVfInterleaveConfigurationEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfInterleaveConfigurationInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfInterleaveConfigurationEntry.setStatus("current")
_CfprApBiosVfInterleaveConfigurationInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfInterleaveConfigurationInstanceId_Object = MibTableColumn
cfprApBiosVfInterleaveConfigurationInstanceId = _CfprApBiosVfInterleaveConfigurationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 34, 1, 1),
    _CfprApBiosVfInterleaveConfigurationInstanceId_Type()
)
cfprApBiosVfInterleaveConfigurationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfInterleaveConfigurationInstanceId.setStatus("current")
_CfprApBiosVfInterleaveConfigurationDn_Type = CfprApManagedObjectDn
_CfprApBiosVfInterleaveConfigurationDn_Object = MibTableColumn
cfprApBiosVfInterleaveConfigurationDn = _CfprApBiosVfInterleaveConfigurationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 34, 1, 2),
    _CfprApBiosVfInterleaveConfigurationDn_Type()
)
cfprApBiosVfInterleaveConfigurationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfInterleaveConfigurationDn.setStatus("current")
_CfprApBiosVfInterleaveConfigurationRn_Type = SnmpAdminString
_CfprApBiosVfInterleaveConfigurationRn_Object = MibTableColumn
cfprApBiosVfInterleaveConfigurationRn = _CfprApBiosVfInterleaveConfigurationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 34, 1, 3),
    _CfprApBiosVfInterleaveConfigurationRn_Type()
)
cfprApBiosVfInterleaveConfigurationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfInterleaveConfigurationRn.setStatus("current")
_CfprApBiosVfInterleaveConfigurationVpChannelInterleaving_Type = CfprApBiosVfInterleaveConfigurationVpChannelInterleaving
_CfprApBiosVfInterleaveConfigurationVpChannelInterleaving_Object = MibTableColumn
cfprApBiosVfInterleaveConfigurationVpChannelInterleaving = _CfprApBiosVfInterleaveConfigurationVpChannelInterleaving_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 34, 1, 4),
    _CfprApBiosVfInterleaveConfigurationVpChannelInterleaving_Type()
)
cfprApBiosVfInterleaveConfigurationVpChannelInterleaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfInterleaveConfigurationVpChannelInterleaving.setStatus("current")
_CfprApBiosVfInterleaveConfigurationVpMemoryInterleaving_Type = CfprApBiosVfInterleaveConfigurationVpMemoryInterleaving
_CfprApBiosVfInterleaveConfigurationVpMemoryInterleaving_Object = MibTableColumn
cfprApBiosVfInterleaveConfigurationVpMemoryInterleaving = _CfprApBiosVfInterleaveConfigurationVpMemoryInterleaving_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 34, 1, 5),
    _CfprApBiosVfInterleaveConfigurationVpMemoryInterleaving_Type()
)
cfprApBiosVfInterleaveConfigurationVpMemoryInterleaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfInterleaveConfigurationVpMemoryInterleaving.setStatus("current")
_CfprApBiosVfInterleaveConfigurationVpRankInterleaving_Type = CfprApBiosVfInterleaveConfigurationVpRankInterleaving
_CfprApBiosVfInterleaveConfigurationVpRankInterleaving_Object = MibTableColumn
cfprApBiosVfInterleaveConfigurationVpRankInterleaving = _CfprApBiosVfInterleaveConfigurationVpRankInterleaving_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 34, 1, 6),
    _CfprApBiosVfInterleaveConfigurationVpRankInterleaving_Type()
)
cfprApBiosVfInterleaveConfigurationVpRankInterleaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfInterleaveConfigurationVpRankInterleaving.setStatus("current")
_CfprApBiosVfLocalX2ApicTable_Object = MibTable
cfprApBiosVfLocalX2ApicTable = _CfprApBiosVfLocalX2ApicTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 35)
)
if mibBuilder.loadTexts:
    cfprApBiosVfLocalX2ApicTable.setStatus("current")
_CfprApBiosVfLocalX2ApicEntry_Object = MibTableRow
cfprApBiosVfLocalX2ApicEntry = _CfprApBiosVfLocalX2ApicEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 35, 1)
)
cfprApBiosVfLocalX2ApicEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfLocalX2ApicInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfLocalX2ApicEntry.setStatus("current")
_CfprApBiosVfLocalX2ApicInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfLocalX2ApicInstanceId_Object = MibTableColumn
cfprApBiosVfLocalX2ApicInstanceId = _CfprApBiosVfLocalX2ApicInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 35, 1, 1),
    _CfprApBiosVfLocalX2ApicInstanceId_Type()
)
cfprApBiosVfLocalX2ApicInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfLocalX2ApicInstanceId.setStatus("current")
_CfprApBiosVfLocalX2ApicDn_Type = CfprApManagedObjectDn
_CfprApBiosVfLocalX2ApicDn_Object = MibTableColumn
cfprApBiosVfLocalX2ApicDn = _CfprApBiosVfLocalX2ApicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 35, 1, 2),
    _CfprApBiosVfLocalX2ApicDn_Type()
)
cfprApBiosVfLocalX2ApicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfLocalX2ApicDn.setStatus("current")
_CfprApBiosVfLocalX2ApicRn_Type = SnmpAdminString
_CfprApBiosVfLocalX2ApicRn_Object = MibTableColumn
cfprApBiosVfLocalX2ApicRn = _CfprApBiosVfLocalX2ApicRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 35, 1, 3),
    _CfprApBiosVfLocalX2ApicRn_Type()
)
cfprApBiosVfLocalX2ApicRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfLocalX2ApicRn.setStatus("current")
_CfprApBiosVfLocalX2ApicVpLocalX2Apic_Type = CfprApBiosVfLocalX2ApicVpLocalX2Apic
_CfprApBiosVfLocalX2ApicVpLocalX2Apic_Object = MibTableColumn
cfprApBiosVfLocalX2ApicVpLocalX2Apic = _CfprApBiosVfLocalX2ApicVpLocalX2Apic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 35, 1, 4),
    _CfprApBiosVfLocalX2ApicVpLocalX2Apic_Type()
)
cfprApBiosVfLocalX2ApicVpLocalX2Apic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfLocalX2ApicVpLocalX2Apic.setStatus("current")
_CfprApBiosVfLvDIMMSupportTable_Object = MibTable
cfprApBiosVfLvDIMMSupportTable = _CfprApBiosVfLvDIMMSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 36)
)
if mibBuilder.loadTexts:
    cfprApBiosVfLvDIMMSupportTable.setStatus("current")
_CfprApBiosVfLvDIMMSupportEntry_Object = MibTableRow
cfprApBiosVfLvDIMMSupportEntry = _CfprApBiosVfLvDIMMSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 36, 1)
)
cfprApBiosVfLvDIMMSupportEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfLvDIMMSupportInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfLvDIMMSupportEntry.setStatus("current")
_CfprApBiosVfLvDIMMSupportInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfLvDIMMSupportInstanceId_Object = MibTableColumn
cfprApBiosVfLvDIMMSupportInstanceId = _CfprApBiosVfLvDIMMSupportInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 36, 1, 1),
    _CfprApBiosVfLvDIMMSupportInstanceId_Type()
)
cfprApBiosVfLvDIMMSupportInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfLvDIMMSupportInstanceId.setStatus("current")
_CfprApBiosVfLvDIMMSupportDn_Type = CfprApManagedObjectDn
_CfprApBiosVfLvDIMMSupportDn_Object = MibTableColumn
cfprApBiosVfLvDIMMSupportDn = _CfprApBiosVfLvDIMMSupportDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 36, 1, 2),
    _CfprApBiosVfLvDIMMSupportDn_Type()
)
cfprApBiosVfLvDIMMSupportDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfLvDIMMSupportDn.setStatus("current")
_CfprApBiosVfLvDIMMSupportRn_Type = SnmpAdminString
_CfprApBiosVfLvDIMMSupportRn_Object = MibTableColumn
cfprApBiosVfLvDIMMSupportRn = _CfprApBiosVfLvDIMMSupportRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 36, 1, 3),
    _CfprApBiosVfLvDIMMSupportRn_Type()
)
cfprApBiosVfLvDIMMSupportRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfLvDIMMSupportRn.setStatus("current")
_CfprApBiosVfLvDIMMSupportVpLvDDRMode_Type = CfprApBiosVfLvDIMMSupportVpLvDDRMode
_CfprApBiosVfLvDIMMSupportVpLvDDRMode_Object = MibTableColumn
cfprApBiosVfLvDIMMSupportVpLvDDRMode = _CfprApBiosVfLvDIMMSupportVpLvDDRMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 36, 1, 4),
    _CfprApBiosVfLvDIMMSupportVpLvDDRMode_Type()
)
cfprApBiosVfLvDIMMSupportVpLvDDRMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfLvDIMMSupportVpLvDDRMode.setStatus("current")
_CfprApBiosVfMaxVariableMTRRSettingTable_Object = MibTable
cfprApBiosVfMaxVariableMTRRSettingTable = _CfprApBiosVfMaxVariableMTRRSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 37)
)
if mibBuilder.loadTexts:
    cfprApBiosVfMaxVariableMTRRSettingTable.setStatus("current")
_CfprApBiosVfMaxVariableMTRRSettingEntry_Object = MibTableRow
cfprApBiosVfMaxVariableMTRRSettingEntry = _CfprApBiosVfMaxVariableMTRRSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 37, 1)
)
cfprApBiosVfMaxVariableMTRRSettingEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfMaxVariableMTRRSettingInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfMaxVariableMTRRSettingEntry.setStatus("current")
_CfprApBiosVfMaxVariableMTRRSettingInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfMaxVariableMTRRSettingInstanceId_Object = MibTableColumn
cfprApBiosVfMaxVariableMTRRSettingInstanceId = _CfprApBiosVfMaxVariableMTRRSettingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 37, 1, 1),
    _CfprApBiosVfMaxVariableMTRRSettingInstanceId_Type()
)
cfprApBiosVfMaxVariableMTRRSettingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfMaxVariableMTRRSettingInstanceId.setStatus("current")
_CfprApBiosVfMaxVariableMTRRSettingDn_Type = CfprApManagedObjectDn
_CfprApBiosVfMaxVariableMTRRSettingDn_Object = MibTableColumn
cfprApBiosVfMaxVariableMTRRSettingDn = _CfprApBiosVfMaxVariableMTRRSettingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 37, 1, 2),
    _CfprApBiosVfMaxVariableMTRRSettingDn_Type()
)
cfprApBiosVfMaxVariableMTRRSettingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfMaxVariableMTRRSettingDn.setStatus("current")
_CfprApBiosVfMaxVariableMTRRSettingRn_Type = SnmpAdminString
_CfprApBiosVfMaxVariableMTRRSettingRn_Object = MibTableColumn
cfprApBiosVfMaxVariableMTRRSettingRn = _CfprApBiosVfMaxVariableMTRRSettingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 37, 1, 3),
    _CfprApBiosVfMaxVariableMTRRSettingRn_Type()
)
cfprApBiosVfMaxVariableMTRRSettingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfMaxVariableMTRRSettingRn.setStatus("current")
_CfprApBiosVfMaxVariableMTRRSettingVpProcessorMtrr_Type = CfprApBiosVfMaxVariableMTRRSettingVpProcessorMtrr
_CfprApBiosVfMaxVariableMTRRSettingVpProcessorMtrr_Object = MibTableColumn
cfprApBiosVfMaxVariableMTRRSettingVpProcessorMtrr = _CfprApBiosVfMaxVariableMTRRSettingVpProcessorMtrr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 37, 1, 4),
    _CfprApBiosVfMaxVariableMTRRSettingVpProcessorMtrr_Type()
)
cfprApBiosVfMaxVariableMTRRSettingVpProcessorMtrr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfMaxVariableMTRRSettingVpProcessorMtrr.setStatus("current")
_CfprApBiosVfMaximumMemoryBelow4GBTable_Object = MibTable
cfprApBiosVfMaximumMemoryBelow4GBTable = _CfprApBiosVfMaximumMemoryBelow4GBTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 38)
)
if mibBuilder.loadTexts:
    cfprApBiosVfMaximumMemoryBelow4GBTable.setStatus("current")
_CfprApBiosVfMaximumMemoryBelow4GBEntry_Object = MibTableRow
cfprApBiosVfMaximumMemoryBelow4GBEntry = _CfprApBiosVfMaximumMemoryBelow4GBEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 38, 1)
)
cfprApBiosVfMaximumMemoryBelow4GBEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfMaximumMemoryBelow4GBInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfMaximumMemoryBelow4GBEntry.setStatus("current")
_CfprApBiosVfMaximumMemoryBelow4GBInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfMaximumMemoryBelow4GBInstanceId_Object = MibTableColumn
cfprApBiosVfMaximumMemoryBelow4GBInstanceId = _CfprApBiosVfMaximumMemoryBelow4GBInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 38, 1, 1),
    _CfprApBiosVfMaximumMemoryBelow4GBInstanceId_Type()
)
cfprApBiosVfMaximumMemoryBelow4GBInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfMaximumMemoryBelow4GBInstanceId.setStatus("current")
_CfprApBiosVfMaximumMemoryBelow4GBDn_Type = CfprApManagedObjectDn
_CfprApBiosVfMaximumMemoryBelow4GBDn_Object = MibTableColumn
cfprApBiosVfMaximumMemoryBelow4GBDn = _CfprApBiosVfMaximumMemoryBelow4GBDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 38, 1, 2),
    _CfprApBiosVfMaximumMemoryBelow4GBDn_Type()
)
cfprApBiosVfMaximumMemoryBelow4GBDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfMaximumMemoryBelow4GBDn.setStatus("current")
_CfprApBiosVfMaximumMemoryBelow4GBRn_Type = SnmpAdminString
_CfprApBiosVfMaximumMemoryBelow4GBRn_Object = MibTableColumn
cfprApBiosVfMaximumMemoryBelow4GBRn = _CfprApBiosVfMaximumMemoryBelow4GBRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 38, 1, 3),
    _CfprApBiosVfMaximumMemoryBelow4GBRn_Type()
)
cfprApBiosVfMaximumMemoryBelow4GBRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfMaximumMemoryBelow4GBRn.setStatus("current")
_CfprApBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB_Type = CfprApBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB
_CfprApBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB_Object = MibTableColumn
cfprApBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB = _CfprApBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 38, 1, 4),
    _CfprApBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB_Type()
)
cfprApBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB.setStatus("current")
_CfprApBiosVfMemoryMappedIOAbove4GBTable_Object = MibTable
cfprApBiosVfMemoryMappedIOAbove4GBTable = _CfprApBiosVfMemoryMappedIOAbove4GBTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 39)
)
if mibBuilder.loadTexts:
    cfprApBiosVfMemoryMappedIOAbove4GBTable.setStatus("current")
_CfprApBiosVfMemoryMappedIOAbove4GBEntry_Object = MibTableRow
cfprApBiosVfMemoryMappedIOAbove4GBEntry = _CfprApBiosVfMemoryMappedIOAbove4GBEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 39, 1)
)
cfprApBiosVfMemoryMappedIOAbove4GBEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfMemoryMappedIOAbove4GBInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfMemoryMappedIOAbove4GBEntry.setStatus("current")
_CfprApBiosVfMemoryMappedIOAbove4GBInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfMemoryMappedIOAbove4GBInstanceId_Object = MibTableColumn
cfprApBiosVfMemoryMappedIOAbove4GBInstanceId = _CfprApBiosVfMemoryMappedIOAbove4GBInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 39, 1, 1),
    _CfprApBiosVfMemoryMappedIOAbove4GBInstanceId_Type()
)
cfprApBiosVfMemoryMappedIOAbove4GBInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfMemoryMappedIOAbove4GBInstanceId.setStatus("current")
_CfprApBiosVfMemoryMappedIOAbove4GBDn_Type = CfprApManagedObjectDn
_CfprApBiosVfMemoryMappedIOAbove4GBDn_Object = MibTableColumn
cfprApBiosVfMemoryMappedIOAbove4GBDn = _CfprApBiosVfMemoryMappedIOAbove4GBDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 39, 1, 2),
    _CfprApBiosVfMemoryMappedIOAbove4GBDn_Type()
)
cfprApBiosVfMemoryMappedIOAbove4GBDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfMemoryMappedIOAbove4GBDn.setStatus("current")
_CfprApBiosVfMemoryMappedIOAbove4GBRn_Type = SnmpAdminString
_CfprApBiosVfMemoryMappedIOAbove4GBRn_Object = MibTableColumn
cfprApBiosVfMemoryMappedIOAbove4GBRn = _CfprApBiosVfMemoryMappedIOAbove4GBRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 39, 1, 3),
    _CfprApBiosVfMemoryMappedIOAbove4GBRn_Type()
)
cfprApBiosVfMemoryMappedIOAbove4GBRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfMemoryMappedIOAbove4GBRn.setStatus("current")
_CfprApBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB_Type = CfprApBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB
_CfprApBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB_Object = MibTableColumn
cfprApBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB = _CfprApBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 39, 1, 4),
    _CfprApBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB_Type()
)
cfprApBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB.setStatus("current")
_CfprApBiosVfMirroringModeTable_Object = MibTable
cfprApBiosVfMirroringModeTable = _CfprApBiosVfMirroringModeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 40)
)
if mibBuilder.loadTexts:
    cfprApBiosVfMirroringModeTable.setStatus("current")
_CfprApBiosVfMirroringModeEntry_Object = MibTableRow
cfprApBiosVfMirroringModeEntry = _CfprApBiosVfMirroringModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 40, 1)
)
cfprApBiosVfMirroringModeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfMirroringModeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfMirroringModeEntry.setStatus("current")
_CfprApBiosVfMirroringModeInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfMirroringModeInstanceId_Object = MibTableColumn
cfprApBiosVfMirroringModeInstanceId = _CfprApBiosVfMirroringModeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 40, 1, 1),
    _CfprApBiosVfMirroringModeInstanceId_Type()
)
cfprApBiosVfMirroringModeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfMirroringModeInstanceId.setStatus("current")
_CfprApBiosVfMirroringModeDn_Type = CfprApManagedObjectDn
_CfprApBiosVfMirroringModeDn_Object = MibTableColumn
cfprApBiosVfMirroringModeDn = _CfprApBiosVfMirroringModeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 40, 1, 2),
    _CfprApBiosVfMirroringModeDn_Type()
)
cfprApBiosVfMirroringModeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfMirroringModeDn.setStatus("current")
_CfprApBiosVfMirroringModeRn_Type = SnmpAdminString
_CfprApBiosVfMirroringModeRn_Object = MibTableColumn
cfprApBiosVfMirroringModeRn = _CfprApBiosVfMirroringModeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 40, 1, 3),
    _CfprApBiosVfMirroringModeRn_Type()
)
cfprApBiosVfMirroringModeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfMirroringModeRn.setStatus("current")
_CfprApBiosVfMirroringModeVpMirroringMode_Type = CfprApBiosVfMirroringModeVpMirroringMode
_CfprApBiosVfMirroringModeVpMirroringMode_Object = MibTableColumn
cfprApBiosVfMirroringModeVpMirroringMode = _CfprApBiosVfMirroringModeVpMirroringMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 40, 1, 4),
    _CfprApBiosVfMirroringModeVpMirroringMode_Type()
)
cfprApBiosVfMirroringModeVpMirroringMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfMirroringModeVpMirroringMode.setStatus("current")
_CfprApBiosVfNUMAOptimizedTable_Object = MibTable
cfprApBiosVfNUMAOptimizedTable = _CfprApBiosVfNUMAOptimizedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 41)
)
if mibBuilder.loadTexts:
    cfprApBiosVfNUMAOptimizedTable.setStatus("current")
_CfprApBiosVfNUMAOptimizedEntry_Object = MibTableRow
cfprApBiosVfNUMAOptimizedEntry = _CfprApBiosVfNUMAOptimizedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 41, 1)
)
cfprApBiosVfNUMAOptimizedEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfNUMAOptimizedInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfNUMAOptimizedEntry.setStatus("current")
_CfprApBiosVfNUMAOptimizedInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfNUMAOptimizedInstanceId_Object = MibTableColumn
cfprApBiosVfNUMAOptimizedInstanceId = _CfprApBiosVfNUMAOptimizedInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 41, 1, 1),
    _CfprApBiosVfNUMAOptimizedInstanceId_Type()
)
cfprApBiosVfNUMAOptimizedInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfNUMAOptimizedInstanceId.setStatus("current")
_CfprApBiosVfNUMAOptimizedDn_Type = CfprApManagedObjectDn
_CfprApBiosVfNUMAOptimizedDn_Object = MibTableColumn
cfprApBiosVfNUMAOptimizedDn = _CfprApBiosVfNUMAOptimizedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 41, 1, 2),
    _CfprApBiosVfNUMAOptimizedDn_Type()
)
cfprApBiosVfNUMAOptimizedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfNUMAOptimizedDn.setStatus("current")
_CfprApBiosVfNUMAOptimizedRn_Type = SnmpAdminString
_CfprApBiosVfNUMAOptimizedRn_Object = MibTableColumn
cfprApBiosVfNUMAOptimizedRn = _CfprApBiosVfNUMAOptimizedRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 41, 1, 3),
    _CfprApBiosVfNUMAOptimizedRn_Type()
)
cfprApBiosVfNUMAOptimizedRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfNUMAOptimizedRn.setStatus("current")
_CfprApBiosVfNUMAOptimizedVpNUMAOptimized_Type = CfprApBiosVfNUMAOptimizedVpNUMAOptimized
_CfprApBiosVfNUMAOptimizedVpNUMAOptimized_Object = MibTableColumn
cfprApBiosVfNUMAOptimizedVpNUMAOptimized = _CfprApBiosVfNUMAOptimizedVpNUMAOptimized_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 41, 1, 4),
    _CfprApBiosVfNUMAOptimizedVpNUMAOptimized_Type()
)
cfprApBiosVfNUMAOptimizedVpNUMAOptimized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfNUMAOptimizedVpNUMAOptimized.setStatus("current")
_CfprApBiosVfOSBootWatchdogTimerTable_Object = MibTable
cfprApBiosVfOSBootWatchdogTimerTable = _CfprApBiosVfOSBootWatchdogTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 42)
)
if mibBuilder.loadTexts:
    cfprApBiosVfOSBootWatchdogTimerTable.setStatus("current")
_CfprApBiosVfOSBootWatchdogTimerEntry_Object = MibTableRow
cfprApBiosVfOSBootWatchdogTimerEntry = _CfprApBiosVfOSBootWatchdogTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 42, 1)
)
cfprApBiosVfOSBootWatchdogTimerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfOSBootWatchdogTimerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfOSBootWatchdogTimerEntry.setStatus("current")
_CfprApBiosVfOSBootWatchdogTimerInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfOSBootWatchdogTimerInstanceId_Object = MibTableColumn
cfprApBiosVfOSBootWatchdogTimerInstanceId = _CfprApBiosVfOSBootWatchdogTimerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 42, 1, 1),
    _CfprApBiosVfOSBootWatchdogTimerInstanceId_Type()
)
cfprApBiosVfOSBootWatchdogTimerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfOSBootWatchdogTimerInstanceId.setStatus("current")
_CfprApBiosVfOSBootWatchdogTimerDn_Type = CfprApManagedObjectDn
_CfprApBiosVfOSBootWatchdogTimerDn_Object = MibTableColumn
cfprApBiosVfOSBootWatchdogTimerDn = _CfprApBiosVfOSBootWatchdogTimerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 42, 1, 2),
    _CfprApBiosVfOSBootWatchdogTimerDn_Type()
)
cfprApBiosVfOSBootWatchdogTimerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfOSBootWatchdogTimerDn.setStatus("current")
_CfprApBiosVfOSBootWatchdogTimerRn_Type = SnmpAdminString
_CfprApBiosVfOSBootWatchdogTimerRn_Object = MibTableColumn
cfprApBiosVfOSBootWatchdogTimerRn = _CfprApBiosVfOSBootWatchdogTimerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 42, 1, 3),
    _CfprApBiosVfOSBootWatchdogTimerRn_Type()
)
cfprApBiosVfOSBootWatchdogTimerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfOSBootWatchdogTimerRn.setStatus("current")
_CfprApBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer_Type = CfprApBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer
_CfprApBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer_Object = MibTableColumn
cfprApBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer = _CfprApBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 42, 1, 4),
    _CfprApBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer_Type()
)
cfprApBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer.setStatus("current")
_CfprApBiosVfOSBootWatchdogTimerPolicyTable_Object = MibTable
cfprApBiosVfOSBootWatchdogTimerPolicyTable = _CfprApBiosVfOSBootWatchdogTimerPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 43)
)
if mibBuilder.loadTexts:
    cfprApBiosVfOSBootWatchdogTimerPolicyTable.setStatus("current")
_CfprApBiosVfOSBootWatchdogTimerPolicyEntry_Object = MibTableRow
cfprApBiosVfOSBootWatchdogTimerPolicyEntry = _CfprApBiosVfOSBootWatchdogTimerPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 43, 1)
)
cfprApBiosVfOSBootWatchdogTimerPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfOSBootWatchdogTimerPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfOSBootWatchdogTimerPolicyEntry.setStatus("current")
_CfprApBiosVfOSBootWatchdogTimerPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfOSBootWatchdogTimerPolicyInstanceId_Object = MibTableColumn
cfprApBiosVfOSBootWatchdogTimerPolicyInstanceId = _CfprApBiosVfOSBootWatchdogTimerPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 43, 1, 1),
    _CfprApBiosVfOSBootWatchdogTimerPolicyInstanceId_Type()
)
cfprApBiosVfOSBootWatchdogTimerPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfOSBootWatchdogTimerPolicyInstanceId.setStatus("current")
_CfprApBiosVfOSBootWatchdogTimerPolicyDn_Type = CfprApManagedObjectDn
_CfprApBiosVfOSBootWatchdogTimerPolicyDn_Object = MibTableColumn
cfprApBiosVfOSBootWatchdogTimerPolicyDn = _CfprApBiosVfOSBootWatchdogTimerPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 43, 1, 2),
    _CfprApBiosVfOSBootWatchdogTimerPolicyDn_Type()
)
cfprApBiosVfOSBootWatchdogTimerPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfOSBootWatchdogTimerPolicyDn.setStatus("current")
_CfprApBiosVfOSBootWatchdogTimerPolicyRn_Type = SnmpAdminString
_CfprApBiosVfOSBootWatchdogTimerPolicyRn_Object = MibTableColumn
cfprApBiosVfOSBootWatchdogTimerPolicyRn = _CfprApBiosVfOSBootWatchdogTimerPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 43, 1, 3),
    _CfprApBiosVfOSBootWatchdogTimerPolicyRn_Type()
)
cfprApBiosVfOSBootWatchdogTimerPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfOSBootWatchdogTimerPolicyRn.setStatus("current")
_CfprApBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy_Type = CfprApBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy
_CfprApBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy_Object = MibTableColumn
cfprApBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy = _CfprApBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 43, 1, 4),
    _CfprApBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy_Type()
)
cfprApBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy.setStatus("current")
_CfprApBiosVfOSBootWatchdogTimerTimeoutTable_Object = MibTable
cfprApBiosVfOSBootWatchdogTimerTimeoutTable = _CfprApBiosVfOSBootWatchdogTimerTimeoutTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 44)
)
if mibBuilder.loadTexts:
    cfprApBiosVfOSBootWatchdogTimerTimeoutTable.setStatus("current")
_CfprApBiosVfOSBootWatchdogTimerTimeoutEntry_Object = MibTableRow
cfprApBiosVfOSBootWatchdogTimerTimeoutEntry = _CfprApBiosVfOSBootWatchdogTimerTimeoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 44, 1)
)
cfprApBiosVfOSBootWatchdogTimerTimeoutEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfOSBootWatchdogTimerTimeoutInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfOSBootWatchdogTimerTimeoutEntry.setStatus("current")
_CfprApBiosVfOSBootWatchdogTimerTimeoutInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfOSBootWatchdogTimerTimeoutInstanceId_Object = MibTableColumn
cfprApBiosVfOSBootWatchdogTimerTimeoutInstanceId = _CfprApBiosVfOSBootWatchdogTimerTimeoutInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 44, 1, 1),
    _CfprApBiosVfOSBootWatchdogTimerTimeoutInstanceId_Type()
)
cfprApBiosVfOSBootWatchdogTimerTimeoutInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfOSBootWatchdogTimerTimeoutInstanceId.setStatus("current")
_CfprApBiosVfOSBootWatchdogTimerTimeoutDn_Type = CfprApManagedObjectDn
_CfprApBiosVfOSBootWatchdogTimerTimeoutDn_Object = MibTableColumn
cfprApBiosVfOSBootWatchdogTimerTimeoutDn = _CfprApBiosVfOSBootWatchdogTimerTimeoutDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 44, 1, 2),
    _CfprApBiosVfOSBootWatchdogTimerTimeoutDn_Type()
)
cfprApBiosVfOSBootWatchdogTimerTimeoutDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfOSBootWatchdogTimerTimeoutDn.setStatus("current")
_CfprApBiosVfOSBootWatchdogTimerTimeoutRn_Type = SnmpAdminString
_CfprApBiosVfOSBootWatchdogTimerTimeoutRn_Object = MibTableColumn
cfprApBiosVfOSBootWatchdogTimerTimeoutRn = _CfprApBiosVfOSBootWatchdogTimerTimeoutRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 44, 1, 3),
    _CfprApBiosVfOSBootWatchdogTimerTimeoutRn_Type()
)
cfprApBiosVfOSBootWatchdogTimerTimeoutRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfOSBootWatchdogTimerTimeoutRn.setStatus("current")
_CfprApBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout_Type = CfprApBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout
_CfprApBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout_Object = MibTableColumn
cfprApBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout = _CfprApBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 44, 1, 4),
    _CfprApBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout_Type()
)
cfprApBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout.setStatus("current")
_CfprApBiosVfOnboardSATAControllerTable_Object = MibTable
cfprApBiosVfOnboardSATAControllerTable = _CfprApBiosVfOnboardSATAControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 45)
)
if mibBuilder.loadTexts:
    cfprApBiosVfOnboardSATAControllerTable.setStatus("current")
_CfprApBiosVfOnboardSATAControllerEntry_Object = MibTableRow
cfprApBiosVfOnboardSATAControllerEntry = _CfprApBiosVfOnboardSATAControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 45, 1)
)
cfprApBiosVfOnboardSATAControllerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfOnboardSATAControllerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfOnboardSATAControllerEntry.setStatus("current")
_CfprApBiosVfOnboardSATAControllerInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfOnboardSATAControllerInstanceId_Object = MibTableColumn
cfprApBiosVfOnboardSATAControllerInstanceId = _CfprApBiosVfOnboardSATAControllerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 45, 1, 1),
    _CfprApBiosVfOnboardSATAControllerInstanceId_Type()
)
cfprApBiosVfOnboardSATAControllerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfOnboardSATAControllerInstanceId.setStatus("current")
_CfprApBiosVfOnboardSATAControllerDn_Type = CfprApManagedObjectDn
_CfprApBiosVfOnboardSATAControllerDn_Object = MibTableColumn
cfprApBiosVfOnboardSATAControllerDn = _CfprApBiosVfOnboardSATAControllerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 45, 1, 2),
    _CfprApBiosVfOnboardSATAControllerDn_Type()
)
cfprApBiosVfOnboardSATAControllerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfOnboardSATAControllerDn.setStatus("current")
_CfprApBiosVfOnboardSATAControllerRn_Type = SnmpAdminString
_CfprApBiosVfOnboardSATAControllerRn_Object = MibTableColumn
cfprApBiosVfOnboardSATAControllerRn = _CfprApBiosVfOnboardSATAControllerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 45, 1, 3),
    _CfprApBiosVfOnboardSATAControllerRn_Type()
)
cfprApBiosVfOnboardSATAControllerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfOnboardSATAControllerRn.setStatus("current")
_CfprApBiosVfOnboardSATAControllerVpOnboardSATAController_Type = CfprApBiosVfOnboardSATAControllerVpOnboardSATAController
_CfprApBiosVfOnboardSATAControllerVpOnboardSATAController_Object = MibTableColumn
cfprApBiosVfOnboardSATAControllerVpOnboardSATAController = _CfprApBiosVfOnboardSATAControllerVpOnboardSATAController_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 45, 1, 4),
    _CfprApBiosVfOnboardSATAControllerVpOnboardSATAController_Type()
)
cfprApBiosVfOnboardSATAControllerVpOnboardSATAController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfOnboardSATAControllerVpOnboardSATAController.setStatus("current")
_CfprApBiosVfOnboardSATAControllerVpSATAMode_Type = CfprApBiosVfOnboardSATAControllerVpSATAMode
_CfprApBiosVfOnboardSATAControllerVpSATAMode_Object = MibTableColumn
cfprApBiosVfOnboardSATAControllerVpSATAMode = _CfprApBiosVfOnboardSATAControllerVpSATAMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 45, 1, 5),
    _CfprApBiosVfOnboardSATAControllerVpSATAMode_Type()
)
cfprApBiosVfOnboardSATAControllerVpSATAMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfOnboardSATAControllerVpSATAMode.setStatus("current")
_CfprApBiosVfOnboardStorageTable_Object = MibTable
cfprApBiosVfOnboardStorageTable = _CfprApBiosVfOnboardStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 46)
)
if mibBuilder.loadTexts:
    cfprApBiosVfOnboardStorageTable.setStatus("current")
_CfprApBiosVfOnboardStorageEntry_Object = MibTableRow
cfprApBiosVfOnboardStorageEntry = _CfprApBiosVfOnboardStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 46, 1)
)
cfprApBiosVfOnboardStorageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfOnboardStorageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfOnboardStorageEntry.setStatus("current")
_CfprApBiosVfOnboardStorageInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfOnboardStorageInstanceId_Object = MibTableColumn
cfprApBiosVfOnboardStorageInstanceId = _CfprApBiosVfOnboardStorageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 46, 1, 1),
    _CfprApBiosVfOnboardStorageInstanceId_Type()
)
cfprApBiosVfOnboardStorageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfOnboardStorageInstanceId.setStatus("current")
_CfprApBiosVfOnboardStorageDn_Type = CfprApManagedObjectDn
_CfprApBiosVfOnboardStorageDn_Object = MibTableColumn
cfprApBiosVfOnboardStorageDn = _CfprApBiosVfOnboardStorageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 46, 1, 2),
    _CfprApBiosVfOnboardStorageDn_Type()
)
cfprApBiosVfOnboardStorageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfOnboardStorageDn.setStatus("current")
_CfprApBiosVfOnboardStorageRn_Type = SnmpAdminString
_CfprApBiosVfOnboardStorageRn_Object = MibTableColumn
cfprApBiosVfOnboardStorageRn = _CfprApBiosVfOnboardStorageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 46, 1, 3),
    _CfprApBiosVfOnboardStorageRn_Type()
)
cfprApBiosVfOnboardStorageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfOnboardStorageRn.setStatus("current")
_CfprApBiosVfOnboardStorageVpOnboardSCUStorageSupport_Type = CfprApBiosVfOnboardStorageVpOnboardSCUStorageSupport
_CfprApBiosVfOnboardStorageVpOnboardSCUStorageSupport_Object = MibTableColumn
cfprApBiosVfOnboardStorageVpOnboardSCUStorageSupport = _CfprApBiosVfOnboardStorageVpOnboardSCUStorageSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 46, 1, 4),
    _CfprApBiosVfOnboardStorageVpOnboardSCUStorageSupport_Type()
)
cfprApBiosVfOnboardStorageVpOnboardSCUStorageSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfOnboardStorageVpOnboardSCUStorageSupport.setStatus("current")
_CfprApBiosVfOptionROMEnableTable_Object = MibTable
cfprApBiosVfOptionROMEnableTable = _CfprApBiosVfOptionROMEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 47)
)
if mibBuilder.loadTexts:
    cfprApBiosVfOptionROMEnableTable.setStatus("current")
_CfprApBiosVfOptionROMEnableEntry_Object = MibTableRow
cfprApBiosVfOptionROMEnableEntry = _CfprApBiosVfOptionROMEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 47, 1)
)
cfprApBiosVfOptionROMEnableEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfOptionROMEnableInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfOptionROMEnableEntry.setStatus("current")
_CfprApBiosVfOptionROMEnableInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfOptionROMEnableInstanceId_Object = MibTableColumn
cfprApBiosVfOptionROMEnableInstanceId = _CfprApBiosVfOptionROMEnableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 47, 1, 1),
    _CfprApBiosVfOptionROMEnableInstanceId_Type()
)
cfprApBiosVfOptionROMEnableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfOptionROMEnableInstanceId.setStatus("current")
_CfprApBiosVfOptionROMEnableDn_Type = CfprApManagedObjectDn
_CfprApBiosVfOptionROMEnableDn_Object = MibTableColumn
cfprApBiosVfOptionROMEnableDn = _CfprApBiosVfOptionROMEnableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 47, 1, 2),
    _CfprApBiosVfOptionROMEnableDn_Type()
)
cfprApBiosVfOptionROMEnableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfOptionROMEnableDn.setStatus("current")
_CfprApBiosVfOptionROMEnableRn_Type = SnmpAdminString
_CfprApBiosVfOptionROMEnableRn_Object = MibTableColumn
cfprApBiosVfOptionROMEnableRn = _CfprApBiosVfOptionROMEnableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 47, 1, 3),
    _CfprApBiosVfOptionROMEnableRn_Type()
)
cfprApBiosVfOptionROMEnableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfOptionROMEnableRn.setStatus("current")
_CfprApBiosVfOptionROMEnableVpState_Type = CfprApBiosVfOptionROMEnableVpState
_CfprApBiosVfOptionROMEnableVpState_Object = MibTableColumn
cfprApBiosVfOptionROMEnableVpState = _CfprApBiosVfOptionROMEnableVpState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 47, 1, 4),
    _CfprApBiosVfOptionROMEnableVpState_Type()
)
cfprApBiosVfOptionROMEnableVpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfOptionROMEnableVpState.setStatus("current")
_CfprApBiosVfOptionROMLoadTable_Object = MibTable
cfprApBiosVfOptionROMLoadTable = _CfprApBiosVfOptionROMLoadTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 48)
)
if mibBuilder.loadTexts:
    cfprApBiosVfOptionROMLoadTable.setStatus("current")
_CfprApBiosVfOptionROMLoadEntry_Object = MibTableRow
cfprApBiosVfOptionROMLoadEntry = _CfprApBiosVfOptionROMLoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 48, 1)
)
cfprApBiosVfOptionROMLoadEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfOptionROMLoadInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfOptionROMLoadEntry.setStatus("current")
_CfprApBiosVfOptionROMLoadInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfOptionROMLoadInstanceId_Object = MibTableColumn
cfprApBiosVfOptionROMLoadInstanceId = _CfprApBiosVfOptionROMLoadInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 48, 1, 1),
    _CfprApBiosVfOptionROMLoadInstanceId_Type()
)
cfprApBiosVfOptionROMLoadInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfOptionROMLoadInstanceId.setStatus("current")
_CfprApBiosVfOptionROMLoadDn_Type = CfprApManagedObjectDn
_CfprApBiosVfOptionROMLoadDn_Object = MibTableColumn
cfprApBiosVfOptionROMLoadDn = _CfprApBiosVfOptionROMLoadDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 48, 1, 2),
    _CfprApBiosVfOptionROMLoadDn_Type()
)
cfprApBiosVfOptionROMLoadDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfOptionROMLoadDn.setStatus("current")
_CfprApBiosVfOptionROMLoadRn_Type = SnmpAdminString
_CfprApBiosVfOptionROMLoadRn_Object = MibTableColumn
cfprApBiosVfOptionROMLoadRn = _CfprApBiosVfOptionROMLoadRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 48, 1, 3),
    _CfprApBiosVfOptionROMLoadRn_Type()
)
cfprApBiosVfOptionROMLoadRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfOptionROMLoadRn.setStatus("current")
_CfprApBiosVfOptionROMLoadVpLoad_Type = CfprApBiosVfOptionROMLoadVpLoad
_CfprApBiosVfOptionROMLoadVpLoad_Object = MibTableColumn
cfprApBiosVfOptionROMLoadVpLoad = _CfprApBiosVfOptionROMLoadVpLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 48, 1, 4),
    _CfprApBiosVfOptionROMLoadVpLoad_Type()
)
cfprApBiosVfOptionROMLoadVpLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfOptionROMLoadVpLoad.setStatus("current")
_CfprApBiosVfPCISlotLinkSpeedTable_Object = MibTable
cfprApBiosVfPCISlotLinkSpeedTable = _CfprApBiosVfPCISlotLinkSpeedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 49)
)
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotLinkSpeedTable.setStatus("current")
_CfprApBiosVfPCISlotLinkSpeedEntry_Object = MibTableRow
cfprApBiosVfPCISlotLinkSpeedEntry = _CfprApBiosVfPCISlotLinkSpeedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 49, 1)
)
cfprApBiosVfPCISlotLinkSpeedEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfPCISlotLinkSpeedInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotLinkSpeedEntry.setStatus("current")
_CfprApBiosVfPCISlotLinkSpeedInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfPCISlotLinkSpeedInstanceId_Object = MibTableColumn
cfprApBiosVfPCISlotLinkSpeedInstanceId = _CfprApBiosVfPCISlotLinkSpeedInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 49, 1, 1),
    _CfprApBiosVfPCISlotLinkSpeedInstanceId_Type()
)
cfprApBiosVfPCISlotLinkSpeedInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotLinkSpeedInstanceId.setStatus("current")
_CfprApBiosVfPCISlotLinkSpeedDn_Type = CfprApManagedObjectDn
_CfprApBiosVfPCISlotLinkSpeedDn_Object = MibTableColumn
cfprApBiosVfPCISlotLinkSpeedDn = _CfprApBiosVfPCISlotLinkSpeedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 49, 1, 2),
    _CfprApBiosVfPCISlotLinkSpeedDn_Type()
)
cfprApBiosVfPCISlotLinkSpeedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotLinkSpeedDn.setStatus("current")
_CfprApBiosVfPCISlotLinkSpeedRn_Type = SnmpAdminString
_CfprApBiosVfPCISlotLinkSpeedRn_Object = MibTableColumn
cfprApBiosVfPCISlotLinkSpeedRn = _CfprApBiosVfPCISlotLinkSpeedRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 49, 1, 3),
    _CfprApBiosVfPCISlotLinkSpeedRn_Type()
)
cfprApBiosVfPCISlotLinkSpeedRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotLinkSpeedRn.setStatus("current")
_CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed_Type = CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed
_CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed_Object = MibTableColumn
cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed = _CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 49, 1, 4),
    _CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed_Type()
)
cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed.setStatus("current")
_CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed_Type = CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed
_CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed_Object = MibTableColumn
cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed = _CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 49, 1, 5),
    _CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed_Type()
)
cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed.setStatus("current")
_CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed_Type = CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed
_CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed_Object = MibTableColumn
cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed = _CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 49, 1, 6),
    _CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed_Type()
)
cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed.setStatus("current")
_CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed_Type = CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed
_CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed_Object = MibTableColumn
cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed = _CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 49, 1, 7),
    _CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed_Type()
)
cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed.setStatus("current")
_CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed_Type = CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed
_CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed_Object = MibTableColumn
cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed = _CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 49, 1, 8),
    _CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed_Type()
)
cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed.setStatus("current")
_CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed_Type = CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed
_CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed_Object = MibTableColumn
cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed = _CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 49, 1, 9),
    _CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed_Type()
)
cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed.setStatus("current")
_CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed_Type = CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed
_CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed_Object = MibTableColumn
cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed = _CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 49, 1, 10),
    _CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed_Type()
)
cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed.setStatus("current")
_CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed_Type = CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed
_CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed_Object = MibTableColumn
cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed = _CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 49, 1, 11),
    _CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed_Type()
)
cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed.setStatus("current")
_CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed_Type = CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed
_CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed_Object = MibTableColumn
cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed = _CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 49, 1, 12),
    _CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed_Type()
)
cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed.setStatus("current")
_CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed_Type = CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed
_CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed_Object = MibTableColumn
cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed = _CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 49, 1, 13),
    _CfprApBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed_Type()
)
cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed.setStatus("current")
_CfprApBiosVfPCISlotOptionROMEnableTable_Object = MibTable
cfprApBiosVfPCISlotOptionROMEnableTable = _CfprApBiosVfPCISlotOptionROMEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 50)
)
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotOptionROMEnableTable.setStatus("current")
_CfprApBiosVfPCISlotOptionROMEnableEntry_Object = MibTableRow
cfprApBiosVfPCISlotOptionROMEnableEntry = _CfprApBiosVfPCISlotOptionROMEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 50, 1)
)
cfprApBiosVfPCISlotOptionROMEnableEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfPCISlotOptionROMEnableInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotOptionROMEnableEntry.setStatus("current")
_CfprApBiosVfPCISlotOptionROMEnableInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfPCISlotOptionROMEnableInstanceId_Object = MibTableColumn
cfprApBiosVfPCISlotOptionROMEnableInstanceId = _CfprApBiosVfPCISlotOptionROMEnableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 50, 1, 1),
    _CfprApBiosVfPCISlotOptionROMEnableInstanceId_Type()
)
cfprApBiosVfPCISlotOptionROMEnableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotOptionROMEnableInstanceId.setStatus("current")
_CfprApBiosVfPCISlotOptionROMEnableDn_Type = CfprApManagedObjectDn
_CfprApBiosVfPCISlotOptionROMEnableDn_Object = MibTableColumn
cfprApBiosVfPCISlotOptionROMEnableDn = _CfprApBiosVfPCISlotOptionROMEnableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 50, 1, 2),
    _CfprApBiosVfPCISlotOptionROMEnableDn_Type()
)
cfprApBiosVfPCISlotOptionROMEnableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotOptionROMEnableDn.setStatus("current")
_CfprApBiosVfPCISlotOptionROMEnableRn_Type = SnmpAdminString
_CfprApBiosVfPCISlotOptionROMEnableRn_Object = MibTableColumn
cfprApBiosVfPCISlotOptionROMEnableRn = _CfprApBiosVfPCISlotOptionROMEnableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 50, 1, 3),
    _CfprApBiosVfPCISlotOptionROMEnableRn_Type()
)
cfprApBiosVfPCISlotOptionROMEnableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotOptionROMEnableRn.setStatus("current")
_CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM_Type = CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM
_CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM_Object = MibTableColumn
cfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM = _CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 50, 1, 4),
    _CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM_Type()
)
cfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM.setStatus("current")
_CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM_Type = CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM
_CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM_Object = MibTableColumn
cfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM = _CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 50, 1, 5),
    _CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM_Type()
)
cfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM.setStatus("current")
_CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM_Type = CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM
_CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM_Object = MibTableColumn
cfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM = _CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 50, 1, 6),
    _CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM_Type()
)
cfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM.setStatus("current")
_CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM_Type = CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM
_CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM_Object = MibTableColumn
cfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM = _CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 50, 1, 7),
    _CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM_Type()
)
cfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM.setStatus("current")
_CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM_Type = CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM
_CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM_Object = MibTableColumn
cfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM = _CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 50, 1, 8),
    _CfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM_Type()
)
cfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM.setStatus("current")
_CfprApBiosVfPCISlotOptionROMEnableVpSlot10State_Type = CfprApBiosVfPCISlotOptionROMEnableVpSlot10State
_CfprApBiosVfPCISlotOptionROMEnableVpSlot10State_Object = MibTableColumn
cfprApBiosVfPCISlotOptionROMEnableVpSlot10State = _CfprApBiosVfPCISlotOptionROMEnableVpSlot10State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 50, 1, 9),
    _CfprApBiosVfPCISlotOptionROMEnableVpSlot10State_Type()
)
cfprApBiosVfPCISlotOptionROMEnableVpSlot10State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotOptionROMEnableVpSlot10State.setStatus("current")
_CfprApBiosVfPCISlotOptionROMEnableVpSlot1State_Type = CfprApBiosVfPCISlotOptionROMEnableVpSlot1State
_CfprApBiosVfPCISlotOptionROMEnableVpSlot1State_Object = MibTableColumn
cfprApBiosVfPCISlotOptionROMEnableVpSlot1State = _CfprApBiosVfPCISlotOptionROMEnableVpSlot1State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 50, 1, 10),
    _CfprApBiosVfPCISlotOptionROMEnableVpSlot1State_Type()
)
cfprApBiosVfPCISlotOptionROMEnableVpSlot1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotOptionROMEnableVpSlot1State.setStatus("current")
_CfprApBiosVfPCISlotOptionROMEnableVpSlot2State_Type = CfprApBiosVfPCISlotOptionROMEnableVpSlot2State
_CfprApBiosVfPCISlotOptionROMEnableVpSlot2State_Object = MibTableColumn
cfprApBiosVfPCISlotOptionROMEnableVpSlot2State = _CfprApBiosVfPCISlotOptionROMEnableVpSlot2State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 50, 1, 11),
    _CfprApBiosVfPCISlotOptionROMEnableVpSlot2State_Type()
)
cfprApBiosVfPCISlotOptionROMEnableVpSlot2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotOptionROMEnableVpSlot2State.setStatus("current")
_CfprApBiosVfPCISlotOptionROMEnableVpSlot3State_Type = CfprApBiosVfPCISlotOptionROMEnableVpSlot3State
_CfprApBiosVfPCISlotOptionROMEnableVpSlot3State_Object = MibTableColumn
cfprApBiosVfPCISlotOptionROMEnableVpSlot3State = _CfprApBiosVfPCISlotOptionROMEnableVpSlot3State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 50, 1, 12),
    _CfprApBiosVfPCISlotOptionROMEnableVpSlot3State_Type()
)
cfprApBiosVfPCISlotOptionROMEnableVpSlot3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotOptionROMEnableVpSlot3State.setStatus("current")
_CfprApBiosVfPCISlotOptionROMEnableVpSlot4State_Type = CfprApBiosVfPCISlotOptionROMEnableVpSlot4State
_CfprApBiosVfPCISlotOptionROMEnableVpSlot4State_Object = MibTableColumn
cfprApBiosVfPCISlotOptionROMEnableVpSlot4State = _CfprApBiosVfPCISlotOptionROMEnableVpSlot4State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 50, 1, 13),
    _CfprApBiosVfPCISlotOptionROMEnableVpSlot4State_Type()
)
cfprApBiosVfPCISlotOptionROMEnableVpSlot4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotOptionROMEnableVpSlot4State.setStatus("current")
_CfprApBiosVfPCISlotOptionROMEnableVpSlot5State_Type = CfprApBiosVfPCISlotOptionROMEnableVpSlot5State
_CfprApBiosVfPCISlotOptionROMEnableVpSlot5State_Object = MibTableColumn
cfprApBiosVfPCISlotOptionROMEnableVpSlot5State = _CfprApBiosVfPCISlotOptionROMEnableVpSlot5State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 50, 1, 14),
    _CfprApBiosVfPCISlotOptionROMEnableVpSlot5State_Type()
)
cfprApBiosVfPCISlotOptionROMEnableVpSlot5State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotOptionROMEnableVpSlot5State.setStatus("current")
_CfprApBiosVfPCISlotOptionROMEnableVpSlot6State_Type = CfprApBiosVfPCISlotOptionROMEnableVpSlot6State
_CfprApBiosVfPCISlotOptionROMEnableVpSlot6State_Object = MibTableColumn
cfprApBiosVfPCISlotOptionROMEnableVpSlot6State = _CfprApBiosVfPCISlotOptionROMEnableVpSlot6State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 50, 1, 15),
    _CfprApBiosVfPCISlotOptionROMEnableVpSlot6State_Type()
)
cfprApBiosVfPCISlotOptionROMEnableVpSlot6State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotOptionROMEnableVpSlot6State.setStatus("current")
_CfprApBiosVfPCISlotOptionROMEnableVpSlot7State_Type = CfprApBiosVfPCISlotOptionROMEnableVpSlot7State
_CfprApBiosVfPCISlotOptionROMEnableVpSlot7State_Object = MibTableColumn
cfprApBiosVfPCISlotOptionROMEnableVpSlot7State = _CfprApBiosVfPCISlotOptionROMEnableVpSlot7State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 50, 1, 16),
    _CfprApBiosVfPCISlotOptionROMEnableVpSlot7State_Type()
)
cfprApBiosVfPCISlotOptionROMEnableVpSlot7State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotOptionROMEnableVpSlot7State.setStatus("current")
_CfprApBiosVfPCISlotOptionROMEnableVpSlot8State_Type = CfprApBiosVfPCISlotOptionROMEnableVpSlot8State
_CfprApBiosVfPCISlotOptionROMEnableVpSlot8State_Object = MibTableColumn
cfprApBiosVfPCISlotOptionROMEnableVpSlot8State = _CfprApBiosVfPCISlotOptionROMEnableVpSlot8State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 50, 1, 17),
    _CfprApBiosVfPCISlotOptionROMEnableVpSlot8State_Type()
)
cfprApBiosVfPCISlotOptionROMEnableVpSlot8State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotOptionROMEnableVpSlot8State.setStatus("current")
_CfprApBiosVfPCISlotOptionROMEnableVpSlot9State_Type = CfprApBiosVfPCISlotOptionROMEnableVpSlot9State
_CfprApBiosVfPCISlotOptionROMEnableVpSlot9State_Object = MibTableColumn
cfprApBiosVfPCISlotOptionROMEnableVpSlot9State = _CfprApBiosVfPCISlotOptionROMEnableVpSlot9State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 50, 1, 18),
    _CfprApBiosVfPCISlotOptionROMEnableVpSlot9State_Type()
)
cfprApBiosVfPCISlotOptionROMEnableVpSlot9State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotOptionROMEnableVpSlot9State.setStatus("current")
_CfprApBiosVfPCISlotOptionROMEnableVpSlotMezzState_Type = CfprApBiosVfPCISlotOptionROMEnableVpSlotMezzState
_CfprApBiosVfPCISlotOptionROMEnableVpSlotMezzState_Object = MibTableColumn
cfprApBiosVfPCISlotOptionROMEnableVpSlotMezzState = _CfprApBiosVfPCISlotOptionROMEnableVpSlotMezzState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 50, 1, 19),
    _CfprApBiosVfPCISlotOptionROMEnableVpSlotMezzState_Type()
)
cfprApBiosVfPCISlotOptionROMEnableVpSlotMezzState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPCISlotOptionROMEnableVpSlotMezzState.setStatus("current")
_CfprApBiosVfPOSTErrorPauseTable_Object = MibTable
cfprApBiosVfPOSTErrorPauseTable = _CfprApBiosVfPOSTErrorPauseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 51)
)
if mibBuilder.loadTexts:
    cfprApBiosVfPOSTErrorPauseTable.setStatus("current")
_CfprApBiosVfPOSTErrorPauseEntry_Object = MibTableRow
cfprApBiosVfPOSTErrorPauseEntry = _CfprApBiosVfPOSTErrorPauseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 51, 1)
)
cfprApBiosVfPOSTErrorPauseEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfPOSTErrorPauseInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfPOSTErrorPauseEntry.setStatus("current")
_CfprApBiosVfPOSTErrorPauseInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfPOSTErrorPauseInstanceId_Object = MibTableColumn
cfprApBiosVfPOSTErrorPauseInstanceId = _CfprApBiosVfPOSTErrorPauseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 51, 1, 1),
    _CfprApBiosVfPOSTErrorPauseInstanceId_Type()
)
cfprApBiosVfPOSTErrorPauseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfPOSTErrorPauseInstanceId.setStatus("current")
_CfprApBiosVfPOSTErrorPauseDn_Type = CfprApManagedObjectDn
_CfprApBiosVfPOSTErrorPauseDn_Object = MibTableColumn
cfprApBiosVfPOSTErrorPauseDn = _CfprApBiosVfPOSTErrorPauseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 51, 1, 2),
    _CfprApBiosVfPOSTErrorPauseDn_Type()
)
cfprApBiosVfPOSTErrorPauseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPOSTErrorPauseDn.setStatus("current")
_CfprApBiosVfPOSTErrorPauseRn_Type = SnmpAdminString
_CfprApBiosVfPOSTErrorPauseRn_Object = MibTableColumn
cfprApBiosVfPOSTErrorPauseRn = _CfprApBiosVfPOSTErrorPauseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 51, 1, 3),
    _CfprApBiosVfPOSTErrorPauseRn_Type()
)
cfprApBiosVfPOSTErrorPauseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPOSTErrorPauseRn.setStatus("current")
_CfprApBiosVfPOSTErrorPauseVpPOSTErrorPause_Type = CfprApBiosVfPOSTErrorPauseVpPOSTErrorPause
_CfprApBiosVfPOSTErrorPauseVpPOSTErrorPause_Object = MibTableColumn
cfprApBiosVfPOSTErrorPauseVpPOSTErrorPause = _CfprApBiosVfPOSTErrorPauseVpPOSTErrorPause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 51, 1, 4),
    _CfprApBiosVfPOSTErrorPauseVpPOSTErrorPause_Type()
)
cfprApBiosVfPOSTErrorPauseVpPOSTErrorPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPOSTErrorPauseVpPOSTErrorPause.setStatus("current")
_CfprApBiosVfPSTATECoordinationTable_Object = MibTable
cfprApBiosVfPSTATECoordinationTable = _CfprApBiosVfPSTATECoordinationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 52)
)
if mibBuilder.loadTexts:
    cfprApBiosVfPSTATECoordinationTable.setStatus("current")
_CfprApBiosVfPSTATECoordinationEntry_Object = MibTableRow
cfprApBiosVfPSTATECoordinationEntry = _CfprApBiosVfPSTATECoordinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 52, 1)
)
cfprApBiosVfPSTATECoordinationEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfPSTATECoordinationInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfPSTATECoordinationEntry.setStatus("current")
_CfprApBiosVfPSTATECoordinationInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfPSTATECoordinationInstanceId_Object = MibTableColumn
cfprApBiosVfPSTATECoordinationInstanceId = _CfprApBiosVfPSTATECoordinationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 52, 1, 1),
    _CfprApBiosVfPSTATECoordinationInstanceId_Type()
)
cfprApBiosVfPSTATECoordinationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfPSTATECoordinationInstanceId.setStatus("current")
_CfprApBiosVfPSTATECoordinationDn_Type = CfprApManagedObjectDn
_CfprApBiosVfPSTATECoordinationDn_Object = MibTableColumn
cfprApBiosVfPSTATECoordinationDn = _CfprApBiosVfPSTATECoordinationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 52, 1, 2),
    _CfprApBiosVfPSTATECoordinationDn_Type()
)
cfprApBiosVfPSTATECoordinationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPSTATECoordinationDn.setStatus("current")
_CfprApBiosVfPSTATECoordinationRn_Type = SnmpAdminString
_CfprApBiosVfPSTATECoordinationRn_Object = MibTableColumn
cfprApBiosVfPSTATECoordinationRn = _CfprApBiosVfPSTATECoordinationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 52, 1, 3),
    _CfprApBiosVfPSTATECoordinationRn_Type()
)
cfprApBiosVfPSTATECoordinationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPSTATECoordinationRn.setStatus("current")
_CfprApBiosVfPSTATECoordinationVpPSTATECoordination_Type = CfprApBiosVfPSTATECoordinationVpPSTATECoordination
_CfprApBiosVfPSTATECoordinationVpPSTATECoordination_Object = MibTableColumn
cfprApBiosVfPSTATECoordinationVpPSTATECoordination = _CfprApBiosVfPSTATECoordinationVpPSTATECoordination_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 52, 1, 4),
    _CfprApBiosVfPSTATECoordinationVpPSTATECoordination_Type()
)
cfprApBiosVfPSTATECoordinationVpPSTATECoordination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPSTATECoordinationVpPSTATECoordination.setStatus("current")
_CfprApBiosVfPackageCStateLimitTable_Object = MibTable
cfprApBiosVfPackageCStateLimitTable = _CfprApBiosVfPackageCStateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 53)
)
if mibBuilder.loadTexts:
    cfprApBiosVfPackageCStateLimitTable.setStatus("current")
_CfprApBiosVfPackageCStateLimitEntry_Object = MibTableRow
cfprApBiosVfPackageCStateLimitEntry = _CfprApBiosVfPackageCStateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 53, 1)
)
cfprApBiosVfPackageCStateLimitEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfPackageCStateLimitInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfPackageCStateLimitEntry.setStatus("current")
_CfprApBiosVfPackageCStateLimitInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfPackageCStateLimitInstanceId_Object = MibTableColumn
cfprApBiosVfPackageCStateLimitInstanceId = _CfprApBiosVfPackageCStateLimitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 53, 1, 1),
    _CfprApBiosVfPackageCStateLimitInstanceId_Type()
)
cfprApBiosVfPackageCStateLimitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfPackageCStateLimitInstanceId.setStatus("current")
_CfprApBiosVfPackageCStateLimitDn_Type = CfprApManagedObjectDn
_CfprApBiosVfPackageCStateLimitDn_Object = MibTableColumn
cfprApBiosVfPackageCStateLimitDn = _CfprApBiosVfPackageCStateLimitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 53, 1, 2),
    _CfprApBiosVfPackageCStateLimitDn_Type()
)
cfprApBiosVfPackageCStateLimitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPackageCStateLimitDn.setStatus("current")
_CfprApBiosVfPackageCStateLimitRn_Type = SnmpAdminString
_CfprApBiosVfPackageCStateLimitRn_Object = MibTableColumn
cfprApBiosVfPackageCStateLimitRn = _CfprApBiosVfPackageCStateLimitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 53, 1, 3),
    _CfprApBiosVfPackageCStateLimitRn_Type()
)
cfprApBiosVfPackageCStateLimitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPackageCStateLimitRn.setStatus("current")
_CfprApBiosVfPackageCStateLimitVpPackageCStateLimit_Type = CfprApBiosVfPackageCStateLimitVpPackageCStateLimit
_CfprApBiosVfPackageCStateLimitVpPackageCStateLimit_Object = MibTableColumn
cfprApBiosVfPackageCStateLimitVpPackageCStateLimit = _CfprApBiosVfPackageCStateLimitVpPackageCStateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 53, 1, 4),
    _CfprApBiosVfPackageCStateLimitVpPackageCStateLimit_Type()
)
cfprApBiosVfPackageCStateLimitVpPackageCStateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfPackageCStateLimitVpPackageCStateLimit.setStatus("current")
_CfprApBiosVfProcessorC1ETable_Object = MibTable
cfprApBiosVfProcessorC1ETable = _CfprApBiosVfProcessorC1ETable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 54)
)
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorC1ETable.setStatus("current")
_CfprApBiosVfProcessorC1EEntry_Object = MibTableRow
cfprApBiosVfProcessorC1EEntry = _CfprApBiosVfProcessorC1EEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 54, 1)
)
cfprApBiosVfProcessorC1EEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfProcessorC1EInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorC1EEntry.setStatus("current")
_CfprApBiosVfProcessorC1EInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfProcessorC1EInstanceId_Object = MibTableColumn
cfprApBiosVfProcessorC1EInstanceId = _CfprApBiosVfProcessorC1EInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 54, 1, 1),
    _CfprApBiosVfProcessorC1EInstanceId_Type()
)
cfprApBiosVfProcessorC1EInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorC1EInstanceId.setStatus("current")
_CfprApBiosVfProcessorC1EDn_Type = CfprApManagedObjectDn
_CfprApBiosVfProcessorC1EDn_Object = MibTableColumn
cfprApBiosVfProcessorC1EDn = _CfprApBiosVfProcessorC1EDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 54, 1, 2),
    _CfprApBiosVfProcessorC1EDn_Type()
)
cfprApBiosVfProcessorC1EDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorC1EDn.setStatus("current")
_CfprApBiosVfProcessorC1ERn_Type = SnmpAdminString
_CfprApBiosVfProcessorC1ERn_Object = MibTableColumn
cfprApBiosVfProcessorC1ERn = _CfprApBiosVfProcessorC1ERn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 54, 1, 3),
    _CfprApBiosVfProcessorC1ERn_Type()
)
cfprApBiosVfProcessorC1ERn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorC1ERn.setStatus("current")
_CfprApBiosVfProcessorC1EVpProcessorC1E_Type = CfprApBiosVfProcessorC1EVpProcessorC1E
_CfprApBiosVfProcessorC1EVpProcessorC1E_Object = MibTableColumn
cfprApBiosVfProcessorC1EVpProcessorC1E = _CfprApBiosVfProcessorC1EVpProcessorC1E_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 54, 1, 4),
    _CfprApBiosVfProcessorC1EVpProcessorC1E_Type()
)
cfprApBiosVfProcessorC1EVpProcessorC1E.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorC1EVpProcessorC1E.setStatus("current")
_CfprApBiosVfProcessorC3ReportTable_Object = MibTable
cfprApBiosVfProcessorC3ReportTable = _CfprApBiosVfProcessorC3ReportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 55)
)
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorC3ReportTable.setStatus("current")
_CfprApBiosVfProcessorC3ReportEntry_Object = MibTableRow
cfprApBiosVfProcessorC3ReportEntry = _CfprApBiosVfProcessorC3ReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 55, 1)
)
cfprApBiosVfProcessorC3ReportEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfProcessorC3ReportInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorC3ReportEntry.setStatus("current")
_CfprApBiosVfProcessorC3ReportInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfProcessorC3ReportInstanceId_Object = MibTableColumn
cfprApBiosVfProcessorC3ReportInstanceId = _CfprApBiosVfProcessorC3ReportInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 55, 1, 1),
    _CfprApBiosVfProcessorC3ReportInstanceId_Type()
)
cfprApBiosVfProcessorC3ReportInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorC3ReportInstanceId.setStatus("current")
_CfprApBiosVfProcessorC3ReportDn_Type = CfprApManagedObjectDn
_CfprApBiosVfProcessorC3ReportDn_Object = MibTableColumn
cfprApBiosVfProcessorC3ReportDn = _CfprApBiosVfProcessorC3ReportDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 55, 1, 2),
    _CfprApBiosVfProcessorC3ReportDn_Type()
)
cfprApBiosVfProcessorC3ReportDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorC3ReportDn.setStatus("current")
_CfprApBiosVfProcessorC3ReportRn_Type = SnmpAdminString
_CfprApBiosVfProcessorC3ReportRn_Object = MibTableColumn
cfprApBiosVfProcessorC3ReportRn = _CfprApBiosVfProcessorC3ReportRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 55, 1, 3),
    _CfprApBiosVfProcessorC3ReportRn_Type()
)
cfprApBiosVfProcessorC3ReportRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorC3ReportRn.setStatus("current")
_CfprApBiosVfProcessorC3ReportVpProcessorC3Report_Type = CfprApBiosVfProcessorC3ReportVpProcessorC3Report
_CfprApBiosVfProcessorC3ReportVpProcessorC3Report_Object = MibTableColumn
cfprApBiosVfProcessorC3ReportVpProcessorC3Report = _CfprApBiosVfProcessorC3ReportVpProcessorC3Report_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 55, 1, 4),
    _CfprApBiosVfProcessorC3ReportVpProcessorC3Report_Type()
)
cfprApBiosVfProcessorC3ReportVpProcessorC3Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorC3ReportVpProcessorC3Report.setStatus("current")
_CfprApBiosVfProcessorC6ReportTable_Object = MibTable
cfprApBiosVfProcessorC6ReportTable = _CfprApBiosVfProcessorC6ReportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 56)
)
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorC6ReportTable.setStatus("current")
_CfprApBiosVfProcessorC6ReportEntry_Object = MibTableRow
cfprApBiosVfProcessorC6ReportEntry = _CfprApBiosVfProcessorC6ReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 56, 1)
)
cfprApBiosVfProcessorC6ReportEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfProcessorC6ReportInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorC6ReportEntry.setStatus("current")
_CfprApBiosVfProcessorC6ReportInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfProcessorC6ReportInstanceId_Object = MibTableColumn
cfprApBiosVfProcessorC6ReportInstanceId = _CfprApBiosVfProcessorC6ReportInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 56, 1, 1),
    _CfprApBiosVfProcessorC6ReportInstanceId_Type()
)
cfprApBiosVfProcessorC6ReportInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorC6ReportInstanceId.setStatus("current")
_CfprApBiosVfProcessorC6ReportDn_Type = CfprApManagedObjectDn
_CfprApBiosVfProcessorC6ReportDn_Object = MibTableColumn
cfprApBiosVfProcessorC6ReportDn = _CfprApBiosVfProcessorC6ReportDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 56, 1, 2),
    _CfprApBiosVfProcessorC6ReportDn_Type()
)
cfprApBiosVfProcessorC6ReportDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorC6ReportDn.setStatus("current")
_CfprApBiosVfProcessorC6ReportRn_Type = SnmpAdminString
_CfprApBiosVfProcessorC6ReportRn_Object = MibTableColumn
cfprApBiosVfProcessorC6ReportRn = _CfprApBiosVfProcessorC6ReportRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 56, 1, 3),
    _CfprApBiosVfProcessorC6ReportRn_Type()
)
cfprApBiosVfProcessorC6ReportRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorC6ReportRn.setStatus("current")
_CfprApBiosVfProcessorC6ReportVpProcessorC6Report_Type = CfprApBiosVfProcessorC6ReportVpProcessorC6Report
_CfprApBiosVfProcessorC6ReportVpProcessorC6Report_Object = MibTableColumn
cfprApBiosVfProcessorC6ReportVpProcessorC6Report = _CfprApBiosVfProcessorC6ReportVpProcessorC6Report_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 56, 1, 4),
    _CfprApBiosVfProcessorC6ReportVpProcessorC6Report_Type()
)
cfprApBiosVfProcessorC6ReportVpProcessorC6Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorC6ReportVpProcessorC6Report.setStatus("current")
_CfprApBiosVfProcessorC7ReportTable_Object = MibTable
cfprApBiosVfProcessorC7ReportTable = _CfprApBiosVfProcessorC7ReportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 57)
)
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorC7ReportTable.setStatus("current")
_CfprApBiosVfProcessorC7ReportEntry_Object = MibTableRow
cfprApBiosVfProcessorC7ReportEntry = _CfprApBiosVfProcessorC7ReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 57, 1)
)
cfprApBiosVfProcessorC7ReportEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfProcessorC7ReportInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorC7ReportEntry.setStatus("current")
_CfprApBiosVfProcessorC7ReportInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfProcessorC7ReportInstanceId_Object = MibTableColumn
cfprApBiosVfProcessorC7ReportInstanceId = _CfprApBiosVfProcessorC7ReportInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 57, 1, 1),
    _CfprApBiosVfProcessorC7ReportInstanceId_Type()
)
cfprApBiosVfProcessorC7ReportInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorC7ReportInstanceId.setStatus("current")
_CfprApBiosVfProcessorC7ReportDn_Type = CfprApManagedObjectDn
_CfprApBiosVfProcessorC7ReportDn_Object = MibTableColumn
cfprApBiosVfProcessorC7ReportDn = _CfprApBiosVfProcessorC7ReportDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 57, 1, 2),
    _CfprApBiosVfProcessorC7ReportDn_Type()
)
cfprApBiosVfProcessorC7ReportDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorC7ReportDn.setStatus("current")
_CfprApBiosVfProcessorC7ReportRn_Type = SnmpAdminString
_CfprApBiosVfProcessorC7ReportRn_Object = MibTableColumn
cfprApBiosVfProcessorC7ReportRn = _CfprApBiosVfProcessorC7ReportRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 57, 1, 3),
    _CfprApBiosVfProcessorC7ReportRn_Type()
)
cfprApBiosVfProcessorC7ReportRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorC7ReportRn.setStatus("current")
_CfprApBiosVfProcessorC7ReportVpProcessorC7Report_Type = CfprApBiosVfProcessorC7ReportVpProcessorC7Report
_CfprApBiosVfProcessorC7ReportVpProcessorC7Report_Object = MibTableColumn
cfprApBiosVfProcessorC7ReportVpProcessorC7Report = _CfprApBiosVfProcessorC7ReportVpProcessorC7Report_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 57, 1, 4),
    _CfprApBiosVfProcessorC7ReportVpProcessorC7Report_Type()
)
cfprApBiosVfProcessorC7ReportVpProcessorC7Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorC7ReportVpProcessorC7Report.setStatus("current")
_CfprApBiosVfProcessorCStateTable_Object = MibTable
cfprApBiosVfProcessorCStateTable = _CfprApBiosVfProcessorCStateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 58)
)
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorCStateTable.setStatus("current")
_CfprApBiosVfProcessorCStateEntry_Object = MibTableRow
cfprApBiosVfProcessorCStateEntry = _CfprApBiosVfProcessorCStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 58, 1)
)
cfprApBiosVfProcessorCStateEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfProcessorCStateInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorCStateEntry.setStatus("current")
_CfprApBiosVfProcessorCStateInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfProcessorCStateInstanceId_Object = MibTableColumn
cfprApBiosVfProcessorCStateInstanceId = _CfprApBiosVfProcessorCStateInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 58, 1, 1),
    _CfprApBiosVfProcessorCStateInstanceId_Type()
)
cfprApBiosVfProcessorCStateInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorCStateInstanceId.setStatus("current")
_CfprApBiosVfProcessorCStateDn_Type = CfprApManagedObjectDn
_CfprApBiosVfProcessorCStateDn_Object = MibTableColumn
cfprApBiosVfProcessorCStateDn = _CfprApBiosVfProcessorCStateDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 58, 1, 2),
    _CfprApBiosVfProcessorCStateDn_Type()
)
cfprApBiosVfProcessorCStateDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorCStateDn.setStatus("current")
_CfprApBiosVfProcessorCStateRn_Type = SnmpAdminString
_CfprApBiosVfProcessorCStateRn_Object = MibTableColumn
cfprApBiosVfProcessorCStateRn = _CfprApBiosVfProcessorCStateRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 58, 1, 3),
    _CfprApBiosVfProcessorCStateRn_Type()
)
cfprApBiosVfProcessorCStateRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorCStateRn.setStatus("current")
_CfprApBiosVfProcessorCStateVpProcessorCState_Type = CfprApBiosVfProcessorCStateVpProcessorCState
_CfprApBiosVfProcessorCStateVpProcessorCState_Object = MibTableColumn
cfprApBiosVfProcessorCStateVpProcessorCState = _CfprApBiosVfProcessorCStateVpProcessorCState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 58, 1, 4),
    _CfprApBiosVfProcessorCStateVpProcessorCState_Type()
)
cfprApBiosVfProcessorCStateVpProcessorCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorCStateVpProcessorCState.setStatus("current")
_CfprApBiosVfProcessorEnergyConfigurationTable_Object = MibTable
cfprApBiosVfProcessorEnergyConfigurationTable = _CfprApBiosVfProcessorEnergyConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 59)
)
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorEnergyConfigurationTable.setStatus("current")
_CfprApBiosVfProcessorEnergyConfigurationEntry_Object = MibTableRow
cfprApBiosVfProcessorEnergyConfigurationEntry = _CfprApBiosVfProcessorEnergyConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 59, 1)
)
cfprApBiosVfProcessorEnergyConfigurationEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfProcessorEnergyConfigurationInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorEnergyConfigurationEntry.setStatus("current")
_CfprApBiosVfProcessorEnergyConfigurationInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfProcessorEnergyConfigurationInstanceId_Object = MibTableColumn
cfprApBiosVfProcessorEnergyConfigurationInstanceId = _CfprApBiosVfProcessorEnergyConfigurationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 59, 1, 1),
    _CfprApBiosVfProcessorEnergyConfigurationInstanceId_Type()
)
cfprApBiosVfProcessorEnergyConfigurationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorEnergyConfigurationInstanceId.setStatus("current")
_CfprApBiosVfProcessorEnergyConfigurationDn_Type = CfprApManagedObjectDn
_CfprApBiosVfProcessorEnergyConfigurationDn_Object = MibTableColumn
cfprApBiosVfProcessorEnergyConfigurationDn = _CfprApBiosVfProcessorEnergyConfigurationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 59, 1, 2),
    _CfprApBiosVfProcessorEnergyConfigurationDn_Type()
)
cfprApBiosVfProcessorEnergyConfigurationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorEnergyConfigurationDn.setStatus("current")
_CfprApBiosVfProcessorEnergyConfigurationRn_Type = SnmpAdminString
_CfprApBiosVfProcessorEnergyConfigurationRn_Object = MibTableColumn
cfprApBiosVfProcessorEnergyConfigurationRn = _CfprApBiosVfProcessorEnergyConfigurationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 59, 1, 3),
    _CfprApBiosVfProcessorEnergyConfigurationRn_Type()
)
cfprApBiosVfProcessorEnergyConfigurationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorEnergyConfigurationRn.setStatus("current")
_CfprApBiosVfProcessorEnergyConfigurationVpEnergyPerformance_Type = CfprApBiosVfProcessorEnergyConfigurationVpEnergyPerformance
_CfprApBiosVfProcessorEnergyConfigurationVpEnergyPerformance_Object = MibTableColumn
cfprApBiosVfProcessorEnergyConfigurationVpEnergyPerformance = _CfprApBiosVfProcessorEnergyConfigurationVpEnergyPerformance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 59, 1, 4),
    _CfprApBiosVfProcessorEnergyConfigurationVpEnergyPerformance_Type()
)
cfprApBiosVfProcessorEnergyConfigurationVpEnergyPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorEnergyConfigurationVpEnergyPerformance.setStatus("current")
_CfprApBiosVfProcessorEnergyConfigurationVpPowerTechnology_Type = CfprApBiosVfProcessorEnergyConfigurationVpPowerTechnology
_CfprApBiosVfProcessorEnergyConfigurationVpPowerTechnology_Object = MibTableColumn
cfprApBiosVfProcessorEnergyConfigurationVpPowerTechnology = _CfprApBiosVfProcessorEnergyConfigurationVpPowerTechnology_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 59, 1, 5),
    _CfprApBiosVfProcessorEnergyConfigurationVpPowerTechnology_Type()
)
cfprApBiosVfProcessorEnergyConfigurationVpPowerTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorEnergyConfigurationVpPowerTechnology.setStatus("current")
_CfprApBiosVfProcessorPrefetchConfigTable_Object = MibTable
cfprApBiosVfProcessorPrefetchConfigTable = _CfprApBiosVfProcessorPrefetchConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 60)
)
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorPrefetchConfigTable.setStatus("current")
_CfprApBiosVfProcessorPrefetchConfigEntry_Object = MibTableRow
cfprApBiosVfProcessorPrefetchConfigEntry = _CfprApBiosVfProcessorPrefetchConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 60, 1)
)
cfprApBiosVfProcessorPrefetchConfigEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfProcessorPrefetchConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorPrefetchConfigEntry.setStatus("current")
_CfprApBiosVfProcessorPrefetchConfigInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfProcessorPrefetchConfigInstanceId_Object = MibTableColumn
cfprApBiosVfProcessorPrefetchConfigInstanceId = _CfprApBiosVfProcessorPrefetchConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 60, 1, 1),
    _CfprApBiosVfProcessorPrefetchConfigInstanceId_Type()
)
cfprApBiosVfProcessorPrefetchConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorPrefetchConfigInstanceId.setStatus("current")
_CfprApBiosVfProcessorPrefetchConfigDn_Type = CfprApManagedObjectDn
_CfprApBiosVfProcessorPrefetchConfigDn_Object = MibTableColumn
cfprApBiosVfProcessorPrefetchConfigDn = _CfprApBiosVfProcessorPrefetchConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 60, 1, 2),
    _CfprApBiosVfProcessorPrefetchConfigDn_Type()
)
cfprApBiosVfProcessorPrefetchConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorPrefetchConfigDn.setStatus("current")
_CfprApBiosVfProcessorPrefetchConfigRn_Type = SnmpAdminString
_CfprApBiosVfProcessorPrefetchConfigRn_Object = MibTableColumn
cfprApBiosVfProcessorPrefetchConfigRn = _CfprApBiosVfProcessorPrefetchConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 60, 1, 3),
    _CfprApBiosVfProcessorPrefetchConfigRn_Type()
)
cfprApBiosVfProcessorPrefetchConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorPrefetchConfigRn.setStatus("current")
_CfprApBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher_Type = CfprApBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher
_CfprApBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher_Object = MibTableColumn
cfprApBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher = _CfprApBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 60, 1, 4),
    _CfprApBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher_Type()
)
cfprApBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher.setStatus("current")
_CfprApBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher_Type = CfprApBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher
_CfprApBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher_Object = MibTableColumn
cfprApBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher = _CfprApBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 60, 1, 5),
    _CfprApBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher_Type()
)
cfprApBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher.setStatus("current")
_CfprApBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch_Type = CfprApBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch
_CfprApBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch_Object = MibTableColumn
cfprApBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch = _CfprApBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 60, 1, 6),
    _CfprApBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch_Type()
)
cfprApBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch.setStatus("current")
_CfprApBiosVfProcessorPrefetchConfigVpHardwarePrefetcher_Type = CfprApBiosVfProcessorPrefetchConfigVpHardwarePrefetcher
_CfprApBiosVfProcessorPrefetchConfigVpHardwarePrefetcher_Object = MibTableColumn
cfprApBiosVfProcessorPrefetchConfigVpHardwarePrefetcher = _CfprApBiosVfProcessorPrefetchConfigVpHardwarePrefetcher_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 60, 1, 7),
    _CfprApBiosVfProcessorPrefetchConfigVpHardwarePrefetcher_Type()
)
cfprApBiosVfProcessorPrefetchConfigVpHardwarePrefetcher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfProcessorPrefetchConfigVpHardwarePrefetcher.setStatus("current")
_CfprApBiosVfQPILinkFrequencySelectTable_Object = MibTable
cfprApBiosVfQPILinkFrequencySelectTable = _CfprApBiosVfQPILinkFrequencySelectTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 61)
)
if mibBuilder.loadTexts:
    cfprApBiosVfQPILinkFrequencySelectTable.setStatus("current")
_CfprApBiosVfQPILinkFrequencySelectEntry_Object = MibTableRow
cfprApBiosVfQPILinkFrequencySelectEntry = _CfprApBiosVfQPILinkFrequencySelectEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 61, 1)
)
cfprApBiosVfQPILinkFrequencySelectEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfQPILinkFrequencySelectInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfQPILinkFrequencySelectEntry.setStatus("current")
_CfprApBiosVfQPILinkFrequencySelectInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfQPILinkFrequencySelectInstanceId_Object = MibTableColumn
cfprApBiosVfQPILinkFrequencySelectInstanceId = _CfprApBiosVfQPILinkFrequencySelectInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 61, 1, 1),
    _CfprApBiosVfQPILinkFrequencySelectInstanceId_Type()
)
cfprApBiosVfQPILinkFrequencySelectInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfQPILinkFrequencySelectInstanceId.setStatus("current")
_CfprApBiosVfQPILinkFrequencySelectDn_Type = CfprApManagedObjectDn
_CfprApBiosVfQPILinkFrequencySelectDn_Object = MibTableColumn
cfprApBiosVfQPILinkFrequencySelectDn = _CfprApBiosVfQPILinkFrequencySelectDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 61, 1, 2),
    _CfprApBiosVfQPILinkFrequencySelectDn_Type()
)
cfprApBiosVfQPILinkFrequencySelectDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfQPILinkFrequencySelectDn.setStatus("current")
_CfprApBiosVfQPILinkFrequencySelectRn_Type = SnmpAdminString
_CfprApBiosVfQPILinkFrequencySelectRn_Object = MibTableColumn
cfprApBiosVfQPILinkFrequencySelectRn = _CfprApBiosVfQPILinkFrequencySelectRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 61, 1, 3),
    _CfprApBiosVfQPILinkFrequencySelectRn_Type()
)
cfprApBiosVfQPILinkFrequencySelectRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfQPILinkFrequencySelectRn.setStatus("current")
_CfprApBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect_Type = CfprApBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect
_CfprApBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect_Object = MibTableColumn
cfprApBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect = _CfprApBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 61, 1, 4),
    _CfprApBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect_Type()
)
cfprApBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect.setStatus("current")
_CfprApBiosVfQuietBootTable_Object = MibTable
cfprApBiosVfQuietBootTable = _CfprApBiosVfQuietBootTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 62)
)
if mibBuilder.loadTexts:
    cfprApBiosVfQuietBootTable.setStatus("current")
_CfprApBiosVfQuietBootEntry_Object = MibTableRow
cfprApBiosVfQuietBootEntry = _CfprApBiosVfQuietBootEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 62, 1)
)
cfprApBiosVfQuietBootEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfQuietBootInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfQuietBootEntry.setStatus("current")
_CfprApBiosVfQuietBootInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfQuietBootInstanceId_Object = MibTableColumn
cfprApBiosVfQuietBootInstanceId = _CfprApBiosVfQuietBootInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 62, 1, 1),
    _CfprApBiosVfQuietBootInstanceId_Type()
)
cfprApBiosVfQuietBootInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfQuietBootInstanceId.setStatus("current")
_CfprApBiosVfQuietBootDn_Type = CfprApManagedObjectDn
_CfprApBiosVfQuietBootDn_Object = MibTableColumn
cfprApBiosVfQuietBootDn = _CfprApBiosVfQuietBootDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 62, 1, 2),
    _CfprApBiosVfQuietBootDn_Type()
)
cfprApBiosVfQuietBootDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfQuietBootDn.setStatus("current")
_CfprApBiosVfQuietBootRn_Type = SnmpAdminString
_CfprApBiosVfQuietBootRn_Object = MibTableColumn
cfprApBiosVfQuietBootRn = _CfprApBiosVfQuietBootRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 62, 1, 3),
    _CfprApBiosVfQuietBootRn_Type()
)
cfprApBiosVfQuietBootRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfQuietBootRn.setStatus("current")
_CfprApBiosVfQuietBootVpQuietBoot_Type = CfprApBiosVfQuietBootVpQuietBoot
_CfprApBiosVfQuietBootVpQuietBoot_Object = MibTableColumn
cfprApBiosVfQuietBootVpQuietBoot = _CfprApBiosVfQuietBootVpQuietBoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 62, 1, 4),
    _CfprApBiosVfQuietBootVpQuietBoot_Type()
)
cfprApBiosVfQuietBootVpQuietBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfQuietBootVpQuietBoot.setStatus("current")
_CfprApBiosVfResumeOnACPowerLossTable_Object = MibTable
cfprApBiosVfResumeOnACPowerLossTable = _CfprApBiosVfResumeOnACPowerLossTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 63)
)
if mibBuilder.loadTexts:
    cfprApBiosVfResumeOnACPowerLossTable.setStatus("current")
_CfprApBiosVfResumeOnACPowerLossEntry_Object = MibTableRow
cfprApBiosVfResumeOnACPowerLossEntry = _CfprApBiosVfResumeOnACPowerLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 63, 1)
)
cfprApBiosVfResumeOnACPowerLossEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfResumeOnACPowerLossInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfResumeOnACPowerLossEntry.setStatus("current")
_CfprApBiosVfResumeOnACPowerLossInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfResumeOnACPowerLossInstanceId_Object = MibTableColumn
cfprApBiosVfResumeOnACPowerLossInstanceId = _CfprApBiosVfResumeOnACPowerLossInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 63, 1, 1),
    _CfprApBiosVfResumeOnACPowerLossInstanceId_Type()
)
cfprApBiosVfResumeOnACPowerLossInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfResumeOnACPowerLossInstanceId.setStatus("current")
_CfprApBiosVfResumeOnACPowerLossDn_Type = CfprApManagedObjectDn
_CfprApBiosVfResumeOnACPowerLossDn_Object = MibTableColumn
cfprApBiosVfResumeOnACPowerLossDn = _CfprApBiosVfResumeOnACPowerLossDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 63, 1, 2),
    _CfprApBiosVfResumeOnACPowerLossDn_Type()
)
cfprApBiosVfResumeOnACPowerLossDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfResumeOnACPowerLossDn.setStatus("current")
_CfprApBiosVfResumeOnACPowerLossRn_Type = SnmpAdminString
_CfprApBiosVfResumeOnACPowerLossRn_Object = MibTableColumn
cfprApBiosVfResumeOnACPowerLossRn = _CfprApBiosVfResumeOnACPowerLossRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 63, 1, 3),
    _CfprApBiosVfResumeOnACPowerLossRn_Type()
)
cfprApBiosVfResumeOnACPowerLossRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfResumeOnACPowerLossRn.setStatus("current")
_CfprApBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss_Type = CfprApBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss
_CfprApBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss_Object = MibTableColumn
cfprApBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss = _CfprApBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 63, 1, 4),
    _CfprApBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss_Type()
)
cfprApBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss.setStatus("current")
_CfprApBiosVfScrubPoliciesTable_Object = MibTable
cfprApBiosVfScrubPoliciesTable = _CfprApBiosVfScrubPoliciesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 64)
)
if mibBuilder.loadTexts:
    cfprApBiosVfScrubPoliciesTable.setStatus("current")
_CfprApBiosVfScrubPoliciesEntry_Object = MibTableRow
cfprApBiosVfScrubPoliciesEntry = _CfprApBiosVfScrubPoliciesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 64, 1)
)
cfprApBiosVfScrubPoliciesEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfScrubPoliciesInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfScrubPoliciesEntry.setStatus("current")
_CfprApBiosVfScrubPoliciesInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfScrubPoliciesInstanceId_Object = MibTableColumn
cfprApBiosVfScrubPoliciesInstanceId = _CfprApBiosVfScrubPoliciesInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 64, 1, 1),
    _CfprApBiosVfScrubPoliciesInstanceId_Type()
)
cfprApBiosVfScrubPoliciesInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfScrubPoliciesInstanceId.setStatus("current")
_CfprApBiosVfScrubPoliciesDn_Type = CfprApManagedObjectDn
_CfprApBiosVfScrubPoliciesDn_Object = MibTableColumn
cfprApBiosVfScrubPoliciesDn = _CfprApBiosVfScrubPoliciesDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 64, 1, 2),
    _CfprApBiosVfScrubPoliciesDn_Type()
)
cfprApBiosVfScrubPoliciesDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfScrubPoliciesDn.setStatus("current")
_CfprApBiosVfScrubPoliciesRn_Type = SnmpAdminString
_CfprApBiosVfScrubPoliciesRn_Object = MibTableColumn
cfprApBiosVfScrubPoliciesRn = _CfprApBiosVfScrubPoliciesRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 64, 1, 3),
    _CfprApBiosVfScrubPoliciesRn_Type()
)
cfprApBiosVfScrubPoliciesRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfScrubPoliciesRn.setStatus("current")
_CfprApBiosVfScrubPoliciesVpDemandScrub_Type = CfprApBiosVfScrubPoliciesVpDemandScrub
_CfprApBiosVfScrubPoliciesVpDemandScrub_Object = MibTableColumn
cfprApBiosVfScrubPoliciesVpDemandScrub = _CfprApBiosVfScrubPoliciesVpDemandScrub_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 64, 1, 4),
    _CfprApBiosVfScrubPoliciesVpDemandScrub_Type()
)
cfprApBiosVfScrubPoliciesVpDemandScrub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfScrubPoliciesVpDemandScrub.setStatus("current")
_CfprApBiosVfScrubPoliciesVpPatrolScrub_Type = CfprApBiosVfScrubPoliciesVpPatrolScrub
_CfprApBiosVfScrubPoliciesVpPatrolScrub_Object = MibTableColumn
cfprApBiosVfScrubPoliciesVpPatrolScrub = _CfprApBiosVfScrubPoliciesVpPatrolScrub_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 64, 1, 5),
    _CfprApBiosVfScrubPoliciesVpPatrolScrub_Type()
)
cfprApBiosVfScrubPoliciesVpPatrolScrub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfScrubPoliciesVpPatrolScrub.setStatus("current")
_CfprApBiosVfSelectMemoryRASConfigurationTable_Object = MibTable
cfprApBiosVfSelectMemoryRASConfigurationTable = _CfprApBiosVfSelectMemoryRASConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 65)
)
if mibBuilder.loadTexts:
    cfprApBiosVfSelectMemoryRASConfigurationTable.setStatus("current")
_CfprApBiosVfSelectMemoryRASConfigurationEntry_Object = MibTableRow
cfprApBiosVfSelectMemoryRASConfigurationEntry = _CfprApBiosVfSelectMemoryRASConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 65, 1)
)
cfprApBiosVfSelectMemoryRASConfigurationEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfSelectMemoryRASConfigurationInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfSelectMemoryRASConfigurationEntry.setStatus("current")
_CfprApBiosVfSelectMemoryRASConfigurationInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfSelectMemoryRASConfigurationInstanceId_Object = MibTableColumn
cfprApBiosVfSelectMemoryRASConfigurationInstanceId = _CfprApBiosVfSelectMemoryRASConfigurationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 65, 1, 1),
    _CfprApBiosVfSelectMemoryRASConfigurationInstanceId_Type()
)
cfprApBiosVfSelectMemoryRASConfigurationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfSelectMemoryRASConfigurationInstanceId.setStatus("current")
_CfprApBiosVfSelectMemoryRASConfigurationDn_Type = CfprApManagedObjectDn
_CfprApBiosVfSelectMemoryRASConfigurationDn_Object = MibTableColumn
cfprApBiosVfSelectMemoryRASConfigurationDn = _CfprApBiosVfSelectMemoryRASConfigurationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 65, 1, 2),
    _CfprApBiosVfSelectMemoryRASConfigurationDn_Type()
)
cfprApBiosVfSelectMemoryRASConfigurationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfSelectMemoryRASConfigurationDn.setStatus("current")
_CfprApBiosVfSelectMemoryRASConfigurationRn_Type = SnmpAdminString
_CfprApBiosVfSelectMemoryRASConfigurationRn_Object = MibTableColumn
cfprApBiosVfSelectMemoryRASConfigurationRn = _CfprApBiosVfSelectMemoryRASConfigurationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 65, 1, 3),
    _CfprApBiosVfSelectMemoryRASConfigurationRn_Type()
)
cfprApBiosVfSelectMemoryRASConfigurationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfSelectMemoryRASConfigurationRn.setStatus("current")
_CfprApBiosVfSelectMemoryRASConfigurationVpSelectMemoryRASConfiguration_Type = CfprApBiosVfSelectMemoryRASConfigurationVpSelectMemoryRASConf
_CfprApBiosVfSelectMemoryRASConfigurationVpSelectMemoryRASConfiguration_Object = MibTableColumn
cfprApBiosVfSelectMemoryRASConfigurationVpSelectMemoryRASConfiguration = _CfprApBiosVfSelectMemoryRASConfigurationVpSelectMemoryRASConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 65, 1, 4),
    _CfprApBiosVfSelectMemoryRASConfigurationVpSelectMemoryRASConfiguration_Type()
)
cfprApBiosVfSelectMemoryRASConfigurationVpSelectMemoryRASConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfSelectMemoryRASConfigurationVpSelectMemoryRASConfiguration.setStatus("current")
_CfprApBiosVfSerialPortAEnableTable_Object = MibTable
cfprApBiosVfSerialPortAEnableTable = _CfprApBiosVfSerialPortAEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 66)
)
if mibBuilder.loadTexts:
    cfprApBiosVfSerialPortAEnableTable.setStatus("current")
_CfprApBiosVfSerialPortAEnableEntry_Object = MibTableRow
cfprApBiosVfSerialPortAEnableEntry = _CfprApBiosVfSerialPortAEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 66, 1)
)
cfprApBiosVfSerialPortAEnableEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfSerialPortAEnableInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfSerialPortAEnableEntry.setStatus("current")
_CfprApBiosVfSerialPortAEnableInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfSerialPortAEnableInstanceId_Object = MibTableColumn
cfprApBiosVfSerialPortAEnableInstanceId = _CfprApBiosVfSerialPortAEnableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 66, 1, 1),
    _CfprApBiosVfSerialPortAEnableInstanceId_Type()
)
cfprApBiosVfSerialPortAEnableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfSerialPortAEnableInstanceId.setStatus("current")
_CfprApBiosVfSerialPortAEnableDn_Type = CfprApManagedObjectDn
_CfprApBiosVfSerialPortAEnableDn_Object = MibTableColumn
cfprApBiosVfSerialPortAEnableDn = _CfprApBiosVfSerialPortAEnableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 66, 1, 2),
    _CfprApBiosVfSerialPortAEnableDn_Type()
)
cfprApBiosVfSerialPortAEnableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfSerialPortAEnableDn.setStatus("current")
_CfprApBiosVfSerialPortAEnableRn_Type = SnmpAdminString
_CfprApBiosVfSerialPortAEnableRn_Object = MibTableColumn
cfprApBiosVfSerialPortAEnableRn = _CfprApBiosVfSerialPortAEnableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 66, 1, 3),
    _CfprApBiosVfSerialPortAEnableRn_Type()
)
cfprApBiosVfSerialPortAEnableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfSerialPortAEnableRn.setStatus("current")
_CfprApBiosVfSerialPortAEnableVpSerialPortAEnable_Type = CfprApBiosVfSerialPortAEnableVpSerialPortAEnable
_CfprApBiosVfSerialPortAEnableVpSerialPortAEnable_Object = MibTableColumn
cfprApBiosVfSerialPortAEnableVpSerialPortAEnable = _CfprApBiosVfSerialPortAEnableVpSerialPortAEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 66, 1, 4),
    _CfprApBiosVfSerialPortAEnableVpSerialPortAEnable_Type()
)
cfprApBiosVfSerialPortAEnableVpSerialPortAEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfSerialPortAEnableVpSerialPortAEnable.setStatus("current")
_CfprApBiosVfSparingModeTable_Object = MibTable
cfprApBiosVfSparingModeTable = _CfprApBiosVfSparingModeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 67)
)
if mibBuilder.loadTexts:
    cfprApBiosVfSparingModeTable.setStatus("current")
_CfprApBiosVfSparingModeEntry_Object = MibTableRow
cfprApBiosVfSparingModeEntry = _CfprApBiosVfSparingModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 67, 1)
)
cfprApBiosVfSparingModeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfSparingModeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfSparingModeEntry.setStatus("current")
_CfprApBiosVfSparingModeInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfSparingModeInstanceId_Object = MibTableColumn
cfprApBiosVfSparingModeInstanceId = _CfprApBiosVfSparingModeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 67, 1, 1),
    _CfprApBiosVfSparingModeInstanceId_Type()
)
cfprApBiosVfSparingModeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfSparingModeInstanceId.setStatus("current")
_CfprApBiosVfSparingModeDn_Type = CfprApManagedObjectDn
_CfprApBiosVfSparingModeDn_Object = MibTableColumn
cfprApBiosVfSparingModeDn = _CfprApBiosVfSparingModeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 67, 1, 2),
    _CfprApBiosVfSparingModeDn_Type()
)
cfprApBiosVfSparingModeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfSparingModeDn.setStatus("current")
_CfprApBiosVfSparingModeRn_Type = SnmpAdminString
_CfprApBiosVfSparingModeRn_Object = MibTableColumn
cfprApBiosVfSparingModeRn = _CfprApBiosVfSparingModeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 67, 1, 3),
    _CfprApBiosVfSparingModeRn_Type()
)
cfprApBiosVfSparingModeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfSparingModeRn.setStatus("current")
_CfprApBiosVfSparingModeVpSparingMode_Type = CfprApBiosVfSparingModeVpSparingMode
_CfprApBiosVfSparingModeVpSparingMode_Object = MibTableColumn
cfprApBiosVfSparingModeVpSparingMode = _CfprApBiosVfSparingModeVpSparingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 67, 1, 4),
    _CfprApBiosVfSparingModeVpSparingMode_Type()
)
cfprApBiosVfSparingModeVpSparingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfSparingModeVpSparingMode.setStatus("current")
_CfprApBiosVfSriovConfigTable_Object = MibTable
cfprApBiosVfSriovConfigTable = _CfprApBiosVfSriovConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 68)
)
if mibBuilder.loadTexts:
    cfprApBiosVfSriovConfigTable.setStatus("current")
_CfprApBiosVfSriovConfigEntry_Object = MibTableRow
cfprApBiosVfSriovConfigEntry = _CfprApBiosVfSriovConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 68, 1)
)
cfprApBiosVfSriovConfigEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfSriovConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfSriovConfigEntry.setStatus("current")
_CfprApBiosVfSriovConfigInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfSriovConfigInstanceId_Object = MibTableColumn
cfprApBiosVfSriovConfigInstanceId = _CfprApBiosVfSriovConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 68, 1, 1),
    _CfprApBiosVfSriovConfigInstanceId_Type()
)
cfprApBiosVfSriovConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfSriovConfigInstanceId.setStatus("current")
_CfprApBiosVfSriovConfigDn_Type = CfprApManagedObjectDn
_CfprApBiosVfSriovConfigDn_Object = MibTableColumn
cfprApBiosVfSriovConfigDn = _CfprApBiosVfSriovConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 68, 1, 2),
    _CfprApBiosVfSriovConfigDn_Type()
)
cfprApBiosVfSriovConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfSriovConfigDn.setStatus("current")
_CfprApBiosVfSriovConfigRn_Type = SnmpAdminString
_CfprApBiosVfSriovConfigRn_Object = MibTableColumn
cfprApBiosVfSriovConfigRn = _CfprApBiosVfSriovConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 68, 1, 3),
    _CfprApBiosVfSriovConfigRn_Type()
)
cfprApBiosVfSriovConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfSriovConfigRn.setStatus("current")
_CfprApBiosVfSriovConfigVpSriov_Type = CfprApBiosVfSriovConfigVpSriov
_CfprApBiosVfSriovConfigVpSriov_Object = MibTableColumn
cfprApBiosVfSriovConfigVpSriov = _CfprApBiosVfSriovConfigVpSriov_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 68, 1, 4),
    _CfprApBiosVfSriovConfigVpSriov_Type()
)
cfprApBiosVfSriovConfigVpSriov.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfSriovConfigVpSriov.setStatus("current")
_CfprApBiosVfTPMSupportTable_Object = MibTable
cfprApBiosVfTPMSupportTable = _CfprApBiosVfTPMSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 69)
)
if mibBuilder.loadTexts:
    cfprApBiosVfTPMSupportTable.setStatus("current")
_CfprApBiosVfTPMSupportEntry_Object = MibTableRow
cfprApBiosVfTPMSupportEntry = _CfprApBiosVfTPMSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 69, 1)
)
cfprApBiosVfTPMSupportEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfTPMSupportInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfTPMSupportEntry.setStatus("current")
_CfprApBiosVfTPMSupportInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfTPMSupportInstanceId_Object = MibTableColumn
cfprApBiosVfTPMSupportInstanceId = _CfprApBiosVfTPMSupportInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 69, 1, 1),
    _CfprApBiosVfTPMSupportInstanceId_Type()
)
cfprApBiosVfTPMSupportInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfTPMSupportInstanceId.setStatus("current")
_CfprApBiosVfTPMSupportDn_Type = CfprApManagedObjectDn
_CfprApBiosVfTPMSupportDn_Object = MibTableColumn
cfprApBiosVfTPMSupportDn = _CfprApBiosVfTPMSupportDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 69, 1, 2),
    _CfprApBiosVfTPMSupportDn_Type()
)
cfprApBiosVfTPMSupportDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfTPMSupportDn.setStatus("current")
_CfprApBiosVfTPMSupportRn_Type = SnmpAdminString
_CfprApBiosVfTPMSupportRn_Object = MibTableColumn
cfprApBiosVfTPMSupportRn = _CfprApBiosVfTPMSupportRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 69, 1, 3),
    _CfprApBiosVfTPMSupportRn_Type()
)
cfprApBiosVfTPMSupportRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfTPMSupportRn.setStatus("current")
_CfprApBiosVfTPMSupportVpTPMSupport_Type = CfprApBiosVfTPMSupportVpTPMSupport
_CfprApBiosVfTPMSupportVpTPMSupport_Object = MibTableColumn
cfprApBiosVfTPMSupportVpTPMSupport = _CfprApBiosVfTPMSupportVpTPMSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 69, 1, 4),
    _CfprApBiosVfTPMSupportVpTPMSupport_Type()
)
cfprApBiosVfTPMSupportVpTPMSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfTPMSupportVpTPMSupport.setStatus("current")
_CfprApBiosVfUCSMBootModeControlTable_Object = MibTable
cfprApBiosVfUCSMBootModeControlTable = _CfprApBiosVfUCSMBootModeControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 70)
)
if mibBuilder.loadTexts:
    cfprApBiosVfUCSMBootModeControlTable.setStatus("current")
_CfprApBiosVfUCSMBootModeControlEntry_Object = MibTableRow
cfprApBiosVfUCSMBootModeControlEntry = _CfprApBiosVfUCSMBootModeControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 70, 1)
)
cfprApBiosVfUCSMBootModeControlEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfUCSMBootModeControlInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfUCSMBootModeControlEntry.setStatus("current")
_CfprApBiosVfUCSMBootModeControlInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfUCSMBootModeControlInstanceId_Object = MibTableColumn
cfprApBiosVfUCSMBootModeControlInstanceId = _CfprApBiosVfUCSMBootModeControlInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 70, 1, 1),
    _CfprApBiosVfUCSMBootModeControlInstanceId_Type()
)
cfprApBiosVfUCSMBootModeControlInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfUCSMBootModeControlInstanceId.setStatus("current")
_CfprApBiosVfUCSMBootModeControlDn_Type = CfprApManagedObjectDn
_CfprApBiosVfUCSMBootModeControlDn_Object = MibTableColumn
cfprApBiosVfUCSMBootModeControlDn = _CfprApBiosVfUCSMBootModeControlDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 70, 1, 2),
    _CfprApBiosVfUCSMBootModeControlDn_Type()
)
cfprApBiosVfUCSMBootModeControlDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUCSMBootModeControlDn.setStatus("current")
_CfprApBiosVfUCSMBootModeControlRn_Type = SnmpAdminString
_CfprApBiosVfUCSMBootModeControlRn_Object = MibTableColumn
cfprApBiosVfUCSMBootModeControlRn = _CfprApBiosVfUCSMBootModeControlRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 70, 1, 3),
    _CfprApBiosVfUCSMBootModeControlRn_Type()
)
cfprApBiosVfUCSMBootModeControlRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUCSMBootModeControlRn.setStatus("current")
_CfprApBiosVfUCSMBootModeControlVpUEFIBootMode_Type = CfprApBiosVfUCSMBootModeControlVpUEFIBootMode
_CfprApBiosVfUCSMBootModeControlVpUEFIBootMode_Object = MibTableColumn
cfprApBiosVfUCSMBootModeControlVpUEFIBootMode = _CfprApBiosVfUCSMBootModeControlVpUEFIBootMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 70, 1, 4),
    _CfprApBiosVfUCSMBootModeControlVpUEFIBootMode_Type()
)
cfprApBiosVfUCSMBootModeControlVpUEFIBootMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUCSMBootModeControlVpUEFIBootMode.setStatus("current")
_CfprApBiosVfUCSMBootOrderRuleControlTable_Object = MibTable
cfprApBiosVfUCSMBootOrderRuleControlTable = _CfprApBiosVfUCSMBootOrderRuleControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 71)
)
if mibBuilder.loadTexts:
    cfprApBiosVfUCSMBootOrderRuleControlTable.setStatus("current")
_CfprApBiosVfUCSMBootOrderRuleControlEntry_Object = MibTableRow
cfprApBiosVfUCSMBootOrderRuleControlEntry = _CfprApBiosVfUCSMBootOrderRuleControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 71, 1)
)
cfprApBiosVfUCSMBootOrderRuleControlEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfUCSMBootOrderRuleControlInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfUCSMBootOrderRuleControlEntry.setStatus("current")
_CfprApBiosVfUCSMBootOrderRuleControlInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfUCSMBootOrderRuleControlInstanceId_Object = MibTableColumn
cfprApBiosVfUCSMBootOrderRuleControlInstanceId = _CfprApBiosVfUCSMBootOrderRuleControlInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 71, 1, 1),
    _CfprApBiosVfUCSMBootOrderRuleControlInstanceId_Type()
)
cfprApBiosVfUCSMBootOrderRuleControlInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfUCSMBootOrderRuleControlInstanceId.setStatus("current")
_CfprApBiosVfUCSMBootOrderRuleControlDn_Type = CfprApManagedObjectDn
_CfprApBiosVfUCSMBootOrderRuleControlDn_Object = MibTableColumn
cfprApBiosVfUCSMBootOrderRuleControlDn = _CfprApBiosVfUCSMBootOrderRuleControlDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 71, 1, 2),
    _CfprApBiosVfUCSMBootOrderRuleControlDn_Type()
)
cfprApBiosVfUCSMBootOrderRuleControlDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUCSMBootOrderRuleControlDn.setStatus("current")
_CfprApBiosVfUCSMBootOrderRuleControlRn_Type = SnmpAdminString
_CfprApBiosVfUCSMBootOrderRuleControlRn_Object = MibTableColumn
cfprApBiosVfUCSMBootOrderRuleControlRn = _CfprApBiosVfUCSMBootOrderRuleControlRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 71, 1, 3),
    _CfprApBiosVfUCSMBootOrderRuleControlRn_Type()
)
cfprApBiosVfUCSMBootOrderRuleControlRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUCSMBootOrderRuleControlRn.setStatus("current")
_CfprApBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule_Type = CfprApBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule
_CfprApBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule_Object = MibTableColumn
cfprApBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule = _CfprApBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 71, 1, 4),
    _CfprApBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule_Type()
)
cfprApBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule.setStatus("current")
_CfprApBiosVfUEFIOSUseLegacyVideoTable_Object = MibTable
cfprApBiosVfUEFIOSUseLegacyVideoTable = _CfprApBiosVfUEFIOSUseLegacyVideoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 72)
)
if mibBuilder.loadTexts:
    cfprApBiosVfUEFIOSUseLegacyVideoTable.setStatus("current")
_CfprApBiosVfUEFIOSUseLegacyVideoEntry_Object = MibTableRow
cfprApBiosVfUEFIOSUseLegacyVideoEntry = _CfprApBiosVfUEFIOSUseLegacyVideoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 72, 1)
)
cfprApBiosVfUEFIOSUseLegacyVideoEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfUEFIOSUseLegacyVideoInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfUEFIOSUseLegacyVideoEntry.setStatus("current")
_CfprApBiosVfUEFIOSUseLegacyVideoInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfUEFIOSUseLegacyVideoInstanceId_Object = MibTableColumn
cfprApBiosVfUEFIOSUseLegacyVideoInstanceId = _CfprApBiosVfUEFIOSUseLegacyVideoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 72, 1, 1),
    _CfprApBiosVfUEFIOSUseLegacyVideoInstanceId_Type()
)
cfprApBiosVfUEFIOSUseLegacyVideoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfUEFIOSUseLegacyVideoInstanceId.setStatus("current")
_CfprApBiosVfUEFIOSUseLegacyVideoDn_Type = CfprApManagedObjectDn
_CfprApBiosVfUEFIOSUseLegacyVideoDn_Object = MibTableColumn
cfprApBiosVfUEFIOSUseLegacyVideoDn = _CfprApBiosVfUEFIOSUseLegacyVideoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 72, 1, 2),
    _CfprApBiosVfUEFIOSUseLegacyVideoDn_Type()
)
cfprApBiosVfUEFIOSUseLegacyVideoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUEFIOSUseLegacyVideoDn.setStatus("current")
_CfprApBiosVfUEFIOSUseLegacyVideoRn_Type = SnmpAdminString
_CfprApBiosVfUEFIOSUseLegacyVideoRn_Object = MibTableColumn
cfprApBiosVfUEFIOSUseLegacyVideoRn = _CfprApBiosVfUEFIOSUseLegacyVideoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 72, 1, 3),
    _CfprApBiosVfUEFIOSUseLegacyVideoRn_Type()
)
cfprApBiosVfUEFIOSUseLegacyVideoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUEFIOSUseLegacyVideoRn.setStatus("current")
_CfprApBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo_Type = CfprApBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo
_CfprApBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo_Object = MibTableColumn
cfprApBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo = _CfprApBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 72, 1, 4),
    _CfprApBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo_Type()
)
cfprApBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo.setStatus("current")
_CfprApBiosVfUSBBootConfigTable_Object = MibTable
cfprApBiosVfUSBBootConfigTable = _CfprApBiosVfUSBBootConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 73)
)
if mibBuilder.loadTexts:
    cfprApBiosVfUSBBootConfigTable.setStatus("current")
_CfprApBiosVfUSBBootConfigEntry_Object = MibTableRow
cfprApBiosVfUSBBootConfigEntry = _CfprApBiosVfUSBBootConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 73, 1)
)
cfprApBiosVfUSBBootConfigEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfUSBBootConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfUSBBootConfigEntry.setStatus("current")
_CfprApBiosVfUSBBootConfigInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfUSBBootConfigInstanceId_Object = MibTableColumn
cfprApBiosVfUSBBootConfigInstanceId = _CfprApBiosVfUSBBootConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 73, 1, 1),
    _CfprApBiosVfUSBBootConfigInstanceId_Type()
)
cfprApBiosVfUSBBootConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBBootConfigInstanceId.setStatus("current")
_CfprApBiosVfUSBBootConfigDn_Type = CfprApManagedObjectDn
_CfprApBiosVfUSBBootConfigDn_Object = MibTableColumn
cfprApBiosVfUSBBootConfigDn = _CfprApBiosVfUSBBootConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 73, 1, 2),
    _CfprApBiosVfUSBBootConfigDn_Type()
)
cfprApBiosVfUSBBootConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBBootConfigDn.setStatus("current")
_CfprApBiosVfUSBBootConfigRn_Type = SnmpAdminString
_CfprApBiosVfUSBBootConfigRn_Object = MibTableColumn
cfprApBiosVfUSBBootConfigRn = _CfprApBiosVfUSBBootConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 73, 1, 3),
    _CfprApBiosVfUSBBootConfigRn_Type()
)
cfprApBiosVfUSBBootConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBBootConfigRn.setStatus("current")
_CfprApBiosVfUSBBootConfigVpLegacyUSBSupport_Type = CfprApBiosVfUSBBootConfigVpLegacyUSBSupport
_CfprApBiosVfUSBBootConfigVpLegacyUSBSupport_Object = MibTableColumn
cfprApBiosVfUSBBootConfigVpLegacyUSBSupport = _CfprApBiosVfUSBBootConfigVpLegacyUSBSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 73, 1, 4),
    _CfprApBiosVfUSBBootConfigVpLegacyUSBSupport_Type()
)
cfprApBiosVfUSBBootConfigVpLegacyUSBSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBBootConfigVpLegacyUSBSupport.setStatus("current")
_CfprApBiosVfUSBBootConfigVpMakeDeviceNonBootable_Type = CfprApBiosVfUSBBootConfigVpMakeDeviceNonBootable
_CfprApBiosVfUSBBootConfigVpMakeDeviceNonBootable_Object = MibTableColumn
cfprApBiosVfUSBBootConfigVpMakeDeviceNonBootable = _CfprApBiosVfUSBBootConfigVpMakeDeviceNonBootable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 73, 1, 5),
    _CfprApBiosVfUSBBootConfigVpMakeDeviceNonBootable_Type()
)
cfprApBiosVfUSBBootConfigVpMakeDeviceNonBootable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBBootConfigVpMakeDeviceNonBootable.setStatus("current")
_CfprApBiosVfUSBConfigurationTable_Object = MibTable
cfprApBiosVfUSBConfigurationTable = _CfprApBiosVfUSBConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 74)
)
if mibBuilder.loadTexts:
    cfprApBiosVfUSBConfigurationTable.setStatus("current")
_CfprApBiosVfUSBConfigurationEntry_Object = MibTableRow
cfprApBiosVfUSBConfigurationEntry = _CfprApBiosVfUSBConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 74, 1)
)
cfprApBiosVfUSBConfigurationEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfUSBConfigurationInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfUSBConfigurationEntry.setStatus("current")
_CfprApBiosVfUSBConfigurationInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfUSBConfigurationInstanceId_Object = MibTableColumn
cfprApBiosVfUSBConfigurationInstanceId = _CfprApBiosVfUSBConfigurationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 74, 1, 1),
    _CfprApBiosVfUSBConfigurationInstanceId_Type()
)
cfprApBiosVfUSBConfigurationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBConfigurationInstanceId.setStatus("current")
_CfprApBiosVfUSBConfigurationDn_Type = CfprApManagedObjectDn
_CfprApBiosVfUSBConfigurationDn_Object = MibTableColumn
cfprApBiosVfUSBConfigurationDn = _CfprApBiosVfUSBConfigurationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 74, 1, 2),
    _CfprApBiosVfUSBConfigurationDn_Type()
)
cfprApBiosVfUSBConfigurationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBConfigurationDn.setStatus("current")
_CfprApBiosVfUSBConfigurationRn_Type = SnmpAdminString
_CfprApBiosVfUSBConfigurationRn_Object = MibTableColumn
cfprApBiosVfUSBConfigurationRn = _CfprApBiosVfUSBConfigurationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 74, 1, 3),
    _CfprApBiosVfUSBConfigurationRn_Type()
)
cfprApBiosVfUSBConfigurationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBConfigurationRn.setStatus("current")
_CfprApBiosVfUSBConfigurationVpLegacyUSBSupport_Type = CfprApBiosVfUSBConfigurationVpLegacyUSBSupport
_CfprApBiosVfUSBConfigurationVpLegacyUSBSupport_Object = MibTableColumn
cfprApBiosVfUSBConfigurationVpLegacyUSBSupport = _CfprApBiosVfUSBConfigurationVpLegacyUSBSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 74, 1, 4),
    _CfprApBiosVfUSBConfigurationVpLegacyUSBSupport_Type()
)
cfprApBiosVfUSBConfigurationVpLegacyUSBSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBConfigurationVpLegacyUSBSupport.setStatus("current")
_CfprApBiosVfUSBConfigurationVpXHCIMode_Type = CfprApBiosVfUSBConfigurationVpXHCIMode
_CfprApBiosVfUSBConfigurationVpXHCIMode_Object = MibTableColumn
cfprApBiosVfUSBConfigurationVpXHCIMode = _CfprApBiosVfUSBConfigurationVpXHCIMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 74, 1, 5),
    _CfprApBiosVfUSBConfigurationVpXHCIMode_Type()
)
cfprApBiosVfUSBConfigurationVpXHCIMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBConfigurationVpXHCIMode.setStatus("current")
_CfprApBiosVfUSBFrontPanelAccessLockTable_Object = MibTable
cfprApBiosVfUSBFrontPanelAccessLockTable = _CfprApBiosVfUSBFrontPanelAccessLockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 75)
)
if mibBuilder.loadTexts:
    cfprApBiosVfUSBFrontPanelAccessLockTable.setStatus("current")
_CfprApBiosVfUSBFrontPanelAccessLockEntry_Object = MibTableRow
cfprApBiosVfUSBFrontPanelAccessLockEntry = _CfprApBiosVfUSBFrontPanelAccessLockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 75, 1)
)
cfprApBiosVfUSBFrontPanelAccessLockEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfUSBFrontPanelAccessLockInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfUSBFrontPanelAccessLockEntry.setStatus("current")
_CfprApBiosVfUSBFrontPanelAccessLockInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfUSBFrontPanelAccessLockInstanceId_Object = MibTableColumn
cfprApBiosVfUSBFrontPanelAccessLockInstanceId = _CfprApBiosVfUSBFrontPanelAccessLockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 75, 1, 1),
    _CfprApBiosVfUSBFrontPanelAccessLockInstanceId_Type()
)
cfprApBiosVfUSBFrontPanelAccessLockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBFrontPanelAccessLockInstanceId.setStatus("current")
_CfprApBiosVfUSBFrontPanelAccessLockDn_Type = CfprApManagedObjectDn
_CfprApBiosVfUSBFrontPanelAccessLockDn_Object = MibTableColumn
cfprApBiosVfUSBFrontPanelAccessLockDn = _CfprApBiosVfUSBFrontPanelAccessLockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 75, 1, 2),
    _CfprApBiosVfUSBFrontPanelAccessLockDn_Type()
)
cfprApBiosVfUSBFrontPanelAccessLockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBFrontPanelAccessLockDn.setStatus("current")
_CfprApBiosVfUSBFrontPanelAccessLockRn_Type = SnmpAdminString
_CfprApBiosVfUSBFrontPanelAccessLockRn_Object = MibTableColumn
cfprApBiosVfUSBFrontPanelAccessLockRn = _CfprApBiosVfUSBFrontPanelAccessLockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 75, 1, 3),
    _CfprApBiosVfUSBFrontPanelAccessLockRn_Type()
)
cfprApBiosVfUSBFrontPanelAccessLockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBFrontPanelAccessLockRn.setStatus("current")
_CfprApBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock_Type = CfprApBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock
_CfprApBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock_Object = MibTableColumn
cfprApBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock = _CfprApBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 75, 1, 4),
    _CfprApBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock_Type()
)
cfprApBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock.setStatus("current")
_CfprApBiosVfUSBPortConfigurationTable_Object = MibTable
cfprApBiosVfUSBPortConfigurationTable = _CfprApBiosVfUSBPortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 76)
)
if mibBuilder.loadTexts:
    cfprApBiosVfUSBPortConfigurationTable.setStatus("current")
_CfprApBiosVfUSBPortConfigurationEntry_Object = MibTableRow
cfprApBiosVfUSBPortConfigurationEntry = _CfprApBiosVfUSBPortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 76, 1)
)
cfprApBiosVfUSBPortConfigurationEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfUSBPortConfigurationInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfUSBPortConfigurationEntry.setStatus("current")
_CfprApBiosVfUSBPortConfigurationInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfUSBPortConfigurationInstanceId_Object = MibTableColumn
cfprApBiosVfUSBPortConfigurationInstanceId = _CfprApBiosVfUSBPortConfigurationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 76, 1, 1),
    _CfprApBiosVfUSBPortConfigurationInstanceId_Type()
)
cfprApBiosVfUSBPortConfigurationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBPortConfigurationInstanceId.setStatus("current")
_CfprApBiosVfUSBPortConfigurationDn_Type = CfprApManagedObjectDn
_CfprApBiosVfUSBPortConfigurationDn_Object = MibTableColumn
cfprApBiosVfUSBPortConfigurationDn = _CfprApBiosVfUSBPortConfigurationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 76, 1, 2),
    _CfprApBiosVfUSBPortConfigurationDn_Type()
)
cfprApBiosVfUSBPortConfigurationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBPortConfigurationDn.setStatus("current")
_CfprApBiosVfUSBPortConfigurationRn_Type = SnmpAdminString
_CfprApBiosVfUSBPortConfigurationRn_Object = MibTableColumn
cfprApBiosVfUSBPortConfigurationRn = _CfprApBiosVfUSBPortConfigurationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 76, 1, 3),
    _CfprApBiosVfUSBPortConfigurationRn_Type()
)
cfprApBiosVfUSBPortConfigurationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBPortConfigurationRn.setStatus("current")
_CfprApBiosVfUSBPortConfigurationVpPort6064Emulation_Type = CfprApBiosVfUSBPortConfigurationVpPort6064Emulation
_CfprApBiosVfUSBPortConfigurationVpPort6064Emulation_Object = MibTableColumn
cfprApBiosVfUSBPortConfigurationVpPort6064Emulation = _CfprApBiosVfUSBPortConfigurationVpPort6064Emulation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 76, 1, 4),
    _CfprApBiosVfUSBPortConfigurationVpPort6064Emulation_Type()
)
cfprApBiosVfUSBPortConfigurationVpPort6064Emulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBPortConfigurationVpPort6064Emulation.setStatus("current")
_CfprApBiosVfUSBPortConfigurationVpUSBPortFront_Type = CfprApBiosVfUSBPortConfigurationVpUSBPortFront
_CfprApBiosVfUSBPortConfigurationVpUSBPortFront_Object = MibTableColumn
cfprApBiosVfUSBPortConfigurationVpUSBPortFront = _CfprApBiosVfUSBPortConfigurationVpUSBPortFront_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 76, 1, 5),
    _CfprApBiosVfUSBPortConfigurationVpUSBPortFront_Type()
)
cfprApBiosVfUSBPortConfigurationVpUSBPortFront.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBPortConfigurationVpUSBPortFront.setStatus("current")
_CfprApBiosVfUSBPortConfigurationVpUSBPortInternal_Type = CfprApBiosVfUSBPortConfigurationVpUSBPortInternal
_CfprApBiosVfUSBPortConfigurationVpUSBPortInternal_Object = MibTableColumn
cfprApBiosVfUSBPortConfigurationVpUSBPortInternal = _CfprApBiosVfUSBPortConfigurationVpUSBPortInternal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 76, 1, 6),
    _CfprApBiosVfUSBPortConfigurationVpUSBPortInternal_Type()
)
cfprApBiosVfUSBPortConfigurationVpUSBPortInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBPortConfigurationVpUSBPortInternal.setStatus("current")
_CfprApBiosVfUSBPortConfigurationVpUSBPortKVM_Type = CfprApBiosVfUSBPortConfigurationVpUSBPortKVM
_CfprApBiosVfUSBPortConfigurationVpUSBPortKVM_Object = MibTableColumn
cfprApBiosVfUSBPortConfigurationVpUSBPortKVM = _CfprApBiosVfUSBPortConfigurationVpUSBPortKVM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 76, 1, 7),
    _CfprApBiosVfUSBPortConfigurationVpUSBPortKVM_Type()
)
cfprApBiosVfUSBPortConfigurationVpUSBPortKVM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBPortConfigurationVpUSBPortKVM.setStatus("current")
_CfprApBiosVfUSBPortConfigurationVpUSBPortRear_Type = CfprApBiosVfUSBPortConfigurationVpUSBPortRear
_CfprApBiosVfUSBPortConfigurationVpUSBPortRear_Object = MibTableColumn
cfprApBiosVfUSBPortConfigurationVpUSBPortRear = _CfprApBiosVfUSBPortConfigurationVpUSBPortRear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 76, 1, 8),
    _CfprApBiosVfUSBPortConfigurationVpUSBPortRear_Type()
)
cfprApBiosVfUSBPortConfigurationVpUSBPortRear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBPortConfigurationVpUSBPortRear.setStatus("current")
_CfprApBiosVfUSBPortConfigurationVpUSBPortSDCard_Type = CfprApBiosVfUSBPortConfigurationVpUSBPortSDCard
_CfprApBiosVfUSBPortConfigurationVpUSBPortSDCard_Object = MibTableColumn
cfprApBiosVfUSBPortConfigurationVpUSBPortSDCard = _CfprApBiosVfUSBPortConfigurationVpUSBPortSDCard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 76, 1, 9),
    _CfprApBiosVfUSBPortConfigurationVpUSBPortSDCard_Type()
)
cfprApBiosVfUSBPortConfigurationVpUSBPortSDCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBPortConfigurationVpUSBPortSDCard.setStatus("current")
_CfprApBiosVfUSBPortConfigurationVpUSBPortVMedia_Type = CfprApBiosVfUSBPortConfigurationVpUSBPortVMedia
_CfprApBiosVfUSBPortConfigurationVpUSBPortVMedia_Object = MibTableColumn
cfprApBiosVfUSBPortConfigurationVpUSBPortVMedia = _CfprApBiosVfUSBPortConfigurationVpUSBPortVMedia_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 76, 1, 10),
    _CfprApBiosVfUSBPortConfigurationVpUSBPortVMedia_Type()
)
cfprApBiosVfUSBPortConfigurationVpUSBPortVMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBPortConfigurationVpUSBPortVMedia.setStatus("current")
_CfprApBiosVfUSBSystemIdlePowerOptimizingSettingTable_Object = MibTable
cfprApBiosVfUSBSystemIdlePowerOptimizingSettingTable = _CfprApBiosVfUSBSystemIdlePowerOptimizingSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 77)
)
if mibBuilder.loadTexts:
    cfprApBiosVfUSBSystemIdlePowerOptimizingSettingTable.setStatus("current")
_CfprApBiosVfUSBSystemIdlePowerOptimizingSettingEntry_Object = MibTableRow
cfprApBiosVfUSBSystemIdlePowerOptimizingSettingEntry = _CfprApBiosVfUSBSystemIdlePowerOptimizingSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 77, 1)
)
cfprApBiosVfUSBSystemIdlePowerOptimizingSettingEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfUSBSystemIdlePowerOptimizingSettingEntry.setStatus("current")
_CfprApBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId_Object = MibTableColumn
cfprApBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId = _CfprApBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 77, 1, 1),
    _CfprApBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId_Type()
)
cfprApBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId.setStatus("current")
_CfprApBiosVfUSBSystemIdlePowerOptimizingSettingDn_Type = CfprApManagedObjectDn
_CfprApBiosVfUSBSystemIdlePowerOptimizingSettingDn_Object = MibTableColumn
cfprApBiosVfUSBSystemIdlePowerOptimizingSettingDn = _CfprApBiosVfUSBSystemIdlePowerOptimizingSettingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 77, 1, 2),
    _CfprApBiosVfUSBSystemIdlePowerOptimizingSettingDn_Type()
)
cfprApBiosVfUSBSystemIdlePowerOptimizingSettingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBSystemIdlePowerOptimizingSettingDn.setStatus("current")
_CfprApBiosVfUSBSystemIdlePowerOptimizingSettingRn_Type = SnmpAdminString
_CfprApBiosVfUSBSystemIdlePowerOptimizingSettingRn_Object = MibTableColumn
cfprApBiosVfUSBSystemIdlePowerOptimizingSettingRn = _CfprApBiosVfUSBSystemIdlePowerOptimizingSettingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 77, 1, 3),
    _CfprApBiosVfUSBSystemIdlePowerOptimizingSettingRn_Type()
)
cfprApBiosVfUSBSystemIdlePowerOptimizingSettingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBSystemIdlePowerOptimizingSettingRn.setStatus("current")
_CfprApBiosVfUSBSystemIdlePowerOptimizingSettingVpUSBIdlePowerOptimizing_Type = CfprApBiosVfUSBSysIdlePowerOptimizingSettingVpUSBIdlePowerOptimize
_CfprApBiosVfUSBSystemIdlePowerOptimizingSettingVpUSBIdlePowerOptimizing_Object = MibTableColumn
cfprApBiosVfUSBSystemIdlePowerOptimizingSettingVpUSBIdlePowerOptimizing = _CfprApBiosVfUSBSystemIdlePowerOptimizingSettingVpUSBIdlePowerOptimizing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 77, 1, 4),
    _CfprApBiosVfUSBSystemIdlePowerOptimizingSettingVpUSBIdlePowerOptimizing_Type()
)
cfprApBiosVfUSBSystemIdlePowerOptimizingSettingVpUSBIdlePowerOptimizing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfUSBSystemIdlePowerOptimizingSettingVpUSBIdlePowerOptimizing.setStatus("current")
_CfprApBiosVfVGAPriorityTable_Object = MibTable
cfprApBiosVfVGAPriorityTable = _CfprApBiosVfVGAPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 78)
)
if mibBuilder.loadTexts:
    cfprApBiosVfVGAPriorityTable.setStatus("current")
_CfprApBiosVfVGAPriorityEntry_Object = MibTableRow
cfprApBiosVfVGAPriorityEntry = _CfprApBiosVfVGAPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 78, 1)
)
cfprApBiosVfVGAPriorityEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-BIOS-MIB", "cfprApBiosVfVGAPriorityInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApBiosVfVGAPriorityEntry.setStatus("current")
_CfprApBiosVfVGAPriorityInstanceId_Type = CfprApManagedObjectId
_CfprApBiosVfVGAPriorityInstanceId_Object = MibTableColumn
cfprApBiosVfVGAPriorityInstanceId = _CfprApBiosVfVGAPriorityInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 78, 1, 1),
    _CfprApBiosVfVGAPriorityInstanceId_Type()
)
cfprApBiosVfVGAPriorityInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApBiosVfVGAPriorityInstanceId.setStatus("current")
_CfprApBiosVfVGAPriorityDn_Type = CfprApManagedObjectDn
_CfprApBiosVfVGAPriorityDn_Object = MibTableColumn
cfprApBiosVfVGAPriorityDn = _CfprApBiosVfVGAPriorityDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 78, 1, 2),
    _CfprApBiosVfVGAPriorityDn_Type()
)
cfprApBiosVfVGAPriorityDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfVGAPriorityDn.setStatus("current")
_CfprApBiosVfVGAPriorityRn_Type = SnmpAdminString
_CfprApBiosVfVGAPriorityRn_Object = MibTableColumn
cfprApBiosVfVGAPriorityRn = _CfprApBiosVfVGAPriorityRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 78, 1, 3),
    _CfprApBiosVfVGAPriorityRn_Type()
)
cfprApBiosVfVGAPriorityRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfVGAPriorityRn.setStatus("current")
_CfprApBiosVfVGAPriorityVpVGAPriority_Type = CfprApBiosVfVGAPriorityVpVGAPriority
_CfprApBiosVfVGAPriorityVpVGAPriority_Object = MibTableColumn
cfprApBiosVfVGAPriorityVpVGAPriority = _CfprApBiosVfVGAPriorityVpVGAPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 5, 78, 1, 4),
    _CfprApBiosVfVGAPriorityVpVGAPriority_Type()
)
cfprApBiosVfVGAPriorityVpVGAPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApBiosVfVGAPriorityVpVGAPriority.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-BIOS-MIB",
    **{"cfprApBiosObjects": cfprApBiosObjects,
       "cfprApBiosBOTTable": cfprApBiosBOTTable,
       "cfprApBiosBOTEntry": cfprApBiosBOTEntry,
       "cfprApBiosBOTInstanceId": cfprApBiosBOTInstanceId,
       "cfprApBiosBOTDn": cfprApBiosBOTDn,
       "cfprApBiosBOTRn": cfprApBiosBOTRn,
       "cfprApBiosBOTLastUpdate": cfprApBiosBOTLastUpdate,
       "cfprApBiosBootDevTable": cfprApBiosBootDevTable,
       "cfprApBiosBootDevEntry": cfprApBiosBootDevEntry,
       "cfprApBiosBootDevInstanceId": cfprApBiosBootDevInstanceId,
       "cfprApBiosBootDevDn": cfprApBiosBootDevDn,
       "cfprApBiosBootDevRn": cfprApBiosBootDevRn,
       "cfprApBiosBootDevDescr": cfprApBiosBootDevDescr,
       "cfprApBiosBootDevDeviceName": cfprApBiosBootDevDeviceName,
       "cfprApBiosBootDevErrValue": cfprApBiosBootDevErrValue,
       "cfprApBiosBootDevOrder": cfprApBiosBootDevOrder,
       "cfprApBiosBootDevGrpTable": cfprApBiosBootDevGrpTable,
       "cfprApBiosBootDevGrpEntry": cfprApBiosBootDevGrpEntry,
       "cfprApBiosBootDevGrpInstanceId": cfprApBiosBootDevGrpInstanceId,
       "cfprApBiosBootDevGrpDn": cfprApBiosBootDevGrpDn,
       "cfprApBiosBootDevGrpRn": cfprApBiosBootDevGrpRn,
       "cfprApBiosBootDevGrpDescr": cfprApBiosBootDevGrpDescr,
       "cfprApBiosBootDevGrpDeviceName": cfprApBiosBootDevGrpDeviceName,
       "cfprApBiosBootDevGrpErrVal": cfprApBiosBootDevGrpErrVal,
       "cfprApBiosBootDevGrpOrder": cfprApBiosBootDevGrpOrder,
       "cfprApBiosBootDevGrpType": cfprApBiosBootDevGrpType,
       "cfprApBiosFeatureRefTable": cfprApBiosFeatureRefTable,
       "cfprApBiosFeatureRefEntry": cfprApBiosFeatureRefEntry,
       "cfprApBiosFeatureRefInstanceId": cfprApBiosFeatureRefInstanceId,
       "cfprApBiosFeatureRefDn": cfprApBiosFeatureRefDn,
       "cfprApBiosFeatureRefRn": cfprApBiosFeatureRefRn,
       "cfprApBiosFeatureRefFtrMoClassName": cfprApBiosFeatureRefFtrMoClassName,
       "cfprApBiosFeatureRefIsSupported": cfprApBiosFeatureRefIsSupported,
       "cfprApBiosFeatureRefName": cfprApBiosFeatureRefName,
       "cfprApBiosParameterRefTable": cfprApBiosParameterRefTable,
       "cfprApBiosParameterRefEntry": cfprApBiosParameterRefEntry,
       "cfprApBiosParameterRefInstanceId": cfprApBiosParameterRefInstanceId,
       "cfprApBiosParameterRefDn": cfprApBiosParameterRefDn,
       "cfprApBiosParameterRefRn": cfprApBiosParameterRefRn,
       "cfprApBiosParameterRefIsSupported": cfprApBiosParameterRefIsSupported,
       "cfprApBiosParameterRefName": cfprApBiosParameterRefName,
       "cfprApBiosParameterRefPropertyName": cfprApBiosParameterRefPropertyName,
       "cfprApBiosRefTable": cfprApBiosRefTable,
       "cfprApBiosRefEntry": cfprApBiosRefEntry,
       "cfprApBiosRefInstanceId": cfprApBiosRefInstanceId,
       "cfprApBiosRefDn": cfprApBiosRefDn,
       "cfprApBiosRefRn": cfprApBiosRefRn,
       "cfprApBiosRefIsSupported": cfprApBiosRefIsSupported,
       "cfprApBiosSettingRefTable": cfprApBiosSettingRefTable,
       "cfprApBiosSettingRefEntry": cfprApBiosSettingRefEntry,
       "cfprApBiosSettingRefInstanceId": cfprApBiosSettingRefInstanceId,
       "cfprApBiosSettingRefDn": cfprApBiosSettingRefDn,
       "cfprApBiosSettingRefRn": cfprApBiosSettingRefRn,
       "cfprApBiosSettingRefConstantName": cfprApBiosSettingRefConstantName,
       "cfprApBiosSettingRefIsDefault": cfprApBiosSettingRefIsDefault,
       "cfprApBiosSettingRefIsSupported": cfprApBiosSettingRefIsSupported,
       "cfprApBiosSettingRefName": cfprApBiosSettingRefName,
       "cfprApBiosSettingsTable": cfprApBiosSettingsTable,
       "cfprApBiosSettingsEntry": cfprApBiosSettingsEntry,
       "cfprApBiosSettingsInstanceId": cfprApBiosSettingsInstanceId,
       "cfprApBiosSettingsDn": cfprApBiosSettingsDn,
       "cfprApBiosSettingsRn": cfprApBiosSettingsRn,
       "cfprApBiosUnitTable": cfprApBiosUnitTable,
       "cfprApBiosUnitEntry": cfprApBiosUnitEntry,
       "cfprApBiosUnitInstanceId": cfprApBiosUnitInstanceId,
       "cfprApBiosUnitDn": cfprApBiosUnitDn,
       "cfprApBiosUnitRn": cfprApBiosUnitRn,
       "cfprApBiosUnitInitSeq": cfprApBiosUnitInitSeq,
       "cfprApBiosUnitInitTs": cfprApBiosUnitInitTs,
       "cfprApBiosUnitModel": cfprApBiosUnitModel,
       "cfprApBiosUnitRevision": cfprApBiosUnitRevision,
       "cfprApBiosUnitSerial": cfprApBiosUnitSerial,
       "cfprApBiosUnitVendor": cfprApBiosUnitVendor,
       "cfprApBiosVIdentityParamsTable": cfprApBiosVIdentityParamsTable,
       "cfprApBiosVIdentityParamsEntry": cfprApBiosVIdentityParamsEntry,
       "cfprApBiosVIdentityParamsInstanceId": cfprApBiosVIdentityParamsInstanceId,
       "cfprApBiosVIdentityParamsDn": cfprApBiosVIdentityParamsDn,
       "cfprApBiosVIdentityParamsRn": cfprApBiosVIdentityParamsRn,
       "cfprApBiosVIdentityParamsLsServerName": cfprApBiosVIdentityParamsLsServerName,
       "cfprApBiosVIdentityParamsLsServerTmplName": cfprApBiosVIdentityParamsLsServerTmplName,
       "cfprApBiosVIdentityParamsSysName": cfprApBiosVIdentityParamsSysName,
       "cfprApBiosVProfileTable": cfprApBiosVProfileTable,
       "cfprApBiosVProfileEntry": cfprApBiosVProfileEntry,
       "cfprApBiosVProfileInstanceId": cfprApBiosVProfileInstanceId,
       "cfprApBiosVProfileDn": cfprApBiosVProfileDn,
       "cfprApBiosVProfileRn": cfprApBiosVProfileRn,
       "cfprApBiosVProfileDescr": cfprApBiosVProfileDescr,
       "cfprApBiosVProfileIntId": cfprApBiosVProfileIntId,
       "cfprApBiosVProfileName": cfprApBiosVProfileName,
       "cfprApBiosVProfilePolicyLevel": cfprApBiosVProfilePolicyLevel,
       "cfprApBiosVProfilePolicyOwner": cfprApBiosVProfilePolicyOwner,
       "cfprApBiosVProfileRebootOnUpdate": cfprApBiosVProfileRebootOnUpdate,
       "cfprApBiosVfACPI10SupportTable": cfprApBiosVfACPI10SupportTable,
       "cfprApBiosVfACPI10SupportEntry": cfprApBiosVfACPI10SupportEntry,
       "cfprApBiosVfACPI10SupportInstanceId": cfprApBiosVfACPI10SupportInstanceId,
       "cfprApBiosVfACPI10SupportDn": cfprApBiosVfACPI10SupportDn,
       "cfprApBiosVfACPI10SupportRn": cfprApBiosVfACPI10SupportRn,
       "cfprApBiosVfACPI10SupportVpACPI10Support": cfprApBiosVfACPI10SupportVpACPI10Support,
       "cfprApBiosVfAllUSBDevicesTable": cfprApBiosVfAllUSBDevicesTable,
       "cfprApBiosVfAllUSBDevicesEntry": cfprApBiosVfAllUSBDevicesEntry,
       "cfprApBiosVfAllUSBDevicesInstanceId": cfprApBiosVfAllUSBDevicesInstanceId,
       "cfprApBiosVfAllUSBDevicesDn": cfprApBiosVfAllUSBDevicesDn,
       "cfprApBiosVfAllUSBDevicesRn": cfprApBiosVfAllUSBDevicesRn,
       "cfprApBiosVfAllUSBDevicesVpAllUSBDevices": cfprApBiosVfAllUSBDevicesVpAllUSBDevices,
       "cfprApBiosVfAltitudeTable": cfprApBiosVfAltitudeTable,
       "cfprApBiosVfAltitudeEntry": cfprApBiosVfAltitudeEntry,
       "cfprApBiosVfAltitudeInstanceId": cfprApBiosVfAltitudeInstanceId,
       "cfprApBiosVfAltitudeDn": cfprApBiosVfAltitudeDn,
       "cfprApBiosVfAltitudeRn": cfprApBiosVfAltitudeRn,
       "cfprApBiosVfAltitudeVpAltitude": cfprApBiosVfAltitudeVpAltitude,
       "cfprApBiosVfAssertNMIOnPERRTable": cfprApBiosVfAssertNMIOnPERRTable,
       "cfprApBiosVfAssertNMIOnPERREntry": cfprApBiosVfAssertNMIOnPERREntry,
       "cfprApBiosVfAssertNMIOnPERRInstanceId": cfprApBiosVfAssertNMIOnPERRInstanceId,
       "cfprApBiosVfAssertNMIOnPERRDn": cfprApBiosVfAssertNMIOnPERRDn,
       "cfprApBiosVfAssertNMIOnPERRRn": cfprApBiosVfAssertNMIOnPERRRn,
       "cfprApBiosVfAssertNMIOnPERRVpAssertNMIOnPERR": cfprApBiosVfAssertNMIOnPERRVpAssertNMIOnPERR,
       "cfprApBiosVfAssertNMIOnSERRTable": cfprApBiosVfAssertNMIOnSERRTable,
       "cfprApBiosVfAssertNMIOnSERREntry": cfprApBiosVfAssertNMIOnSERREntry,
       "cfprApBiosVfAssertNMIOnSERRInstanceId": cfprApBiosVfAssertNMIOnSERRInstanceId,
       "cfprApBiosVfAssertNMIOnSERRDn": cfprApBiosVfAssertNMIOnSERRDn,
       "cfprApBiosVfAssertNMIOnSERRRn": cfprApBiosVfAssertNMIOnSERRRn,
       "cfprApBiosVfAssertNMIOnSERRVpAssertNMIOnSERR": cfprApBiosVfAssertNMIOnSERRVpAssertNMIOnSERR,
       "cfprApBiosVfBootOptionRetryTable": cfprApBiosVfBootOptionRetryTable,
       "cfprApBiosVfBootOptionRetryEntry": cfprApBiosVfBootOptionRetryEntry,
       "cfprApBiosVfBootOptionRetryInstanceId": cfprApBiosVfBootOptionRetryInstanceId,
       "cfprApBiosVfBootOptionRetryDn": cfprApBiosVfBootOptionRetryDn,
       "cfprApBiosVfBootOptionRetryRn": cfprApBiosVfBootOptionRetryRn,
       "cfprApBiosVfBootOptionRetryVpBootOptionRetry": cfprApBiosVfBootOptionRetryVpBootOptionRetry,
       "cfprApBiosVfCPUPerformanceTable": cfprApBiosVfCPUPerformanceTable,
       "cfprApBiosVfCPUPerformanceEntry": cfprApBiosVfCPUPerformanceEntry,
       "cfprApBiosVfCPUPerformanceInstanceId": cfprApBiosVfCPUPerformanceInstanceId,
       "cfprApBiosVfCPUPerformanceDn": cfprApBiosVfCPUPerformanceDn,
       "cfprApBiosVfCPUPerformanceRn": cfprApBiosVfCPUPerformanceRn,
       "cfprApBiosVfCPUPerformanceVpCPUPerformance": cfprApBiosVfCPUPerformanceVpCPUPerformance,
       "cfprApBiosVfConsoleRedirectionTable": cfprApBiosVfConsoleRedirectionTable,
       "cfprApBiosVfConsoleRedirectionEntry": cfprApBiosVfConsoleRedirectionEntry,
       "cfprApBiosVfConsoleRedirectionInstanceId": cfprApBiosVfConsoleRedirectionInstanceId,
       "cfprApBiosVfConsoleRedirectionDn": cfprApBiosVfConsoleRedirectionDn,
       "cfprApBiosVfConsoleRedirectionRn": cfprApBiosVfConsoleRedirectionRn,
       "cfprApBiosVfConsoleRedirectionVpBaudRate": cfprApBiosVfConsoleRedirectionVpBaudRate,
       "cfprApBiosVfConsoleRedirectionVpConsoleRedirection": cfprApBiosVfConsoleRedirectionVpConsoleRedirection,
       "cfprApBiosVfConsoleRedirectionVpFlowControl": cfprApBiosVfConsoleRedirectionVpFlowControl,
       "cfprApBiosVfConsoleRedirectionVpLegacyOSRedirection": cfprApBiosVfConsoleRedirectionVpLegacyOSRedirection,
       "cfprApBiosVfConsoleRedirectionVpPuttyKeyPad": cfprApBiosVfConsoleRedirectionVpPuttyKeyPad,
       "cfprApBiosVfConsoleRedirectionVpTerminalType": cfprApBiosVfConsoleRedirectionVpTerminalType,
       "cfprApBiosVfCoreMultiProcessingTable": cfprApBiosVfCoreMultiProcessingTable,
       "cfprApBiosVfCoreMultiProcessingEntry": cfprApBiosVfCoreMultiProcessingEntry,
       "cfprApBiosVfCoreMultiProcessingInstanceId": cfprApBiosVfCoreMultiProcessingInstanceId,
       "cfprApBiosVfCoreMultiProcessingDn": cfprApBiosVfCoreMultiProcessingDn,
       "cfprApBiosVfCoreMultiProcessingRn": cfprApBiosVfCoreMultiProcessingRn,
       "cfprApBiosVfCoreMultiProcessingVpCoreMultiProcessing": cfprApBiosVfCoreMultiProcessingVpCoreMultiProcessing,
       "cfprApBiosVfDRAMClockThrottlingTable": cfprApBiosVfDRAMClockThrottlingTable,
       "cfprApBiosVfDRAMClockThrottlingEntry": cfprApBiosVfDRAMClockThrottlingEntry,
       "cfprApBiosVfDRAMClockThrottlingInstanceId": cfprApBiosVfDRAMClockThrottlingInstanceId,
       "cfprApBiosVfDRAMClockThrottlingDn": cfprApBiosVfDRAMClockThrottlingDn,
       "cfprApBiosVfDRAMClockThrottlingRn": cfprApBiosVfDRAMClockThrottlingRn,
       "cfprApBiosVfDRAMClockThrottlingVpDRAMClockThrottling": cfprApBiosVfDRAMClockThrottlingVpDRAMClockThrottling,
       "cfprApBiosVfDirectCacheAccessTable": cfprApBiosVfDirectCacheAccessTable,
       "cfprApBiosVfDirectCacheAccessEntry": cfprApBiosVfDirectCacheAccessEntry,
       "cfprApBiosVfDirectCacheAccessInstanceId": cfprApBiosVfDirectCacheAccessInstanceId,
       "cfprApBiosVfDirectCacheAccessDn": cfprApBiosVfDirectCacheAccessDn,
       "cfprApBiosVfDirectCacheAccessRn": cfprApBiosVfDirectCacheAccessRn,
       "cfprApBiosVfDirectCacheAccessVpDirectCacheAccess": cfprApBiosVfDirectCacheAccessVpDirectCacheAccess,
       "cfprApBiosVfDramRefreshRateTable": cfprApBiosVfDramRefreshRateTable,
       "cfprApBiosVfDramRefreshRateEntry": cfprApBiosVfDramRefreshRateEntry,
       "cfprApBiosVfDramRefreshRateInstanceId": cfprApBiosVfDramRefreshRateInstanceId,
       "cfprApBiosVfDramRefreshRateDn": cfprApBiosVfDramRefreshRateDn,
       "cfprApBiosVfDramRefreshRateRn": cfprApBiosVfDramRefreshRateRn,
       "cfprApBiosVfDramRefreshRateVpDramRefreshRate": cfprApBiosVfDramRefreshRateVpDramRefreshRate,
       "cfprApBiosVfEnhancedIntelSpeedStepTechTable": cfprApBiosVfEnhancedIntelSpeedStepTechTable,
       "cfprApBiosVfEnhancedIntelSpeedStepTechEntry": cfprApBiosVfEnhancedIntelSpeedStepTechEntry,
       "cfprApBiosVfEnhancedIntelSpeedStepTechInstanceId": cfprApBiosVfEnhancedIntelSpeedStepTechInstanceId,
       "cfprApBiosVfEnhancedIntelSpeedStepTechDn": cfprApBiosVfEnhancedIntelSpeedStepTechDn,
       "cfprApBiosVfEnhancedIntelSpeedStepTechRn": cfprApBiosVfEnhancedIntelSpeedStepTechRn,
       "cfprApBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech": cfprApBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech,
       "cfprApBiosVfExecuteDisableBitTable": cfprApBiosVfExecuteDisableBitTable,
       "cfprApBiosVfExecuteDisableBitEntry": cfprApBiosVfExecuteDisableBitEntry,
       "cfprApBiosVfExecuteDisableBitInstanceId": cfprApBiosVfExecuteDisableBitInstanceId,
       "cfprApBiosVfExecuteDisableBitDn": cfprApBiosVfExecuteDisableBitDn,
       "cfprApBiosVfExecuteDisableBitRn": cfprApBiosVfExecuteDisableBitRn,
       "cfprApBiosVfExecuteDisableBitVpExecuteDisableBit": cfprApBiosVfExecuteDisableBitVpExecuteDisableBit,
       "cfprApBiosVfFRB2TimerTable": cfprApBiosVfFRB2TimerTable,
       "cfprApBiosVfFRB2TimerEntry": cfprApBiosVfFRB2TimerEntry,
       "cfprApBiosVfFRB2TimerInstanceId": cfprApBiosVfFRB2TimerInstanceId,
       "cfprApBiosVfFRB2TimerDn": cfprApBiosVfFRB2TimerDn,
       "cfprApBiosVfFRB2TimerRn": cfprApBiosVfFRB2TimerRn,
       "cfprApBiosVfFRB2TimerVpFRB2Timer": cfprApBiosVfFRB2TimerVpFRB2Timer,
       "cfprApBiosVfFrequencyFloorOverrideTable": cfprApBiosVfFrequencyFloorOverrideTable,
       "cfprApBiosVfFrequencyFloorOverrideEntry": cfprApBiosVfFrequencyFloorOverrideEntry,
       "cfprApBiosVfFrequencyFloorOverrideInstanceId": cfprApBiosVfFrequencyFloorOverrideInstanceId,
       "cfprApBiosVfFrequencyFloorOverrideDn": cfprApBiosVfFrequencyFloorOverrideDn,
       "cfprApBiosVfFrequencyFloorOverrideRn": cfprApBiosVfFrequencyFloorOverrideRn,
       "cfprApBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride": cfprApBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride,
       "cfprApBiosVfFrontPanelLockoutTable": cfprApBiosVfFrontPanelLockoutTable,
       "cfprApBiosVfFrontPanelLockoutEntry": cfprApBiosVfFrontPanelLockoutEntry,
       "cfprApBiosVfFrontPanelLockoutInstanceId": cfprApBiosVfFrontPanelLockoutInstanceId,
       "cfprApBiosVfFrontPanelLockoutDn": cfprApBiosVfFrontPanelLockoutDn,
       "cfprApBiosVfFrontPanelLockoutRn": cfprApBiosVfFrontPanelLockoutRn,
       "cfprApBiosVfFrontPanelLockoutVpFrontPanelLockout": cfprApBiosVfFrontPanelLockoutVpFrontPanelLockout,
       "cfprApBiosVfIntelEntrySASRAIDModuleTable": cfprApBiosVfIntelEntrySASRAIDModuleTable,
       "cfprApBiosVfIntelEntrySASRAIDModuleEntry": cfprApBiosVfIntelEntrySASRAIDModuleEntry,
       "cfprApBiosVfIntelEntrySASRAIDModuleInstanceId": cfprApBiosVfIntelEntrySASRAIDModuleInstanceId,
       "cfprApBiosVfIntelEntrySASRAIDModuleDn": cfprApBiosVfIntelEntrySASRAIDModuleDn,
       "cfprApBiosVfIntelEntrySASRAIDModuleRn": cfprApBiosVfIntelEntrySASRAIDModuleRn,
       "cfprApBiosVfIntelEntrySASRAIDModuleVpSASRAID": cfprApBiosVfIntelEntrySASRAIDModuleVpSASRAID,
       "cfprApBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule": cfprApBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule,
       "cfprApBiosVfIntelHyperThreadingTechTable": cfprApBiosVfIntelHyperThreadingTechTable,
       "cfprApBiosVfIntelHyperThreadingTechEntry": cfprApBiosVfIntelHyperThreadingTechEntry,
       "cfprApBiosVfIntelHyperThreadingTechInstanceId": cfprApBiosVfIntelHyperThreadingTechInstanceId,
       "cfprApBiosVfIntelHyperThreadingTechDn": cfprApBiosVfIntelHyperThreadingTechDn,
       "cfprApBiosVfIntelHyperThreadingTechRn": cfprApBiosVfIntelHyperThreadingTechRn,
       "cfprApBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech": cfprApBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech,
       "cfprApBiosVfIntelTurboBoostTechTable": cfprApBiosVfIntelTurboBoostTechTable,
       "cfprApBiosVfIntelTurboBoostTechEntry": cfprApBiosVfIntelTurboBoostTechEntry,
       "cfprApBiosVfIntelTurboBoostTechInstanceId": cfprApBiosVfIntelTurboBoostTechInstanceId,
       "cfprApBiosVfIntelTurboBoostTechDn": cfprApBiosVfIntelTurboBoostTechDn,
       "cfprApBiosVfIntelTurboBoostTechRn": cfprApBiosVfIntelTurboBoostTechRn,
       "cfprApBiosVfIntelTurboBoostTechVpIntelTurboBoostTech": cfprApBiosVfIntelTurboBoostTechVpIntelTurboBoostTech,
       "cfprApBiosVfIntelVTForDirectedIOTable": cfprApBiosVfIntelVTForDirectedIOTable,
       "cfprApBiosVfIntelVTForDirectedIOEntry": cfprApBiosVfIntelVTForDirectedIOEntry,
       "cfprApBiosVfIntelVTForDirectedIOInstanceId": cfprApBiosVfIntelVTForDirectedIOInstanceId,
       "cfprApBiosVfIntelVTForDirectedIODn": cfprApBiosVfIntelVTForDirectedIODn,
       "cfprApBiosVfIntelVTForDirectedIORn": cfprApBiosVfIntelVTForDirectedIORn,
       "cfprApBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport": cfprApBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport,
       "cfprApBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport": cfprApBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport,
       "cfprApBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping": cfprApBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping,
       "cfprApBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport": cfprApBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport,
       "cfprApBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO": cfprApBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO,
       "cfprApBiosVfIntelVirtualizationTechnologyTable": cfprApBiosVfIntelVirtualizationTechnologyTable,
       "cfprApBiosVfIntelVirtualizationTechnologyEntry": cfprApBiosVfIntelVirtualizationTechnologyEntry,
       "cfprApBiosVfIntelVirtualizationTechnologyInstanceId": cfprApBiosVfIntelVirtualizationTechnologyInstanceId,
       "cfprApBiosVfIntelVirtualizationTechnologyDn": cfprApBiosVfIntelVirtualizationTechnologyDn,
       "cfprApBiosVfIntelVirtualizationTechnologyRn": cfprApBiosVfIntelVirtualizationTechnologyRn,
       "cfprApBiosVfIntelVirtualizationTechnologyVpIntelVirtualizationTechnology": cfprApBiosVfIntelVirtualizationTechnologyVpIntelVirtualizationTechnology,
       "cfprApBiosVfInterleaveConfigurationTable": cfprApBiosVfInterleaveConfigurationTable,
       "cfprApBiosVfInterleaveConfigurationEntry": cfprApBiosVfInterleaveConfigurationEntry,
       "cfprApBiosVfInterleaveConfigurationInstanceId": cfprApBiosVfInterleaveConfigurationInstanceId,
       "cfprApBiosVfInterleaveConfigurationDn": cfprApBiosVfInterleaveConfigurationDn,
       "cfprApBiosVfInterleaveConfigurationRn": cfprApBiosVfInterleaveConfigurationRn,
       "cfprApBiosVfInterleaveConfigurationVpChannelInterleaving": cfprApBiosVfInterleaveConfigurationVpChannelInterleaving,
       "cfprApBiosVfInterleaveConfigurationVpMemoryInterleaving": cfprApBiosVfInterleaveConfigurationVpMemoryInterleaving,
       "cfprApBiosVfInterleaveConfigurationVpRankInterleaving": cfprApBiosVfInterleaveConfigurationVpRankInterleaving,
       "cfprApBiosVfLocalX2ApicTable": cfprApBiosVfLocalX2ApicTable,
       "cfprApBiosVfLocalX2ApicEntry": cfprApBiosVfLocalX2ApicEntry,
       "cfprApBiosVfLocalX2ApicInstanceId": cfprApBiosVfLocalX2ApicInstanceId,
       "cfprApBiosVfLocalX2ApicDn": cfprApBiosVfLocalX2ApicDn,
       "cfprApBiosVfLocalX2ApicRn": cfprApBiosVfLocalX2ApicRn,
       "cfprApBiosVfLocalX2ApicVpLocalX2Apic": cfprApBiosVfLocalX2ApicVpLocalX2Apic,
       "cfprApBiosVfLvDIMMSupportTable": cfprApBiosVfLvDIMMSupportTable,
       "cfprApBiosVfLvDIMMSupportEntry": cfprApBiosVfLvDIMMSupportEntry,
       "cfprApBiosVfLvDIMMSupportInstanceId": cfprApBiosVfLvDIMMSupportInstanceId,
       "cfprApBiosVfLvDIMMSupportDn": cfprApBiosVfLvDIMMSupportDn,
       "cfprApBiosVfLvDIMMSupportRn": cfprApBiosVfLvDIMMSupportRn,
       "cfprApBiosVfLvDIMMSupportVpLvDDRMode": cfprApBiosVfLvDIMMSupportVpLvDDRMode,
       "cfprApBiosVfMaxVariableMTRRSettingTable": cfprApBiosVfMaxVariableMTRRSettingTable,
       "cfprApBiosVfMaxVariableMTRRSettingEntry": cfprApBiosVfMaxVariableMTRRSettingEntry,
       "cfprApBiosVfMaxVariableMTRRSettingInstanceId": cfprApBiosVfMaxVariableMTRRSettingInstanceId,
       "cfprApBiosVfMaxVariableMTRRSettingDn": cfprApBiosVfMaxVariableMTRRSettingDn,
       "cfprApBiosVfMaxVariableMTRRSettingRn": cfprApBiosVfMaxVariableMTRRSettingRn,
       "cfprApBiosVfMaxVariableMTRRSettingVpProcessorMtrr": cfprApBiosVfMaxVariableMTRRSettingVpProcessorMtrr,
       "cfprApBiosVfMaximumMemoryBelow4GBTable": cfprApBiosVfMaximumMemoryBelow4GBTable,
       "cfprApBiosVfMaximumMemoryBelow4GBEntry": cfprApBiosVfMaximumMemoryBelow4GBEntry,
       "cfprApBiosVfMaximumMemoryBelow4GBInstanceId": cfprApBiosVfMaximumMemoryBelow4GBInstanceId,
       "cfprApBiosVfMaximumMemoryBelow4GBDn": cfprApBiosVfMaximumMemoryBelow4GBDn,
       "cfprApBiosVfMaximumMemoryBelow4GBRn": cfprApBiosVfMaximumMemoryBelow4GBRn,
       "cfprApBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB": cfprApBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB,
       "cfprApBiosVfMemoryMappedIOAbove4GBTable": cfprApBiosVfMemoryMappedIOAbove4GBTable,
       "cfprApBiosVfMemoryMappedIOAbove4GBEntry": cfprApBiosVfMemoryMappedIOAbove4GBEntry,
       "cfprApBiosVfMemoryMappedIOAbove4GBInstanceId": cfprApBiosVfMemoryMappedIOAbove4GBInstanceId,
       "cfprApBiosVfMemoryMappedIOAbove4GBDn": cfprApBiosVfMemoryMappedIOAbove4GBDn,
       "cfprApBiosVfMemoryMappedIOAbove4GBRn": cfprApBiosVfMemoryMappedIOAbove4GBRn,
       "cfprApBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB": cfprApBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB,
       "cfprApBiosVfMirroringModeTable": cfprApBiosVfMirroringModeTable,
       "cfprApBiosVfMirroringModeEntry": cfprApBiosVfMirroringModeEntry,
       "cfprApBiosVfMirroringModeInstanceId": cfprApBiosVfMirroringModeInstanceId,
       "cfprApBiosVfMirroringModeDn": cfprApBiosVfMirroringModeDn,
       "cfprApBiosVfMirroringModeRn": cfprApBiosVfMirroringModeRn,
       "cfprApBiosVfMirroringModeVpMirroringMode": cfprApBiosVfMirroringModeVpMirroringMode,
       "cfprApBiosVfNUMAOptimizedTable": cfprApBiosVfNUMAOptimizedTable,
       "cfprApBiosVfNUMAOptimizedEntry": cfprApBiosVfNUMAOptimizedEntry,
       "cfprApBiosVfNUMAOptimizedInstanceId": cfprApBiosVfNUMAOptimizedInstanceId,
       "cfprApBiosVfNUMAOptimizedDn": cfprApBiosVfNUMAOptimizedDn,
       "cfprApBiosVfNUMAOptimizedRn": cfprApBiosVfNUMAOptimizedRn,
       "cfprApBiosVfNUMAOptimizedVpNUMAOptimized": cfprApBiosVfNUMAOptimizedVpNUMAOptimized,
       "cfprApBiosVfOSBootWatchdogTimerTable": cfprApBiosVfOSBootWatchdogTimerTable,
       "cfprApBiosVfOSBootWatchdogTimerEntry": cfprApBiosVfOSBootWatchdogTimerEntry,
       "cfprApBiosVfOSBootWatchdogTimerInstanceId": cfprApBiosVfOSBootWatchdogTimerInstanceId,
       "cfprApBiosVfOSBootWatchdogTimerDn": cfprApBiosVfOSBootWatchdogTimerDn,
       "cfprApBiosVfOSBootWatchdogTimerRn": cfprApBiosVfOSBootWatchdogTimerRn,
       "cfprApBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer": cfprApBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer,
       "cfprApBiosVfOSBootWatchdogTimerPolicyTable": cfprApBiosVfOSBootWatchdogTimerPolicyTable,
       "cfprApBiosVfOSBootWatchdogTimerPolicyEntry": cfprApBiosVfOSBootWatchdogTimerPolicyEntry,
       "cfprApBiosVfOSBootWatchdogTimerPolicyInstanceId": cfprApBiosVfOSBootWatchdogTimerPolicyInstanceId,
       "cfprApBiosVfOSBootWatchdogTimerPolicyDn": cfprApBiosVfOSBootWatchdogTimerPolicyDn,
       "cfprApBiosVfOSBootWatchdogTimerPolicyRn": cfprApBiosVfOSBootWatchdogTimerPolicyRn,
       "cfprApBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy": cfprApBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy,
       "cfprApBiosVfOSBootWatchdogTimerTimeoutTable": cfprApBiosVfOSBootWatchdogTimerTimeoutTable,
       "cfprApBiosVfOSBootWatchdogTimerTimeoutEntry": cfprApBiosVfOSBootWatchdogTimerTimeoutEntry,
       "cfprApBiosVfOSBootWatchdogTimerTimeoutInstanceId": cfprApBiosVfOSBootWatchdogTimerTimeoutInstanceId,
       "cfprApBiosVfOSBootWatchdogTimerTimeoutDn": cfprApBiosVfOSBootWatchdogTimerTimeoutDn,
       "cfprApBiosVfOSBootWatchdogTimerTimeoutRn": cfprApBiosVfOSBootWatchdogTimerTimeoutRn,
       "cfprApBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout": cfprApBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout,
       "cfprApBiosVfOnboardSATAControllerTable": cfprApBiosVfOnboardSATAControllerTable,
       "cfprApBiosVfOnboardSATAControllerEntry": cfprApBiosVfOnboardSATAControllerEntry,
       "cfprApBiosVfOnboardSATAControllerInstanceId": cfprApBiosVfOnboardSATAControllerInstanceId,
       "cfprApBiosVfOnboardSATAControllerDn": cfprApBiosVfOnboardSATAControllerDn,
       "cfprApBiosVfOnboardSATAControllerRn": cfprApBiosVfOnboardSATAControllerRn,
       "cfprApBiosVfOnboardSATAControllerVpOnboardSATAController": cfprApBiosVfOnboardSATAControllerVpOnboardSATAController,
       "cfprApBiosVfOnboardSATAControllerVpSATAMode": cfprApBiosVfOnboardSATAControllerVpSATAMode,
       "cfprApBiosVfOnboardStorageTable": cfprApBiosVfOnboardStorageTable,
       "cfprApBiosVfOnboardStorageEntry": cfprApBiosVfOnboardStorageEntry,
       "cfprApBiosVfOnboardStorageInstanceId": cfprApBiosVfOnboardStorageInstanceId,
       "cfprApBiosVfOnboardStorageDn": cfprApBiosVfOnboardStorageDn,
       "cfprApBiosVfOnboardStorageRn": cfprApBiosVfOnboardStorageRn,
       "cfprApBiosVfOnboardStorageVpOnboardSCUStorageSupport": cfprApBiosVfOnboardStorageVpOnboardSCUStorageSupport,
       "cfprApBiosVfOptionROMEnableTable": cfprApBiosVfOptionROMEnableTable,
       "cfprApBiosVfOptionROMEnableEntry": cfprApBiosVfOptionROMEnableEntry,
       "cfprApBiosVfOptionROMEnableInstanceId": cfprApBiosVfOptionROMEnableInstanceId,
       "cfprApBiosVfOptionROMEnableDn": cfprApBiosVfOptionROMEnableDn,
       "cfprApBiosVfOptionROMEnableRn": cfprApBiosVfOptionROMEnableRn,
       "cfprApBiosVfOptionROMEnableVpState": cfprApBiosVfOptionROMEnableVpState,
       "cfprApBiosVfOptionROMLoadTable": cfprApBiosVfOptionROMLoadTable,
       "cfprApBiosVfOptionROMLoadEntry": cfprApBiosVfOptionROMLoadEntry,
       "cfprApBiosVfOptionROMLoadInstanceId": cfprApBiosVfOptionROMLoadInstanceId,
       "cfprApBiosVfOptionROMLoadDn": cfprApBiosVfOptionROMLoadDn,
       "cfprApBiosVfOptionROMLoadRn": cfprApBiosVfOptionROMLoadRn,
       "cfprApBiosVfOptionROMLoadVpLoad": cfprApBiosVfOptionROMLoadVpLoad,
       "cfprApBiosVfPCISlotLinkSpeedTable": cfprApBiosVfPCISlotLinkSpeedTable,
       "cfprApBiosVfPCISlotLinkSpeedEntry": cfprApBiosVfPCISlotLinkSpeedEntry,
       "cfprApBiosVfPCISlotLinkSpeedInstanceId": cfprApBiosVfPCISlotLinkSpeedInstanceId,
       "cfprApBiosVfPCISlotLinkSpeedDn": cfprApBiosVfPCISlotLinkSpeedDn,
       "cfprApBiosVfPCISlotLinkSpeedRn": cfprApBiosVfPCISlotLinkSpeedRn,
       "cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed": cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed,
       "cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed": cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed,
       "cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed": cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed,
       "cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed": cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed,
       "cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed": cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed,
       "cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed": cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed,
       "cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed": cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed,
       "cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed": cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed,
       "cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed": cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed,
       "cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed": cfprApBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed,
       "cfprApBiosVfPCISlotOptionROMEnableTable": cfprApBiosVfPCISlotOptionROMEnableTable,
       "cfprApBiosVfPCISlotOptionROMEnableEntry": cfprApBiosVfPCISlotOptionROMEnableEntry,
       "cfprApBiosVfPCISlotOptionROMEnableInstanceId": cfprApBiosVfPCISlotOptionROMEnableInstanceId,
       "cfprApBiosVfPCISlotOptionROMEnableDn": cfprApBiosVfPCISlotOptionROMEnableDn,
       "cfprApBiosVfPCISlotOptionROMEnableRn": cfprApBiosVfPCISlotOptionROMEnableRn,
       "cfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM": cfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM,
       "cfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM": cfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM,
       "cfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM": cfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM,
       "cfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM": cfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM,
       "cfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM": cfprApBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM,
       "cfprApBiosVfPCISlotOptionROMEnableVpSlot10State": cfprApBiosVfPCISlotOptionROMEnableVpSlot10State,
       "cfprApBiosVfPCISlotOptionROMEnableVpSlot1State": cfprApBiosVfPCISlotOptionROMEnableVpSlot1State,
       "cfprApBiosVfPCISlotOptionROMEnableVpSlot2State": cfprApBiosVfPCISlotOptionROMEnableVpSlot2State,
       "cfprApBiosVfPCISlotOptionROMEnableVpSlot3State": cfprApBiosVfPCISlotOptionROMEnableVpSlot3State,
       "cfprApBiosVfPCISlotOptionROMEnableVpSlot4State": cfprApBiosVfPCISlotOptionROMEnableVpSlot4State,
       "cfprApBiosVfPCISlotOptionROMEnableVpSlot5State": cfprApBiosVfPCISlotOptionROMEnableVpSlot5State,
       "cfprApBiosVfPCISlotOptionROMEnableVpSlot6State": cfprApBiosVfPCISlotOptionROMEnableVpSlot6State,
       "cfprApBiosVfPCISlotOptionROMEnableVpSlot7State": cfprApBiosVfPCISlotOptionROMEnableVpSlot7State,
       "cfprApBiosVfPCISlotOptionROMEnableVpSlot8State": cfprApBiosVfPCISlotOptionROMEnableVpSlot8State,
       "cfprApBiosVfPCISlotOptionROMEnableVpSlot9State": cfprApBiosVfPCISlotOptionROMEnableVpSlot9State,
       "cfprApBiosVfPCISlotOptionROMEnableVpSlotMezzState": cfprApBiosVfPCISlotOptionROMEnableVpSlotMezzState,
       "cfprApBiosVfPOSTErrorPauseTable": cfprApBiosVfPOSTErrorPauseTable,
       "cfprApBiosVfPOSTErrorPauseEntry": cfprApBiosVfPOSTErrorPauseEntry,
       "cfprApBiosVfPOSTErrorPauseInstanceId": cfprApBiosVfPOSTErrorPauseInstanceId,
       "cfprApBiosVfPOSTErrorPauseDn": cfprApBiosVfPOSTErrorPauseDn,
       "cfprApBiosVfPOSTErrorPauseRn": cfprApBiosVfPOSTErrorPauseRn,
       "cfprApBiosVfPOSTErrorPauseVpPOSTErrorPause": cfprApBiosVfPOSTErrorPauseVpPOSTErrorPause,
       "cfprApBiosVfPSTATECoordinationTable": cfprApBiosVfPSTATECoordinationTable,
       "cfprApBiosVfPSTATECoordinationEntry": cfprApBiosVfPSTATECoordinationEntry,
       "cfprApBiosVfPSTATECoordinationInstanceId": cfprApBiosVfPSTATECoordinationInstanceId,
       "cfprApBiosVfPSTATECoordinationDn": cfprApBiosVfPSTATECoordinationDn,
       "cfprApBiosVfPSTATECoordinationRn": cfprApBiosVfPSTATECoordinationRn,
       "cfprApBiosVfPSTATECoordinationVpPSTATECoordination": cfprApBiosVfPSTATECoordinationVpPSTATECoordination,
       "cfprApBiosVfPackageCStateLimitTable": cfprApBiosVfPackageCStateLimitTable,
       "cfprApBiosVfPackageCStateLimitEntry": cfprApBiosVfPackageCStateLimitEntry,
       "cfprApBiosVfPackageCStateLimitInstanceId": cfprApBiosVfPackageCStateLimitInstanceId,
       "cfprApBiosVfPackageCStateLimitDn": cfprApBiosVfPackageCStateLimitDn,
       "cfprApBiosVfPackageCStateLimitRn": cfprApBiosVfPackageCStateLimitRn,
       "cfprApBiosVfPackageCStateLimitVpPackageCStateLimit": cfprApBiosVfPackageCStateLimitVpPackageCStateLimit,
       "cfprApBiosVfProcessorC1ETable": cfprApBiosVfProcessorC1ETable,
       "cfprApBiosVfProcessorC1EEntry": cfprApBiosVfProcessorC1EEntry,
       "cfprApBiosVfProcessorC1EInstanceId": cfprApBiosVfProcessorC1EInstanceId,
       "cfprApBiosVfProcessorC1EDn": cfprApBiosVfProcessorC1EDn,
       "cfprApBiosVfProcessorC1ERn": cfprApBiosVfProcessorC1ERn,
       "cfprApBiosVfProcessorC1EVpProcessorC1E": cfprApBiosVfProcessorC1EVpProcessorC1E,
       "cfprApBiosVfProcessorC3ReportTable": cfprApBiosVfProcessorC3ReportTable,
       "cfprApBiosVfProcessorC3ReportEntry": cfprApBiosVfProcessorC3ReportEntry,
       "cfprApBiosVfProcessorC3ReportInstanceId": cfprApBiosVfProcessorC3ReportInstanceId,
       "cfprApBiosVfProcessorC3ReportDn": cfprApBiosVfProcessorC3ReportDn,
       "cfprApBiosVfProcessorC3ReportRn": cfprApBiosVfProcessorC3ReportRn,
       "cfprApBiosVfProcessorC3ReportVpProcessorC3Report": cfprApBiosVfProcessorC3ReportVpProcessorC3Report,
       "cfprApBiosVfProcessorC6ReportTable": cfprApBiosVfProcessorC6ReportTable,
       "cfprApBiosVfProcessorC6ReportEntry": cfprApBiosVfProcessorC6ReportEntry,
       "cfprApBiosVfProcessorC6ReportInstanceId": cfprApBiosVfProcessorC6ReportInstanceId,
       "cfprApBiosVfProcessorC6ReportDn": cfprApBiosVfProcessorC6ReportDn,
       "cfprApBiosVfProcessorC6ReportRn": cfprApBiosVfProcessorC6ReportRn,
       "cfprApBiosVfProcessorC6ReportVpProcessorC6Report": cfprApBiosVfProcessorC6ReportVpProcessorC6Report,
       "cfprApBiosVfProcessorC7ReportTable": cfprApBiosVfProcessorC7ReportTable,
       "cfprApBiosVfProcessorC7ReportEntry": cfprApBiosVfProcessorC7ReportEntry,
       "cfprApBiosVfProcessorC7ReportInstanceId": cfprApBiosVfProcessorC7ReportInstanceId,
       "cfprApBiosVfProcessorC7ReportDn": cfprApBiosVfProcessorC7ReportDn,
       "cfprApBiosVfProcessorC7ReportRn": cfprApBiosVfProcessorC7ReportRn,
       "cfprApBiosVfProcessorC7ReportVpProcessorC7Report": cfprApBiosVfProcessorC7ReportVpProcessorC7Report,
       "cfprApBiosVfProcessorCStateTable": cfprApBiosVfProcessorCStateTable,
       "cfprApBiosVfProcessorCStateEntry": cfprApBiosVfProcessorCStateEntry,
       "cfprApBiosVfProcessorCStateInstanceId": cfprApBiosVfProcessorCStateInstanceId,
       "cfprApBiosVfProcessorCStateDn": cfprApBiosVfProcessorCStateDn,
       "cfprApBiosVfProcessorCStateRn": cfprApBiosVfProcessorCStateRn,
       "cfprApBiosVfProcessorCStateVpProcessorCState": cfprApBiosVfProcessorCStateVpProcessorCState,
       "cfprApBiosVfProcessorEnergyConfigurationTable": cfprApBiosVfProcessorEnergyConfigurationTable,
       "cfprApBiosVfProcessorEnergyConfigurationEntry": cfprApBiosVfProcessorEnergyConfigurationEntry,
       "cfprApBiosVfProcessorEnergyConfigurationInstanceId": cfprApBiosVfProcessorEnergyConfigurationInstanceId,
       "cfprApBiosVfProcessorEnergyConfigurationDn": cfprApBiosVfProcessorEnergyConfigurationDn,
       "cfprApBiosVfProcessorEnergyConfigurationRn": cfprApBiosVfProcessorEnergyConfigurationRn,
       "cfprApBiosVfProcessorEnergyConfigurationVpEnergyPerformance": cfprApBiosVfProcessorEnergyConfigurationVpEnergyPerformance,
       "cfprApBiosVfProcessorEnergyConfigurationVpPowerTechnology": cfprApBiosVfProcessorEnergyConfigurationVpPowerTechnology,
       "cfprApBiosVfProcessorPrefetchConfigTable": cfprApBiosVfProcessorPrefetchConfigTable,
       "cfprApBiosVfProcessorPrefetchConfigEntry": cfprApBiosVfProcessorPrefetchConfigEntry,
       "cfprApBiosVfProcessorPrefetchConfigInstanceId": cfprApBiosVfProcessorPrefetchConfigInstanceId,
       "cfprApBiosVfProcessorPrefetchConfigDn": cfprApBiosVfProcessorPrefetchConfigDn,
       "cfprApBiosVfProcessorPrefetchConfigRn": cfprApBiosVfProcessorPrefetchConfigRn,
       "cfprApBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher": cfprApBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher,
       "cfprApBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher": cfprApBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher,
       "cfprApBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch": cfprApBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch,
       "cfprApBiosVfProcessorPrefetchConfigVpHardwarePrefetcher": cfprApBiosVfProcessorPrefetchConfigVpHardwarePrefetcher,
       "cfprApBiosVfQPILinkFrequencySelectTable": cfprApBiosVfQPILinkFrequencySelectTable,
       "cfprApBiosVfQPILinkFrequencySelectEntry": cfprApBiosVfQPILinkFrequencySelectEntry,
       "cfprApBiosVfQPILinkFrequencySelectInstanceId": cfprApBiosVfQPILinkFrequencySelectInstanceId,
       "cfprApBiosVfQPILinkFrequencySelectDn": cfprApBiosVfQPILinkFrequencySelectDn,
       "cfprApBiosVfQPILinkFrequencySelectRn": cfprApBiosVfQPILinkFrequencySelectRn,
       "cfprApBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect": cfprApBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect,
       "cfprApBiosVfQuietBootTable": cfprApBiosVfQuietBootTable,
       "cfprApBiosVfQuietBootEntry": cfprApBiosVfQuietBootEntry,
       "cfprApBiosVfQuietBootInstanceId": cfprApBiosVfQuietBootInstanceId,
       "cfprApBiosVfQuietBootDn": cfprApBiosVfQuietBootDn,
       "cfprApBiosVfQuietBootRn": cfprApBiosVfQuietBootRn,
       "cfprApBiosVfQuietBootVpQuietBoot": cfprApBiosVfQuietBootVpQuietBoot,
       "cfprApBiosVfResumeOnACPowerLossTable": cfprApBiosVfResumeOnACPowerLossTable,
       "cfprApBiosVfResumeOnACPowerLossEntry": cfprApBiosVfResumeOnACPowerLossEntry,
       "cfprApBiosVfResumeOnACPowerLossInstanceId": cfprApBiosVfResumeOnACPowerLossInstanceId,
       "cfprApBiosVfResumeOnACPowerLossDn": cfprApBiosVfResumeOnACPowerLossDn,
       "cfprApBiosVfResumeOnACPowerLossRn": cfprApBiosVfResumeOnACPowerLossRn,
       "cfprApBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss": cfprApBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss,
       "cfprApBiosVfScrubPoliciesTable": cfprApBiosVfScrubPoliciesTable,
       "cfprApBiosVfScrubPoliciesEntry": cfprApBiosVfScrubPoliciesEntry,
       "cfprApBiosVfScrubPoliciesInstanceId": cfprApBiosVfScrubPoliciesInstanceId,
       "cfprApBiosVfScrubPoliciesDn": cfprApBiosVfScrubPoliciesDn,
       "cfprApBiosVfScrubPoliciesRn": cfprApBiosVfScrubPoliciesRn,
       "cfprApBiosVfScrubPoliciesVpDemandScrub": cfprApBiosVfScrubPoliciesVpDemandScrub,
       "cfprApBiosVfScrubPoliciesVpPatrolScrub": cfprApBiosVfScrubPoliciesVpPatrolScrub,
       "cfprApBiosVfSelectMemoryRASConfigurationTable": cfprApBiosVfSelectMemoryRASConfigurationTable,
       "cfprApBiosVfSelectMemoryRASConfigurationEntry": cfprApBiosVfSelectMemoryRASConfigurationEntry,
       "cfprApBiosVfSelectMemoryRASConfigurationInstanceId": cfprApBiosVfSelectMemoryRASConfigurationInstanceId,
       "cfprApBiosVfSelectMemoryRASConfigurationDn": cfprApBiosVfSelectMemoryRASConfigurationDn,
       "cfprApBiosVfSelectMemoryRASConfigurationRn": cfprApBiosVfSelectMemoryRASConfigurationRn,
       "cfprApBiosVfSelectMemoryRASConfigurationVpSelectMemoryRASConfiguration": cfprApBiosVfSelectMemoryRASConfigurationVpSelectMemoryRASConfiguration,
       "cfprApBiosVfSerialPortAEnableTable": cfprApBiosVfSerialPortAEnableTable,
       "cfprApBiosVfSerialPortAEnableEntry": cfprApBiosVfSerialPortAEnableEntry,
       "cfprApBiosVfSerialPortAEnableInstanceId": cfprApBiosVfSerialPortAEnableInstanceId,
       "cfprApBiosVfSerialPortAEnableDn": cfprApBiosVfSerialPortAEnableDn,
       "cfprApBiosVfSerialPortAEnableRn": cfprApBiosVfSerialPortAEnableRn,
       "cfprApBiosVfSerialPortAEnableVpSerialPortAEnable": cfprApBiosVfSerialPortAEnableVpSerialPortAEnable,
       "cfprApBiosVfSparingModeTable": cfprApBiosVfSparingModeTable,
       "cfprApBiosVfSparingModeEntry": cfprApBiosVfSparingModeEntry,
       "cfprApBiosVfSparingModeInstanceId": cfprApBiosVfSparingModeInstanceId,
       "cfprApBiosVfSparingModeDn": cfprApBiosVfSparingModeDn,
       "cfprApBiosVfSparingModeRn": cfprApBiosVfSparingModeRn,
       "cfprApBiosVfSparingModeVpSparingMode": cfprApBiosVfSparingModeVpSparingMode,
       "cfprApBiosVfSriovConfigTable": cfprApBiosVfSriovConfigTable,
       "cfprApBiosVfSriovConfigEntry": cfprApBiosVfSriovConfigEntry,
       "cfprApBiosVfSriovConfigInstanceId": cfprApBiosVfSriovConfigInstanceId,
       "cfprApBiosVfSriovConfigDn": cfprApBiosVfSriovConfigDn,
       "cfprApBiosVfSriovConfigRn": cfprApBiosVfSriovConfigRn,
       "cfprApBiosVfSriovConfigVpSriov": cfprApBiosVfSriovConfigVpSriov,
       "cfprApBiosVfTPMSupportTable": cfprApBiosVfTPMSupportTable,
       "cfprApBiosVfTPMSupportEntry": cfprApBiosVfTPMSupportEntry,
       "cfprApBiosVfTPMSupportInstanceId": cfprApBiosVfTPMSupportInstanceId,
       "cfprApBiosVfTPMSupportDn": cfprApBiosVfTPMSupportDn,
       "cfprApBiosVfTPMSupportRn": cfprApBiosVfTPMSupportRn,
       "cfprApBiosVfTPMSupportVpTPMSupport": cfprApBiosVfTPMSupportVpTPMSupport,
       "cfprApBiosVfUCSMBootModeControlTable": cfprApBiosVfUCSMBootModeControlTable,
       "cfprApBiosVfUCSMBootModeControlEntry": cfprApBiosVfUCSMBootModeControlEntry,
       "cfprApBiosVfUCSMBootModeControlInstanceId": cfprApBiosVfUCSMBootModeControlInstanceId,
       "cfprApBiosVfUCSMBootModeControlDn": cfprApBiosVfUCSMBootModeControlDn,
       "cfprApBiosVfUCSMBootModeControlRn": cfprApBiosVfUCSMBootModeControlRn,
       "cfprApBiosVfUCSMBootModeControlVpUEFIBootMode": cfprApBiosVfUCSMBootModeControlVpUEFIBootMode,
       "cfprApBiosVfUCSMBootOrderRuleControlTable": cfprApBiosVfUCSMBootOrderRuleControlTable,
       "cfprApBiosVfUCSMBootOrderRuleControlEntry": cfprApBiosVfUCSMBootOrderRuleControlEntry,
       "cfprApBiosVfUCSMBootOrderRuleControlInstanceId": cfprApBiosVfUCSMBootOrderRuleControlInstanceId,
       "cfprApBiosVfUCSMBootOrderRuleControlDn": cfprApBiosVfUCSMBootOrderRuleControlDn,
       "cfprApBiosVfUCSMBootOrderRuleControlRn": cfprApBiosVfUCSMBootOrderRuleControlRn,
       "cfprApBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule": cfprApBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule,
       "cfprApBiosVfUEFIOSUseLegacyVideoTable": cfprApBiosVfUEFIOSUseLegacyVideoTable,
       "cfprApBiosVfUEFIOSUseLegacyVideoEntry": cfprApBiosVfUEFIOSUseLegacyVideoEntry,
       "cfprApBiosVfUEFIOSUseLegacyVideoInstanceId": cfprApBiosVfUEFIOSUseLegacyVideoInstanceId,
       "cfprApBiosVfUEFIOSUseLegacyVideoDn": cfprApBiosVfUEFIOSUseLegacyVideoDn,
       "cfprApBiosVfUEFIOSUseLegacyVideoRn": cfprApBiosVfUEFIOSUseLegacyVideoRn,
       "cfprApBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo": cfprApBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo,
       "cfprApBiosVfUSBBootConfigTable": cfprApBiosVfUSBBootConfigTable,
       "cfprApBiosVfUSBBootConfigEntry": cfprApBiosVfUSBBootConfigEntry,
       "cfprApBiosVfUSBBootConfigInstanceId": cfprApBiosVfUSBBootConfigInstanceId,
       "cfprApBiosVfUSBBootConfigDn": cfprApBiosVfUSBBootConfigDn,
       "cfprApBiosVfUSBBootConfigRn": cfprApBiosVfUSBBootConfigRn,
       "cfprApBiosVfUSBBootConfigVpLegacyUSBSupport": cfprApBiosVfUSBBootConfigVpLegacyUSBSupport,
       "cfprApBiosVfUSBBootConfigVpMakeDeviceNonBootable": cfprApBiosVfUSBBootConfigVpMakeDeviceNonBootable,
       "cfprApBiosVfUSBConfigurationTable": cfprApBiosVfUSBConfigurationTable,
       "cfprApBiosVfUSBConfigurationEntry": cfprApBiosVfUSBConfigurationEntry,
       "cfprApBiosVfUSBConfigurationInstanceId": cfprApBiosVfUSBConfigurationInstanceId,
       "cfprApBiosVfUSBConfigurationDn": cfprApBiosVfUSBConfigurationDn,
       "cfprApBiosVfUSBConfigurationRn": cfprApBiosVfUSBConfigurationRn,
       "cfprApBiosVfUSBConfigurationVpLegacyUSBSupport": cfprApBiosVfUSBConfigurationVpLegacyUSBSupport,
       "cfprApBiosVfUSBConfigurationVpXHCIMode": cfprApBiosVfUSBConfigurationVpXHCIMode,
       "cfprApBiosVfUSBFrontPanelAccessLockTable": cfprApBiosVfUSBFrontPanelAccessLockTable,
       "cfprApBiosVfUSBFrontPanelAccessLockEntry": cfprApBiosVfUSBFrontPanelAccessLockEntry,
       "cfprApBiosVfUSBFrontPanelAccessLockInstanceId": cfprApBiosVfUSBFrontPanelAccessLockInstanceId,
       "cfprApBiosVfUSBFrontPanelAccessLockDn": cfprApBiosVfUSBFrontPanelAccessLockDn,
       "cfprApBiosVfUSBFrontPanelAccessLockRn": cfprApBiosVfUSBFrontPanelAccessLockRn,
       "cfprApBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock": cfprApBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock,
       "cfprApBiosVfUSBPortConfigurationTable": cfprApBiosVfUSBPortConfigurationTable,
       "cfprApBiosVfUSBPortConfigurationEntry": cfprApBiosVfUSBPortConfigurationEntry,
       "cfprApBiosVfUSBPortConfigurationInstanceId": cfprApBiosVfUSBPortConfigurationInstanceId,
       "cfprApBiosVfUSBPortConfigurationDn": cfprApBiosVfUSBPortConfigurationDn,
       "cfprApBiosVfUSBPortConfigurationRn": cfprApBiosVfUSBPortConfigurationRn,
       "cfprApBiosVfUSBPortConfigurationVpPort6064Emulation": cfprApBiosVfUSBPortConfigurationVpPort6064Emulation,
       "cfprApBiosVfUSBPortConfigurationVpUSBPortFront": cfprApBiosVfUSBPortConfigurationVpUSBPortFront,
       "cfprApBiosVfUSBPortConfigurationVpUSBPortInternal": cfprApBiosVfUSBPortConfigurationVpUSBPortInternal,
       "cfprApBiosVfUSBPortConfigurationVpUSBPortKVM": cfprApBiosVfUSBPortConfigurationVpUSBPortKVM,
       "cfprApBiosVfUSBPortConfigurationVpUSBPortRear": cfprApBiosVfUSBPortConfigurationVpUSBPortRear,
       "cfprApBiosVfUSBPortConfigurationVpUSBPortSDCard": cfprApBiosVfUSBPortConfigurationVpUSBPortSDCard,
       "cfprApBiosVfUSBPortConfigurationVpUSBPortVMedia": cfprApBiosVfUSBPortConfigurationVpUSBPortVMedia,
       "cfprApBiosVfUSBSystemIdlePowerOptimizingSettingTable": cfprApBiosVfUSBSystemIdlePowerOptimizingSettingTable,
       "cfprApBiosVfUSBSystemIdlePowerOptimizingSettingEntry": cfprApBiosVfUSBSystemIdlePowerOptimizingSettingEntry,
       "cfprApBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId": cfprApBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId,
       "cfprApBiosVfUSBSystemIdlePowerOptimizingSettingDn": cfprApBiosVfUSBSystemIdlePowerOptimizingSettingDn,
       "cfprApBiosVfUSBSystemIdlePowerOptimizingSettingRn": cfprApBiosVfUSBSystemIdlePowerOptimizingSettingRn,
       "cfprApBiosVfUSBSystemIdlePowerOptimizingSettingVpUSBIdlePowerOptimizing": cfprApBiosVfUSBSystemIdlePowerOptimizingSettingVpUSBIdlePowerOptimizing,
       "cfprApBiosVfVGAPriorityTable": cfprApBiosVfVGAPriorityTable,
       "cfprApBiosVfVGAPriorityEntry": cfprApBiosVfVGAPriorityEntry,
       "cfprApBiosVfVGAPriorityInstanceId": cfprApBiosVfVGAPriorityInstanceId,
       "cfprApBiosVfVGAPriorityDn": cfprApBiosVfVGAPriorityDn,
       "cfprApBiosVfVGAPriorityRn": cfprApBiosVfVGAPriorityRn,
       "cfprApBiosVfVGAPriorityVpVGAPriority": cfprApBiosVfVGAPriorityVpVGAPriority}
)
