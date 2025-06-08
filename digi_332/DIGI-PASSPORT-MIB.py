# SNMP MIB module (DIGI-PASSPORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/digi_332/DIGI-PASSPORT-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:54:30 2025
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

(digiPassport,) = mibBuilder.importSymbols(
    "DIGI-SMI",
    "digiPassport")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""




class Switch(Integer32):
    """Custom type Switch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )





class Action(Integer32):
    """Custom type Action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("execute", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 20)
)
_GeneralModel_Type = DisplayString
_GeneralModel_Object = MibScalar
generalModel = _GeneralModel_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 20, 11),
    _GeneralModel_Type()
)
generalModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generalModel.setStatus("mandatory")
_GeneralFirmwareVersion_Type = DisplayString
_GeneralFirmwareVersion_Object = MibScalar
generalFirmwareVersion = _GeneralFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 20, 12),
    _GeneralFirmwareVersion_Type()
)
generalFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generalFirmwareVersion.setStatus("mandatory")
_GeneralBootcodeVersion_Type = DisplayString
_GeneralBootcodeVersion_Object = MibScalar
generalBootcodeVersion = _GeneralBootcodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 20, 13),
    _GeneralBootcodeVersion_Type()
)
generalBootcodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generalBootcodeVersion.setStatus("mandatory")
_GeneralHWRevision_Type = DisplayString
_GeneralHWRevision_Object = MibScalar
generalHWRevision = _GeneralHWRevision_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 20, 14),
    _GeneralHWRevision_Type()
)
generalHWRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generalHWRevision.setStatus("mandatory")
_GeneralFlashSize_Type = Integer32
_GeneralFlashSize_Object = MibScalar
generalFlashSize = _GeneralFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 20, 15),
    _GeneralFlashSize_Type()
)
generalFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generalFlashSize.setStatus("mandatory")
_GeneralEtherAddress_Type = PhysAddress
_GeneralEtherAddress_Object = MibScalar
generalEtherAddress = _GeneralEtherAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 20, 16),
    _GeneralEtherAddress_Type()
)
generalEtherAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generalEtherAddress.setStatus("mandatory")
_GeneralIPAddress_Type = IpAddress
_GeneralIPAddress_Object = MibScalar
generalIPAddress = _GeneralIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 20, 17),
    _GeneralIPAddress_Type()
)
generalIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generalIPAddress.setStatus("mandatory")
_GeneralDevicename_Type = DisplayString
_GeneralDevicename_Object = MibScalar
generalDevicename = _GeneralDevicename_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 20, 18),
    _GeneralDevicename_Type()
)
generalDevicename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generalDevicename.setStatus("mandatory")


class _GeneralLocating_Type(Integer32):
    """Custom type generalLocating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 0),
          ("start", 1),
          ("stop", 2))
    )


_GeneralLocating_Type.__name__ = "Integer32"
_GeneralLocating_Object = MibScalar
generalLocating = _GeneralLocating_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 20, 19),
    _GeneralLocating_Type()
)
generalLocating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generalLocating.setStatus("mandatory")


class _GeneralPowerStatus_Type(Integer32):
    """Custom type generalPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerAllOK", 0),
          ("power1Failure", 1),
          ("power2Failure", 2))
    )


_GeneralPowerStatus_Type.__name__ = "Integer32"
_GeneralPowerStatus_Object = MibScalar
generalPowerStatus = _GeneralPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 20, 20),
    _GeneralPowerStatus_Type()
)
generalPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generalPowerStatus.setStatus("mandatory")


class _GeneralSaveApplyConfig_Type(Integer32):
    """Custom type generalSaveApplyConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 0),
          ("save", 1),
          ("saveapply", 2))
    )


_GeneralSaveApplyConfig_Type.__name__ = "Integer32"
_GeneralSaveApplyConfig_Object = MibScalar
generalSaveApplyConfig = _GeneralSaveApplyConfig_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 20, 30),
    _GeneralSaveApplyConfig_Type()
)
generalSaveApplyConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generalSaveApplyConfig.setStatus("mandatory")
_Processor_ObjectIdentity = ObjectIdentity
processor = _Processor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 21)
)


class _ProcessorUtilization_Type(Integer32):
    """Custom type processorUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ProcessorUtilization_Type.__name__ = "Integer32"
_ProcessorUtilization_Object = MibScalar
processorUtilization = _ProcessorUtilization_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 21, 11),
    _ProcessorUtilization_Type()
)
processorUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorUtilization.setStatus("mandatory")
_Memory_ObjectIdentity = ObjectIdentity
memory = _Memory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 22)
)
_MemoryTotalMemory_Type = Integer32
_MemoryTotalMemory_Object = MibScalar
memoryTotalMemory = _MemoryTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 22, 11),
    _MemoryTotalMemory_Type()
)
memoryTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryTotalMemory.setStatus("mandatory")
_MemoryAvailable_Type = Integer32
_MemoryAvailable_Object = MibScalar
memoryAvailable = _MemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 22, 12),
    _MemoryAvailable_Type()
)
memoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryAvailable.setStatus("mandatory")
_Time_ObjectIdentity = ObjectIdentity
time = _Time_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 23)
)


class _TimeSystemCurrent_Type(DisplayString):
    """Custom type timeSystemCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_TimeSystemCurrent_Type.__name__ = "DisplayString"
_TimeSystemCurrent_Object = MibScalar
timeSystemCurrent = _TimeSystemCurrent_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 23, 11),
    _TimeSystemCurrent_Type()
)
timeSystemCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeSystemCurrent.setStatus("mandatory")
_TimeNTPEnable_Type = Switch
_TimeNTPEnable_Object = MibScalar
timeNTPEnable = _TimeNTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 23, 12),
    _TimeNTPEnable_Type()
)
timeNTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeNTPEnable.setStatus("mandatory")
_TimeNTPAutoConfig_Type = Switch
_TimeNTPAutoConfig_Object = MibScalar
timeNTPAutoConfig = _TimeNTPAutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 23, 13),
    _TimeNTPAutoConfig_Type()
)
timeNTPAutoConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeNTPAutoConfig.setStatus("mandatory")
_TimeNTPServer_Type = DisplayString
_TimeNTPServer_Object = MibScalar
timeNTPServer = _TimeNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 23, 14),
    _TimeNTPServer_Type()
)
timeNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeNTPServer.setStatus("mandatory")
_TimeNTPInterval_Type = Integer32
_TimeNTPInterval_Object = MibScalar
timeNTPInterval = _TimeNTPInterval_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 23, 15),
    _TimeNTPInterval_Type()
)
timeNTPInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeNTPInterval.setStatus("mandatory")
_TimeNTPDHCPOptEnable_Type = Switch
_TimeNTPDHCPOptEnable_Object = MibScalar
timeNTPDHCPOptEnable = _TimeNTPDHCPOptEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 23, 16),
    _TimeNTPDHCPOptEnable_Type()
)
timeNTPDHCPOptEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeNTPDHCPOptEnable.setStatus("mandatory")
_Boot_ObjectIdentity = ObjectIdentity
boot = _Boot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 24)
)
_BootReboot_Type = Action
_BootReboot_Object = MibScalar
bootReboot = _BootReboot_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 24, 11),
    _BootReboot_Type()
)
bootReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootReboot.setStatus("mandatory")
_Port_ObjectIdentity = ObjectIdentity
port = _Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25)
)
_PortManageTable_Object = MibTable
portManageTable = _PortManageTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 11)
)
if mibBuilder.loadTexts:
    portManageTable.setStatus("mandatory")
_PortManageEntry_Object = MibTableRow
portManageEntry = _PortManageEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 11, 1)
)
portManageEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "portManageIndex"),
)
if mibBuilder.loadTexts:
    portManageEntry.setStatus("mandatory")
_PortManageIndex_Type = Integer32
_PortManageIndex_Object = MibTableColumn
portManageIndex = _PortManageIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 11, 1, 11),
    _PortManageIndex_Type()
)
portManageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portManageIndex.setStatus("mandatory")
_PortsEnable_Type = Switch
_PortsEnable_Object = MibTableColumn
portsEnable = _PortsEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 11, 1, 12),
    _PortsEnable_Type()
)
portsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsEnable.setStatus("mandatory")
_PortsRealPortEnable_Type = Switch
_PortsRealPortEnable_Object = MibTableColumn
portsRealPortEnable = _PortsRealPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 11, 1, 13),
    _PortsRealPortEnable_Type()
)
portsRealPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsRealPortEnable.setStatus("mandatory")
_PortsResetProcess_Type = Action
_PortsResetProcess_Object = MibTableColumn
portsResetProcess = _PortsResetProcess_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 11, 1, 14),
    _PortsResetProcess_Type()
)
portsResetProcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsResetProcess.setStatus("mandatory")
_PortsResetToFactoryDefault_Type = Action
_PortsResetToFactoryDefault_Object = MibTableColumn
portsResetToFactoryDefault = _PortsResetToFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 11, 1, 15),
    _PortsResetToFactoryDefault_Type()
)
portsResetToFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsResetToFactoryDefault.setStatus("mandatory")
_PortsAddRow_Type = Action
_PortsAddRow_Object = MibTableColumn
portsAddRow = _PortsAddRow_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 11, 1, 16),
    _PortsAddRow_Type()
)
portsAddRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsAddRow.setStatus("mandatory")
_PortsDelRow_Type = Action
_PortsDelRow_Object = MibTableColumn
portsDelRow = _PortsDelRow_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 11, 1, 17),
    _PortsDelRow_Type()
)
portsDelRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsDelRow.setStatus("mandatory")
_PortsGroupName_Type = DisplayString
_PortsGroupName_Object = MibTableColumn
portsGroupName = _PortsGroupName_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 11, 1, 18),
    _PortsGroupName_Type()
)
portsGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsGroupName.setStatus("mandatory")
_PortApplyAllPortsTable_Object = MibTable
portApplyAllPortsTable = _PortApplyAllPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 12)
)
if mibBuilder.loadTexts:
    portApplyAllPortsTable.setStatus("mandatory")
_PortApplyAllPortsEntry_Object = MibTableRow
portApplyAllPortsEntry = _PortApplyAllPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 12, 1)
)
portApplyAllPortsEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "portApplyAllPortsIndex"),
)
if mibBuilder.loadTexts:
    portApplyAllPortsEntry.setStatus("mandatory")
_PortApplyAllPortsIndex_Type = Integer32
_PortApplyAllPortsIndex_Object = MibTableColumn
portApplyAllPortsIndex = _PortApplyAllPortsIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 12, 1, 11),
    _PortApplyAllPortsIndex_Type()
)
portApplyAllPortsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portApplyAllPortsIndex.setStatus("mandatory")
_PortsApplyAllPorts_Type = Switch
_PortsApplyAllPorts_Object = MibTableColumn
portsApplyAllPorts = _PortsApplyAllPorts_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 12, 1, 12),
    _PortsApplyAllPorts_Type()
)
portsApplyAllPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsApplyAllPorts.setStatus("mandatory")
_DetectionTable_Object = MibTable
detectionTable = _DetectionTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 13)
)
if mibBuilder.loadTexts:
    detectionTable.setStatus("mandatory")
_DetectionEntry_Object = MibTableRow
detectionEntry = _DetectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 13, 1)
)
detectionEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "detectIndex"),
)
if mibBuilder.loadTexts:
    detectionEntry.setStatus("mandatory")
_DetectIndex_Type = Integer32
_DetectIndex_Object = MibTableColumn
detectIndex = _DetectIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 13, 1, 11),
    _DetectIndex_Type()
)
detectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    detectIndex.setStatus("mandatory")


class _DetectMethod_Type(Integer32):
    """Custom type detectMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("active", 1),
          ("passive", 2))
    )


_DetectMethod_Type.__name__ = "Integer32"
_DetectMethod_Object = MibTableColumn
detectMethod = _DetectMethod_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 13, 1, 21),
    _DetectMethod_Type()
)
detectMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    detectMethod.setStatus("mandatory")
_DetectInitDelay_Type = Integer32
_DetectInitDelay_Object = MibTableColumn
detectInitDelay = _DetectInitDelay_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 13, 1, 22),
    _DetectInitDelay_Type()
)
detectInitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    detectInitDelay.setStatus("mandatory")
_DetectInterval_Type = Integer32
_DetectInterval_Object = MibTableColumn
detectInterval = _DetectInterval_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 13, 1, 23),
    _DetectInterval_Type()
)
detectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    detectInterval.setStatus("mandatory")
_DetectTime_Type = DisplayString
_DetectTime_Object = MibTableColumn
detectTime = _DetectTime_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 13, 1, 24),
    _DetectTime_Type()
)
detectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    detectTime.setStatus("mandatory")
_DetectProbeStr_Type = DisplayString
_DetectProbeStr_Object = MibTableColumn
detectProbeStr = _DetectProbeStr_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 13, 1, 25),
    _DetectProbeStr_Type()
)
detectProbeStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    detectProbeStr.setStatus("mandatory")
_DetectedOS_Type = DisplayString
_DetectedOS_Object = MibTableColumn
detectedOS = _DetectedOS_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 13, 1, 26),
    _DetectedOS_Type()
)
detectedOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    detectedOS.setStatus("mandatory")
_UseDetectedTitle_Type = Switch
_UseDetectedTitle_Object = MibTableColumn
useDetectedTitle = _UseDetectedTitle_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 13, 1, 27),
    _UseDetectedTitle_Type()
)
useDetectedTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    useDetectedTitle.setStatus("mandatory")
_TitleNamingRule_Type = DisplayString
_TitleNamingRule_Object = MibTableColumn
titleNamingRule = _TitleNamingRule_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 13, 1, 28),
    _TitleNamingRule_Type()
)
titleNamingRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    titleNamingRule.setStatus("mandatory")
_UseDetectedTypeOfCS_Type = Switch
_UseDetectedTypeOfCS_Object = MibTableColumn
useDetectedTypeOfCS = _UseDetectedTypeOfCS_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 13, 1, 29),
    _UseDetectedTypeOfCS_Type()
)
useDetectedTypeOfCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    useDetectedTypeOfCS.setStatus("mandatory")
_UseDetectedFreeKVM_Type = Switch
_UseDetectedFreeKVM_Object = MibTableColumn
useDetectedFreeKVM = _UseDetectedFreeKVM_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 13, 1, 30),
    _UseDetectedFreeKVM_Type()
)
useDetectedFreeKVM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    useDetectedFreeKVM.setStatus("mandatory")
_UseDetectedSerialParams_Type = Switch
_UseDetectedSerialParams_Object = MibTableColumn
useDetectedSerialParams = _UseDetectedSerialParams_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 13, 1, 31),
    _UseDetectedSerialParams_Type()
)
useDetectedSerialParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    useDetectedSerialParams.setStatus("mandatory")


class _DetectDeviceVia_Type(Integer32):
    """Custom type detectDeviceVia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("dsr", 1))
    )


_DetectDeviceVia_Type.__name__ = "Integer32"
_DetectDeviceVia_Object = MibTableColumn
detectDeviceVia = _DetectDeviceVia_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 13, 1, 32),
    _DetectDeviceVia_Type()
)
detectDeviceVia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    detectDeviceVia.setStatus("mandatory")
_PortTitleTable_Object = MibTable
portTitleTable = _PortTitleTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 14)
)
if mibBuilder.loadTexts:
    portTitleTable.setStatus("mandatory")
_PortTitleEntry_Object = MibTableRow
portTitleEntry = _PortTitleEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 14, 1)
)
portTitleEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "portTitleIndex"),
)
if mibBuilder.loadTexts:
    portTitleEntry.setStatus("mandatory")
_PortTitleIndex_Type = Integer32
_PortTitleIndex_Object = MibTableColumn
portTitleIndex = _PortTitleIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 14, 1, 11),
    _PortTitleIndex_Type()
)
portTitleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTitleIndex.setStatus("mandatory")
_PortTitle_Type = DisplayString
_PortTitle_Object = MibTableColumn
portTitle = _PortTitle_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 14, 1, 14),
    _PortTitle_Type()
)
portTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTitle.setStatus("mandatory")
_HostmodeTable_Object = MibTable
hostmodeTable = _HostmodeTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15)
)
if mibBuilder.loadTexts:
    hostmodeTable.setStatus("mandatory")
_HostmodeEntry_Object = MibTableRow
hostmodeEntry = _HostmodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1)
)
hostmodeEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "hostmodeIndex"),
)
if mibBuilder.loadTexts:
    hostmodeEntry.setStatus("mandatory")
_HostmodeIndex_Type = Integer32
_HostmodeIndex_Object = MibTableColumn
hostmodeIndex = _HostmodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 11),
    _HostmodeIndex_Type()
)
hostmodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostmodeIndex.setStatus("mandatory")


class _HostMode_Type(Integer32):
    """Custom type hostMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ts", 0),
          ("cs", 1),
          ("di", 2),
          ("dits", 3),
          ("ppp", 4))
    )


_HostMode_Type.__name__ = "Integer32"
_HostMode_Object = MibTableColumn
hostMode = _HostMode_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 12),
    _HostMode_Type()
)
hostMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostMode.setStatus("mandatory")


class _HostTypeCS_Type(Integer32):
    """Custom type hostTypeCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("powerctrl", 3),
          ("mssac", 4))
    )


_HostTypeCS_Type.__name__ = "Integer32"
_HostTypeCS_Object = MibTableColumn
hostTypeCS = _HostTypeCS_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 13),
    _HostTypeCS_Type()
)
hostTypeCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostTypeCS.setStatus("mandatory")
_HostEnableRackableCard_Type = Switch
_HostEnableRackableCard_Object = MibTableColumn
hostEnableRackableCard = _HostEnableRackableCard_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 14),
    _HostEnableRackableCard_Type()
)
hostEnableRackableCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostEnableRackableCard.setStatus("mandatory")
_HostEnableAssignedIP_Type = Switch
_HostEnableAssignedIP_Object = MibTableColumn
hostEnableAssignedIP = _HostEnableAssignedIP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 15),
    _HostEnableAssignedIP_Type()
)
hostEnableAssignedIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostEnableAssignedIP.setStatus("mandatory")
_HostAssignedIP_Type = DisplayString
_HostAssignedIP_Object = MibTableColumn
hostAssignedIP = _HostAssignedIP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 16),
    _HostAssignedIP_Type()
)
hostAssignedIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostAssignedIP.setStatus("mandatory")
_HostLocalPort_Type = Integer32
_HostLocalPort_Object = MibTableColumn
hostLocalPort = _HostLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 17),
    _HostLocalPort_Type()
)
hostLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostLocalPort.setStatus("mandatory")


class _HostProtocol_Type(Integer32):
    """Custom type hostProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("telnet", 1),
          ("ssh", 2),
          ("rawTCP", 3))
    )


_HostProtocol_Type.__name__ = "Integer32"
_HostProtocol_Object = MibTableColumn
hostProtocol = _HostProtocol_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 18),
    _HostProtocol_Type()
)
hostProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostProtocol.setStatus("mandatory")


class _HostInactivity_Type(Integer32):
    """Custom type hostInactivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_HostInactivity_Type.__name__ = "Integer32"
_HostInactivity_Object = MibTableColumn
hostInactivity = _HostInactivity_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 19),
    _HostInactivity_Type()
)
hostInactivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostInactivity.setStatus("mandatory")
_HostEnableEscapeChar_Type = Switch
_HostEnableEscapeChar_Object = MibTableColumn
hostEnableEscapeChar = _HostEnableEscapeChar_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 20),
    _HostEnableEscapeChar_Type()
)
hostEnableEscapeChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostEnableEscapeChar.setStatus("deprecated")
_HostEscapeChar_Type = DisplayString
_HostEscapeChar_Object = MibTableColumn
hostEscapeChar = _HostEscapeChar_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 21),
    _HostEscapeChar_Type()
)
hostEscapeChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostEscapeChar.setStatus("mandatory")
_HostBreakSeq_Type = DisplayString
_HostBreakSeq_Object = MibTableColumn
hostBreakSeq = _HostBreakSeq_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 22),
    _HostBreakSeq_Type()
)
hostBreakSeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostBreakSeq.setStatus("mandatory")
_HostUseComment_Type = Switch
_HostUseComment_Object = MibTableColumn
hostUseComment = _HostUseComment_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 23),
    _HostUseComment_Type()
)
hostUseComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostUseComment.setStatus("mandatory")


class _HostQuickConnect_Type(Integer32):
    """Custom type hostQuickConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localclient", 1),
          ("webapplet", 2),
          ("userdefined", 3))
    )


_HostQuickConnect_Type.__name__ = "Integer32"
_HostQuickConnect_Object = MibTableColumn
hostQuickConnect = _HostQuickConnect_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 24),
    _HostQuickConnect_Type()
)
hostQuickConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostQuickConnect.setStatus("mandatory")


class _HostAppletEncode_Type(Integer32):
    """Custom type hostAppletEncode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("english", 1),
          ("korean", 2),
          ("japanese", 3),
          ("utf8", 4))
    )


_HostAppletEncode_Type.__name__ = "Integer32"
_HostAppletEncode_Object = MibTableColumn
hostAppletEncode = _HostAppletEncode_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 25),
    _HostAppletEncode_Type()
)
hostAppletEncode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostAppletEncode.setStatus("mandatory")


class _HostTSOption_Type(Integer32):
    """Custom type hostTSOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("remoteConnection", 0),
          ("shellProgram", 1))
    )


_HostTSOption_Type.__name__ = "Integer32"
_HostTSOption_Object = MibTableColumn
hostTSOption = _HostTSOption_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 26),
    _HostTSOption_Type()
)
hostTSOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostTSOption.setStatus("mandatory")
_HostDestIP_Type = DisplayString
_HostDestIP_Object = MibTableColumn
hostDestIP = _HostDestIP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 27),
    _HostDestIP_Type()
)
hostDestIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostDestIP.setStatus("mandatory")
_HostDestPort_Type = Integer32
_HostDestPort_Object = MibTableColumn
hostDestPort = _HostDestPort_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 28),
    _HostDestPort_Type()
)
hostDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostDestPort.setStatus("mandatory")
_HostTSShellProgramPath_Type = DisplayString
_HostTSShellProgramPath_Object = MibTableColumn
hostTSShellProgramPath = _HostTSShellProgramPath_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 29),
    _HostTSShellProgramPath_Type()
)
hostTSShellProgramPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostTSShellProgramPath.setStatus("mandatory")
_HostModemInitStr_Type = DisplayString
_HostModemInitStr_Object = MibTableColumn
hostModemInitStr = _HostModemInitStr_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 30),
    _HostModemInitStr_Type()
)
hostModemInitStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostModemInitStr.setStatus("mandatory")
_HostEnableCallback_Type = Switch
_HostEnableCallback_Object = MibTableColumn
hostEnableCallback = _HostEnableCallback_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 31),
    _HostEnableCallback_Type()
)
hostEnableCallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostEnableCallback.setStatus("mandatory")
_HostCallbackNumber_Type = DisplayString
_HostCallbackNumber_Object = MibTableColumn
hostCallbackNumber = _HostCallbackNumber_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 32),
    _HostCallbackNumber_Type()
)
hostCallbackNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostCallbackNumber.setStatus("mandatory")
_HostEnableModemTest_Type = Switch
_HostEnableModemTest_Object = MibTableColumn
hostEnableModemTest = _HostEnableModemTest_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 33),
    _HostEnableModemTest_Type()
)
hostEnableModemTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostEnableModemTest.setStatus("mandatory")
_HostModemTestNumber_Type = DisplayString
_HostModemTestNumber_Object = MibTableColumn
hostModemTestNumber = _HostModemTestNumber_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 34),
    _HostModemTestNumber_Type()
)
hostModemTestNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostModemTestNumber.setStatus("mandatory")


class _HostModemTestInterval_Type(Integer32):
    """Custom type hostModemTestInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 720),
    )


_HostModemTestInterval_Type.__name__ = "Integer32"
_HostModemTestInterval_Object = MibTableColumn
hostModemTestInterval = _HostModemTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 35),
    _HostModemTestInterval_Type()
)
hostModemTestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostModemTestInterval.setStatus("mandatory")


class _HostServiceProcessor_Type(Integer32):
    """Custom type hostServiceProcessor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ipmi", 1),
          ("iLO", 2),
          ("drac", 3))
    )


_HostServiceProcessor_Type.__name__ = "Integer32"
_HostServiceProcessor_Object = MibTableColumn
hostServiceProcessor = _HostServiceProcessor_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 36),
    _HostServiceProcessor_Type()
)
hostServiceProcessor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostServiceProcessor.setStatus("mandatory")
_HostEnableCallbackLogin_Type = Switch
_HostEnableCallbackLogin_Object = MibTableColumn
hostEnableCallbackLogin = _HostEnableCallbackLogin_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 37),
    _HostEnableCallbackLogin_Type()
)
hostEnableCallbackLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostEnableCallbackLogin.setStatus("mandatory")
_HostEnableCallbackNumberChange_Type = Switch
_HostEnableCallbackNumberChange_Object = MibTableColumn
hostEnableCallbackNumberChange = _HostEnableCallbackNumberChange_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 38),
    _HostEnableCallbackNumberChange_Type()
)
hostEnableCallbackNumberChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostEnableCallbackNumberChange.setStatus("mandatory")


class _HostEnableAppletColumns_Type(Integer32):
    """Custom type hostEnableAppletColumns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 200),
    )


_HostEnableAppletColumns_Type.__name__ = "Integer32"
_HostEnableAppletColumns_Object = MibTableColumn
hostEnableAppletColumns = _HostEnableAppletColumns_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 39),
    _HostEnableAppletColumns_Type()
)
hostEnableAppletColumns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostEnableAppletColumns.setStatus("mandatory")


class _HostEnableAppletRows_Type(Integer32):
    """Custom type hostEnableAppletRows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_HostEnableAppletRows_Type.__name__ = "Integer32"
_HostEnableAppletRows_Object = MibTableColumn
hostEnableAppletRows = _HostEnableAppletRows_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 40),
    _HostEnableAppletRows_Type()
)
hostEnableAppletRows.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostEnableAppletRows.setStatus("mandatory")
_HostEnableDisPortInfo_Type = Switch
_HostEnableDisPortInfo_Object = MibTableColumn
hostEnableDisPortInfo = _HostEnableDisPortInfo_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 41),
    _HostEnableDisPortInfo_Type()
)
hostEnableDisPortInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostEnableDisPortInfo.setStatus("mandatory")


class _HostEnableEscapeOption_Type(Integer32):
    """Custom type hostEnableEscapeOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("ctrl", 1),
          ("alt", 2))
    )


_HostEnableEscapeOption_Type.__name__ = "Integer32"
_HostEnableEscapeOption_Object = MibTableColumn
hostEnableEscapeOption = _HostEnableEscapeOption_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 15, 1, 42),
    _HostEnableEscapeOption_Type()
)
hostEnableEscapeOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostEnableEscapeOption.setStatus("deprecated")
_ParamTable_Object = MibTable
paramTable = _ParamTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 16)
)
if mibBuilder.loadTexts:
    paramTable.setStatus("mandatory")
_ParamEntry_Object = MibTableRow
paramEntry = _ParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 16, 1)
)
paramEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "paramIndex"),
)
if mibBuilder.loadTexts:
    paramEntry.setStatus("mandatory")
_ParamIndex_Type = Integer32
_ParamIndex_Object = MibTableColumn
paramIndex = _ParamIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 16, 1, 11),
    _ParamIndex_Type()
)
paramIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramIndex.setStatus("mandatory")


class _ParamType_Type(Integer32):
    """Custom type paramType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rs232", 0),
          ("rs485ECHO", 1),
          ("rs485NOECHO", 2),
          ("rs422", 3))
    )


_ParamType_Type.__name__ = "Integer32"
_ParamType_Object = MibTableColumn
paramType = _ParamType_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 16, 1, 12),
    _ParamType_Type()
)
paramType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramType.setStatus("mandatory")


class _ParamBaud_Type(Integer32):
    """Custom type paramBaud based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(75,
              150,
              200,
              300,
              600,
              1200,
              1800,
              2400,
              4800,
              9600,
              19200,
              38400,
              57600,
              115200,
              230400)
        )
    )
    namedValues = NamedValues(
        *(("b75", 75),
          ("b150", 150),
          ("b200", 200),
          ("b300", 300),
          ("b600", 600),
          ("b1200", 1200),
          ("b1800", 1800),
          ("b2400", 2400),
          ("b4800", 4800),
          ("b9600", 9600),
          ("b19200", 19200),
          ("b38400", 38400),
          ("b57600", 57600),
          ("b115200", 115200),
          ("b230400", 230400))
    )


_ParamBaud_Type.__name__ = "Integer32"
_ParamBaud_Object = MibTableColumn
paramBaud = _ParamBaud_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 16, 1, 13),
    _ParamBaud_Type()
)
paramBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramBaud.setStatus("mandatory")


class _ParamDatabits_Type(Integer32):
    """Custom type paramDatabits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("seven", 7),
          ("eight", 8))
    )


_ParamDatabits_Type.__name__ = "Integer32"
_ParamDatabits_Object = MibTableColumn
paramDatabits = _ParamDatabits_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 16, 1, 14),
    _ParamDatabits_Type()
)
paramDatabits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramDatabits.setStatus("mandatory")


class _ParamParity_Type(Integer32):
    """Custom type paramParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("even", 1),
          ("odd", 2))
    )


_ParamParity_Type.__name__ = "Integer32"
_ParamParity_Object = MibTableColumn
paramParity = _ParamParity_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 16, 1, 15),
    _ParamParity_Type()
)
paramParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramParity.setStatus("mandatory")


class _ParamStopbits_Type(Integer32):
    """Custom type paramStopbits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_ParamStopbits_Type.__name__ = "Integer32"
_ParamStopbits_Object = MibTableColumn
paramStopbits = _ParamStopbits_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 16, 1, 16),
    _ParamStopbits_Type()
)
paramStopbits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramStopbits.setStatus("mandatory")


class _ParamFlowctrl_Type(Integer32):
    """Custom type paramFlowctrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("xonxoff", 1),
          ("hardware", 2))
    )


_ParamFlowctrl_Type.__name__ = "Integer32"
_ParamFlowctrl_Object = MibTableColumn
paramFlowctrl = _ParamFlowctrl_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 16, 1, 17),
    _ParamFlowctrl_Type()
)
paramFlowctrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramFlowctrl.setStatus("mandatory")


class _ParamDTROpt_Type(Integer32):
    """Custom type paramDTROpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 0),
          ("low", 1),
          ("highonopen", 2))
    )


_ParamDTROpt_Type.__name__ = "Integer32"
_ParamDTROpt_Object = MibTableColumn
paramDTROpt = _ParamDTROpt_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 16, 1, 18),
    _ParamDTROpt_Type()
)
paramDTROpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramDTROpt.setStatus("mandatory")
_ParamEnableDelimiter_Type = Switch
_ParamEnableDelimiter_Object = MibTableColumn
paramEnableDelimiter = _ParamEnableDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 16, 1, 19),
    _ParamEnableDelimiter_Type()
)
paramEnableDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramEnableDelimiter.setStatus("mandatory")
_ParamDelimiter_Type = DisplayString
_ParamDelimiter_Object = MibTableColumn
paramDelimiter = _ParamDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 16, 1, 20),
    _ParamDelimiter_Type()
)
paramDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramDelimiter.setStatus("mandatory")


class _ParamDeilmiterOption_Type(Integer32):
    """Custom type paramDeilmiterOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("include", 0),
          ("exclude", 1))
    )


_ParamDeilmiterOption_Type.__name__ = "Integer32"
_ParamDeilmiterOption_Object = MibTableColumn
paramDeilmiterOption = _ParamDeilmiterOption_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 16, 1, 21),
    _ParamDeilmiterOption_Type()
)
paramDeilmiterOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramDeilmiterOption.setStatus("mandatory")


class _ParamInterCharTimeout_Type(Integer32):
    """Custom type paramInterCharTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_ParamInterCharTimeout_Type.__name__ = "Integer32"
_ParamInterCharTimeout_Object = MibTableColumn
paramInterCharTimeout = _ParamInterCharTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 16, 1, 22),
    _ParamInterCharTimeout_Type()
)
paramInterCharTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramInterCharTimeout.setStatus("mandatory")
_ParamRemoteDestIP_Type = DisplayString
_ParamRemoteDestIP_Object = MibTableColumn
paramRemoteDestIP = _ParamRemoteDestIP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 16, 1, 23),
    _ParamRemoteDestIP_Type()
)
paramRemoteDestIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramRemoteDestIP.setStatus("mandatory")
_ParamRemoteDestPort_Type = Integer32
_ParamRemoteDestPort_Object = MibTableColumn
paramRemoteDestPort = _ParamRemoteDestPort_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 16, 1, 24),
    _ParamRemoteDestPort_Type()
)
paramRemoteDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramRemoteDestPort.setStatus("mandatory")


class _ParamRemoteProtocol_Type(Integer32):
    """Custom type paramRemoteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("telnet", 1),
          ("ssh", 2),
          ("rawtcp", 3),
          ("rmcpsol", 4))
    )


_ParamRemoteProtocol_Type.__name__ = "Integer32"
_ParamRemoteProtocol_Object = MibTableColumn
paramRemoteProtocol = _ParamRemoteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 16, 1, 25),
    _ParamRemoteProtocol_Type()
)
paramRemoteProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramRemoteProtocol.setStatus("mandatory")
_ParamRemoteContinuousConnect_Type = Switch
_ParamRemoteContinuousConnect_Object = MibTableColumn
paramRemoteContinuousConnect = _ParamRemoteContinuousConnect_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 16, 1, 26),
    _ParamRemoteContinuousConnect_Type()
)
paramRemoteContinuousConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramRemoteContinuousConnect.setStatus("mandatory")
_ParamRemoteEstablishInterval_Type = Integer32
_ParamRemoteEstablishInterval_Object = MibTableColumn
paramRemoteEstablishInterval = _ParamRemoteEstablishInterval_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 16, 1, 27),
    _ParamRemoteEstablishInterval_Type()
)
paramRemoteEstablishInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramRemoteEstablishInterval.setStatus("mandatory")


class _ParamRemoteOEMType_Type(Integer32):
    """Custom type paramRemoteOEMType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("intelIpmiV2Bmc", 1))
    )


_ParamRemoteOEMType_Type.__name__ = "Integer32"
_ParamRemoteOEMType_Object = MibTableColumn
paramRemoteOEMType = _ParamRemoteOEMType_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 16, 1, 28),
    _ParamRemoteOEMType_Type()
)
paramRemoteOEMType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramRemoteOEMType.setStatus("mandatory")
_ParamRemoteUsername_Type = DisplayString
_ParamRemoteUsername_Object = MibTableColumn
paramRemoteUsername = _ParamRemoteUsername_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 16, 1, 29),
    _ParamRemoteUsername_Type()
)
paramRemoteUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramRemoteUsername.setStatus("mandatory")
_ParamRemotePassword_Type = DisplayString
_ParamRemotePassword_Object = MibTableColumn
paramRemotePassword = _ParamRemotePassword_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 16, 1, 30),
    _ParamRemotePassword_Type()
)
paramRemotePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramRemotePassword.setStatus("mandatory")
_ParamRemoteSupportProtocol_Type = Switch
_ParamRemoteSupportProtocol_Object = MibTableColumn
paramRemoteSupportProtocol = _ParamRemoteSupportProtocol_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 16, 1, 31),
    _ParamRemoteSupportProtocol_Type()
)
paramRemoteSupportProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramRemoteSupportProtocol.setStatus("mandatory")
_ParamRemoteAutomaticLogin_Type = Switch
_ParamRemoteAutomaticLogin_Object = MibTableColumn
paramRemoteAutomaticLogin = _ParamRemoteAutomaticLogin_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 16, 1, 32),
    _ParamRemoteAutomaticLogin_Type()
)
paramRemoteAutomaticLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramRemoteAutomaticLogin.setStatus("mandatory")
_ParamRemoteUseCustomScript_Type = Switch
_ParamRemoteUseCustomScript_Object = MibTableColumn
paramRemoteUseCustomScript = _ParamRemoteUseCustomScript_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 16, 1, 33),
    _ParamRemoteUseCustomScript_Type()
)
paramRemoteUseCustomScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramRemoteUseCustomScript.setStatus("mandatory")
_ParamFlushBuf_Type = Switch
_ParamFlushBuf_Object = MibTableColumn
paramFlushBuf = _ParamFlushBuf_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 16, 1, 34),
    _ParamFlushBuf_Type()
)
paramFlushBuf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramFlushBuf.setStatus("mandatory")
_LoggingTable_Object = MibTable
loggingTable = _LoggingTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 17)
)
if mibBuilder.loadTexts:
    loggingTable.setStatus("mandatory")
_LoggingEntry_Object = MibTableRow
loggingEntry = _LoggingEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 17, 1)
)
loggingEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "loggingIndex"),
)
if mibBuilder.loadTexts:
    loggingEntry.setStatus("mandatory")
_LoggingIndex_Type = Integer32
_LoggingIndex_Object = MibTableColumn
loggingIndex = _LoggingIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 17, 1, 11),
    _LoggingIndex_Type()
)
loggingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingIndex.setStatus("mandatory")
_LoggingEnablePortLogging_Type = Switch
_LoggingEnablePortLogging_Object = MibTableColumn
loggingEnablePortLogging = _LoggingEnablePortLogging_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 17, 1, 12),
    _LoggingEnablePortLogging_Type()
)
loggingEnablePortLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loggingEnablePortLogging.setStatus("mandatory")


class _LoggingOption_Type(Integer32):
    """Custom type loggingOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("deviceoutput", 1),
          ("userinput", 2),
          ("bothwarrow", 3),
          ("bothwoarrow", 4))
    )


_LoggingOption_Type.__name__ = "Integer32"
_LoggingOption_Object = MibTableColumn
loggingOption = _LoggingOption_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 17, 1, 13),
    _LoggingOption_Type()
)
loggingOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loggingOption.setStatus("mandatory")


class _LoggingStoLoc_Type(Integer32):
    """Custom type loggingStoLoc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("memory", 1),
          ("cfcard", 2),
          ("nfs", 3),
          ("usb", 4),
          ("samba", 10))
    )


_LoggingStoLoc_Type.__name__ = "Integer32"
_LoggingStoLoc_Object = MibTableColumn
loggingStoLoc = _LoggingStoLoc_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 17, 1, 14),
    _LoggingStoLoc_Type()
)
loggingStoLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loggingStoLoc.setStatus("mandatory")
_LoggingSyslog_Type = Switch
_LoggingSyslog_Object = MibTableColumn
loggingSyslog = _LoggingSyslog_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 17, 1, 15),
    _LoggingSyslog_Type()
)
loggingSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loggingSyslog.setStatus("mandatory")
_LoggingBufferSize_Type = Integer32
_LoggingBufferSize_Object = MibTableColumn
loggingBufferSize = _LoggingBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 17, 1, 16),
    _LoggingBufferSize_Type()
)
loggingBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loggingBufferSize.setStatus("mandatory")


class _LoggingFileByTitle_Type(Integer32):
    """Custom type loggingFileByTitle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("specifybelow", 0),
          ("useporttitle", 1))
    )


_LoggingFileByTitle_Type.__name__ = "Integer32"
_LoggingFileByTitle_Object = MibTableColumn
loggingFileByTitle = _LoggingFileByTitle_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 17, 1, 17),
    _LoggingFileByTitle_Type()
)
loggingFileByTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loggingFileByTitle.setStatus("mandatory")
_LoggingFilename_Type = DisplayString
_LoggingFilename_Object = MibTableColumn
loggingFilename = _LoggingFilename_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 17, 1, 18),
    _LoggingFilename_Type()
)
loggingFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loggingFilename.setStatus("mandatory")
_LoggingTimeStamp_Type = Switch
_LoggingTimeStamp_Object = MibTableColumn
loggingTimeStamp = _LoggingTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 17, 1, 19),
    _LoggingTimeStamp_Type()
)
loggingTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loggingTimeStamp.setStatus("mandatory")
_LoggingShowOnConn_Type = Switch
_LoggingShowOnConn_Object = MibTableColumn
loggingShowOnConn = _LoggingShowOnConn_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 17, 1, 20),
    _LoggingShowOnConn_Type()
)
loggingShowOnConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loggingShowOnConn.setStatus("mandatory")
_LoggingStringM_Type = Switch
_LoggingStringM_Object = MibTableColumn
loggingStringM = _LoggingStringM_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 17, 1, 21),
    _LoggingStringM_Type()
)
loggingStringM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loggingStringM.setStatus("mandatory")
_LoggingBackupOnMount_Type = Switch
_LoggingBackupOnMount_Object = MibTableColumn
loggingBackupOnMount = _LoggingBackupOnMount_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 17, 1, 22),
    _LoggingBackupOnMount_Type()
)
loggingBackupOnMount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loggingBackupOnMount.setStatus("mandatory")


class _LoggingFacility_Type(Integer32):
    """Custom type loggingFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("local1", 1),
          ("local2", 2),
          ("local3", 3),
          ("local4", 4),
          ("local5", 5),
          ("local6", 6),
          ("local7", 7))
    )


_LoggingFacility_Type.__name__ = "Integer32"
_LoggingFacility_Object = MibTableColumn
loggingFacility = _LoggingFacility_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 17, 1, 23),
    _LoggingFacility_Type()
)
loggingFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loggingFacility.setStatus("mandatory")


class _LoggingCharLength_Type(Integer32):
    """Custom type loggingCharLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 4096),
    )


_LoggingCharLength_Type.__name__ = "Integer32"
_LoggingCharLength_Object = MibTableColumn
loggingCharLength = _LoggingCharLength_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 17, 1, 24),
    _LoggingCharLength_Type()
)
loggingCharLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loggingCharLength.setStatus("mandatory")
_BackupfileNumber_Type = Integer32
_BackupfileNumber_Object = MibTableColumn
backupfileNumber = _BackupfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 17, 1, 25),
    _BackupfileNumber_Type()
)
backupfileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupfileNumber.setStatus("mandatory")
_KeywordsTable_Object = MibTable
keywordsTable = _KeywordsTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18)
)
if mibBuilder.loadTexts:
    keywordsTable.setStatus("mandatory")
_KeywordsEntry_Object = MibTableRow
keywordsEntry = _KeywordsEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1)
)
keywordsEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "keywordsPortIndex"),
    (0, "DIGI-PASSPORT-MIB", "keywordIndex"),
)
if mibBuilder.loadTexts:
    keywordsEntry.setStatus("mandatory")
_KeywordsPortIndex_Type = Integer32
_KeywordsPortIndex_Object = MibTableColumn
keywordsPortIndex = _KeywordsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 11),
    _KeywordsPortIndex_Type()
)
keywordsPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keywordsPortIndex.setStatus("mandatory")
_KeywordIndex_Type = Integer32
_KeywordIndex_Object = MibTableColumn
keywordIndex = _KeywordIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 12),
    _KeywordIndex_Type()
)
keywordIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keywordIndex.setStatus("mandatory")
_KeywordString_Type = DisplayString
_KeywordString_Object = MibTableColumn
keywordString = _KeywordString_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 13),
    _KeywordString_Type()
)
keywordString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keywordString.setStatus("mandatory")
_KeywordMailEnable_Type = Switch
_KeywordMailEnable_Object = MibTableColumn
keywordMailEnable = _KeywordMailEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 14),
    _KeywordMailEnable_Type()
)
keywordMailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keywordMailEnable.setStatus("mandatory")
_KeywordMailTitle_Type = DisplayString
_KeywordMailTitle_Object = MibTableColumn
keywordMailTitle = _KeywordMailTitle_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 15),
    _KeywordMailTitle_Type()
)
keywordMailTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keywordMailTitle.setStatus("mandatory")
_KeywordMailto_Type = DisplayString
_KeywordMailto_Object = MibTableColumn
keywordMailto = _KeywordMailto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 16),
    _KeywordMailto_Type()
)
keywordMailto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keywordMailto.setStatus("mandatory")
_KeywordTrapEnable_Type = Switch
_KeywordTrapEnable_Object = MibTableColumn
keywordTrapEnable = _KeywordTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 17),
    _KeywordTrapEnable_Type()
)
keywordTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keywordTrapEnable.setStatus("mandatory")
_KeywordTrapMsgTitle_Type = DisplayString
_KeywordTrapMsgTitle_Object = MibTableColumn
keywordTrapMsgTitle = _KeywordTrapMsgTitle_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 18),
    _KeywordTrapMsgTitle_Type()
)
keywordTrapMsgTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keywordTrapMsgTitle.setStatus("mandatory")
_KeywordTrapToGlobal_Type = Switch
_KeywordTrapToGlobal_Object = MibTableColumn
keywordTrapToGlobal = _KeywordTrapToGlobal_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 19),
    _KeywordTrapToGlobal_Type()
)
keywordTrapToGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keywordTrapToGlobal.setStatus("mandatory")
_Keyword1stTrapDest_Type = IpAddress
_Keyword1stTrapDest_Object = MibTableColumn
keyword1stTrapDest = _Keyword1stTrapDest_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 20),
    _Keyword1stTrapDest_Type()
)
keyword1stTrapDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyword1stTrapDest.setStatus("mandatory")
_Keyword1stTrapDestComm_Type = DisplayString
_Keyword1stTrapDestComm_Object = MibTableColumn
keyword1stTrapDestComm = _Keyword1stTrapDestComm_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 21),
    _Keyword1stTrapDestComm_Type()
)
keyword1stTrapDestComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyword1stTrapDestComm.setStatus("mandatory")


class _Keyword1stTrapDestVer_Type(Integer32):
    """Custom type keyword1stTrapDestVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 0),
          ("v2c", 1),
          ("v3", 2))
    )


_Keyword1stTrapDestVer_Type.__name__ = "Integer32"
_Keyword1stTrapDestVer_Object = MibTableColumn
keyword1stTrapDestVer = _Keyword1stTrapDestVer_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 22),
    _Keyword1stTrapDestVer_Type()
)
keyword1stTrapDestVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyword1stTrapDestVer.setStatus("mandatory")
_Keyword1stTrapUserName_Type = DisplayString
_Keyword1stTrapUserName_Object = MibTableColumn
keyword1stTrapUserName = _Keyword1stTrapUserName_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 23),
    _Keyword1stTrapUserName_Type()
)
keyword1stTrapUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyword1stTrapUserName.setStatus("mandatory")


class _Keyword1stTrapSecurityLevel_Type(Integer32):
    """Custom type keyword1stTrapSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAuthNoPriv", 0),
          ("authNoPriv", 1),
          ("authPriv", 2))
    )


_Keyword1stTrapSecurityLevel_Type.__name__ = "Integer32"
_Keyword1stTrapSecurityLevel_Object = MibTableColumn
keyword1stTrapSecurityLevel = _Keyword1stTrapSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 24),
    _Keyword1stTrapSecurityLevel_Type()
)
keyword1stTrapSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyword1stTrapSecurityLevel.setStatus("mandatory")


class _Keyword1stTrapAuthProto_Type(Integer32):
    """Custom type keyword1stTrapAuthProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("md5", 0),
          ("sha", 1))
    )


_Keyword1stTrapAuthProto_Type.__name__ = "Integer32"
_Keyword1stTrapAuthProto_Object = MibTableColumn
keyword1stTrapAuthProto = _Keyword1stTrapAuthProto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 25),
    _Keyword1stTrapAuthProto_Type()
)
keyword1stTrapAuthProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyword1stTrapAuthProto.setStatus("mandatory")
_Keyword1stTrapAuthPasswd_Type = DisplayString
_Keyword1stTrapAuthPasswd_Object = MibTableColumn
keyword1stTrapAuthPasswd = _Keyword1stTrapAuthPasswd_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 26),
    _Keyword1stTrapAuthPasswd_Type()
)
keyword1stTrapAuthPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyword1stTrapAuthPasswd.setStatus("mandatory")


class _Keyword1stTrapPrivProto_Type(Integer32):
    """Custom type keyword1stTrapPrivProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("des", 0),
          ("aes", 1))
    )


_Keyword1stTrapPrivProto_Type.__name__ = "Integer32"
_Keyword1stTrapPrivProto_Object = MibTableColumn
keyword1stTrapPrivProto = _Keyword1stTrapPrivProto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 27),
    _Keyword1stTrapPrivProto_Type()
)
keyword1stTrapPrivProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyword1stTrapPrivProto.setStatus("mandatory")
_Keyword1stTrapPrivPasswd_Type = DisplayString
_Keyword1stTrapPrivPasswd_Object = MibTableColumn
keyword1stTrapPrivPasswd = _Keyword1stTrapPrivPasswd_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 28),
    _Keyword1stTrapPrivPasswd_Type()
)
keyword1stTrapPrivPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyword1stTrapPrivPasswd.setStatus("mandatory")
_Keyword1stTrapEngineID_Type = DisplayString
_Keyword1stTrapEngineID_Object = MibTableColumn
keyword1stTrapEngineID = _Keyword1stTrapEngineID_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 29),
    _Keyword1stTrapEngineID_Type()
)
keyword1stTrapEngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyword1stTrapEngineID.setStatus("mandatory")
_Keyword2ndTrapDest_Type = IpAddress
_Keyword2ndTrapDest_Object = MibTableColumn
keyword2ndTrapDest = _Keyword2ndTrapDest_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 30),
    _Keyword2ndTrapDest_Type()
)
keyword2ndTrapDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyword2ndTrapDest.setStatus("mandatory")
_Keyword2ndTrapDestComm_Type = DisplayString
_Keyword2ndTrapDestComm_Object = MibTableColumn
keyword2ndTrapDestComm = _Keyword2ndTrapDestComm_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 31),
    _Keyword2ndTrapDestComm_Type()
)
keyword2ndTrapDestComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyword2ndTrapDestComm.setStatus("mandatory")


class _Keyword2ndTrapDestVer_Type(Integer32):
    """Custom type keyword2ndTrapDestVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 0),
          ("v2c", 1),
          ("v3", 2))
    )


_Keyword2ndTrapDestVer_Type.__name__ = "Integer32"
_Keyword2ndTrapDestVer_Object = MibTableColumn
keyword2ndTrapDestVer = _Keyword2ndTrapDestVer_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 32),
    _Keyword2ndTrapDestVer_Type()
)
keyword2ndTrapDestVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyword2ndTrapDestVer.setStatus("mandatory")
_Keyword2ndTrapUserName_Type = DisplayString
_Keyword2ndTrapUserName_Object = MibTableColumn
keyword2ndTrapUserName = _Keyword2ndTrapUserName_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 33),
    _Keyword2ndTrapUserName_Type()
)
keyword2ndTrapUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyword2ndTrapUserName.setStatus("mandatory")


class _Keyword2ndTrapSecurityLevel_Type(Integer32):
    """Custom type keyword2ndTrapSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAuthNoPriv", 0),
          ("authNoPriv", 1),
          ("authPriv", 2))
    )


_Keyword2ndTrapSecurityLevel_Type.__name__ = "Integer32"
_Keyword2ndTrapSecurityLevel_Object = MibTableColumn
keyword2ndTrapSecurityLevel = _Keyword2ndTrapSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 34),
    _Keyword2ndTrapSecurityLevel_Type()
)
keyword2ndTrapSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyword2ndTrapSecurityLevel.setStatus("mandatory")


class _Keyword2ndTrapAuthProto_Type(Integer32):
    """Custom type keyword2ndTrapAuthProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("md5", 0),
          ("sha", 1))
    )


_Keyword2ndTrapAuthProto_Type.__name__ = "Integer32"
_Keyword2ndTrapAuthProto_Object = MibTableColumn
keyword2ndTrapAuthProto = _Keyword2ndTrapAuthProto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 35),
    _Keyword2ndTrapAuthProto_Type()
)
keyword2ndTrapAuthProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyword2ndTrapAuthProto.setStatus("mandatory")
_Keyword2ndTrapAuthPasswd_Type = DisplayString
_Keyword2ndTrapAuthPasswd_Object = MibTableColumn
keyword2ndTrapAuthPasswd = _Keyword2ndTrapAuthPasswd_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 36),
    _Keyword2ndTrapAuthPasswd_Type()
)
keyword2ndTrapAuthPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyword2ndTrapAuthPasswd.setStatus("mandatory")


class _Keyword2ndTrapPrivProto_Type(Integer32):
    """Custom type keyword2ndTrapPrivProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("des", 0),
          ("aes", 1))
    )


_Keyword2ndTrapPrivProto_Type.__name__ = "Integer32"
_Keyword2ndTrapPrivProto_Object = MibTableColumn
keyword2ndTrapPrivProto = _Keyword2ndTrapPrivProto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 37),
    _Keyword2ndTrapPrivProto_Type()
)
keyword2ndTrapPrivProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyword2ndTrapPrivProto.setStatus("mandatory")
_Keyword2ndTrapPrivPasswd_Type = DisplayString
_Keyword2ndTrapPrivPasswd_Object = MibTableColumn
keyword2ndTrapPrivPasswd = _Keyword2ndTrapPrivPasswd_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 38),
    _Keyword2ndTrapPrivPasswd_Type()
)
keyword2ndTrapPrivPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyword2ndTrapPrivPasswd.setStatus("mandatory")
_Keyword2ndTrapEngineID_Type = DisplayString
_Keyword2ndTrapEngineID_Object = MibTableColumn
keyword2ndTrapEngineID = _Keyword2ndTrapEngineID_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 39),
    _Keyword2ndTrapEngineID_Type()
)
keyword2ndTrapEngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyword2ndTrapEngineID.setStatus("mandatory")
_KeywordCaseSensitive_Type = Switch
_KeywordCaseSensitive_Object = MibTableColumn
keywordCaseSensitive = _KeywordCaseSensitive_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 40),
    _KeywordCaseSensitive_Type()
)
keywordCaseSensitive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keywordCaseSensitive.setStatus("mandatory")
_KeywordAddRow_Type = Action
_KeywordAddRow_Object = MibTableColumn
keywordAddRow = _KeywordAddRow_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 41),
    _KeywordAddRow_Type()
)
keywordAddRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keywordAddRow.setStatus("mandatory")
_KeywordDeleteRow_Type = Action
_KeywordDeleteRow_Object = MibTableColumn
keywordDeleteRow = _KeywordDeleteRow_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 18, 1, 42),
    _KeywordDeleteRow_Type()
)
keywordDeleteRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keywordDeleteRow.setStatus("mandatory")
_AuthTable_Object = MibTable
authTable = _AuthTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 19)
)
if mibBuilder.loadTexts:
    authTable.setStatus("mandatory")
_AuthEntry_Object = MibTableRow
authEntry = _AuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 19, 1)
)
authEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "authIndex"),
)
if mibBuilder.loadTexts:
    authEntry.setStatus("mandatory")
_AuthIndex_Type = Integer32
_AuthIndex_Object = MibTableColumn
authIndex = _AuthIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 19, 1, 11),
    _AuthIndex_Type()
)
authIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authIndex.setStatus("mandatory")


class _AuthMethod_Type(Integer32):
    """Custom type authMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              11,
              12,
              13,
              14,
              21,
              22,
              23,
              24,
              31,
              32,
              33,
              34,
              41,
              42,
              43,
              101)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("local", 1),
          ("radius", 11),
          ("radiuslocal", 12),
          ("localradius", 13),
          ("radiusdownlocal", 14),
          ("tacacs", 21),
          ("tacacslocal", 22),
          ("localtacacs", 23),
          ("tacasdownlocal", 24),
          ("ldap", 31),
          ("ldaplocal", 32),
          ("localldap", 33),
          ("ldapdownlocal", 34),
          ("kerberos", 41),
          ("kerberoslocal", 42),
          ("localkerberos", 43),
          ("custom", 101))
    )


_AuthMethod_Type.__name__ = "Integer32"
_AuthMethod_Object = MibTableColumn
authMethod = _AuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 19, 1, 12),
    _AuthMethod_Type()
)
authMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authMethod.setStatus("mandatory")
_AuthPrimaryIPAddress_Type = DisplayString
_AuthPrimaryIPAddress_Object = MibTableColumn
authPrimaryIPAddress = _AuthPrimaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 19, 1, 13),
    _AuthPrimaryIPAddress_Type()
)
authPrimaryIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authPrimaryIPAddress.setStatus("mandatory")
_AuthSecondaryIPAddress_Type = DisplayString
_AuthSecondaryIPAddress_Object = MibTableColumn
authSecondaryIPAddress = _AuthSecondaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 19, 1, 14),
    _AuthSecondaryIPAddress_Type()
)
authSecondaryIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authSecondaryIPAddress.setStatus("mandatory")
_AuthPrimaryAcctIPAddress_Type = DisplayString
_AuthPrimaryAcctIPAddress_Object = MibTableColumn
authPrimaryAcctIPAddress = _AuthPrimaryAcctIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 19, 1, 15),
    _AuthPrimaryAcctIPAddress_Type()
)
authPrimaryAcctIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authPrimaryAcctIPAddress.setStatus("mandatory")
_AuthSecondaryAcctIPAddress_Type = DisplayString
_AuthSecondaryAcctIPAddress_Object = MibTableColumn
authSecondaryAcctIPAddress = _AuthSecondaryAcctIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 19, 1, 16),
    _AuthSecondaryAcctIPAddress_Type()
)
authSecondaryAcctIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authSecondaryAcctIPAddress.setStatus("mandatory")
_AuthSecret_Type = DisplayString
_AuthSecret_Object = MibTableColumn
authSecret = _AuthSecret_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 19, 1, 17),
    _AuthSecret_Type()
)
authSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authSecret.setStatus("mandatory")
_AuthTimeout_Type = Integer32
_AuthTimeout_Object = MibTableColumn
authTimeout = _AuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 19, 1, 18),
    _AuthTimeout_Type()
)
authTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authTimeout.setStatus("mandatory")
_AuthRetries_Type = Integer32
_AuthRetries_Object = MibTableColumn
authRetries = _AuthRetries_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 19, 1, 19),
    _AuthRetries_Type()
)
authRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authRetries.setStatus("mandatory")
_AuthLDAPSearchBase_Type = DisplayString
_AuthLDAPSearchBase_Object = MibTableColumn
authLDAPSearchBase = _AuthLDAPSearchBase_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 19, 1, 20),
    _AuthLDAPSearchBase_Type()
)
authLDAPSearchBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authLDAPSearchBase.setStatus("mandatory")
_AuthLDAPActiveDirectoryDomain_Type = DisplayString
_AuthLDAPActiveDirectoryDomain_Object = MibTableColumn
authLDAPActiveDirectoryDomain = _AuthLDAPActiveDirectoryDomain_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 19, 1, 21),
    _AuthLDAPActiveDirectoryDomain_Type()
)
authLDAPActiveDirectoryDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authLDAPActiveDirectoryDomain.setStatus("mandatory")
_AuthKRBPrimaryRealm_Type = DisplayString
_AuthKRBPrimaryRealm_Object = MibTableColumn
authKRBPrimaryRealm = _AuthKRBPrimaryRealm_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 19, 1, 22),
    _AuthKRBPrimaryRealm_Type()
)
authKRBPrimaryRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authKRBPrimaryRealm.setStatus("mandatory")
_AuthKRBSecondaryRealm_Type = DisplayString
_AuthKRBSecondaryRealm_Object = MibTableColumn
authKRBSecondaryRealm = _AuthKRBSecondaryRealm_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 19, 1, 23),
    _AuthKRBSecondaryRealm_Type()
)
authKRBSecondaryRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authKRBSecondaryRealm.setStatus("mandatory")
_AuthAuthorService_Type = DisplayString
_AuthAuthorService_Object = MibTableColumn
authAuthorService = _AuthAuthorService_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 19, 1, 24),
    _AuthAuthorService_Type()
)
authAuthorService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authAuthorService.setStatus("mandatory")


class _AuthLdapSecure_Type(Integer32):
    """Custom type authLdapSecure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("starttls", 1))
    )


_AuthLdapSecure_Type.__name__ = "Integer32"
_AuthLdapSecure_Object = MibTableColumn
authLdapSecure = _AuthLdapSecure_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 19, 1, 25),
    _AuthLdapSecure_Type()
)
authLdapSecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authLdapSecure.setStatus("mandatory")
_AuthPPPUser_Type = DisplayString
_AuthPPPUser_Object = MibTableColumn
authPPPUser = _AuthPPPUser_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 19, 1, 26),
    _AuthPPPUser_Type()
)
authPPPUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authPPPUser.setStatus("mandatory")
_UsracctlTable_Object = MibTable
usracctlTable = _UsracctlTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20)
)
if mibBuilder.loadTexts:
    usracctlTable.setStatus("mandatory")
_UsracctlEntry_Object = MibTableRow
usracctlEntry = _UsracctlEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1)
)
usracctlEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "usracctlIndex"),
)
if mibBuilder.loadTexts:
    usracctlEntry.setStatus("mandatory")
_UsracctlIndex_Type = Integer32
_UsracctlIndex_Object = MibTableColumn
usracctlIndex = _UsracctlIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 11),
    _UsracctlIndex_Type()
)
usracctlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usracctlIndex.setStatus("mandatory")


class _UsracctlEveryonePortPerm_Type(Integer32):
    """Custom type usracctlEveryonePortPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("restricted", 0),
          ("permitted", 1))
    )


_UsracctlEveryonePortPerm_Type.__name__ = "Integer32"
_UsracctlEveryonePortPerm_Object = MibTableColumn
usracctlEveryonePortPerm = _UsracctlEveryonePortPerm_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 12),
    _UsracctlEveryonePortPerm_Type()
)
usracctlEveryonePortPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlEveryonePortPerm.setStatus("mandatory")
_UsracctlPortPermittedUsers_Type = DisplayString
_UsracctlPortPermittedUsers_Object = MibTableColumn
usracctlPortPermittedUsers = _UsracctlPortPermittedUsers_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 13),
    _UsracctlPortPermittedUsers_Type()
)
usracctlPortPermittedUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlPortPermittedUsers.setStatus("mandatory")
_UsracctlPortRestrictedUsers_Type = DisplayString
_UsracctlPortRestrictedUsers_Object = MibTableColumn
usracctlPortRestrictedUsers = _UsracctlPortRestrictedUsers_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 14),
    _UsracctlPortRestrictedUsers_Type()
)
usracctlPortRestrictedUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlPortRestrictedUsers.setStatus("mandatory")
_UsracctlPortPermittedLists_Type = DisplayString
_UsracctlPortPermittedLists_Object = MibTableColumn
usracctlPortPermittedLists = _UsracctlPortPermittedLists_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 15),
    _UsracctlPortPermittedLists_Type()
)
usracctlPortPermittedLists.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlPortPermittedLists.setStatus("mandatory")
_UsracctlPortRestrictedLists_Type = DisplayString
_UsracctlPortRestrictedLists_Object = MibTableColumn
usracctlPortRestrictedLists = _UsracctlPortRestrictedLists_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 16),
    _UsracctlPortRestrictedLists_Type()
)
usracctlPortRestrictedLists.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlPortRestrictedLists.setStatus("mandatory")


class _UsracctlEveryoneMonitorPerm_Type(Integer32):
    """Custom type usracctlEveryoneMonitorPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("restricted", 0),
          ("permitted", 1))
    )


_UsracctlEveryoneMonitorPerm_Type.__name__ = "Integer32"
_UsracctlEveryoneMonitorPerm_Object = MibTableColumn
usracctlEveryoneMonitorPerm = _UsracctlEveryoneMonitorPerm_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 17),
    _UsracctlEveryoneMonitorPerm_Type()
)
usracctlEveryoneMonitorPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlEveryoneMonitorPerm.setStatus("mandatory")
_UsracctlMonitorPermittedUsers_Type = DisplayString
_UsracctlMonitorPermittedUsers_Object = MibTableColumn
usracctlMonitorPermittedUsers = _UsracctlMonitorPermittedUsers_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 18),
    _UsracctlMonitorPermittedUsers_Type()
)
usracctlMonitorPermittedUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlMonitorPermittedUsers.setStatus("mandatory")
_UsracctlMonitorRestrictedUsers_Type = DisplayString
_UsracctlMonitorRestrictedUsers_Object = MibTableColumn
usracctlMonitorRestrictedUsers = _UsracctlMonitorRestrictedUsers_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 19),
    _UsracctlMonitorRestrictedUsers_Type()
)
usracctlMonitorRestrictedUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlMonitorRestrictedUsers.setStatus("mandatory")
_UsracctlMonitorPermittedLists_Type = DisplayString
_UsracctlMonitorPermittedLists_Object = MibTableColumn
usracctlMonitorPermittedLists = _UsracctlMonitorPermittedLists_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 20),
    _UsracctlMonitorPermittedLists_Type()
)
usracctlMonitorPermittedLists.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlMonitorPermittedLists.setStatus("mandatory")
_UsracctlMonitorRestrictedLists_Type = DisplayString
_UsracctlMonitorRestrictedLists_Object = MibTableColumn
usracctlMonitorRestrictedLists = _UsracctlMonitorRestrictedLists_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 21),
    _UsracctlMonitorRestrictedLists_Type()
)
usracctlMonitorRestrictedLists.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlMonitorRestrictedLists.setStatus("mandatory")


class _UsracctlEveryonePowerPerm_Type(Integer32):
    """Custom type usracctlEveryonePowerPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("restricted", 0),
          ("permitted", 1))
    )


_UsracctlEveryonePowerPerm_Type.__name__ = "Integer32"
_UsracctlEveryonePowerPerm_Object = MibTableColumn
usracctlEveryonePowerPerm = _UsracctlEveryonePowerPerm_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 22),
    _UsracctlEveryonePowerPerm_Type()
)
usracctlEveryonePowerPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlEveryonePowerPerm.setStatus("mandatory")
_UsracctlPowerPermittedUsers_Type = DisplayString
_UsracctlPowerPermittedUsers_Object = MibTableColumn
usracctlPowerPermittedUsers = _UsracctlPowerPermittedUsers_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 23),
    _UsracctlPowerPermittedUsers_Type()
)
usracctlPowerPermittedUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlPowerPermittedUsers.setStatus("mandatory")
_UsracctlPowerRestrictedUsers_Type = DisplayString
_UsracctlPowerRestrictedUsers_Object = MibTableColumn
usracctlPowerRestrictedUsers = _UsracctlPowerRestrictedUsers_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 24),
    _UsracctlPowerRestrictedUsers_Type()
)
usracctlPowerRestrictedUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlPowerRestrictedUsers.setStatus("mandatory")
_UsracctlPowerPermittedLists_Type = DisplayString
_UsracctlPowerPermittedLists_Object = MibTableColumn
usracctlPowerPermittedLists = _UsracctlPowerPermittedLists_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 25),
    _UsracctlPowerPermittedLists_Type()
)
usracctlPowerPermittedLists.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlPowerPermittedLists.setStatus("mandatory")
_UsracctlPowerRestrictedLists_Type = DisplayString
_UsracctlPowerRestrictedLists_Object = MibTableColumn
usracctlPowerRestrictedLists = _UsracctlPowerRestrictedLists_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 26),
    _UsracctlPowerRestrictedLists_Type()
)
usracctlPowerRestrictedLists.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlPowerRestrictedLists.setStatus("mandatory")
_UsracctlEnableMultipleSession_Type = Switch
_UsracctlEnableMultipleSession_Object = MibTableColumn
usracctlEnableMultipleSession = _UsracctlEnableMultipleSession_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 27),
    _UsracctlEnableMultipleSession_Type()
)
usracctlEnableMultipleSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlEnableMultipleSession.setStatus("mandatory")


class _UsracctlSessionDisplayMode_Type(Integer32):
    """Custom type usracctlSessionDisplayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("serverOutput", 1),
          ("userInput", 2),
          ("both", 3))
    )


_UsracctlSessionDisplayMode_Type.__name__ = "Integer32"
_UsracctlSessionDisplayMode_Object = MibTableColumn
usracctlSessionDisplayMode = _UsracctlSessionDisplayMode_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 28),
    _UsracctlSessionDisplayMode_Type()
)
usracctlSessionDisplayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlSessionDisplayMode.setStatus("mandatory")
_UsracctlSniffDisplayDirectionArrow_Type = Switch
_UsracctlSniffDisplayDirectionArrow_Object = MibTableColumn
usracctlSniffDisplayDirectionArrow = _UsracctlSniffDisplayDirectionArrow_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 29),
    _UsracctlSniffDisplayDirectionArrow_Type()
)
usracctlSniffDisplayDirectionArrow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlSniffDisplayDirectionArrow.setStatus("mandatory")


class _UsracctlEveryoneLogPerm_Type(Integer32):
    """Custom type usracctlEveryoneLogPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("restricted", 0),
          ("permitted", 1))
    )


_UsracctlEveryoneLogPerm_Type.__name__ = "Integer32"
_UsracctlEveryoneLogPerm_Object = MibTableColumn
usracctlEveryoneLogPerm = _UsracctlEveryoneLogPerm_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 30),
    _UsracctlEveryoneLogPerm_Type()
)
usracctlEveryoneLogPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlEveryoneLogPerm.setStatus("mandatory")
_UsracctlLogPermittedUsers_Type = DisplayString
_UsracctlLogPermittedUsers_Object = MibTableColumn
usracctlLogPermittedUsers = _UsracctlLogPermittedUsers_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 31),
    _UsracctlLogPermittedUsers_Type()
)
usracctlLogPermittedUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlLogPermittedUsers.setStatus("mandatory")
_UsracctlLogRestrictedUsers_Type = DisplayString
_UsracctlLogRestrictedUsers_Object = MibTableColumn
usracctlLogRestrictedUsers = _UsracctlLogRestrictedUsers_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 32),
    _UsracctlLogRestrictedUsers_Type()
)
usracctlLogRestrictedUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlLogRestrictedUsers.setStatus("mandatory")
_UsracctlLogPermittedLists_Type = DisplayString
_UsracctlLogPermittedLists_Object = MibTableColumn
usracctlLogPermittedLists = _UsracctlLogPermittedLists_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 33),
    _UsracctlLogPermittedLists_Type()
)
usracctlLogPermittedLists.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlLogPermittedLists.setStatus("mandatory")
_UsracctlLogRestrictedLists_Type = DisplayString
_UsracctlLogRestrictedLists_Object = MibTableColumn
usracctlLogRestrictedLists = _UsracctlLogRestrictedLists_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 34),
    _UsracctlLogRestrictedLists_Type()
)
usracctlLogRestrictedLists.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlLogRestrictedLists.setStatus("mandatory")


class _UsracctlEveryoneBreakPerm_Type(Integer32):
    """Custom type usracctlEveryoneBreakPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("restricted", 0),
          ("permitted", 1))
    )


_UsracctlEveryoneBreakPerm_Type.__name__ = "Integer32"
_UsracctlEveryoneBreakPerm_Object = MibTableColumn
usracctlEveryoneBreakPerm = _UsracctlEveryoneBreakPerm_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 35),
    _UsracctlEveryoneBreakPerm_Type()
)
usracctlEveryoneBreakPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlEveryoneBreakPerm.setStatus("mandatory")
_UsracctlBreakPermittedUsers_Type = DisplayString
_UsracctlBreakPermittedUsers_Object = MibTableColumn
usracctlBreakPermittedUsers = _UsracctlBreakPermittedUsers_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 36),
    _UsracctlBreakPermittedUsers_Type()
)
usracctlBreakPermittedUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlBreakPermittedUsers.setStatus("mandatory")
_UsracctlBreakRestrictedUsers_Type = DisplayString
_UsracctlBreakRestrictedUsers_Object = MibTableColumn
usracctlBreakRestrictedUsers = _UsracctlBreakRestrictedUsers_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 37),
    _UsracctlBreakRestrictedUsers_Type()
)
usracctlBreakRestrictedUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlBreakRestrictedUsers.setStatus("mandatory")
_UsracctlBreakPermittedLists_Type = DisplayString
_UsracctlBreakPermittedLists_Object = MibTableColumn
usracctlBreakPermittedLists = _UsracctlBreakPermittedLists_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 38),
    _UsracctlBreakPermittedLists_Type()
)
usracctlBreakPermittedLists.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlBreakPermittedLists.setStatus("mandatory")
_UsracctlBreakRestrictedLists_Type = DisplayString
_UsracctlBreakRestrictedLists_Object = MibTableColumn
usracctlBreakRestrictedLists = _UsracctlBreakRestrictedLists_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 20, 1, 39),
    _UsracctlBreakRestrictedLists_Type()
)
usracctlBreakRestrictedLists.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usracctlBreakRestrictedLists.setStatus("mandatory")
_AlertTable_Object = MibTable
alertTable = _AlertTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21)
)
if mibBuilder.loadTexts:
    alertTable.setStatus("mandatory")
_AlertEntry_Object = MibTableRow
alertEntry = _AlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1)
)
alertEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "alertIndex"),
)
if mibBuilder.loadTexts:
    alertEntry.setStatus("mandatory")
_AlertIndex_Type = Integer32
_AlertIndex_Object = MibTableColumn
alertIndex = _AlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 11),
    _AlertIndex_Type()
)
alertIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertIndex.setStatus("mandatory")
_AlertLoginMail_Type = Switch
_AlertLoginMail_Object = MibTableColumn
alertLoginMail = _AlertLoginMail_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 12),
    _AlertLoginMail_Type()
)
alertLoginMail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertLoginMail.setStatus("mandatory")
_AlertLoginMailTitle_Type = DisplayString
_AlertLoginMailTitle_Object = MibTableColumn
alertLoginMailTitle = _AlertLoginMailTitle_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 13),
    _AlertLoginMailTitle_Type()
)
alertLoginMailTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertLoginMailTitle.setStatus("mandatory")
_AlertLoginMailto_Type = DisplayString
_AlertLoginMailto_Object = MibTableColumn
alertLoginMailto = _AlertLoginMailto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 14),
    _AlertLoginMailto_Type()
)
alertLoginMailto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertLoginMailto.setStatus("mandatory")
_AlertDevConnMail_Type = Switch
_AlertDevConnMail_Object = MibTableColumn
alertDevConnMail = _AlertDevConnMail_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 15),
    _AlertDevConnMail_Type()
)
alertDevConnMail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertDevConnMail.setStatus("mandatory")
_AlertDevConnMailTitle_Type = DisplayString
_AlertDevConnMailTitle_Object = MibTableColumn
alertDevConnMailTitle = _AlertDevConnMailTitle_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 16),
    _AlertDevConnMailTitle_Type()
)
alertDevConnMailTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertDevConnMailTitle.setStatus("mandatory")
_AlertDevConnMailto_Type = DisplayString
_AlertDevConnMailto_Object = MibTableColumn
alertDevConnMailto = _AlertDevConnMailto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 17),
    _AlertDevConnMailto_Type()
)
alertDevConnMailto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertDevConnMailto.setStatus("mandatory")
_AlertDetectionMail_Type = Switch
_AlertDetectionMail_Object = MibTableColumn
alertDetectionMail = _AlertDetectionMail_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 18),
    _AlertDetectionMail_Type()
)
alertDetectionMail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertDetectionMail.setStatus("mandatory")
_AlertDetectionMailTitle_Type = DisplayString
_AlertDetectionMailTitle_Object = MibTableColumn
alertDetectionMailTitle = _AlertDetectionMailTitle_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 19),
    _AlertDetectionMailTitle_Type()
)
alertDetectionMailTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertDetectionMailTitle.setStatus("mandatory")
_AlertDetectionMailto_Type = DisplayString
_AlertDetectionMailto_Object = MibTableColumn
alertDetectionMailto = _AlertDetectionMailto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 20),
    _AlertDetectionMailto_Type()
)
alertDetectionMailto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertDetectionMailto.setStatus("mandatory")
_AlertModemTestMail_Type = Switch
_AlertModemTestMail_Object = MibTableColumn
alertModemTestMail = _AlertModemTestMail_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 21),
    _AlertModemTestMail_Type()
)
alertModemTestMail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertModemTestMail.setStatus("mandatory")
_AlertModemTestMailTitle_Type = DisplayString
_AlertModemTestMailTitle_Object = MibTableColumn
alertModemTestMailTitle = _AlertModemTestMailTitle_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 22),
    _AlertModemTestMailTitle_Type()
)
alertModemTestMailTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertModemTestMailTitle.setStatus("mandatory")
_AlertModemTestMailto_Type = DisplayString
_AlertModemTestMailto_Object = MibTableColumn
alertModemTestMailto = _AlertModemTestMailto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 23),
    _AlertModemTestMailto_Type()
)
alertModemTestMailto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertModemTestMailto.setStatus("mandatory")
_AlertIPMIMail_Type = Switch
_AlertIPMIMail_Object = MibTableColumn
alertIPMIMail = _AlertIPMIMail_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 24),
    _AlertIPMIMail_Type()
)
alertIPMIMail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertIPMIMail.setStatus("mandatory")
_AlertIPMIMailTitle_Type = DisplayString
_AlertIPMIMailTitle_Object = MibTableColumn
alertIPMIMailTitle = _AlertIPMIMailTitle_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 25),
    _AlertIPMIMailTitle_Type()
)
alertIPMIMailTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertIPMIMailTitle.setStatus("mandatory")
_AlertIPMIMailto_Type = DisplayString
_AlertIPMIMailto_Object = MibTableColumn
alertIPMIMailto = _AlertIPMIMailto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 26),
    _AlertIPMIMailto_Type()
)
alertIPMIMailto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertIPMIMailto.setStatus("mandatory")
_AlertLoginTrap_Type = Switch
_AlertLoginTrap_Object = MibTableColumn
alertLoginTrap = _AlertLoginTrap_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 27),
    _AlertLoginTrap_Type()
)
alertLoginTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertLoginTrap.setStatus("mandatory")
_AlertDevConnTrap_Type = Switch
_AlertDevConnTrap_Object = MibTableColumn
alertDevConnTrap = _AlertDevConnTrap_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 28),
    _AlertDevConnTrap_Type()
)
alertDevConnTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertDevConnTrap.setStatus("mandatory")
_AlertDetectionTrap_Type = Switch
_AlertDetectionTrap_Object = MibTableColumn
alertDetectionTrap = _AlertDetectionTrap_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 29),
    _AlertDetectionTrap_Type()
)
alertDetectionTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertDetectionTrap.setStatus("mandatory")
_AlertModemTestTrap_Type = Switch
_AlertModemTestTrap_Object = MibTableColumn
alertModemTestTrap = _AlertModemTestTrap_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 30),
    _AlertModemTestTrap_Type()
)
alertModemTestTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertModemTestTrap.setStatus("mandatory")
_AlertIPMITrap_Type = Switch
_AlertIPMITrap_Object = MibTableColumn
alertIPMITrap = _AlertIPMITrap_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 31),
    _AlertIPMITrap_Type()
)
alertIPMITrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertIPMITrap.setStatus("mandatory")
_AlertToGlobalSNMP_Type = Switch
_AlertToGlobalSNMP_Object = MibTableColumn
alertToGlobalSNMP = _AlertToGlobalSNMP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 32),
    _AlertToGlobalSNMP_Type()
)
alertToGlobalSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertToGlobalSNMP.setStatus("mandatory")
_Alert1stTrapRcvIP_Type = DisplayString
_Alert1stTrapRcvIP_Object = MibTableColumn
alert1stTrapRcvIP = _Alert1stTrapRcvIP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 33),
    _Alert1stTrapRcvIP_Type()
)
alert1stTrapRcvIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alert1stTrapRcvIP.setStatus("mandatory")
_Alert1stTrapRcvComm_Type = DisplayString
_Alert1stTrapRcvComm_Object = MibTableColumn
alert1stTrapRcvComm = _Alert1stTrapRcvComm_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 34),
    _Alert1stTrapRcvComm_Type()
)
alert1stTrapRcvComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alert1stTrapRcvComm.setStatus("mandatory")


class _Alert1stTrapRcvVer_Type(Integer32):
    """Custom type alert1stTrapRcvVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 0),
          ("v2c", 1),
          ("v3", 2))
    )


_Alert1stTrapRcvVer_Type.__name__ = "Integer32"
_Alert1stTrapRcvVer_Object = MibTableColumn
alert1stTrapRcvVer = _Alert1stTrapRcvVer_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 35),
    _Alert1stTrapRcvVer_Type()
)
alert1stTrapRcvVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alert1stTrapRcvVer.setStatus("mandatory")
_Alert1stTrapRcvUserName_Type = DisplayString
_Alert1stTrapRcvUserName_Object = MibTableColumn
alert1stTrapRcvUserName = _Alert1stTrapRcvUserName_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 36),
    _Alert1stTrapRcvUserName_Type()
)
alert1stTrapRcvUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alert1stTrapRcvUserName.setStatus("mandatory")


class _Alert1stTrapRcvSecurityLevel_Type(Integer32):
    """Custom type alert1stTrapRcvSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAuthNoPriv", 0),
          ("authNoPriv", 1),
          ("authPriv", 2))
    )


_Alert1stTrapRcvSecurityLevel_Type.__name__ = "Integer32"
_Alert1stTrapRcvSecurityLevel_Object = MibTableColumn
alert1stTrapRcvSecurityLevel = _Alert1stTrapRcvSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 37),
    _Alert1stTrapRcvSecurityLevel_Type()
)
alert1stTrapRcvSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alert1stTrapRcvSecurityLevel.setStatus("mandatory")


class _Alert1stTrapRcvAuthProto_Type(Integer32):
    """Custom type alert1stTrapRcvAuthProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("md5", 0),
          ("sha", 1))
    )


_Alert1stTrapRcvAuthProto_Type.__name__ = "Integer32"
_Alert1stTrapRcvAuthProto_Object = MibTableColumn
alert1stTrapRcvAuthProto = _Alert1stTrapRcvAuthProto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 38),
    _Alert1stTrapRcvAuthProto_Type()
)
alert1stTrapRcvAuthProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alert1stTrapRcvAuthProto.setStatus("mandatory")
_Alert1stTrapRcvAuthPasswd_Type = DisplayString
_Alert1stTrapRcvAuthPasswd_Object = MibTableColumn
alert1stTrapRcvAuthPasswd = _Alert1stTrapRcvAuthPasswd_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 39),
    _Alert1stTrapRcvAuthPasswd_Type()
)
alert1stTrapRcvAuthPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alert1stTrapRcvAuthPasswd.setStatus("mandatory")


class _Alert1stTrapRcvPrivProto_Type(Integer32):
    """Custom type alert1stTrapRcvPrivProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("des", 0),
          ("aes", 1))
    )


_Alert1stTrapRcvPrivProto_Type.__name__ = "Integer32"
_Alert1stTrapRcvPrivProto_Object = MibTableColumn
alert1stTrapRcvPrivProto = _Alert1stTrapRcvPrivProto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 40),
    _Alert1stTrapRcvPrivProto_Type()
)
alert1stTrapRcvPrivProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alert1stTrapRcvPrivProto.setStatus("mandatory")
_Alert1stTrapRcvPrivPasswd_Type = DisplayString
_Alert1stTrapRcvPrivPasswd_Object = MibTableColumn
alert1stTrapRcvPrivPasswd = _Alert1stTrapRcvPrivPasswd_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 41),
    _Alert1stTrapRcvPrivPasswd_Type()
)
alert1stTrapRcvPrivPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alert1stTrapRcvPrivPasswd.setStatus("mandatory")
_Alert1stTrapRcvEngineID_Type = DisplayString
_Alert1stTrapRcvEngineID_Object = MibTableColumn
alert1stTrapRcvEngineID = _Alert1stTrapRcvEngineID_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 42),
    _Alert1stTrapRcvEngineID_Type()
)
alert1stTrapRcvEngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alert1stTrapRcvEngineID.setStatus("mandatory")
_Alert2ndTrapRcvIP_Type = DisplayString
_Alert2ndTrapRcvIP_Object = MibTableColumn
alert2ndTrapRcvIP = _Alert2ndTrapRcvIP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 43),
    _Alert2ndTrapRcvIP_Type()
)
alert2ndTrapRcvIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alert2ndTrapRcvIP.setStatus("mandatory")
_Alert2ndTrapRcvComm_Type = DisplayString
_Alert2ndTrapRcvComm_Object = MibTableColumn
alert2ndTrapRcvComm = _Alert2ndTrapRcvComm_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 44),
    _Alert2ndTrapRcvComm_Type()
)
alert2ndTrapRcvComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alert2ndTrapRcvComm.setStatus("mandatory")


class _Alert2ndTrapRcvVer_Type(Integer32):
    """Custom type alert2ndTrapRcvVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 0),
          ("v2c", 1),
          ("v3", 2))
    )


_Alert2ndTrapRcvVer_Type.__name__ = "Integer32"
_Alert2ndTrapRcvVer_Object = MibTableColumn
alert2ndTrapRcvVer = _Alert2ndTrapRcvVer_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 45),
    _Alert2ndTrapRcvVer_Type()
)
alert2ndTrapRcvVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alert2ndTrapRcvVer.setStatus("mandatory")
_Alert2ndTrapRcvUserName_Type = DisplayString
_Alert2ndTrapRcvUserName_Object = MibTableColumn
alert2ndTrapRcvUserName = _Alert2ndTrapRcvUserName_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 46),
    _Alert2ndTrapRcvUserName_Type()
)
alert2ndTrapRcvUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alert2ndTrapRcvUserName.setStatus("mandatory")


class _Alert2ndTrapRcvSecurityLevel_Type(Integer32):
    """Custom type alert2ndTrapRcvSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAuthNoPriv", 0),
          ("authNoPriv", 1),
          ("authPriv", 2))
    )


_Alert2ndTrapRcvSecurityLevel_Type.__name__ = "Integer32"
_Alert2ndTrapRcvSecurityLevel_Object = MibTableColumn
alert2ndTrapRcvSecurityLevel = _Alert2ndTrapRcvSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 47),
    _Alert2ndTrapRcvSecurityLevel_Type()
)
alert2ndTrapRcvSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alert2ndTrapRcvSecurityLevel.setStatus("mandatory")


class _Alert2ndTrapRcvAuthProto_Type(Integer32):
    """Custom type alert2ndTrapRcvAuthProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("md5", 0),
          ("sha", 1))
    )


_Alert2ndTrapRcvAuthProto_Type.__name__ = "Integer32"
_Alert2ndTrapRcvAuthProto_Object = MibTableColumn
alert2ndTrapRcvAuthProto = _Alert2ndTrapRcvAuthProto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 48),
    _Alert2ndTrapRcvAuthProto_Type()
)
alert2ndTrapRcvAuthProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alert2ndTrapRcvAuthProto.setStatus("mandatory")
_Alert2ndTrapRcvAuthPasswd_Type = DisplayString
_Alert2ndTrapRcvAuthPasswd_Object = MibTableColumn
alert2ndTrapRcvAuthPasswd = _Alert2ndTrapRcvAuthPasswd_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 49),
    _Alert2ndTrapRcvAuthPasswd_Type()
)
alert2ndTrapRcvAuthPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alert2ndTrapRcvAuthPasswd.setStatus("mandatory")


class _Alert2ndTrapRcvPrivProto_Type(Integer32):
    """Custom type alert2ndTrapRcvPrivProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("des", 0),
          ("aes", 1))
    )


_Alert2ndTrapRcvPrivProto_Type.__name__ = "Integer32"
_Alert2ndTrapRcvPrivProto_Object = MibTableColumn
alert2ndTrapRcvPrivProto = _Alert2ndTrapRcvPrivProto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 50),
    _Alert2ndTrapRcvPrivProto_Type()
)
alert2ndTrapRcvPrivProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alert2ndTrapRcvPrivProto.setStatus("mandatory")
_Alert2ndTrapRcvPrivPasswd_Type = DisplayString
_Alert2ndTrapRcvPrivPasswd_Object = MibTableColumn
alert2ndTrapRcvPrivPasswd = _Alert2ndTrapRcvPrivPasswd_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 51),
    _Alert2ndTrapRcvPrivPasswd_Type()
)
alert2ndTrapRcvPrivPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alert2ndTrapRcvPrivPasswd.setStatus("mandatory")
_Alert2ndTrapRcvEngineID_Type = DisplayString
_Alert2ndTrapRcvEngineID_Object = MibTableColumn
alert2ndTrapRcvEngineID = _Alert2ndTrapRcvEngineID_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 21, 1, 52),
    _Alert2ndTrapRcvEngineID_Type()
)
alert2ndTrapRcvEngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alert2ndTrapRcvEngineID.setStatus("mandatory")
_PowerTable_Object = MibTable
powerTable = _PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 22)
)
if mibBuilder.loadTexts:
    powerTable.setStatus("mandatory")
_PowerEntry_Object = MibTableRow
powerEntry = _PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 22, 1)
)
powerEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "powerIndex"),
)
if mibBuilder.loadTexts:
    powerEntry.setStatus("mandatory")
_PowerIndex_Type = Integer32
_PowerIndex_Object = MibTableColumn
powerIndex = _PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 22, 1, 11),
    _PowerIndex_Type()
)
powerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerIndex.setStatus("mandatory")


class _PowerStatus_Type(Integer32):
    """Custom type powerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("powered-on", 1),
          ("powered-off", 2),
          ("reboot", 3),
          ("turning-on", 4),
          ("turning-off", 5),
          ("rebooting", 6))
    )


_PowerStatus_Type.__name__ = "Integer32"
_PowerStatus_Object = MibTableColumn
powerStatus = _PowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 22, 1, 12),
    _PowerStatus_Type()
)
powerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStatus.setStatus("mandatory")


class _PowerControl_Type(Integer32):
    """Custom type powerControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("power-on", 2),
          ("power-off", 3),
          ("reboot", 4))
    )


_PowerControl_Type.__name__ = "Integer32"
_PowerControl_Object = MibTableColumn
powerControl = _PowerControl_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 22, 1, 13),
    _PowerControl_Type()
)
powerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerControl.setStatus("mandatory")
_IpmiConfigTable_Object = MibTable
ipmiConfigTable = _IpmiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 23)
)
if mibBuilder.loadTexts:
    ipmiConfigTable.setStatus("mandatory")
_IpmiConfigEntry_Object = MibTableRow
ipmiConfigEntry = _IpmiConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 23, 1)
)
ipmiConfigEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "ipmiConfigIndex"),
)
if mibBuilder.loadTexts:
    ipmiConfigEntry.setStatus("mandatory")
_IpmiConfigIndex_Type = Integer32
_IpmiConfigIndex_Object = MibTableColumn
ipmiConfigIndex = _IpmiConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 23, 1, 11),
    _IpmiConfigIndex_Type()
)
ipmiConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmiConfigIndex.setStatus("mandatory")
_IpmiConfigUserName_Type = DisplayString
_IpmiConfigUserName_Object = MibTableColumn
ipmiConfigUserName = _IpmiConfigUserName_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 23, 1, 12),
    _IpmiConfigUserName_Type()
)
ipmiConfigUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmiConfigUserName.setStatus("mandatory")
_IpmiConfigPassword_Type = DisplayString
_IpmiConfigPassword_Object = MibTableColumn
ipmiConfigPassword = _IpmiConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 23, 1, 13),
    _IpmiConfigPassword_Type()
)
ipmiConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmiConfigPassword.setStatus("mandatory")


class _IpmiConfigOEMType_Type(Integer32):
    """Custom type ipmiConfigOEMType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("intelIpmiV2Bmc", 1))
    )


_IpmiConfigOEMType_Type.__name__ = "Integer32"
_IpmiConfigOEMType_Object = MibTableColumn
ipmiConfigOEMType = _IpmiConfigOEMType_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 23, 1, 14),
    _IpmiConfigOEMType_Type()
)
ipmiConfigOEMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmiConfigOEMType.setStatus("mandatory")
_IpmiSensorTable_Object = MibTable
ipmiSensorTable = _IpmiSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 24)
)
if mibBuilder.loadTexts:
    ipmiSensorTable.setStatus("mandatory")
_IpmiSensorEntry_Object = MibTableRow
ipmiSensorEntry = _IpmiSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 24, 1)
)
ipmiSensorEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "ipmiPortIndex"),
    (0, "DIGI-PASSPORT-MIB", "ipmiSensorIndex"),
)
if mibBuilder.loadTexts:
    ipmiSensorEntry.setStatus("mandatory")
_IpmiPortIndex_Type = Integer32
_IpmiPortIndex_Object = MibTableColumn
ipmiPortIndex = _IpmiPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 24, 1, 11),
    _IpmiPortIndex_Type()
)
ipmiPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmiPortIndex.setStatus("mandatory")
_IpmiSensorIndex_Type = Integer32
_IpmiSensorIndex_Object = MibTableColumn
ipmiSensorIndex = _IpmiSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 24, 1, 12),
    _IpmiSensorIndex_Type()
)
ipmiSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmiSensorIndex.setStatus("mandatory")
_IpmiSensorType_Type = DisplayString
_IpmiSensorType_Object = MibTableColumn
ipmiSensorType = _IpmiSensorType_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 24, 1, 13),
    _IpmiSensorType_Type()
)
ipmiSensorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmiSensorType.setStatus("mandatory")
_IpmiSensorEmailAlert_Type = Switch
_IpmiSensorEmailAlert_Object = MibTableColumn
ipmiSensorEmailAlert = _IpmiSensorEmailAlert_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 24, 1, 14),
    _IpmiSensorEmailAlert_Type()
)
ipmiSensorEmailAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmiSensorEmailAlert.setStatus("mandatory")
_IpmiSensorSNMPAlert_Type = Switch
_IpmiSensorSNMPAlert_Object = MibTableColumn
ipmiSensorSNMPAlert = _IpmiSensorSNMPAlert_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 24, 1, 15),
    _IpmiSensorSNMPAlert_Type()
)
ipmiSensorSNMPAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmiSensorSNMPAlert.setStatus("mandatory")
_IpmiSensorAddRow_Type = Action
_IpmiSensorAddRow_Object = MibTableColumn
ipmiSensorAddRow = _IpmiSensorAddRow_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 24, 1, 16),
    _IpmiSensorAddRow_Type()
)
ipmiSensorAddRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmiSensorAddRow.setStatus("mandatory")
_IpmiSensorDeleteRow_Type = Action
_IpmiSensorDeleteRow_Object = MibTableColumn
ipmiSensorDeleteRow = _IpmiSensorDeleteRow_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 24, 1, 17),
    _IpmiSensorDeleteRow_Type()
)
ipmiSensorDeleteRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmiSensorDeleteRow.setStatus("mandatory")
_PortsStatTable_Object = MibTable
portsStatTable = _PortsStatTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 25)
)
if mibBuilder.loadTexts:
    portsStatTable.setStatus("mandatory")
_PortsStatEntry_Object = MibTableRow
portsStatEntry = _PortsStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 25, 1)
)
portsStatEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "portsStatIndex"),
)
if mibBuilder.loadTexts:
    portsStatEntry.setStatus("mandatory")


class _PortsStatIndex_Type(Integer32):
    """Custom type portsStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_PortsStatIndex_Type.__name__ = "Integer32"
_PortsStatIndex_Object = MibTableColumn
portsStatIndex = _PortsStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 25, 1, 11),
    _PortsStatIndex_Type()
)
portsStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsStatIndex.setStatus("mandatory")
_PortsStatBaudRate_Type = Integer32
_PortsStatBaudRate_Object = MibTableColumn
portsStatBaudRate = _PortsStatBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 25, 1, 12),
    _PortsStatBaudRate_Type()
)
portsStatBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsStatBaudRate.setStatus("mandatory")
_PortsStatTx_Type = Integer32
_PortsStatTx_Object = MibTableColumn
portsStatTx = _PortsStatTx_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 25, 1, 13),
    _PortsStatTx_Type()
)
portsStatTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsStatTx.setStatus("mandatory")
_PortsStatRx_Type = Integer32
_PortsStatRx_Object = MibTableColumn
portsStatRx = _PortsStatRx_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 25, 1, 14),
    _PortsStatRx_Type()
)
portsStatRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsStatRx.setStatus("mandatory")
_PortsStatRTS_Type = Switch
_PortsStatRTS_Object = MibTableColumn
portsStatRTS = _PortsStatRTS_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 25, 1, 15),
    _PortsStatRTS_Type()
)
portsStatRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsStatRTS.setStatus("mandatory")
_PortsStatCTS_Type = Switch
_PortsStatCTS_Object = MibTableColumn
portsStatCTS = _PortsStatCTS_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 25, 1, 16),
    _PortsStatCTS_Type()
)
portsStatCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsStatCTS.setStatus("mandatory")
_PortsStatDTR_Type = Switch
_PortsStatDTR_Object = MibTableColumn
portsStatDTR = _PortsStatDTR_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 25, 1, 17),
    _PortsStatDTR_Type()
)
portsStatDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsStatDTR.setStatus("mandatory")
_PortsStatDSR_Type = Switch
_PortsStatDSR_Object = MibTableColumn
portsStatDSR = _PortsStatDSR_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 25, 1, 18),
    _PortsStatDSR_Type()
)
portsStatDSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsStatDSR.setStatus("mandatory")
_PortsStatCD_Type = Switch
_PortsStatCD_Object = MibTableColumn
portsStatCD = _PortsStatCD_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 25, 1, 19),
    _PortsStatCD_Type()
)
portsStatCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsStatCD.setStatus("mandatory")


class _PortsStatOper_Type(Integer32):
    """Custom type portsStatOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2),
          ("busy", 3))
    )


_PortsStatOper_Type.__name__ = "Integer32"
_PortsStatOper_Object = MibTableColumn
portsStatOper = _PortsStatOper_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 25, 1, 20),
    _PortsStatOper_Type()
)
portsStatOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsStatOper.setStatus("mandatory")
_InstantPortsParamTable_Object = MibTable
instantPortsParamTable = _InstantPortsParamTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 26)
)
if mibBuilder.loadTexts:
    instantPortsParamTable.setStatus("mandatory")
_InstantPortsParamEntry_Object = MibTableRow
instantPortsParamEntry = _InstantPortsParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 26, 1)
)
instantPortsParamEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "instantPortsParamIndex"),
)
if mibBuilder.loadTexts:
    instantPortsParamEntry.setStatus("mandatory")
_InstantPortsParamIndex_Type = Integer32
_InstantPortsParamIndex_Object = MibTableColumn
instantPortsParamIndex = _InstantPortsParamIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 26, 1, 11),
    _InstantPortsParamIndex_Type()
)
instantPortsParamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instantPortsParamIndex.setStatus("mandatory")
_InstantPortsParamString_Type = DisplayString
_InstantPortsParamString_Object = MibTableColumn
instantPortsParamString = _InstantPortsParamString_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 25, 26, 1, 12),
    _InstantPortsParamString_Type()
)
instantPortsParamString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    instantPortsParamString.setStatus("mandatory")
_Peripheral_ObjectIdentity = ObjectIdentity
peripheral = _Peripheral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26)
)
_Pccard_ObjectIdentity = ObjectIdentity
pccard = _Pccard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11)
)


class _PccardType_Type(Integer32):
    """Custom type pccardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", -1),
          ("empty", 0),
          ("flashmemory", 1),
          ("network", 2),
          ("wirelessnet", 3),
          ("modem", 4))
    )


_PccardType_Type.__name__ = "Integer32"
_PccardType_Object = MibScalar
pccardType = _PccardType_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 11),
    _PccardType_Type()
)
pccardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pccardType.setStatus("mandatory")


class _PccardIpmode_Type(Integer32):
    """Custom type pccardIpmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("staticip", 1),
          ("dhcp", 2))
    )


_PccardIpmode_Type.__name__ = "Integer32"
_PccardIpmode_Object = MibScalar
pccardIpmode = _PccardIpmode_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 12),
    _PccardIpmode_Type()
)
pccardIpmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardIpmode.setStatus("mandatory")
_PccardIpAddress_Type = IpAddress
_PccardIpAddress_Object = MibScalar
pccardIpAddress = _PccardIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 13),
    _PccardIpAddress_Type()
)
pccardIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardIpAddress.setStatus("mandatory")
_PccardSubnet_Type = IpAddress
_PccardSubnet_Object = MibScalar
pccardSubnet = _PccardSubnet_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 14),
    _PccardSubnet_Type()
)
pccardSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardSubnet.setStatus("mandatory")
_PccardGateway_Type = IpAddress
_PccardGateway_Object = MibScalar
pccardGateway = _PccardGateway_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 15),
    _PccardGateway_Type()
)
pccardGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardGateway.setStatus("mandatory")
_PccardSSID_Type = DisplayString
_PccardSSID_Object = MibScalar
pccardSSID = _PccardSSID_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 16),
    _PccardSSID_Type()
)
pccardSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardSSID.setStatus("mandatory")
_PccardWEPEnable_Type = Switch
_PccardWEPEnable_Object = MibScalar
pccardWEPEnable = _PccardWEPEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 17),
    _PccardWEPEnable_Type()
)
pccardWEPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardWEPEnable.setStatus("mandatory")


class _PccardWEPMode_Type(Integer32):
    """Custom type pccardWEPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("encrypt", 1),
          ("shared", 2))
    )


_PccardWEPMode_Type.__name__ = "Integer32"
_PccardWEPMode_Object = MibScalar
pccardWEPMode = _PccardWEPMode_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 18),
    _PccardWEPMode_Type()
)
pccardWEPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardWEPMode.setStatus("mandatory")


class _PccardWEPLength_Type(Integer32):
    """Custom type pccardWEPLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("b40", 1),
          ("b128", 2))
    )


_PccardWEPLength_Type.__name__ = "Integer32"
_PccardWEPLength_Object = MibScalar
pccardWEPLength = _PccardWEPLength_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 19),
    _PccardWEPLength_Type()
)
pccardWEPLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardWEPLength.setStatus("mandatory")
_PccardWEPKeyStr_Type = DisplayString
_PccardWEPKeyStr_Object = MibScalar
pccardWEPKeyStr = _PccardWEPKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 20),
    _PccardWEPKeyStr_Type()
)
pccardWEPKeyStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardWEPKeyStr.setStatus("mandatory")
_PccardModemInitStr_Type = DisplayString
_PccardModemInitStr_Object = MibScalar
pccardModemInitStr = _PccardModemInitStr_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 21),
    _PccardModemInitStr_Type()
)
pccardModemInitStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardModemInitStr.setStatus("mandatory")
_PccardModemCallback_Type = Switch
_PccardModemCallback_Object = MibScalar
pccardModemCallback = _PccardModemCallback_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 22),
    _PccardModemCallback_Type()
)
pccardModemCallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardModemCallback.setStatus("mandatory")
_PccardModemCallbackNumber_Type = DisplayString
_PccardModemCallbackNumber_Object = MibScalar
pccardModemCallbackNumber = _PccardModemCallbackNumber_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 23),
    _PccardModemCallbackNumber_Type()
)
pccardModemCallbackNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardModemCallbackNumber.setStatus("mandatory")
_PccardModemTestEnable_Type = Switch
_PccardModemTestEnable_Object = MibScalar
pccardModemTestEnable = _PccardModemTestEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 24),
    _PccardModemTestEnable_Type()
)
pccardModemTestEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardModemTestEnable.setStatus("mandatory")
_PccardModemTestNumber_Type = DisplayString
_PccardModemTestNumber_Object = MibScalar
pccardModemTestNumber = _PccardModemTestNumber_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 25),
    _PccardModemTestNumber_Type()
)
pccardModemTestNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardModemTestNumber.setStatus("mandatory")
_PccardModemTestInterval_Type = Integer32
_PccardModemTestInterval_Object = MibScalar
pccardModemTestInterval = _PccardModemTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 26),
    _PccardModemTestInterval_Type()
)
pccardModemTestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardModemTestInterval.setStatus("mandatory")
_PccardModemTestMail_Type = Switch
_PccardModemTestMail_Object = MibScalar
pccardModemTestMail = _PccardModemTestMail_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 27),
    _PccardModemTestMail_Type()
)
pccardModemTestMail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardModemTestMail.setStatus("mandatory")
_PccardModemTestMailTitle_Type = DisplayString
_PccardModemTestMailTitle_Object = MibScalar
pccardModemTestMailTitle = _PccardModemTestMailTitle_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 28),
    _PccardModemTestMailTitle_Type()
)
pccardModemTestMailTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardModemTestMailTitle.setStatus("mandatory")
_PccardModemTestMailto_Type = DisplayString
_PccardModemTestMailto_Object = MibScalar
pccardModemTestMailto = _PccardModemTestMailto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 29),
    _PccardModemTestMailto_Type()
)
pccardModemTestMailto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardModemTestMailto.setStatus("mandatory")
_PccardModemTestTrap_Type = Switch
_PccardModemTestTrap_Object = MibScalar
pccardModemTestTrap = _PccardModemTestTrap_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 30),
    _PccardModemTestTrap_Type()
)
pccardModemTestTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardModemTestTrap.setStatus("mandatory")
_PccardTrapToGlobalSNMP_Type = Switch
_PccardTrapToGlobalSNMP_Object = MibScalar
pccardTrapToGlobalSNMP = _PccardTrapToGlobalSNMP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 31),
    _PccardTrapToGlobalSNMP_Type()
)
pccardTrapToGlobalSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardTrapToGlobalSNMP.setStatus("mandatory")
_PccardTrapRcvTable_Object = MibTable
pccardTrapRcvTable = _PccardTrapRcvTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 32)
)
if mibBuilder.loadTexts:
    pccardTrapRcvTable.setStatus("mandatory")
_PccardTrapRcvEntry_Object = MibTableRow
pccardTrapRcvEntry = _PccardTrapRcvEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 32, 1)
)
pccardTrapRcvEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "pccardTrapRcvIndex"),
)
if mibBuilder.loadTexts:
    pccardTrapRcvEntry.setStatus("mandatory")
_PccardTrapRcvIndex_Type = Integer32
_PccardTrapRcvIndex_Object = MibTableColumn
pccardTrapRcvIndex = _PccardTrapRcvIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 32, 1, 11),
    _PccardTrapRcvIndex_Type()
)
pccardTrapRcvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pccardTrapRcvIndex.setStatus("mandatory")
_PccardTrapRcvIP_Type = DisplayString
_PccardTrapRcvIP_Object = MibTableColumn
pccardTrapRcvIP = _PccardTrapRcvIP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 32, 1, 12),
    _PccardTrapRcvIP_Type()
)
pccardTrapRcvIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardTrapRcvIP.setStatus("mandatory")
_PccardTrapRcvComm_Type = DisplayString
_PccardTrapRcvComm_Object = MibTableColumn
pccardTrapRcvComm = _PccardTrapRcvComm_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 32, 1, 13),
    _PccardTrapRcvComm_Type()
)
pccardTrapRcvComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardTrapRcvComm.setStatus("mandatory")
_PccardTrapRcvVer_Type = DisplayString
_PccardTrapRcvVer_Object = MibTableColumn
pccardTrapRcvVer = _PccardTrapRcvVer_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 32, 1, 14),
    _PccardTrapRcvVer_Type()
)
pccardTrapRcvVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardTrapRcvVer.setStatus("mandatory")
_PccardTrapRcvUserName_Type = DisplayString
_PccardTrapRcvUserName_Object = MibTableColumn
pccardTrapRcvUserName = _PccardTrapRcvUserName_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 32, 1, 15),
    _PccardTrapRcvUserName_Type()
)
pccardTrapRcvUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardTrapRcvUserName.setStatus("mandatory")


class _PccardTrapRcvSecurityLevel_Type(Integer32):
    """Custom type pccardTrapRcvSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAuthNoPriv", 0),
          ("authNoPriv", 1),
          ("authPriv", 2))
    )


_PccardTrapRcvSecurityLevel_Type.__name__ = "Integer32"
_PccardTrapRcvSecurityLevel_Object = MibTableColumn
pccardTrapRcvSecurityLevel = _PccardTrapRcvSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 32, 1, 16),
    _PccardTrapRcvSecurityLevel_Type()
)
pccardTrapRcvSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardTrapRcvSecurityLevel.setStatus("mandatory")


class _PccardTrapRcvAuthProto_Type(Integer32):
    """Custom type pccardTrapRcvAuthProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("md5", 0),
          ("sha", 1))
    )


_PccardTrapRcvAuthProto_Type.__name__ = "Integer32"
_PccardTrapRcvAuthProto_Object = MibTableColumn
pccardTrapRcvAuthProto = _PccardTrapRcvAuthProto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 32, 1, 17),
    _PccardTrapRcvAuthProto_Type()
)
pccardTrapRcvAuthProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardTrapRcvAuthProto.setStatus("mandatory")
_PccardTrapRcvAuthPasswd_Type = DisplayString
_PccardTrapRcvAuthPasswd_Object = MibTableColumn
pccardTrapRcvAuthPasswd = _PccardTrapRcvAuthPasswd_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 32, 1, 18),
    _PccardTrapRcvAuthPasswd_Type()
)
pccardTrapRcvAuthPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardTrapRcvAuthPasswd.setStatus("mandatory")


class _PccardTrapRcvPrivProto_Type(Integer32):
    """Custom type pccardTrapRcvPrivProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("des", 0),
          ("aes", 1))
    )


_PccardTrapRcvPrivProto_Type.__name__ = "Integer32"
_PccardTrapRcvPrivProto_Object = MibTableColumn
pccardTrapRcvPrivProto = _PccardTrapRcvPrivProto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 32, 1, 19),
    _PccardTrapRcvPrivProto_Type()
)
pccardTrapRcvPrivProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardTrapRcvPrivProto.setStatus("mandatory")
_PccardTrapRcvPrivPasswd_Type = DisplayString
_PccardTrapRcvPrivPasswd_Object = MibTableColumn
pccardTrapRcvPrivPasswd = _PccardTrapRcvPrivPasswd_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 32, 1, 20),
    _PccardTrapRcvPrivPasswd_Type()
)
pccardTrapRcvPrivPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardTrapRcvPrivPasswd.setStatus("mandatory")
_PccardTrapRcvEngineID_Type = DisplayString
_PccardTrapRcvEngineID_Object = MibTableColumn
pccardTrapRcvEngineID = _PccardTrapRcvEngineID_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 32, 1, 21),
    _PccardTrapRcvEngineID_Type()
)
pccardTrapRcvEngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardTrapRcvEngineID.setStatus("mandatory")
_PccardEnableCallbackLogin_Type = Switch
_PccardEnableCallbackLogin_Object = MibScalar
pccardEnableCallbackLogin = _PccardEnableCallbackLogin_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 33),
    _PccardEnableCallbackLogin_Type()
)
pccardEnableCallbackLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardEnableCallbackLogin.setStatus("mandatory")
_PccardEnableCallbackNumberChange_Type = Switch
_PccardEnableCallbackNumberChange_Object = MibScalar
pccardEnableCallbackNumberChange = _PccardEnableCallbackNumberChange_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 34),
    _PccardEnableCallbackNumberChange_Type()
)
pccardEnableCallbackNumberChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardEnableCallbackNumberChange.setStatus("mandatory")


class _PccardIPv6Mode_Type(Integer32):
    """Custom type pccardIPv6Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("manualConfig", 1),
          ("dhcpv6", 2),
          ("autoConfig", 3))
    )


_PccardIPv6Mode_Type.__name__ = "Integer32"
_PccardIPv6Mode_Object = MibScalar
pccardIPv6Mode = _PccardIPv6Mode_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 35),
    _PccardIPv6Mode_Type()
)
pccardIPv6Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardIPv6Mode.setStatus("mandatory")
_PccardIPv6Address_Type = DisplayString
_PccardIPv6Address_Object = MibScalar
pccardIPv6Address = _PccardIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 36),
    _PccardIPv6Address_Type()
)
pccardIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardIPv6Address.setStatus("mandatory")
_PccardIPv6Gateway_Type = DisplayString
_PccardIPv6Gateway_Object = MibScalar
pccardIPv6Gateway = _PccardIPv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 37),
    _PccardIPv6Gateway_Type()
)
pccardIPv6Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardIPv6Gateway.setStatus("mandatory")
_PccardIPv6SecondaryIPAddress_Type = DisplayString
_PccardIPv6SecondaryIPAddress_Object = MibScalar
pccardIPv6SecondaryIPAddress = _PccardIPv6SecondaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 38),
    _PccardIPv6SecondaryIPAddress_Type()
)
pccardIPv6SecondaryIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardIPv6SecondaryIPAddress.setStatus("mandatory")
_PccardIPv6Enable6to4tunneling_Type = Switch
_PccardIPv6Enable6to4tunneling_Object = MibScalar
pccardIPv6Enable6to4tunneling = _PccardIPv6Enable6to4tunneling_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 39),
    _PccardIPv6Enable6to4tunneling_Type()
)
pccardIPv6Enable6to4tunneling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardIPv6Enable6to4tunneling.setStatus("mandatory")
_PccardIPv6To4Relay_Type = DisplayString
_PccardIPv6To4Relay_Object = MibScalar
pccardIPv6To4Relay = _PccardIPv6To4Relay_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 40),
    _PccardIPv6To4Relay_Type()
)
pccardIPv6To4Relay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardIPv6To4Relay.setStatus("mandatory")
_PccardIPv6OverwriteLocalIPV4_Type = DisplayString
_PccardIPv6OverwriteLocalIPV4_Object = MibScalar
pccardIPv6OverwriteLocalIPV4 = _PccardIPv6OverwriteLocalIPV4_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 41),
    _PccardIPv6OverwriteLocalIPV4_Type()
)
pccardIPv6OverwriteLocalIPV4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardIPv6OverwriteLocalIPV4.setStatus("mandatory")


class _PccardAuthMethod_Type(Integer32):
    """Custom type pccardAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("local", 1))
    )


_PccardAuthMethod_Type.__name__ = "Integer32"
_PccardAuthMethod_Object = MibScalar
pccardAuthMethod = _PccardAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 42),
    _PccardAuthMethod_Type()
)
pccardAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardAuthMethod.setStatus("mandatory")
_PccardPPPUser_Type = DisplayString
_PccardPPPUser_Object = MibScalar
pccardPPPUser = _PccardPPPUser_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 11, 43),
    _PccardPPPUser_Type()
)
pccardPPPUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccardPPPUser.setStatus("mandatory")
_Modem_ObjectIdentity = ObjectIdentity
modem = _Modem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12)
)
_ModemEnablePPP_Type = Switch
_ModemEnablePPP_Object = MibScalar
modemEnablePPP = _ModemEnablePPP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 11),
    _ModemEnablePPP_Type()
)
modemEnablePPP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemEnablePPP.setStatus("mandatory")
_ModemInitString_Type = DisplayString
_ModemInitString_Object = MibScalar
modemInitString = _ModemInitString_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 12),
    _ModemInitString_Type()
)
modemInitString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemInitString.setStatus("mandatory")
_ModemEnableCallback_Type = Switch
_ModemEnableCallback_Object = MibScalar
modemEnableCallback = _ModemEnableCallback_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 13),
    _ModemEnableCallback_Type()
)
modemEnableCallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemEnableCallback.setStatus("mandatory")
_ModemCallbackNumber_Type = DisplayString
_ModemCallbackNumber_Object = MibScalar
modemCallbackNumber = _ModemCallbackNumber_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 14),
    _ModemCallbackNumber_Type()
)
modemCallbackNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemCallbackNumber.setStatus("mandatory")
_ModemEnableModemTest_Type = Switch
_ModemEnableModemTest_Object = MibScalar
modemEnableModemTest = _ModemEnableModemTest_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 15),
    _ModemEnableModemTest_Type()
)
modemEnableModemTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemEnableModemTest.setStatus("mandatory")
_ModemTestNumber_Type = DisplayString
_ModemTestNumber_Object = MibScalar
modemTestNumber = _ModemTestNumber_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 16),
    _ModemTestNumber_Type()
)
modemTestNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemTestNumber.setStatus("mandatory")
_ModemTestInterval_Type = Integer32
_ModemTestInterval_Object = MibScalar
modemTestInterval = _ModemTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 17),
    _ModemTestInterval_Type()
)
modemTestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemTestInterval.setStatus("mandatory")
_ModemTestMail_Type = Switch
_ModemTestMail_Object = MibScalar
modemTestMail = _ModemTestMail_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 18),
    _ModemTestMail_Type()
)
modemTestMail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemTestMail.setStatus("mandatory")
_ModemTestMailTitle_Type = DisplayString
_ModemTestMailTitle_Object = MibScalar
modemTestMailTitle = _ModemTestMailTitle_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 19),
    _ModemTestMailTitle_Type()
)
modemTestMailTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemTestMailTitle.setStatus("mandatory")
_ModemTestMailto_Type = DisplayString
_ModemTestMailto_Object = MibScalar
modemTestMailto = _ModemTestMailto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 20),
    _ModemTestMailto_Type()
)
modemTestMailto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemTestMailto.setStatus("mandatory")
_ModemTestTrap_Type = Switch
_ModemTestTrap_Object = MibScalar
modemTestTrap = _ModemTestTrap_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 21),
    _ModemTestTrap_Type()
)
modemTestTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemTestTrap.setStatus("mandatory")
_ModemTrapToGlobalSNMP_Type = Switch
_ModemTrapToGlobalSNMP_Object = MibScalar
modemTrapToGlobalSNMP = _ModemTrapToGlobalSNMP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 22),
    _ModemTrapToGlobalSNMP_Type()
)
modemTrapToGlobalSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemTrapToGlobalSNMP.setStatus("mandatory")
_ModemTrapRcvTable_Object = MibTable
modemTrapRcvTable = _ModemTrapRcvTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 23)
)
if mibBuilder.loadTexts:
    modemTrapRcvTable.setStatus("mandatory")
_ModemTrapRcvEntry_Object = MibTableRow
modemTrapRcvEntry = _ModemTrapRcvEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 23, 1)
)
modemTrapRcvEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "modemTrapRcvIndex"),
)
if mibBuilder.loadTexts:
    modemTrapRcvEntry.setStatus("mandatory")
_ModemTrapRcvIndex_Type = Integer32
_ModemTrapRcvIndex_Object = MibTableColumn
modemTrapRcvIndex = _ModemTrapRcvIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 23, 1, 11),
    _ModemTrapRcvIndex_Type()
)
modemTrapRcvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemTrapRcvIndex.setStatus("mandatory")
_ModemTrapRcvIP_Type = DisplayString
_ModemTrapRcvIP_Object = MibTableColumn
modemTrapRcvIP = _ModemTrapRcvIP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 23, 1, 12),
    _ModemTrapRcvIP_Type()
)
modemTrapRcvIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemTrapRcvIP.setStatus("mandatory")
_ModemTrapRcvComm_Type = DisplayString
_ModemTrapRcvComm_Object = MibTableColumn
modemTrapRcvComm = _ModemTrapRcvComm_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 23, 1, 13),
    _ModemTrapRcvComm_Type()
)
modemTrapRcvComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemTrapRcvComm.setStatus("mandatory")
_ModemTrapRcvVer_Type = DisplayString
_ModemTrapRcvVer_Object = MibTableColumn
modemTrapRcvVer = _ModemTrapRcvVer_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 23, 1, 14),
    _ModemTrapRcvVer_Type()
)
modemTrapRcvVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemTrapRcvVer.setStatus("mandatory")
_ModemTrapRcvUserName_Type = DisplayString
_ModemTrapRcvUserName_Object = MibTableColumn
modemTrapRcvUserName = _ModemTrapRcvUserName_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 23, 1, 15),
    _ModemTrapRcvUserName_Type()
)
modemTrapRcvUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemTrapRcvUserName.setStatus("mandatory")


class _ModemTrapRcvSecurityLevel_Type(Integer32):
    """Custom type modemTrapRcvSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAuthNoPriv", 0),
          ("authNoPriv", 1),
          ("authPriv", 2))
    )


_ModemTrapRcvSecurityLevel_Type.__name__ = "Integer32"
_ModemTrapRcvSecurityLevel_Object = MibTableColumn
modemTrapRcvSecurityLevel = _ModemTrapRcvSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 23, 1, 16),
    _ModemTrapRcvSecurityLevel_Type()
)
modemTrapRcvSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemTrapRcvSecurityLevel.setStatus("mandatory")


class _ModemTrapRcvAuthProto_Type(Integer32):
    """Custom type modemTrapRcvAuthProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("md5", 0),
          ("sha", 1))
    )


_ModemTrapRcvAuthProto_Type.__name__ = "Integer32"
_ModemTrapRcvAuthProto_Object = MibTableColumn
modemTrapRcvAuthProto = _ModemTrapRcvAuthProto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 23, 1, 17),
    _ModemTrapRcvAuthProto_Type()
)
modemTrapRcvAuthProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemTrapRcvAuthProto.setStatus("mandatory")
_ModemTrapRcvAuthPasswd_Type = DisplayString
_ModemTrapRcvAuthPasswd_Object = MibTableColumn
modemTrapRcvAuthPasswd = _ModemTrapRcvAuthPasswd_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 23, 1, 18),
    _ModemTrapRcvAuthPasswd_Type()
)
modemTrapRcvAuthPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemTrapRcvAuthPasswd.setStatus("mandatory")


class _ModemTrapRcvPrivProto_Type(Integer32):
    """Custom type modemTrapRcvPrivProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("des", 0),
          ("aes", 1))
    )


_ModemTrapRcvPrivProto_Type.__name__ = "Integer32"
_ModemTrapRcvPrivProto_Object = MibTableColumn
modemTrapRcvPrivProto = _ModemTrapRcvPrivProto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 23, 1, 19),
    _ModemTrapRcvPrivProto_Type()
)
modemTrapRcvPrivProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemTrapRcvPrivProto.setStatus("mandatory")
_ModemTrapRcvPrivPasswd_Type = DisplayString
_ModemTrapRcvPrivPasswd_Object = MibTableColumn
modemTrapRcvPrivPasswd = _ModemTrapRcvPrivPasswd_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 23, 1, 20),
    _ModemTrapRcvPrivPasswd_Type()
)
modemTrapRcvPrivPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemTrapRcvPrivPasswd.setStatus("mandatory")
_ModemTrapRcvEngineID_Type = DisplayString
_ModemTrapRcvEngineID_Object = MibTableColumn
modemTrapRcvEngineID = _ModemTrapRcvEngineID_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 23, 1, 21),
    _ModemTrapRcvEngineID_Type()
)
modemTrapRcvEngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemTrapRcvEngineID.setStatus("mandatory")
_ModemEnableCallbackLogin_Type = Switch
_ModemEnableCallbackLogin_Object = MibScalar
modemEnableCallbackLogin = _ModemEnableCallbackLogin_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 24),
    _ModemEnableCallbackLogin_Type()
)
modemEnableCallbackLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemEnableCallbackLogin.setStatus("mandatory")
_ModemEnableCallbackNumberChange_Type = Switch
_ModemEnableCallbackNumberChange_Object = MibScalar
modemEnableCallbackNumberChange = _ModemEnableCallbackNumberChange_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 25),
    _ModemEnableCallbackNumberChange_Type()
)
modemEnableCallbackNumberChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemEnableCallbackNumberChange.setStatus("mandatory")
_ModemSecondaryCallbackNumber_Type = DisplayString
_ModemSecondaryCallbackNumber_Object = MibScalar
modemSecondaryCallbackNumber = _ModemSecondaryCallbackNumber_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 26),
    _ModemSecondaryCallbackNumber_Type()
)
modemSecondaryCallbackNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemSecondaryCallbackNumber.setStatus("mandatory")


class _ModemAuthMethod_Type(Integer32):
    """Custom type modemAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("local", 1))
    )


_ModemAuthMethod_Type.__name__ = "Integer32"
_ModemAuthMethod_Object = MibScalar
modemAuthMethod = _ModemAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 27),
    _ModemAuthMethod_Type()
)
modemAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAuthMethod.setStatus("mandatory")
_ModemPPPUser_Type = DisplayString
_ModemPPPUser_Object = MibScalar
modemPPPUser = _ModemPPPUser_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 12, 28),
    _ModemPPPUser_Type()
)
modemPPPUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemPPPUser.setStatus("mandatory")
_Usb_ObjectIdentity = ObjectIdentity
usb = _Usb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 13)
)
_UsbTable_Object = MibTable
usbTable = _UsbTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 13, 11)
)
if mibBuilder.loadTexts:
    usbTable.setStatus("mandatory")
_UsbEntry_Object = MibTableRow
usbEntry = _UsbEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 13, 11, 1)
)
usbEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "usbIndex"),
)
if mibBuilder.loadTexts:
    usbEntry.setStatus("mandatory")
_UsbIndex_Type = Integer32
_UsbIndex_Object = MibTableColumn
usbIndex = _UsbIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 13, 11, 1, 11),
    _UsbIndex_Type()
)
usbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbIndex.setStatus("mandatory")


class _UsbType_Type(Integer32):
    """Custom type usbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", -1),
          ("empty", 0),
          ("flashmemory", 1))
    )


_UsbType_Type.__name__ = "Integer32"
_UsbType_Object = MibTableColumn
usbType = _UsbType_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 13, 11, 1, 12),
    _UsbType_Type()
)
usbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbType.setStatus("mandatory")
_UsbModel_Type = DisplayString
_UsbModel_Object = MibTableColumn
usbModel = _UsbModel_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 13, 11, 1, 13),
    _UsbModel_Type()
)
usbModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbModel.setStatus("mandatory")
_UsbSize_Type = Integer32
_UsbSize_Object = MibTableColumn
usbSize = _UsbSize_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 13, 11, 1, 14),
    _UsbSize_Type()
)
usbSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbSize.setStatus("mandatory")
_UsbFileSystem_Type = Integer32
_UsbFileSystem_Object = MibTableColumn
usbFileSystem = _UsbFileSystem_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 13, 11, 1, 15),
    _UsbFileSystem_Type()
)
usbFileSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbFileSystem.setStatus("mandatory")
_UsbTotalSize_Type = Integer32
_UsbTotalSize_Object = MibTableColumn
usbTotalSize = _UsbTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 13, 11, 1, 16),
    _UsbTotalSize_Type()
)
usbTotalSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usbTotalSize.setStatus("mandatory")


class _UsbIpmode_Type(Integer32):
    """Custom type usbIpmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("staticip", 1),
          ("dhcp", 2))
    )


_UsbIpmode_Type.__name__ = "Integer32"
_UsbIpmode_Object = MibTableColumn
usbIpmode = _UsbIpmode_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 13, 11, 1, 17),
    _UsbIpmode_Type()
)
usbIpmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usbIpmode.setStatus("mandatory")
_UsbIpAddress_Type = IpAddress
_UsbIpAddress_Object = MibTableColumn
usbIpAddress = _UsbIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 13, 11, 1, 18),
    _UsbIpAddress_Type()
)
usbIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usbIpAddress.setStatus("mandatory")
_UsbSubnet_Type = IpAddress
_UsbSubnet_Object = MibTableColumn
usbSubnet = _UsbSubnet_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 13, 11, 1, 19),
    _UsbSubnet_Type()
)
usbSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usbSubnet.setStatus("mandatory")
_UsbGateway_Type = IpAddress
_UsbGateway_Object = MibTableColumn
usbGateway = _UsbGateway_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 13, 11, 1, 20),
    _UsbGateway_Type()
)
usbGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usbGateway.setStatus("mandatory")
_UsbSSID_Type = DisplayString
_UsbSSID_Object = MibTableColumn
usbSSID = _UsbSSID_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 13, 11, 1, 21),
    _UsbSSID_Type()
)
usbSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usbSSID.setStatus("mandatory")
_UsbWEPEnable_Type = Switch
_UsbWEPEnable_Object = MibTableColumn
usbWEPEnable = _UsbWEPEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 13, 11, 1, 22),
    _UsbWEPEnable_Type()
)
usbWEPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usbWEPEnable.setStatus("mandatory")


class _UsbWEPMode_Type(Integer32):
    """Custom type usbWEPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("encrypt", 1),
          ("shared", 2))
    )


_UsbWEPMode_Type.__name__ = "Integer32"
_UsbWEPMode_Object = MibTableColumn
usbWEPMode = _UsbWEPMode_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 13, 11, 1, 23),
    _UsbWEPMode_Type()
)
usbWEPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usbWEPMode.setStatus("mandatory")


class _UsbWEPLength_Type(Integer32):
    """Custom type usbWEPLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("b40", 1),
          ("b128", 2))
    )


_UsbWEPLength_Type.__name__ = "Integer32"
_UsbWEPLength_Object = MibTableColumn
usbWEPLength = _UsbWEPLength_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 13, 11, 1, 24),
    _UsbWEPLength_Type()
)
usbWEPLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usbWEPLength.setStatus("mandatory")
_UsbWEPKeyStr_Type = DisplayString
_UsbWEPKeyStr_Object = MibTableColumn
usbWEPKeyStr = _UsbWEPKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 26, 13, 11, 1, 25),
    _UsbWEPKeyStr_Type()
)
usbWEPKeyStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usbWEPKeyStr.setStatus("mandatory")
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27)
)
_Netip_ObjectIdentity = ObjectIdentity
netip = _Netip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11)
)
_FirstIPConfig_ObjectIdentity = ObjectIdentity
firstIPConfig = _FirstIPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 11)
)
_FirstIPv4Config_ObjectIdentity = ObjectIdentity
firstIPv4Config = _FirstIPv4Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 11, 11)
)


class _FirstIPv4Mode_Type(Integer32):
    """Custom type firstIPv4Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("staticIP", 1),
          ("dhcp", 2),
          ("pppoe", 3))
    )


_FirstIPv4Mode_Type.__name__ = "Integer32"
_FirstIPv4Mode_Object = MibScalar
firstIPv4Mode = _FirstIPv4Mode_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 11, 11, 11),
    _FirstIPv4Mode_Type()
)
firstIPv4Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firstIPv4Mode.setStatus("mandatory")
_FirstIPv4PrimaryIPAddress_Type = IpAddress
_FirstIPv4PrimaryIPAddress_Object = MibScalar
firstIPv4PrimaryIPAddress = _FirstIPv4PrimaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 11, 11, 12),
    _FirstIPv4PrimaryIPAddress_Type()
)
firstIPv4PrimaryIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firstIPv4PrimaryIPAddress.setStatus("mandatory")
_FirstIPv4PrimarySubMask_Type = IpAddress
_FirstIPv4PrimarySubMask_Object = MibScalar
firstIPv4PrimarySubMask = _FirstIPv4PrimarySubMask_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 11, 11, 13),
    _FirstIPv4PrimarySubMask_Type()
)
firstIPv4PrimarySubMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firstIPv4PrimarySubMask.setStatus("mandatory")
_FirstIPv4PrimaryGateway_Type = IpAddress
_FirstIPv4PrimaryGateway_Object = MibScalar
firstIPv4PrimaryGateway = _FirstIPv4PrimaryGateway_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 11, 11, 14),
    _FirstIPv4PrimaryGateway_Type()
)
firstIPv4PrimaryGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firstIPv4PrimaryGateway.setStatus("mandatory")
_FirstIPv4EnableSecondaryIP_Type = Switch
_FirstIPv4EnableSecondaryIP_Object = MibScalar
firstIPv4EnableSecondaryIP = _FirstIPv4EnableSecondaryIP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 11, 11, 15),
    _FirstIPv4EnableSecondaryIP_Type()
)
firstIPv4EnableSecondaryIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firstIPv4EnableSecondaryIP.setStatus("mandatory")
_FirstIPv4SecondaryIPAddress_Type = IpAddress
_FirstIPv4SecondaryIPAddress_Object = MibScalar
firstIPv4SecondaryIPAddress = _FirstIPv4SecondaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 11, 11, 16),
    _FirstIPv4SecondaryIPAddress_Type()
)
firstIPv4SecondaryIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firstIPv4SecondaryIPAddress.setStatus("mandatory")
_FirstIPv4SecondarySubMask_Type = IpAddress
_FirstIPv4SecondarySubMask_Object = MibScalar
firstIPv4SecondarySubMask = _FirstIPv4SecondarySubMask_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 11, 11, 17),
    _FirstIPv4SecondarySubMask_Type()
)
firstIPv4SecondarySubMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firstIPv4SecondarySubMask.setStatus("mandatory")
_FirstIPv4SecondaryGateway_Type = IpAddress
_FirstIPv4SecondaryGateway_Object = MibScalar
firstIPv4SecondaryGateway = _FirstIPv4SecondaryGateway_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 11, 11, 18),
    _FirstIPv4SecondaryGateway_Type()
)
firstIPv4SecondaryGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firstIPv4SecondaryGateway.setStatus("mandatory")
_FirstIPv6Config_ObjectIdentity = ObjectIdentity
firstIPv6Config = _FirstIPv6Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 11, 12)
)


class _FirstIPv6Mode_Type(Integer32):
    """Custom type firstIPv6Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("manualConfig", 1),
          ("dhcpv6", 2),
          ("autoConfig", 3))
    )


_FirstIPv6Mode_Type.__name__ = "Integer32"
_FirstIPv6Mode_Object = MibScalar
firstIPv6Mode = _FirstIPv6Mode_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 11, 12, 11),
    _FirstIPv6Mode_Type()
)
firstIPv6Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firstIPv6Mode.setStatus("mandatory")
_FirstIPv6Address_Type = DisplayString
_FirstIPv6Address_Object = MibScalar
firstIPv6Address = _FirstIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 11, 12, 12),
    _FirstIPv6Address_Type()
)
firstIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firstIPv6Address.setStatus("mandatory")
_FirstIPv6Gateway_Type = DisplayString
_FirstIPv6Gateway_Object = MibScalar
firstIPv6Gateway = _FirstIPv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 11, 12, 13),
    _FirstIPv6Gateway_Type()
)
firstIPv6Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firstIPv6Gateway.setStatus("mandatory")
_FirstIPv6SecondaryIPAddress_Type = DisplayString
_FirstIPv6SecondaryIPAddress_Object = MibScalar
firstIPv6SecondaryIPAddress = _FirstIPv6SecondaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 11, 12, 14),
    _FirstIPv6SecondaryIPAddress_Type()
)
firstIPv6SecondaryIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firstIPv6SecondaryIPAddress.setStatus("mandatory")
_FirstIPv6Enable6to4tunneling_Type = Switch
_FirstIPv6Enable6to4tunneling_Object = MibScalar
firstIPv6Enable6to4tunneling = _FirstIPv6Enable6to4tunneling_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 11, 12, 15),
    _FirstIPv6Enable6to4tunneling_Type()
)
firstIPv6Enable6to4tunneling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firstIPv6Enable6to4tunneling.setStatus("mandatory")
_FirstIPv6To4Relay_Type = DisplayString
_FirstIPv6To4Relay_Object = MibScalar
firstIPv6To4Relay = _FirstIPv6To4Relay_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 11, 12, 16),
    _FirstIPv6To4Relay_Type()
)
firstIPv6To4Relay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firstIPv6To4Relay.setStatus("mandatory")
_FirstIPv6OverwriteLocalIPV4_Type = DisplayString
_FirstIPv6OverwriteLocalIPV4_Object = MibScalar
firstIPv6OverwriteLocalIPV4 = _FirstIPv6OverwriteLocalIPV4_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 11, 12, 17),
    _FirstIPv6OverwriteLocalIPV4_Type()
)
firstIPv6OverwriteLocalIPV4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firstIPv6OverwriteLocalIPV4.setStatus("mandatory")
_SecondIPConfig_ObjectIdentity = ObjectIdentity
secondIPConfig = _SecondIPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 12)
)
_SecondIPv4Config_ObjectIdentity = ObjectIdentity
secondIPv4Config = _SecondIPv4Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 12, 11)
)


class _SecondIPv4Mode_Type(Integer32):
    """Custom type secondIPv4Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("staticIP", 1),
          ("dhcp", 2),
          ("pppoe", 3))
    )


_SecondIPv4Mode_Type.__name__ = "Integer32"
_SecondIPv4Mode_Object = MibScalar
secondIPv4Mode = _SecondIPv4Mode_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 12, 11, 11),
    _SecondIPv4Mode_Type()
)
secondIPv4Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondIPv4Mode.setStatus("mandatory")
_SecondIPv4PrimaryIPAddress_Type = IpAddress
_SecondIPv4PrimaryIPAddress_Object = MibScalar
secondIPv4PrimaryIPAddress = _SecondIPv4PrimaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 12, 11, 12),
    _SecondIPv4PrimaryIPAddress_Type()
)
secondIPv4PrimaryIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondIPv4PrimaryIPAddress.setStatus("mandatory")
_SecondIPv4PrimarySubMask_Type = IpAddress
_SecondIPv4PrimarySubMask_Object = MibScalar
secondIPv4PrimarySubMask = _SecondIPv4PrimarySubMask_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 12, 11, 13),
    _SecondIPv4PrimarySubMask_Type()
)
secondIPv4PrimarySubMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondIPv4PrimarySubMask.setStatus("mandatory")
_SecondIPv4PrimaryGateway_Type = IpAddress
_SecondIPv4PrimaryGateway_Object = MibScalar
secondIPv4PrimaryGateway = _SecondIPv4PrimaryGateway_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 12, 11, 14),
    _SecondIPv4PrimaryGateway_Type()
)
secondIPv4PrimaryGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondIPv4PrimaryGateway.setStatus("mandatory")
_SecondIPv4EnableSecondaryIP_Type = Switch
_SecondIPv4EnableSecondaryIP_Object = MibScalar
secondIPv4EnableSecondaryIP = _SecondIPv4EnableSecondaryIP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 12, 11, 15),
    _SecondIPv4EnableSecondaryIP_Type()
)
secondIPv4EnableSecondaryIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondIPv4EnableSecondaryIP.setStatus("mandatory")
_SecondIPv4SecondaryIPAddress_Type = IpAddress
_SecondIPv4SecondaryIPAddress_Object = MibScalar
secondIPv4SecondaryIPAddress = _SecondIPv4SecondaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 12, 11, 16),
    _SecondIPv4SecondaryIPAddress_Type()
)
secondIPv4SecondaryIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondIPv4SecondaryIPAddress.setStatus("mandatory")
_SecondIPv4SecondarySubMask_Type = IpAddress
_SecondIPv4SecondarySubMask_Object = MibScalar
secondIPv4SecondarySubMask = _SecondIPv4SecondarySubMask_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 12, 11, 17),
    _SecondIPv4SecondarySubMask_Type()
)
secondIPv4SecondarySubMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondIPv4SecondarySubMask.setStatus("mandatory")
_SecondIPv4SecondaryGateway_Type = IpAddress
_SecondIPv4SecondaryGateway_Object = MibScalar
secondIPv4SecondaryGateway = _SecondIPv4SecondaryGateway_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 12, 11, 18),
    _SecondIPv4SecondaryGateway_Type()
)
secondIPv4SecondaryGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondIPv4SecondaryGateway.setStatus("mandatory")
_SecondIPv6Config_ObjectIdentity = ObjectIdentity
secondIPv6Config = _SecondIPv6Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 12, 12)
)


class _SecondIPv6Mode_Type(Integer32):
    """Custom type secondIPv6Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("manualConfig", 1),
          ("dhcpv6", 2),
          ("autoConfig", 3))
    )


_SecondIPv6Mode_Type.__name__ = "Integer32"
_SecondIPv6Mode_Object = MibScalar
secondIPv6Mode = _SecondIPv6Mode_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 12, 12, 11),
    _SecondIPv6Mode_Type()
)
secondIPv6Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondIPv6Mode.setStatus("mandatory")
_SecondIPv6Address_Type = DisplayString
_SecondIPv6Address_Object = MibScalar
secondIPv6Address = _SecondIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 12, 12, 12),
    _SecondIPv6Address_Type()
)
secondIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondIPv6Address.setStatus("mandatory")
_SecondIPv6Gateway_Type = DisplayString
_SecondIPv6Gateway_Object = MibScalar
secondIPv6Gateway = _SecondIPv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 12, 12, 13),
    _SecondIPv6Gateway_Type()
)
secondIPv6Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondIPv6Gateway.setStatus("mandatory")
_SecondIPv6SecondaryIPAddress_Type = DisplayString
_SecondIPv6SecondaryIPAddress_Object = MibScalar
secondIPv6SecondaryIPAddress = _SecondIPv6SecondaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 12, 12, 14),
    _SecondIPv6SecondaryIPAddress_Type()
)
secondIPv6SecondaryIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondIPv6SecondaryIPAddress.setStatus("mandatory")
_SecondIPv6Enable6to4tunneling_Type = Switch
_SecondIPv6Enable6to4tunneling_Object = MibScalar
secondIPv6Enable6to4tunneling = _SecondIPv6Enable6to4tunneling_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 12, 12, 15),
    _SecondIPv6Enable6to4tunneling_Type()
)
secondIPv6Enable6to4tunneling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondIPv6Enable6to4tunneling.setStatus("mandatory")
_SecondIPv6To4Relay_Type = DisplayString
_SecondIPv6To4Relay_Object = MibScalar
secondIPv6To4Relay = _SecondIPv6To4Relay_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 12, 12, 16),
    _SecondIPv6To4Relay_Type()
)
secondIPv6To4Relay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondIPv6To4Relay.setStatus("mandatory")
_SecondIPv6OverwriteLocalIPV4_Type = DisplayString
_SecondIPv6OverwriteLocalIPV4_Object = MibScalar
secondIPv6OverwriteLocalIPV4 = _SecondIPv6OverwriteLocalIPV4_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 12, 12, 17),
    _SecondIPv6OverwriteLocalIPV4_Type()
)
secondIPv6OverwriteLocalIPV4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondIPv6OverwriteLocalIPV4.setStatus("mandatory")
_NetipUseOldIPOnDHCPFailure_Type = Switch
_NetipUseOldIPOnDHCPFailure_Object = MibScalar
netipUseOldIPOnDHCPFailure = _NetipUseOldIPOnDHCPFailure_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 13),
    _NetipUseOldIPOnDHCPFailure_Type()
)
netipUseOldIPOnDHCPFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netipUseOldIPOnDHCPFailure.setStatus("mandatory")
_NetipUseManualDNS_Type = Switch
_NetipUseManualDNS_Object = MibScalar
netipUseManualDNS = _NetipUseManualDNS_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 14),
    _NetipUseManualDNS_Type()
)
netipUseManualDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netipUseManualDNS.setStatus("mandatory")
_NetipPrimaryNameServer_Type = DisplayString
_NetipPrimaryNameServer_Object = MibScalar
netipPrimaryNameServer = _NetipPrimaryNameServer_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 15),
    _NetipPrimaryNameServer_Type()
)
netipPrimaryNameServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netipPrimaryNameServer.setStatus("mandatory")
_NetipSecondaryNameServer_Type = DisplayString
_NetipSecondaryNameServer_Object = MibScalar
netipSecondaryNameServer = _NetipSecondaryNameServer_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 16),
    _NetipSecondaryNameServer_Type()
)
netipSecondaryNameServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netipSecondaryNameServer.setStatus("mandatory")
_SourceBasedRouting_Type = Switch
_SourceBasedRouting_Object = MibScalar
sourceBasedRouting = _SourceBasedRouting_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 11, 17),
    _SourceBasedRouting_Type()
)
sourceBasedRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourceBasedRouting.setStatus("mandatory")
_SnmpOther_ObjectIdentity = ObjectIdentity
snmpOther = _SnmpOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 12)
)
_SnmpPowerOnTraps_Type = Switch
_SnmpPowerOnTraps_Object = MibScalar
snmpPowerOnTraps = _SnmpPowerOnTraps_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 12, 11),
    _SnmpPowerOnTraps_Type()
)
snmpPowerOnTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpPowerOnTraps.setStatus("mandatory")
_SnmpPowerOnEmails_Type = Switch
_SnmpPowerOnEmails_Object = MibScalar
snmpPowerOnEmails = _SnmpPowerOnEmails_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 12, 12),
    _SnmpPowerOnEmails_Type()
)
snmpPowerOnEmails.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpPowerOnEmails.setStatus("mandatory")
_SnmpAuthenTraps_Type = Switch
_SnmpAuthenTraps_Object = MibScalar
snmpAuthenTraps = _SnmpAuthenTraps_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 12, 13),
    _SnmpAuthenTraps_Type()
)
snmpAuthenTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAuthenTraps.setStatus("mandatory")
_SnmpAuthenEmails_Type = Switch
_SnmpAuthenEmails_Object = MibScalar
snmpAuthenEmails = _SnmpAuthenEmails_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 12, 14),
    _SnmpAuthenEmails_Type()
)
snmpAuthenEmails.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAuthenEmails.setStatus("mandatory")
_SnmpLinkUpTraps_Type = Switch
_SnmpLinkUpTraps_Object = MibScalar
snmpLinkUpTraps = _SnmpLinkUpTraps_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 12, 15),
    _SnmpLinkUpTraps_Type()
)
snmpLinkUpTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpLinkUpTraps.setStatus("mandatory")
_SnmpLinkUpEmails_Type = Switch
_SnmpLinkUpEmails_Object = MibScalar
snmpLinkUpEmails = _SnmpLinkUpEmails_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 12, 16),
    _SnmpLinkUpEmails_Type()
)
snmpLinkUpEmails.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpLinkUpEmails.setStatus("mandatory")
_SnmpLinkDownTraps_Type = Switch
_SnmpLinkDownTraps_Object = MibScalar
snmpLinkDownTraps = _SnmpLinkDownTraps_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 12, 17),
    _SnmpLinkDownTraps_Type()
)
snmpLinkDownTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpLinkDownTraps.setStatus("mandatory")
_SnmpLinkDownEmails_Type = Switch
_SnmpLinkDownEmails_Object = MibScalar
snmpLinkDownEmails = _SnmpLinkDownEmails_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 12, 18),
    _SnmpLinkDownEmails_Type()
)
snmpLinkDownEmails.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpLinkDownEmails.setStatus("mandatory")
_SnmpLoginTraps_Type = Switch
_SnmpLoginTraps_Object = MibScalar
snmpLoginTraps = _SnmpLoginTraps_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 12, 19),
    _SnmpLoginTraps_Type()
)
snmpLoginTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpLoginTraps.setStatus("mandatory")
_SnmpLoginEmails_Type = Switch
_SnmpLoginEmails_Object = MibScalar
snmpLoginEmails = _SnmpLoginEmails_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 12, 20),
    _SnmpLoginEmails_Type()
)
snmpLoginEmails.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpLoginEmails.setStatus("mandatory")
_SnmpMailto_Type = DisplayString
_SnmpMailto_Object = MibScalar
snmpMailto = _SnmpMailto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 12, 21),
    _SnmpMailto_Type()
)
snmpMailto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpMailto.setStatus("mandatory")
_SnmpTrapRcvTable_Object = MibTable
snmpTrapRcvTable = _SnmpTrapRcvTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 12, 22)
)
if mibBuilder.loadTexts:
    snmpTrapRcvTable.setStatus("mandatory")
_SnmpTrapRcvEntry_Object = MibTableRow
snmpTrapRcvEntry = _SnmpTrapRcvEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 12, 22, 1)
)
snmpTrapRcvEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "snmpTrapRcvIndex"),
)
if mibBuilder.loadTexts:
    snmpTrapRcvEntry.setStatus("mandatory")


class _SnmpTrapRcvIndex_Type(Integer32):
    """Custom type snmpTrapRcvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SnmpTrapRcvIndex_Type.__name__ = "Integer32"
_SnmpTrapRcvIndex_Object = MibTableColumn
snmpTrapRcvIndex = _SnmpTrapRcvIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 12, 22, 1, 11),
    _SnmpTrapRcvIndex_Type()
)
snmpTrapRcvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapRcvIndex.setStatus("mandatory")
_SnmpTrapRcvIP_Type = DisplayString
_SnmpTrapRcvIP_Object = MibTableColumn
snmpTrapRcvIP = _SnmpTrapRcvIP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 12, 22, 1, 12),
    _SnmpTrapRcvIP_Type()
)
snmpTrapRcvIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapRcvIP.setStatus("mandatory")
_SnmpTrapRcvComm_Type = DisplayString
_SnmpTrapRcvComm_Object = MibTableColumn
snmpTrapRcvComm = _SnmpTrapRcvComm_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 12, 22, 1, 13),
    _SnmpTrapRcvComm_Type()
)
snmpTrapRcvComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapRcvComm.setStatus("mandatory")


class _SnmpTrapRcvVer_Type(Integer32):
    """Custom type snmpTrapRcvVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 0),
          ("v2c", 1),
          ("v3", 2))
    )


_SnmpTrapRcvVer_Type.__name__ = "Integer32"
_SnmpTrapRcvVer_Object = MibTableColumn
snmpTrapRcvVer = _SnmpTrapRcvVer_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 12, 22, 1, 14),
    _SnmpTrapRcvVer_Type()
)
snmpTrapRcvVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapRcvVer.setStatus("mandatory")
_SnmpTrapRcvUserName_Type = DisplayString
_SnmpTrapRcvUserName_Object = MibTableColumn
snmpTrapRcvUserName = _SnmpTrapRcvUserName_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 12, 22, 1, 15),
    _SnmpTrapRcvUserName_Type()
)
snmpTrapRcvUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapRcvUserName.setStatus("mandatory")


class _SnmpTrapRcvSecurityLevel_Type(Integer32):
    """Custom type snmpTrapRcvSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAuthNoPriv", 0),
          ("authNoPriv", 1),
          ("authPriv", 2))
    )


_SnmpTrapRcvSecurityLevel_Type.__name__ = "Integer32"
_SnmpTrapRcvSecurityLevel_Object = MibTableColumn
snmpTrapRcvSecurityLevel = _SnmpTrapRcvSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 12, 22, 1, 16),
    _SnmpTrapRcvSecurityLevel_Type()
)
snmpTrapRcvSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapRcvSecurityLevel.setStatus("mandatory")


class _SnmpTrapRcvAuthProto_Type(Integer32):
    """Custom type snmpTrapRcvAuthProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("md5", 0),
          ("sha", 1))
    )


_SnmpTrapRcvAuthProto_Type.__name__ = "Integer32"
_SnmpTrapRcvAuthProto_Object = MibTableColumn
snmpTrapRcvAuthProto = _SnmpTrapRcvAuthProto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 12, 22, 1, 17),
    _SnmpTrapRcvAuthProto_Type()
)
snmpTrapRcvAuthProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapRcvAuthProto.setStatus("mandatory")
_SnmpTrapRcvAuthPasswd_Type = DisplayString
_SnmpTrapRcvAuthPasswd_Object = MibTableColumn
snmpTrapRcvAuthPasswd = _SnmpTrapRcvAuthPasswd_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 12, 22, 1, 18),
    _SnmpTrapRcvAuthPasswd_Type()
)
snmpTrapRcvAuthPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapRcvAuthPasswd.setStatus("mandatory")


class _SnmpTrapRcvPrivProto_Type(Integer32):
    """Custom type snmpTrapRcvPrivProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("des", 0),
          ("aes", 1))
    )


_SnmpTrapRcvPrivProto_Type.__name__ = "Integer32"
_SnmpTrapRcvPrivProto_Object = MibTableColumn
snmpTrapRcvPrivProto = _SnmpTrapRcvPrivProto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 12, 22, 1, 19),
    _SnmpTrapRcvPrivProto_Type()
)
snmpTrapRcvPrivProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapRcvPrivProto.setStatus("mandatory")
_SnmpTrapRcvPrivPasswd_Type = DisplayString
_SnmpTrapRcvPrivPasswd_Object = MibTableColumn
snmpTrapRcvPrivPasswd = _SnmpTrapRcvPrivPasswd_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 12, 22, 1, 20),
    _SnmpTrapRcvPrivPasswd_Type()
)
snmpTrapRcvPrivPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapRcvPrivPasswd.setStatus("mandatory")
_SnmpTrapRcvEngineID_Type = DisplayString
_SnmpTrapRcvEngineID_Object = MibTableColumn
snmpTrapRcvEngineID = _SnmpTrapRcvEngineID_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 12, 22, 1, 21),
    _SnmpTrapRcvEngineID_Type()
)
snmpTrapRcvEngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapRcvEngineID.setStatus("mandatory")
_Dyndns_ObjectIdentity = ObjectIdentity
dyndns = _Dyndns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 13)
)
_DyndnsEnable_Type = Switch
_DyndnsEnable_Object = MibScalar
dyndnsEnable = _DyndnsEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 13, 11),
    _DyndnsEnable_Type()
)
dyndnsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dyndnsEnable.setStatus("mandatory")
_DyndnsDomain_Type = DisplayString
_DyndnsDomain_Object = MibScalar
dyndnsDomain = _DyndnsDomain_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 13, 12),
    _DyndnsDomain_Type()
)
dyndnsDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dyndnsDomain.setStatus("mandatory")
_DyndnsUser_Type = DisplayString
_DyndnsUser_Object = MibScalar
dyndnsUser = _DyndnsUser_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 13, 13),
    _DyndnsUser_Type()
)
dyndnsUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dyndnsUser.setStatus("mandatory")
_DyndnsPassword_Type = DisplayString
_DyndnsPassword_Object = MibScalar
dyndnsPassword = _DyndnsPassword_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 13, 14),
    _DyndnsPassword_Type()
)
dyndnsPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dyndnsPassword.setStatus("mandatory")
_DyndnsEnableCustomProgram_Type = Switch
_DyndnsEnableCustomProgram_Object = MibScalar
dyndnsEnableCustomProgram = _DyndnsEnableCustomProgram_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 13, 15),
    _DyndnsEnableCustomProgram_Type()
)
dyndnsEnableCustomProgram.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dyndnsEnableCustomProgram.setStatus("mandatory")
_DyndnsCustomProgramPath_Type = DisplayString
_DyndnsCustomProgramPath_Object = MibScalar
dyndnsCustomProgramPath = _DyndnsCustomProgramPath_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 13, 16),
    _DyndnsCustomProgramPath_Type()
)
dyndnsCustomProgramPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dyndnsCustomProgramPath.setStatus("mandatory")
_DyndnsEnableKeyOpt_Type = Switch
_DyndnsEnableKeyOpt_Object = MibScalar
dyndnsEnableKeyOpt = _DyndnsEnableKeyOpt_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 13, 17),
    _DyndnsEnableKeyOpt_Type()
)
dyndnsEnableKeyOpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dyndnsEnableKeyOpt.setStatus("mandatory")
_DyndnsUpdateKey_Type = DisplayString
_DyndnsUpdateKey_Object = MibScalar
dyndnsUpdateKey = _DyndnsUpdateKey_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 13, 18),
    _DyndnsUpdateKey_Type()
)
dyndnsUpdateKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dyndnsUpdateKey.setStatus("mandatory")
_DyndnsIPv4Addr_Type = DisplayString
_DyndnsIPv4Addr_Object = MibScalar
dyndnsIPv4Addr = _DyndnsIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 13, 19),
    _DyndnsIPv4Addr_Type()
)
dyndnsIPv4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dyndnsIPv4Addr.setStatus("mandatory")
_DyndnsIPv6Addr_Type = DisplayString
_DyndnsIPv6Addr_Object = MibScalar
dyndnsIPv6Addr = _DyndnsIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 13, 20),
    _DyndnsIPv6Addr_Type()
)
dyndnsIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dyndnsIPv6Addr.setStatus("mandatory")
_Smtp_ObjectIdentity = ObjectIdentity
smtp = _Smtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 14)
)
_SmtpPrimaryEnable_Type = Switch
_SmtpPrimaryEnable_Object = MibScalar
smtpPrimaryEnable = _SmtpPrimaryEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 14, 11),
    _SmtpPrimaryEnable_Type()
)
smtpPrimaryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpPrimaryEnable.setStatus("mandatory")
_SmtpPrimaryAddress_Type = DisplayString
_SmtpPrimaryAddress_Object = MibScalar
smtpPrimaryAddress = _SmtpPrimaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 14, 12),
    _SmtpPrimaryAddress_Type()
)
smtpPrimaryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpPrimaryAddress.setStatus("mandatory")


class _SmtpPrimaryMode_Type(Integer32):
    """Custom type smtpPrimaryMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("woAuth", 1),
          ("popbeforeSMTP", 2),
          ("wAuth", 3))
    )


_SmtpPrimaryMode_Type.__name__ = "Integer32"
_SmtpPrimaryMode_Object = MibScalar
smtpPrimaryMode = _SmtpPrimaryMode_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 14, 13),
    _SmtpPrimaryMode_Type()
)
smtpPrimaryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpPrimaryMode.setStatus("mandatory")
_SmtpPrimaryUser_Type = DisplayString
_SmtpPrimaryUser_Object = MibScalar
smtpPrimaryUser = _SmtpPrimaryUser_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 14, 14),
    _SmtpPrimaryUser_Type()
)
smtpPrimaryUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpPrimaryUser.setStatus("mandatory")
_SmtpPrimaryPassword_Type = DisplayString
_SmtpPrimaryPassword_Object = MibScalar
smtpPrimaryPassword = _SmtpPrimaryPassword_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 14, 15),
    _SmtpPrimaryPassword_Type()
)
smtpPrimaryPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpPrimaryPassword.setStatus("mandatory")
_SmtpSecondaryEnable_Type = Switch
_SmtpSecondaryEnable_Object = MibScalar
smtpSecondaryEnable = _SmtpSecondaryEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 14, 16),
    _SmtpSecondaryEnable_Type()
)
smtpSecondaryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpSecondaryEnable.setStatus("mandatory")
_SmtpSecondaryAddress_Type = DisplayString
_SmtpSecondaryAddress_Object = MibScalar
smtpSecondaryAddress = _SmtpSecondaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 14, 17),
    _SmtpSecondaryAddress_Type()
)
smtpSecondaryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpSecondaryAddress.setStatus("mandatory")


class _SmtpSecondaryMode_Type(Integer32):
    """Custom type smtpSecondaryMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("woAuth", 1),
          ("popbeforeSMTP", 2),
          ("wAuth", 3))
    )


_SmtpSecondaryMode_Type.__name__ = "Integer32"
_SmtpSecondaryMode_Object = MibScalar
smtpSecondaryMode = _SmtpSecondaryMode_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 14, 18),
    _SmtpSecondaryMode_Type()
)
smtpSecondaryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpSecondaryMode.setStatus("mandatory")
_SmtpSecondaryUser_Type = DisplayString
_SmtpSecondaryUser_Object = MibScalar
smtpSecondaryUser = _SmtpSecondaryUser_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 14, 19),
    _SmtpSecondaryUser_Type()
)
smtpSecondaryUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpSecondaryUser.setStatus("mandatory")
_SmtpSecondaryPassword_Type = DisplayString
_SmtpSecondaryPassword_Object = MibScalar
smtpSecondaryPassword = _SmtpSecondaryPassword_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 14, 20),
    _SmtpSecondaryPassword_Type()
)
smtpSecondaryPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpSecondaryPassword.setStatus("mandatory")
_SmtpFromAddress_Type = DisplayString
_SmtpFromAddress_Object = MibScalar
smtpFromAddress = _SmtpFromAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 14, 21),
    _SmtpFromAddress_Type()
)
smtpFromAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpFromAddress.setStatus("mandatory")
_Ipfilter_ObjectIdentity = ObjectIdentity
ipfilter = _Ipfilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 15)
)
_IpfilterTable_Object = MibTable
ipfilterTable = _IpfilterTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 15, 14)
)
if mibBuilder.loadTexts:
    ipfilterTable.setStatus("mandatory")
_IpfilterEntry_Object = MibTableRow
ipfilterEntry = _IpfilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 15, 14, 1)
)
ipfilterEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "ipfilterIndex"),
)
if mibBuilder.loadTexts:
    ipfilterEntry.setStatus("mandatory")
_IpfilterIndex_Type = Integer32
_IpfilterIndex_Object = MibTableColumn
ipfilterIndex = _IpfilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 15, 14, 1, 11),
    _IpfilterIndex_Type()
)
ipfilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfilterIndex.setStatus("mandatory")
_IpfilterIface_Type = DisplayString
_IpfilterIface_Object = MibTableColumn
ipfilterIface = _IpfilterIface_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 15, 14, 1, 12),
    _IpfilterIface_Type()
)
ipfilterIface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipfilterIface.setStatus("mandatory")


class _IpfilterOpt_Type(Integer32):
    """Custom type ipfilterOpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("invert", 1))
    )


_IpfilterOpt_Type.__name__ = "Integer32"
_IpfilterOpt_Object = MibTableColumn
ipfilterOpt = _IpfilterOpt_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 15, 14, 1, 13),
    _IpfilterOpt_Type()
)
ipfilterOpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipfilterOpt.setStatus("mandatory")
_IpfilterIPMask_Type = DisplayString
_IpfilterIPMask_Object = MibTableColumn
ipfilterIPMask = _IpfilterIPMask_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 15, 14, 1, 14),
    _IpfilterIPMask_Type()
)
ipfilterIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipfilterIPMask.setStatus("mandatory")
_IpfilterPort_Type = DisplayString
_IpfilterPort_Object = MibTableColumn
ipfilterPort = _IpfilterPort_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 15, 14, 1, 15),
    _IpfilterPort_Type()
)
ipfilterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipfilterPort.setStatus("mandatory")
_IpfilterRule_Type = DisplayString
_IpfilterRule_Object = MibTableColumn
ipfilterRule = _IpfilterRule_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 15, 14, 1, 16),
    _IpfilterRule_Type()
)
ipfilterRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipfilterRule.setStatus("mandatory")


class _IpfilterProtocol_Type(Integer32):
    """Custom type ipfilterProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2),
          ("icmp", 3),
          ("http", 4),
          ("https", 5),
          ("telnet", 6),
          ("ssh", 7),
          ("port", 100),
          ("cluster", 200))
    )


_IpfilterProtocol_Type.__name__ = "Integer32"
_IpfilterProtocol_Object = MibTableColumn
ipfilterProtocol = _IpfilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 15, 14, 1, 17),
    _IpfilterProtocol_Type()
)
ipfilterProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipfilterProtocol.setStatus("mandatory")
_IpfilterAddRow_Type = Action
_IpfilterAddRow_Object = MibTableColumn
ipfilterAddRow = _IpfilterAddRow_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 15, 14, 1, 18),
    _IpfilterAddRow_Type()
)
ipfilterAddRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipfilterAddRow.setStatus("mandatory")
_IpfilterDeleteRow_Type = Action
_IpfilterDeleteRow_Object = MibTableColumn
ipfilterDeleteRow = _IpfilterDeleteRow_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 15, 14, 1, 19),
    _IpfilterDeleteRow_Type()
)
ipfilterDeleteRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipfilterDeleteRow.setStatus("mandatory")
_Nfs_ObjectIdentity = ObjectIdentity
nfs = _Nfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17)
)
_NfsPrimaryEnable_Type = Switch
_NfsPrimaryEnable_Object = MibScalar
nfsPrimaryEnable = _NfsPrimaryEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 11),
    _NfsPrimaryEnable_Type()
)
nfsPrimaryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsPrimaryEnable.setStatus("mandatory")
_NfsPrimaryAddress_Type = DisplayString
_NfsPrimaryAddress_Object = MibScalar
nfsPrimaryAddress = _NfsPrimaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 12),
    _NfsPrimaryAddress_Type()
)
nfsPrimaryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsPrimaryAddress.setStatus("mandatory")
_NfsPrimaryExported_Type = DisplayString
_NfsPrimaryExported_Object = MibScalar
nfsPrimaryExported = _NfsPrimaryExported_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 13),
    _NfsPrimaryExported_Type()
)
nfsPrimaryExported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsPrimaryExported.setStatus("mandatory")
_NfsPrimaryTimeout_Type = Integer32
_NfsPrimaryTimeout_Object = MibScalar
nfsPrimaryTimeout = _NfsPrimaryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 14),
    _NfsPrimaryTimeout_Type()
)
nfsPrimaryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsPrimaryTimeout.setStatus("mandatory")
_NfsPrimaryRetryInterval_Type = Integer32
_NfsPrimaryRetryInterval_Object = MibScalar
nfsPrimaryRetryInterval = _NfsPrimaryRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 15),
    _NfsPrimaryRetryInterval_Type()
)
nfsPrimaryRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsPrimaryRetryInterval.setStatus("mandatory")
_NfsPrimaryEnableEncrypt_Type = Switch
_NfsPrimaryEnableEncrypt_Object = MibScalar
nfsPrimaryEnableEncrypt = _NfsPrimaryEnableEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 16),
    _NfsPrimaryEnableEncrypt_Type()
)
nfsPrimaryEnableEncrypt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsPrimaryEnableEncrypt.setStatus("mandatory")
_NfsPrimaryUser_Type = DisplayString
_NfsPrimaryUser_Object = MibScalar
nfsPrimaryUser = _NfsPrimaryUser_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 17),
    _NfsPrimaryUser_Type()
)
nfsPrimaryUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsPrimaryUser.setStatus("mandatory")
_NfsPrimaryPassword_Type = DisplayString
_NfsPrimaryPassword_Object = MibScalar
nfsPrimaryPassword = _NfsPrimaryPassword_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 18),
    _NfsPrimaryPassword_Type()
)
nfsPrimaryPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsPrimaryPassword.setStatus("mandatory")
_NfsSecondaryEnable_Type = Switch
_NfsSecondaryEnable_Object = MibScalar
nfsSecondaryEnable = _NfsSecondaryEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 19),
    _NfsSecondaryEnable_Type()
)
nfsSecondaryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsSecondaryEnable.setStatus("mandatory")
_NfsSecondaryAddress_Type = DisplayString
_NfsSecondaryAddress_Object = MibScalar
nfsSecondaryAddress = _NfsSecondaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 20),
    _NfsSecondaryAddress_Type()
)
nfsSecondaryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsSecondaryAddress.setStatus("mandatory")
_NfsSecondaryExported_Type = DisplayString
_NfsSecondaryExported_Object = MibScalar
nfsSecondaryExported = _NfsSecondaryExported_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 21),
    _NfsSecondaryExported_Type()
)
nfsSecondaryExported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsSecondaryExported.setStatus("mandatory")
_NfsSecondaryTimeout_Type = Integer32
_NfsSecondaryTimeout_Object = MibScalar
nfsSecondaryTimeout = _NfsSecondaryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 22),
    _NfsSecondaryTimeout_Type()
)
nfsSecondaryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsSecondaryTimeout.setStatus("mandatory")
_NfsSecondaryRetryInterval_Type = Integer32
_NfsSecondaryRetryInterval_Object = MibScalar
nfsSecondaryRetryInterval = _NfsSecondaryRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 23),
    _NfsSecondaryRetryInterval_Type()
)
nfsSecondaryRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsSecondaryRetryInterval.setStatus("mandatory")
_NfsSecondaryEnableEncrypt_Type = Switch
_NfsSecondaryEnableEncrypt_Object = MibScalar
nfsSecondaryEnableEncrypt = _NfsSecondaryEnableEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 24),
    _NfsSecondaryEnableEncrypt_Type()
)
nfsSecondaryEnableEncrypt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsSecondaryEnableEncrypt.setStatus("mandatory")
_NfsSecondaryUser_Type = DisplayString
_NfsSecondaryUser_Object = MibScalar
nfsSecondaryUser = _NfsSecondaryUser_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 25),
    _NfsSecondaryUser_Type()
)
nfsSecondaryUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsSecondaryUser.setStatus("mandatory")
_NfsSecondaryPassword_Type = DisplayString
_NfsSecondaryPassword_Object = MibScalar
nfsSecondaryPassword = _NfsSecondaryPassword_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 26),
    _NfsSecondaryPassword_Type()
)
nfsSecondaryPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsSecondaryPassword.setStatus("mandatory")
_NfsMailEnable_Type = Switch
_NfsMailEnable_Object = MibScalar
nfsMailEnable = _NfsMailEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 27),
    _NfsMailEnable_Type()
)
nfsMailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsMailEnable.setStatus("mandatory")
_NfsMailTitle_Type = DisplayString
_NfsMailTitle_Object = MibScalar
nfsMailTitle = _NfsMailTitle_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 28),
    _NfsMailTitle_Type()
)
nfsMailTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsMailTitle.setStatus("mandatory")
_NfsMailto_Type = DisplayString
_NfsMailto_Object = MibScalar
nfsMailto = _NfsMailto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 29),
    _NfsMailto_Type()
)
nfsMailto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsMailto.setStatus("mandatory")
_NfsTrapEnable_Type = Switch
_NfsTrapEnable_Object = MibScalar
nfsTrapEnable = _NfsTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 30),
    _NfsTrapEnable_Type()
)
nfsTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsTrapEnable.setStatus("mandatory")
_NfsTrapToGlobal_Type = Switch
_NfsTrapToGlobal_Object = MibScalar
nfsTrapToGlobal = _NfsTrapToGlobal_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 31),
    _NfsTrapToGlobal_Type()
)
nfsTrapToGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsTrapToGlobal.setStatus("mandatory")
_NfsTrapRcvTable_Object = MibTable
nfsTrapRcvTable = _NfsTrapRcvTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 32)
)
if mibBuilder.loadTexts:
    nfsTrapRcvTable.setStatus("mandatory")
_NfsTrapRcvEntry_Object = MibTableRow
nfsTrapRcvEntry = _NfsTrapRcvEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 32, 1)
)
nfsTrapRcvEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "nfsTrapRcvIndex"),
)
if mibBuilder.loadTexts:
    nfsTrapRcvEntry.setStatus("mandatory")


class _NfsTrapRcvIndex_Type(Integer32):
    """Custom type nfsTrapRcvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_NfsTrapRcvIndex_Type.__name__ = "Integer32"
_NfsTrapRcvIndex_Object = MibTableColumn
nfsTrapRcvIndex = _NfsTrapRcvIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 32, 1, 11),
    _NfsTrapRcvIndex_Type()
)
nfsTrapRcvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsTrapRcvIndex.setStatus("mandatory")
_NfsTrapRcvIP_Type = DisplayString
_NfsTrapRcvIP_Object = MibTableColumn
nfsTrapRcvIP = _NfsTrapRcvIP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 32, 1, 12),
    _NfsTrapRcvIP_Type()
)
nfsTrapRcvIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsTrapRcvIP.setStatus("mandatory")
_NfsTrapRcvComm_Type = DisplayString
_NfsTrapRcvComm_Object = MibTableColumn
nfsTrapRcvComm = _NfsTrapRcvComm_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 32, 1, 13),
    _NfsTrapRcvComm_Type()
)
nfsTrapRcvComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsTrapRcvComm.setStatus("mandatory")


class _NfsTrapRcvVer_Type(Integer32):
    """Custom type nfsTrapRcvVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 0),
          ("v2c", 1),
          ("v3", 2))
    )


_NfsTrapRcvVer_Type.__name__ = "Integer32"
_NfsTrapRcvVer_Object = MibTableColumn
nfsTrapRcvVer = _NfsTrapRcvVer_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 32, 1, 14),
    _NfsTrapRcvVer_Type()
)
nfsTrapRcvVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsTrapRcvVer.setStatus("mandatory")
_NfsTrapRcvUserName_Type = DisplayString
_NfsTrapRcvUserName_Object = MibTableColumn
nfsTrapRcvUserName = _NfsTrapRcvUserName_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 32, 1, 15),
    _NfsTrapRcvUserName_Type()
)
nfsTrapRcvUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsTrapRcvUserName.setStatus("mandatory")


class _NfsTrapRcvSecurityLevel_Type(Integer32):
    """Custom type nfsTrapRcvSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAuthNoPriv", 0),
          ("authNoPriv", 1),
          ("authPriv", 2))
    )


_NfsTrapRcvSecurityLevel_Type.__name__ = "Integer32"
_NfsTrapRcvSecurityLevel_Object = MibTableColumn
nfsTrapRcvSecurityLevel = _NfsTrapRcvSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 32, 1, 16),
    _NfsTrapRcvSecurityLevel_Type()
)
nfsTrapRcvSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsTrapRcvSecurityLevel.setStatus("mandatory")


class _NfsTrapRcvAuthProto_Type(Integer32):
    """Custom type nfsTrapRcvAuthProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("md5", 0),
          ("sha", 1))
    )


_NfsTrapRcvAuthProto_Type.__name__ = "Integer32"
_NfsTrapRcvAuthProto_Object = MibTableColumn
nfsTrapRcvAuthProto = _NfsTrapRcvAuthProto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 32, 1, 17),
    _NfsTrapRcvAuthProto_Type()
)
nfsTrapRcvAuthProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsTrapRcvAuthProto.setStatus("mandatory")
_NfsTrapRcvAuthPasswd_Type = DisplayString
_NfsTrapRcvAuthPasswd_Object = MibTableColumn
nfsTrapRcvAuthPasswd = _NfsTrapRcvAuthPasswd_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 32, 1, 18),
    _NfsTrapRcvAuthPasswd_Type()
)
nfsTrapRcvAuthPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsTrapRcvAuthPasswd.setStatus("mandatory")


class _NfsTrapRcvPrivProto_Type(Integer32):
    """Custom type nfsTrapRcvPrivProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("des", 0),
          ("aes", 1))
    )


_NfsTrapRcvPrivProto_Type.__name__ = "Integer32"
_NfsTrapRcvPrivProto_Object = MibTableColumn
nfsTrapRcvPrivProto = _NfsTrapRcvPrivProto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 32, 1, 19),
    _NfsTrapRcvPrivProto_Type()
)
nfsTrapRcvPrivProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsTrapRcvPrivProto.setStatus("mandatory")
_NfsTrapRcvPrivPasswd_Type = DisplayString
_NfsTrapRcvPrivPasswd_Object = MibTableColumn
nfsTrapRcvPrivPasswd = _NfsTrapRcvPrivPasswd_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 32, 1, 20),
    _NfsTrapRcvPrivPasswd_Type()
)
nfsTrapRcvPrivPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsTrapRcvPrivPasswd.setStatus("mandatory")
_NfsTrapRcvEngineID_Type = DisplayString
_NfsTrapRcvEngineID_Object = MibTableColumn
nfsTrapRcvEngineID = _NfsTrapRcvEngineID_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 17, 32, 1, 21),
    _NfsTrapRcvEngineID_Type()
)
nfsTrapRcvEngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfsTrapRcvEngineID.setStatus("mandatory")
_Web_ObjectIdentity = ObjectIdentity
web = _Web_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 18)
)
_WebRefreshRate_Type = Integer32
_WebRefreshRate_Object = MibScalar
webRefreshRate = _WebRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 18, 11),
    _WebRefreshRate_Type()
)
webRefreshRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webRefreshRate.setStatus("mandatory")
_WebLoginTimeout_Type = Integer32
_WebLoginTimeout_Object = MibScalar
webLoginTimeout = _WebLoginTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 18, 12),
    _WebLoginTimeout_Type()
)
webLoginTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webLoginTimeout.setStatus("mandatory")


class _WebAuthMethod_Type(Integer32):
    """Custom type webAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              11,
              12,
              13,
              14,
              21,
              22,
              23,
              24,
              31,
              32,
              33,
              34,
              41,
              42,
              43,
              101)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("radius", 11),
          ("radiuslocal", 12),
          ("localradius", 13),
          ("radiusdownlocal", 14),
          ("tacacs", 21),
          ("tacacslocal", 22),
          ("localtacacs", 23),
          ("tacasdownlocal", 24),
          ("ldap", 31),
          ("ldaplocal", 32),
          ("localldap", 33),
          ("ldapdownlocal", 34),
          ("kerberos", 41),
          ("kerberoslocal", 42),
          ("localkerberos", 43),
          ("custom", 101))
    )


_WebAuthMethod_Type.__name__ = "Integer32"
_WebAuthMethod_Object = MibScalar
webAuthMethod = _WebAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 18, 13),
    _WebAuthMethod_Type()
)
webAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webAuthMethod.setStatus("mandatory")
_WebAuthPrimaryIPAddress_Type = DisplayString
_WebAuthPrimaryIPAddress_Object = MibScalar
webAuthPrimaryIPAddress = _WebAuthPrimaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 18, 14),
    _WebAuthPrimaryIPAddress_Type()
)
webAuthPrimaryIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webAuthPrimaryIPAddress.setStatus("mandatory")
_WebAuthSecondaryIPAddress_Type = DisplayString
_WebAuthSecondaryIPAddress_Object = MibScalar
webAuthSecondaryIPAddress = _WebAuthSecondaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 18, 15),
    _WebAuthSecondaryIPAddress_Type()
)
webAuthSecondaryIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webAuthSecondaryIPAddress.setStatus("mandatory")
_WebAuthSecret_Type = DisplayString
_WebAuthSecret_Object = MibScalar
webAuthSecret = _WebAuthSecret_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 18, 16),
    _WebAuthSecret_Type()
)
webAuthSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webAuthSecret.setStatus("mandatory")
_WebAuthTimeout_Type = Integer32
_WebAuthTimeout_Object = MibScalar
webAuthTimeout = _WebAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 18, 17),
    _WebAuthTimeout_Type()
)
webAuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webAuthTimeout.setStatus("mandatory")
_WebAuthRetries_Type = Integer32
_WebAuthRetries_Object = MibScalar
webAuthRetries = _WebAuthRetries_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 18, 18),
    _WebAuthRetries_Type()
)
webAuthRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webAuthRetries.setStatus("mandatory")
_WebAuthLDAPSearchBase_Type = DisplayString
_WebAuthLDAPSearchBase_Object = MibScalar
webAuthLDAPSearchBase = _WebAuthLDAPSearchBase_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 18, 19),
    _WebAuthLDAPSearchBase_Type()
)
webAuthLDAPSearchBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webAuthLDAPSearchBase.setStatus("mandatory")
_WebAuthLDAPActiveDirectoryDomain_Type = DisplayString
_WebAuthLDAPActiveDirectoryDomain_Object = MibScalar
webAuthLDAPActiveDirectoryDomain = _WebAuthLDAPActiveDirectoryDomain_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 18, 20),
    _WebAuthLDAPActiveDirectoryDomain_Type()
)
webAuthLDAPActiveDirectoryDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webAuthLDAPActiveDirectoryDomain.setStatus("mandatory")
_WebAuthKRBPrimaryRealm_Type = DisplayString
_WebAuthKRBPrimaryRealm_Object = MibScalar
webAuthKRBPrimaryRealm = _WebAuthKRBPrimaryRealm_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 18, 21),
    _WebAuthKRBPrimaryRealm_Type()
)
webAuthKRBPrimaryRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webAuthKRBPrimaryRealm.setStatus("mandatory")
_WebAuthKRBSecondaryRealm_Type = DisplayString
_WebAuthKRBSecondaryRealm_Object = MibScalar
webAuthKRBSecondaryRealm = _WebAuthKRBSecondaryRealm_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 18, 22),
    _WebAuthKRBSecondaryRealm_Type()
)
webAuthKRBSecondaryRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webAuthKRBSecondaryRealm.setStatus("mandatory")


class _WebRootAccessEnable_Type(Integer32):
    """Custom type webRootAccessEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("on", 0),
          ("off", 1))
    )


_WebRootAccessEnable_Type.__name__ = "Integer32"
_WebRootAccessEnable_Object = MibScalar
webRootAccessEnable = _WebRootAccessEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 18, 23),
    _WebRootAccessEnable_Type()
)
webRootAccessEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webRootAccessEnable.setStatus("mandatory")
_WebSerialPortsCountsOnConnectionPage_Type = Integer32
_WebSerialPortsCountsOnConnectionPage_Object = MibScalar
webSerialPortsCountsOnConnectionPage = _WebSerialPortsCountsOnConnectionPage_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 18, 24),
    _WebSerialPortsCountsOnConnectionPage_Type()
)
webSerialPortsCountsOnConnectionPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webSerialPortsCountsOnConnectionPage.setStatus("mandatory")


class _WebAppletOption_Type(Integer32):
    """Custom type webAppletOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("builtinSSH2", 0),
          ("builtinSSH1", 1),
          ("userdefined", 2))
    )


_WebAppletOption_Type.__name__ = "Integer32"
_WebAppletOption_Object = MibScalar
webAppletOption = _WebAppletOption_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 18, 25),
    _WebAppletOption_Type()
)
webAppletOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webAppletOption.setStatus("mandatory")
_WebHttpPort_Type = Integer32
_WebHttpPort_Object = MibScalar
webHttpPort = _WebHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 18, 26),
    _WebHttpPort_Type()
)
webHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webHttpPort.setStatus("mandatory")
_WebHttpsPort_Type = Integer32
_WebHttpsPort_Object = MibScalar
webHttpsPort = _WebHttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 18, 27),
    _WebHttpsPort_Type()
)
webHttpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webHttpsPort.setStatus("mandatory")
_WebBlockingTime_Type = Integer32
_WebBlockingTime_Object = MibScalar
webBlockingTime = _WebBlockingTime_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 18, 28),
    _WebBlockingTime_Type()
)
webBlockingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webBlockingTime.setStatus("mandatory")
_WebAuthAuthorService_Type = DisplayString
_WebAuthAuthorService_Object = MibScalar
webAuthAuthorService = _WebAuthAuthorService_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 18, 29),
    _WebAuthAuthorService_Type()
)
webAuthAuthorService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webAuthAuthorService.setStatus("mandatory")


class _WebAuthLdapSecure_Type(Integer32):
    """Custom type webAuthLdapSecure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("starttls", 1))
    )


_WebAuthLdapSecure_Type.__name__ = "Integer32"
_WebAuthLdapSecure_Object = MibScalar
webAuthLdapSecure = _WebAuthLdapSecure_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 18, 30),
    _WebAuthLdapSecure_Type()
)
webAuthLdapSecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webAuthLdapSecure.setStatus("mandatory")
_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 19)
)
_EthernetMode_Type = DisplayString
_EthernetMode_Object = MibScalar
ethernetMode = _EthernetMode_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 19, 11),
    _EthernetMode_Type()
)
ethernetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetMode.setStatus("mandatory")
_TcpOther_ObjectIdentity = ObjectIdentity
tcpOther = _TcpOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 20)
)
_TcpOtherKeepAliveIdle_Type = Integer32
_TcpOtherKeepAliveIdle_Object = MibScalar
tcpOtherKeepAliveIdle = _TcpOtherKeepAliveIdle_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 20, 11),
    _TcpOtherKeepAliveIdle_Type()
)
tcpOtherKeepAliveIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpOtherKeepAliveIdle.setStatus("mandatory")
_TcpOtherKeepAliveProbe_Type = Integer32
_TcpOtherKeepAliveProbe_Object = MibScalar
tcpOtherKeepAliveProbe = _TcpOtherKeepAliveProbe_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 20, 12),
    _TcpOtherKeepAliveProbe_Type()
)
tcpOtherKeepAliveProbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpOtherKeepAliveProbe.setStatus("mandatory")
_TcpOtherKeepAliveInterval_Type = Integer32
_TcpOtherKeepAliveInterval_Object = MibScalar
tcpOtherKeepAliveInterval = _TcpOtherKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 20, 13),
    _TcpOtherKeepAliveInterval_Type()
)
tcpOtherKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpOtherKeepAliveInterval.setStatus("mandatory")
_TcpOtherReverseDNSLookup_Type = Switch
_TcpOtherReverseDNSLookup_Object = MibScalar
tcpOtherReverseDNSLookup = _TcpOtherReverseDNSLookup_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 20, 14),
    _TcpOtherReverseDNSLookup_Type()
)
tcpOtherReverseDNSLookup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpOtherReverseDNSLookup.setStatus("mandatory")
_TcpOtherIPv4Forward_Type = Switch
_TcpOtherIPv4Forward_Object = MibScalar
tcpOtherIPv4Forward = _TcpOtherIPv4Forward_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 20, 15),
    _TcpOtherIPv4Forward_Type()
)
tcpOtherIPv4Forward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpOtherIPv4Forward.setStatus("mandatory")
_Ppp_ObjectIdentity = ObjectIdentity
ppp = _Ppp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 21)
)
_PppEnableDynamicPool_Type = Switch
_PppEnableDynamicPool_Object = MibScalar
pppEnableDynamicPool = _PppEnableDynamicPool_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 21, 11),
    _PppEnableDynamicPool_Type()
)
pppEnableDynamicPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppEnableDynamicPool.setStatus("mandatory")
_PppIpAddr_Type = DisplayString
_PppIpAddr_Object = MibScalar
pppIpAddr = _PppIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 21, 12),
    _PppIpAddr_Type()
)
pppIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppIpAddr.setStatus("mandatory")
_PppNumOfAddr_Type = Integer32
_PppNumOfAddr_Object = MibScalar
pppNumOfAddr = _PppNumOfAddr_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 21, 13),
    _PppNumOfAddr_Type()
)
pppNumOfAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppNumOfAddr.setStatus("mandatory")
_PppIncommingTable_Object = MibTable
pppIncommingTable = _PppIncommingTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 21, 14)
)
if mibBuilder.loadTexts:
    pppIncommingTable.setStatus("mandatory")
_PppIncommingEntry_Object = MibTableRow
pppIncommingEntry = _PppIncommingEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 21, 14, 1)
)
pppIncommingEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "pppIncommingIndex"),
)
if mibBuilder.loadTexts:
    pppIncommingEntry.setStatus("mandatory")
_PppIncommingIndex_Type = Integer32
_PppIncommingIndex_Object = MibTableColumn
pppIncommingIndex = _PppIncommingIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 21, 14, 1, 11),
    _PppIncommingIndex_Type()
)
pppIncommingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppIncommingIndex.setStatus("mandatory")
_PppUsername_Type = DisplayString
_PppUsername_Object = MibTableColumn
pppUsername = _PppUsername_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 21, 14, 1, 12),
    _PppUsername_Type()
)
pppUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppUsername.setStatus("mandatory")
_PppPassword_Type = DisplayString
_PppPassword_Object = MibTableColumn
pppPassword = _PppPassword_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 21, 14, 1, 13),
    _PppPassword_Type()
)
pppPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppPassword.setStatus("mandatory")


class _PppAuthentication_Type(Integer32):
    """Custom type pppAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chapPap", 0),
          ("chap", 1),
          ("pap", 2),
          ("cleartext", 3))
    )


_PppAuthentication_Type.__name__ = "Integer32"
_PppAuthentication_Object = MibTableColumn
pppAuthentication = _PppAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 21, 14, 1, 14),
    _PppAuthentication_Type()
)
pppAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppAuthentication.setStatus("mandatory")


class _PppPeerOpt_Type(Integer32):
    """Custom type pppPeerOpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automaticallyAssignRemoteIPAddressFromIPAddressPool", 0),
          ("allowRemotePeerToSpecifyRemoteIPAddress", 1),
          ("assignStaticRemoteIPAddress", 2))
    )


_PppPeerOpt_Type.__name__ = "Integer32"
_PppPeerOpt_Object = MibTableColumn
pppPeerOpt = _PppPeerOpt_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 21, 14, 1, 15),
    _PppPeerOpt_Type()
)
pppPeerOpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppPeerOpt.setStatus("mandatory")
_PppRemoteIP_Type = DisplayString
_PppRemoteIP_Object = MibTableColumn
pppRemoteIP = _PppRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 21, 14, 1, 16),
    _PppRemoteIP_Type()
)
pppRemoteIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppRemoteIP.setStatus("mandatory")
_PppAllowClientAccess_Type = Switch
_PppAllowClientAccess_Object = MibTableColumn
pppAllowClientAccess = _PppAllowClientAccess_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 21, 14, 1, 17),
    _PppAllowClientAccess_Type()
)
pppAllowClientAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppAllowClientAccess.setStatus("mandatory")


class _PppLocalPeerOpt_Type(Integer32):
    """Custom type pppLocalPeerOpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("automaticallyAssignLocalIpAddressFromIpAddressPool", 0),
          ("assignStaticLocalIpAddress", 1))
    )


_PppLocalPeerOpt_Type.__name__ = "Integer32"
_PppLocalPeerOpt_Object = MibTableColumn
pppLocalPeerOpt = _PppLocalPeerOpt_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 21, 14, 1, 18),
    _PppLocalPeerOpt_Type()
)
pppLocalPeerOpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLocalPeerOpt.setStatus("mandatory")
_PppLocalIP_Type = DisplayString
_PppLocalIP_Object = MibTableColumn
pppLocalIP = _PppLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 21, 14, 1, 19),
    _PppLocalIP_Type()
)
pppLocalIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLocalIP.setStatus("mandatory")
_PppEnableIdleTimeout_Type = Switch
_PppEnableIdleTimeout_Object = MibTableColumn
pppEnableIdleTimeout = _PppEnableIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 21, 14, 1, 20),
    _PppEnableIdleTimeout_Type()
)
pppEnableIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppEnableIdleTimeout.setStatus("mandatory")
_PppTimeout_Type = Integer32
_PppTimeout_Object = MibTableColumn
pppTimeout = _PppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 21, 14, 1, 21),
    _PppTimeout_Type()
)
pppTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppTimeout.setStatus("mandatory")
_PppAddRow_Type = Action
_PppAddRow_Object = MibTableColumn
pppAddRow = _PppAddRow_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 21, 14, 1, 22),
    _PppAddRow_Type()
)
pppAddRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppAddRow.setStatus("mandatory")
_PppDelRow_Type = Action
_PppDelRow_Object = MibTableColumn
pppDelRow = _PppDelRow_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 21, 14, 1, 23),
    _PppDelRow_Type()
)
pppDelRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppDelRow.setStatus("mandatory")
_PppProccessArpRequest_Type = Switch
_PppProccessArpRequest_Object = MibScalar
pppProccessArpRequest = _PppProccessArpRequest_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 21, 15),
    _PppProccessArpRequest_Type()
)
pppProccessArpRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppProccessArpRequest.setStatus("mandatory")
_Samba_ObjectIdentity = ObjectIdentity
samba = _Samba_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 23)
)
_SambaEnableService_Type = Switch
_SambaEnableService_Object = MibScalar
sambaEnableService = _SambaEnableService_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 23, 11),
    _SambaEnableService_Type()
)
sambaEnableService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sambaEnableService.setStatus("mandatory")
_SambaServerName_Type = DisplayString
_SambaServerName_Object = MibScalar
sambaServerName = _SambaServerName_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 23, 12),
    _SambaServerName_Type()
)
sambaServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sambaServerName.setStatus("mandatory")
_SambaMountPath_Type = DisplayString
_SambaMountPath_Object = MibScalar
sambaMountPath = _SambaMountPath_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 23, 13),
    _SambaMountPath_Type()
)
sambaMountPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sambaMountPath.setStatus("mandatory")


class _SambaTimeout_Type(Integer32):
    """Custom type sambaTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_SambaTimeout_Type.__name__ = "Integer32"
_SambaTimeout_Object = MibScalar
sambaTimeout = _SambaTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 23, 14),
    _SambaTimeout_Type()
)
sambaTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sambaTimeout.setStatus("mandatory")


class _SambaInterval_Type(Integer32):
    """Custom type sambaInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_SambaInterval_Type.__name__ = "Integer32"
_SambaInterval_Object = MibScalar
sambaInterval = _SambaInterval_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 23, 15),
    _SambaInterval_Type()
)
sambaInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sambaInterval.setStatus("mandatory")
_SambaServerUser_Type = DisplayString
_SambaServerUser_Object = MibScalar
sambaServerUser = _SambaServerUser_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 23, 16),
    _SambaServerUser_Type()
)
sambaServerUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sambaServerUser.setStatus("mandatory")
_SambaServerPassword_Type = DisplayString
_SambaServerPassword_Object = MibScalar
sambaServerPassword = _SambaServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 23, 17),
    _SambaServerPassword_Type()
)
sambaServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sambaServerPassword.setStatus("mandatory")
_SambaEnableEmailAlert_Type = Switch
_SambaEnableEmailAlert_Object = MibScalar
sambaEnableEmailAlert = _SambaEnableEmailAlert_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 23, 18),
    _SambaEnableEmailAlert_Type()
)
sambaEnableEmailAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sambaEnableEmailAlert.setStatus("mandatory")
_SambaEmailTitle_Type = DisplayString
_SambaEmailTitle_Object = MibScalar
sambaEmailTitle = _SambaEmailTitle_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 23, 19),
    _SambaEmailTitle_Type()
)
sambaEmailTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sambaEmailTitle.setStatus("mandatory")
_SambaEmailTo_Type = DisplayString
_SambaEmailTo_Object = MibScalar
sambaEmailTo = _SambaEmailTo_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 23, 20),
    _SambaEmailTo_Type()
)
sambaEmailTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sambaEmailTo.setStatus("mandatory")
_SambaEnableTrap_Type = Switch
_SambaEnableTrap_Object = MibScalar
sambaEnableTrap = _SambaEnableTrap_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 23, 21),
    _SambaEnableTrap_Type()
)
sambaEnableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sambaEnableTrap.setStatus("mandatory")
_SambaTrapToGlobal_Type = Switch
_SambaTrapToGlobal_Object = MibScalar
sambaTrapToGlobal = _SambaTrapToGlobal_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 23, 22),
    _SambaTrapToGlobal_Type()
)
sambaTrapToGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sambaTrapToGlobal.setStatus("mandatory")
_SambaTrapRcvTable_Object = MibTable
sambaTrapRcvTable = _SambaTrapRcvTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 23, 23)
)
if mibBuilder.loadTexts:
    sambaTrapRcvTable.setStatus("mandatory")
_SambaTrapRcvEntry_Object = MibTableRow
sambaTrapRcvEntry = _SambaTrapRcvEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 23, 23, 1)
)
sambaTrapRcvEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "sambaTrapRcvIndex"),
)
if mibBuilder.loadTexts:
    sambaTrapRcvEntry.setStatus("mandatory")


class _SambaTrapRcvIndex_Type(Integer32):
    """Custom type sambaTrapRcvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SambaTrapRcvIndex_Type.__name__ = "Integer32"
_SambaTrapRcvIndex_Object = MibTableColumn
sambaTrapRcvIndex = _SambaTrapRcvIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 23, 23, 1, 11),
    _SambaTrapRcvIndex_Type()
)
sambaTrapRcvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sambaTrapRcvIndex.setStatus("mandatory")
_SambaTrapRcvIP_Type = DisplayString
_SambaTrapRcvIP_Object = MibTableColumn
sambaTrapRcvIP = _SambaTrapRcvIP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 23, 23, 1, 12),
    _SambaTrapRcvIP_Type()
)
sambaTrapRcvIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sambaTrapRcvIP.setStatus("mandatory")
_SambaTrapRcvComm_Type = DisplayString
_SambaTrapRcvComm_Object = MibTableColumn
sambaTrapRcvComm = _SambaTrapRcvComm_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 23, 23, 1, 13),
    _SambaTrapRcvComm_Type()
)
sambaTrapRcvComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sambaTrapRcvComm.setStatus("mandatory")


class _SambaTrapRcvVer_Type(Integer32):
    """Custom type sambaTrapRcvVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 0),
          ("v2c", 1),
          ("v3", 2))
    )


_SambaTrapRcvVer_Type.__name__ = "Integer32"
_SambaTrapRcvVer_Object = MibTableColumn
sambaTrapRcvVer = _SambaTrapRcvVer_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 23, 23, 1, 14),
    _SambaTrapRcvVer_Type()
)
sambaTrapRcvVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sambaTrapRcvVer.setStatus("mandatory")
_SambaTrapRcvUserName_Type = DisplayString
_SambaTrapRcvUserName_Object = MibTableColumn
sambaTrapRcvUserName = _SambaTrapRcvUserName_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 23, 23, 1, 15),
    _SambaTrapRcvUserName_Type()
)
sambaTrapRcvUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sambaTrapRcvUserName.setStatus("mandatory")


class _SambaTrapRcvSecurityLevel_Type(Integer32):
    """Custom type sambaTrapRcvSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAuthNoPriv", 0),
          ("authNoPriv", 1),
          ("authPriv", 2))
    )


_SambaTrapRcvSecurityLevel_Type.__name__ = "Integer32"
_SambaTrapRcvSecurityLevel_Object = MibTableColumn
sambaTrapRcvSecurityLevel = _SambaTrapRcvSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 23, 23, 1, 16),
    _SambaTrapRcvSecurityLevel_Type()
)
sambaTrapRcvSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sambaTrapRcvSecurityLevel.setStatus("mandatory")


class _SambaTrapRcvAuthProto_Type(Integer32):
    """Custom type sambaTrapRcvAuthProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("md5", 0),
          ("sha", 1))
    )


_SambaTrapRcvAuthProto_Type.__name__ = "Integer32"
_SambaTrapRcvAuthProto_Object = MibTableColumn
sambaTrapRcvAuthProto = _SambaTrapRcvAuthProto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 23, 23, 1, 17),
    _SambaTrapRcvAuthProto_Type()
)
sambaTrapRcvAuthProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sambaTrapRcvAuthProto.setStatus("mandatory")
_SambaTrapRcvAuthPasswd_Type = DisplayString
_SambaTrapRcvAuthPasswd_Object = MibTableColumn
sambaTrapRcvAuthPasswd = _SambaTrapRcvAuthPasswd_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 23, 23, 1, 18),
    _SambaTrapRcvAuthPasswd_Type()
)
sambaTrapRcvAuthPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sambaTrapRcvAuthPasswd.setStatus("mandatory")


class _SambaTrapRcvPrivProto_Type(Integer32):
    """Custom type sambaTrapRcvPrivProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("des", 0),
          ("aes", 1))
    )


_SambaTrapRcvPrivProto_Type.__name__ = "Integer32"
_SambaTrapRcvPrivProto_Object = MibTableColumn
sambaTrapRcvPrivProto = _SambaTrapRcvPrivProto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 23, 23, 1, 19),
    _SambaTrapRcvPrivProto_Type()
)
sambaTrapRcvPrivProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sambaTrapRcvPrivProto.setStatus("mandatory")
_SambaTrapRcvPrivPasswd_Type = DisplayString
_SambaTrapRcvPrivPasswd_Object = MibTableColumn
sambaTrapRcvPrivPasswd = _SambaTrapRcvPrivPasswd_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 23, 23, 1, 20),
    _SambaTrapRcvPrivPasswd_Type()
)
sambaTrapRcvPrivPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sambaTrapRcvPrivPasswd.setStatus("mandatory")
_SambaTrapRcvEngineID_Type = DisplayString
_SambaTrapRcvEngineID_Object = MibTableColumn
sambaTrapRcvEngineID = _SambaTrapRcvEngineID_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 27, 23, 23, 1, 21),
    _SambaTrapRcvEngineID_Type()
)
sambaTrapRcvEngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sambaTrapRcvEngineID.setStatus("mandatory")
_SystemLogging_ObjectIdentity = ObjectIdentity
systemLogging = _SystemLogging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 28)
)


class _SystemLoggingStoLoc_Type(Integer32):
    """Custom type systemLoggingStoLoc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("memory", 1),
          ("cfcard", 2),
          ("nfs", 3),
          ("usb", 4),
          ("samba", 10))
    )


_SystemLoggingStoLoc_Type.__name__ = "Integer32"
_SystemLoggingStoLoc_Object = MibScalar
systemLoggingStoLoc = _SystemLoggingStoLoc_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 28, 12),
    _SystemLoggingStoLoc_Type()
)
systemLoggingStoLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLoggingStoLoc.setStatus("mandatory")
_SystemLoggingBufferSize_Type = Integer32
_SystemLoggingBufferSize_Object = MibScalar
systemLoggingBufferSize = _SystemLoggingBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 28, 14),
    _SystemLoggingBufferSize_Type()
)
systemLoggingBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLoggingBufferSize.setStatus("mandatory")
_SystemLoggingFilename_Type = DisplayString
_SystemLoggingFilename_Object = MibScalar
systemLoggingFilename = _SystemLoggingFilename_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 28, 15),
    _SystemLoggingFilename_Type()
)
systemLoggingFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLoggingFilename.setStatus("mandatory")
_SystemLoggingBackupOnMount_Type = Switch
_SystemLoggingBackupOnMount_Object = MibScalar
systemLoggingBackupOnMount = _SystemLoggingBackupOnMount_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 28, 16),
    _SystemLoggingBackupOnMount_Type()
)
systemLoggingBackupOnMount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLoggingBackupOnMount.setStatus("mandatory")
_SystemLoggingMailEnable_Type = Switch
_SystemLoggingMailEnable_Object = MibScalar
systemLoggingMailEnable = _SystemLoggingMailEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 28, 17),
    _SystemLoggingMailEnable_Type()
)
systemLoggingMailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLoggingMailEnable.setStatus("mandatory")
_SystemLoggingMailMessageNum_Type = Integer32
_SystemLoggingMailMessageNum_Object = MibScalar
systemLoggingMailMessageNum = _SystemLoggingMailMessageNum_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 28, 18),
    _SystemLoggingMailMessageNum_Type()
)
systemLoggingMailMessageNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLoggingMailMessageNum.setStatus("mandatory")
_SystemLoggingMailto_Type = DisplayString
_SystemLoggingMailto_Object = MibScalar
systemLoggingMailto = _SystemLoggingMailto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 28, 19),
    _SystemLoggingMailto_Type()
)
systemLoggingMailto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLoggingMailto.setStatus("mandatory")
_AccesslistTable_Object = MibTable
accesslistTable = _AccesslistTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 29)
)
if mibBuilder.loadTexts:
    accesslistTable.setStatus("mandatory")
_AccesslistEntry_Object = MibTableRow
accesslistEntry = _AccesslistEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 29, 1)
)
accesslistEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "accesslistIndex"),
    (0, "DIGI-PASSPORT-MIB", "accesslistUserIndex"),
)
if mibBuilder.loadTexts:
    accesslistEntry.setStatus("mandatory")
_AccesslistIndex_Type = Integer32
_AccesslistIndex_Object = MibTableColumn
accesslistIndex = _AccesslistIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 29, 1, 11),
    _AccesslistIndex_Type()
)
accesslistIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accesslistIndex.setStatus("mandatory")
_AccesslistUserIndex_Type = Integer32
_AccesslistUserIndex_Object = MibTableColumn
accesslistUserIndex = _AccesslistUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 29, 1, 12),
    _AccesslistUserIndex_Type()
)
accesslistUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accesslistUserIndex.setStatus("mandatory")
_AccesslistName_Type = DisplayString
_AccesslistName_Object = MibTableColumn
accesslistName = _AccesslistName_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 29, 1, 13),
    _AccesslistName_Type()
)
accesslistName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accesslistName.setStatus("mandatory")
_AccesslistUsers_Type = DisplayString
_AccesslistUsers_Object = MibTableColumn
accesslistUsers = _AccesslistUsers_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 29, 1, 14),
    _AccesslistUsers_Type()
)
accesslistUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accesslistUsers.setStatus("mandatory")
_AccesslistAddRow_Type = Action
_AccesslistAddRow_Object = MibTableColumn
accesslistAddRow = _AccesslistAddRow_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 29, 1, 15),
    _AccesslistAddRow_Type()
)
accesslistAddRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accesslistAddRow.setStatus("mandatory")
_AccesslistDeleteRow_Type = Action
_AccesslistDeleteRow_Object = MibTableColumn
accesslistDeleteRow = _AccesslistDeleteRow_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 29, 1, 16),
    _AccesslistDeleteRow_Type()
)
accesslistDeleteRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accesslistDeleteRow.setStatus("mandatory")
_WhoTable_Object = MibTable
whoTable = _WhoTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 30)
)
if mibBuilder.loadTexts:
    whoTable.setStatus("mandatory")
_WhoEntry_Object = MibTableRow
whoEntry = _WhoEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 30, 1)
)
whoEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "whoIndex"),
)
if mibBuilder.loadTexts:
    whoEntry.setStatus("mandatory")
_WhoIndex_Type = Integer32
_WhoIndex_Object = MibTableColumn
whoIndex = _WhoIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 30, 1, 11),
    _WhoIndex_Type()
)
whoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whoIndex.setStatus("mandatory")
_WhoUser_Type = DisplayString
_WhoUser_Object = MibTableColumn
whoUser = _WhoUser_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 30, 1, 12),
    _WhoUser_Type()
)
whoUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whoUser.setStatus("mandatory")
_WhoTTY_Type = DisplayString
_WhoTTY_Object = MibTableColumn
whoTTY = _WhoTTY_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 30, 1, 13),
    _WhoTTY_Type()
)
whoTTY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whoTTY.setStatus("mandatory")
_WhoFrom_Type = DisplayString
_WhoFrom_Object = MibTableColumn
whoFrom = _WhoFrom_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 30, 1, 14),
    _WhoFrom_Type()
)
whoFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whoFrom.setStatus("mandatory")
_WhoSessions_Type = Integer32
_WhoSessions_Object = MibTableColumn
whoSessions = _WhoSessions_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 30, 1, 16),
    _WhoSessions_Type()
)
whoSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whoSessions.setStatus("mandatory")
_SecurityProfile_ObjectIdentity = ObjectIdentity
securityProfile = _SecurityProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 31)
)


class _SecurityProfLevel_Type(Integer32):
    """Custom type securityProfLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("custom", 0),
          ("standard", 1),
          ("secure", 2))
    )


_SecurityProfLevel_Type.__name__ = "Integer32"
_SecurityProfLevel_Object = MibScalar
securityProfLevel = _SecurityProfLevel_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 31, 10),
    _SecurityProfLevel_Type()
)
securityProfLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfLevel.setStatus("mandatory")
_SecurityProfSnmpEnable_Type = Switch
_SecurityProfSnmpEnable_Object = MibScalar
securityProfSnmpEnable = _SecurityProfSnmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 31, 11),
    _SecurityProfSnmpEnable_Type()
)
securityProfSnmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfSnmpEnable.setStatus("mandatory")
_SecurityProfDiscoverEnable_Type = Switch
_SecurityProfDiscoverEnable_Object = MibScalar
securityProfDiscoverEnable = _SecurityProfDiscoverEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 31, 12),
    _SecurityProfDiscoverEnable_Type()
)
securityProfDiscoverEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfDiscoverEnable.setStatus("mandatory")
_SecurityProfTelnetEnable_Type = Switch
_SecurityProfTelnetEnable_Object = MibScalar
securityProfTelnetEnable = _SecurityProfTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 31, 13),
    _SecurityProfTelnetEnable_Type()
)
securityProfTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfTelnetEnable.setStatus("mandatory")
_SecurityProfSshEnable_Type = Switch
_SecurityProfSshEnable_Object = MibScalar
securityProfSshEnable = _SecurityProfSshEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 31, 14),
    _SecurityProfSshEnable_Type()
)
securityProfSshEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfSshEnable.setStatus("mandatory")


class _SecurityProfSSHV1Enable_Type(Integer32):
    """Custom type securityProfSSHV1Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_SecurityProfSSHV1Enable_Type.__name__ = "Integer32"
_SecurityProfSSHV1Enable_Object = MibScalar
securityProfSSHV1Enable = _SecurityProfSSHV1Enable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 31, 15),
    _SecurityProfSSHV1Enable_Type()
)
securityProfSSHV1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfSSHV1Enable.setStatus("mandatory")


class _SecurityProfHttpEnable_Type(Integer32):
    """Custom type securityProfHttpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("redirect", 2))
    )


_SecurityProfHttpEnable_Type.__name__ = "Integer32"
_SecurityProfHttpEnable_Object = MibScalar
securityProfHttpEnable = _SecurityProfHttpEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 31, 16),
    _SecurityProfHttpEnable_Type()
)
securityProfHttpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfHttpEnable.setStatus("mandatory")
_SecurityProfHttpsEnable_Type = Switch
_SecurityProfHttpsEnable_Object = MibScalar
securityProfHttpsEnable = _SecurityProfHttpsEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 31, 17),
    _SecurityProfHttpsEnable_Type()
)
securityProfHttpsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfHttpsEnable.setStatus("mandatory")


class _SecurityProfAllPortsEnable_Type(Integer32):
    """Custom type securityProfAllPortsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("custom", 0),
          ("off", 1),
          ("on", 2))
    )


_SecurityProfAllPortsEnable_Type.__name__ = "Integer32"
_SecurityProfAllPortsEnable_Object = MibScalar
securityProfAllPortsEnable = _SecurityProfAllPortsEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 31, 18),
    _SecurityProfAllPortsEnable_Type()
)
securityProfAllPortsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfAllPortsEnable.setStatus("mandatory")


class _SecurityProfSetAllPortsTo_Type(Integer32):
    """Custom type securityProfSetAllPortsTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("custom", 0),
          ("telnet", 1),
          ("ssh", 2),
          ("rawtcp", 3))
    )


_SecurityProfSetAllPortsTo_Type.__name__ = "Integer32"
_SecurityProfSetAllPortsTo_Object = MibScalar
securityProfSetAllPortsTo = _SecurityProfSetAllPortsTo_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 31, 19),
    _SecurityProfSetAllPortsTo_Type()
)
securityProfSetAllPortsTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfSetAllPortsTo.setStatus("mandatory")
_SecurityProfStealthEnable_Type = Switch
_SecurityProfStealthEnable_Object = MibScalar
securityProfStealthEnable = _SecurityProfStealthEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 31, 20),
    _SecurityProfStealthEnable_Type()
)
securityProfStealthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfStealthEnable.setStatus("mandatory")


class _SecurityProfMinPasswordLength_Type(Integer32):
    """Custom type securityProfMinPasswordLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 255),
    )


_SecurityProfMinPasswordLength_Type.__name__ = "Integer32"
_SecurityProfMinPasswordLength_Object = MibScalar
securityProfMinPasswordLength = _SecurityProfMinPasswordLength_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 31, 21),
    _SecurityProfMinPasswordLength_Type()
)
securityProfMinPasswordLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfMinPasswordLength.setStatus("mandatory")
_SecurityProfMaxPasswordAge_Type = Integer32
_SecurityProfMaxPasswordAge_Object = MibScalar
securityProfMaxPasswordAge = _SecurityProfMaxPasswordAge_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 31, 22),
    _SecurityProfMaxPasswordAge_Type()
)
securityProfMaxPasswordAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfMaxPasswordAge.setStatus("mandatory")
_SecurityProfPasswordComplexity_Type = Switch
_SecurityProfPasswordComplexity_Object = MibScalar
securityProfPasswordComplexity = _SecurityProfPasswordComplexity_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 31, 23),
    _SecurityProfPasswordComplexity_Type()
)
securityProfPasswordComplexity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfPasswordComplexity.setStatus("mandatory")
_SecurityProfMaxPasswordHistory_Type = Switch
_SecurityProfMaxPasswordHistory_Object = MibScalar
securityProfMaxPasswordHistory = _SecurityProfMaxPasswordHistory_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 31, 24),
    _SecurityProfMaxPasswordHistory_Type()
)
securityProfMaxPasswordHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfMaxPasswordHistory.setStatus("mandatory")
_SecurityProfSnmpv1N2cEnable_Type = Switch
_SecurityProfSnmpv1N2cEnable_Object = MibScalar
securityProfSnmpv1N2cEnable = _SecurityProfSnmpv1N2cEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 31, 25),
    _SecurityProfSnmpv1N2cEnable_Type()
)
securityProfSnmpv1N2cEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfSnmpv1N2cEnable.setStatus("mandatory")
_SecurityProfSSLv2Enable_Type = Switch
_SecurityProfSSLv2Enable_Object = MibScalar
securityProfSSLv2Enable = _SecurityProfSSLv2Enable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 31, 26),
    _SecurityProfSSLv2Enable_Type()
)
securityProfSSLv2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfSSLv2Enable.setStatus("mandatory")
_SecurityProfSSLv3Enable_Type = Switch
_SecurityProfSSLv3Enable_Object = MibScalar
securityProfSSLv3Enable = _SecurityProfSSLv3Enable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 31, 27),
    _SecurityProfSSLv3Enable_Type()
)
securityProfSSLv3Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfSSLv3Enable.setStatus("mandatory")
_SecurityProfTLSv1Enable_Type = Switch
_SecurityProfTLSv1Enable_Object = MibScalar
securityProfTLSv1Enable = _SecurityProfTLSv1Enable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 31, 28),
    _SecurityProfTLSv1Enable_Type()
)
securityProfTLSv1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfTLSv1Enable.setStatus("mandatory")
_AutoBackup_ObjectIdentity = ObjectIdentity
autoBackup = _AutoBackup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 32)
)


class _AutoBackupOption_Type(Integer32):
    """Custom type autoBackupOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("periodically", 1),
          ("onchange", 2))
    )


_AutoBackupOption_Type.__name__ = "Integer32"
_AutoBackupOption_Object = MibScalar
autoBackupOption = _AutoBackupOption_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 32, 11),
    _AutoBackupOption_Type()
)
autoBackupOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoBackupOption.setStatus("mandatory")


class _AutoBackupLocation_Type(Integer32):
    """Custom type autoBackupLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              10)
        )
    )
    namedValues = NamedValues(
        *(("cfcard", 1),
          ("nfs", 2),
          ("userspace", 3),
          ("email", 4),
          ("usb", 5),
          ("samba", 10))
    )


_AutoBackupLocation_Type.__name__ = "Integer32"
_AutoBackupLocation_Object = MibScalar
autoBackupLocation = _AutoBackupLocation_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 32, 12),
    _AutoBackupLocation_Type()
)
autoBackupLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoBackupLocation.setStatus("mandatory")
_AutoBackupEncrypt_Type = Switch
_AutoBackupEncrypt_Object = MibScalar
autoBackupEncrypt = _AutoBackupEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 32, 13),
    _AutoBackupEncrypt_Type()
)
autoBackupEncrypt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoBackupEncrypt.setStatus("mandatory")
_AutoBackupFilename_Type = DisplayString
_AutoBackupFilename_Object = MibScalar
autoBackupFilename = _AutoBackupFilename_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 32, 14),
    _AutoBackupFilename_Type()
)
autoBackupFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoBackupFilename.setStatus("mandatory")


class _AutoBackupPeriod_Type(Integer32):
    """Custom type autoBackupPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 720),
    )


_AutoBackupPeriod_Type.__name__ = "Integer32"
_AutoBackupPeriod_Object = MibScalar
autoBackupPeriod = _AutoBackupPeriod_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 32, 15),
    _AutoBackupPeriod_Type()
)
autoBackupPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoBackupPeriod.setStatus("mandatory")
_AutoBackupMailto_Type = DisplayString
_AutoBackupMailto_Object = MibScalar
autoBackupMailto = _AutoBackupMailto_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 32, 16),
    _AutoBackupMailto_Type()
)
autoBackupMailto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoBackupMailto.setStatus("mandatory")
_SyslogNGTable_Object = MibTable
syslogNGTable = _SyslogNGTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 33)
)
if mibBuilder.loadTexts:
    syslogNGTable.setStatus("mandatory")
_SyslogNGEntry_Object = MibTableRow
syslogNGEntry = _SyslogNGEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 33, 1)
)
syslogNGEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "syslogNGIndex"),
)
if mibBuilder.loadTexts:
    syslogNGEntry.setStatus("mandatory")
_SyslogNGIndex_Type = Integer32
_SyslogNGIndex_Object = MibTableColumn
syslogNGIndex = _SyslogNGIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 33, 1, 11),
    _SyslogNGIndex_Type()
)
syslogNGIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogNGIndex.setStatus("mandatory")
_SyslogNGFilter_Type = DisplayString
_SyslogNGFilter_Object = MibTableColumn
syslogNGFilter = _SyslogNGFilter_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 33, 1, 12),
    _SyslogNGFilter_Type()
)
syslogNGFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogNGFilter.setStatus("mandatory")


class _SyslogNGDestination_Type(Integer32):
    """Custom type syslogNGDestination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("file", 1),
          ("udp", 2),
          ("tcp", 3),
          ("systemlog", 4))
    )


_SyslogNGDestination_Type.__name__ = "Integer32"
_SyslogNGDestination_Object = MibTableColumn
syslogNGDestination = _SyslogNGDestination_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 33, 1, 13),
    _SyslogNGDestination_Type()
)
syslogNGDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogNGDestination.setStatus("mandatory")
_SyslogNGLocation_Type = DisplayString
_SyslogNGLocation_Object = MibTableColumn
syslogNGLocation = _SyslogNGLocation_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 33, 1, 14),
    _SyslogNGLocation_Type()
)
syslogNGLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogNGLocation.setStatus("mandatory")
_SyslogNGAddRow_Type = Action
_SyslogNGAddRow_Object = MibTableColumn
syslogNGAddRow = _SyslogNGAddRow_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 33, 1, 15),
    _SyslogNGAddRow_Type()
)
syslogNGAddRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogNGAddRow.setStatus("mandatory")
_SyslogNGDeleteRow_Type = Action
_SyslogNGDeleteRow_Object = MibTableColumn
syslogNGDeleteRow = _SyslogNGDeleteRow_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 33, 1, 16),
    _SyslogNGDeleteRow_Type()
)
syslogNGDeleteRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogNGDeleteRow.setStatus("mandatory")
_PowerUnit_ObjectIdentity = ObjectIdentity
powerUnit = _PowerUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34)
)
_PowerUnitStatusTable_Object = MibTable
powerUnitStatusTable = _PowerUnitStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 1)
)
if mibBuilder.loadTexts:
    powerUnitStatusTable.setStatus("mandatory")
_PowerUnitStatusEntry_Object = MibTableRow
powerUnitStatusEntry = _PowerUnitStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 1, 1)
)
powerUnitStatusEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "powerUnitStatusIndex"),
)
if mibBuilder.loadTexts:
    powerUnitStatusEntry.setStatus("mandatory")


class _PowerUnitStatusIndex_Type(Integer32):
    """Custom type powerUnitStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_PowerUnitStatusIndex_Type.__name__ = "Integer32"
_PowerUnitStatusIndex_Object = MibTableColumn
powerUnitStatusIndex = _PowerUnitStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 1, 1, 11),
    _PowerUnitStatusIndex_Type()
)
powerUnitStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitStatusIndex.setStatus("mandatory")
_PowerUnitStatusModel_Type = DisplayString
_PowerUnitStatusModel_Object = MibTableColumn
powerUnitStatusModel = _PowerUnitStatusModel_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 1, 1, 12),
    _PowerUnitStatusModel_Type()
)
powerUnitStatusModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitStatusModel.setStatus("mandatory")
_PowerUnitStatusAlarm_Type = DisplayString
_PowerUnitStatusAlarm_Object = MibTableColumn
powerUnitStatusAlarm = _PowerUnitStatusAlarm_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 1, 1, 13),
    _PowerUnitStatusAlarm_Type()
)
powerUnitStatusAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitStatusAlarm.setStatus("mandatory")
_PowerUnitStatusTemperature_Type = DisplayString
_PowerUnitStatusTemperature_Object = MibTableColumn
powerUnitStatusTemperature = _PowerUnitStatusTemperature_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 1, 1, 14),
    _PowerUnitStatusTemperature_Type()
)
powerUnitStatusTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitStatusTemperature.setStatus("mandatory")
_PowerUnitStatusCircuitBreaker_Type = DisplayString
_PowerUnitStatusCircuitBreaker_Object = MibTableColumn
powerUnitStatusCircuitBreaker = _PowerUnitStatusCircuitBreaker_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 1, 1, 15),
    _PowerUnitStatusCircuitBreaker_Type()
)
powerUnitStatusCircuitBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitStatusCircuitBreaker.setStatus("mandatory")
_PowerUnitStatusRMSVoltage_Type = DisplayString
_PowerUnitStatusRMSVoltage_Object = MibTableColumn
powerUnitStatusRMSVoltage = _PowerUnitStatusRMSVoltage_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 1, 1, 16),
    _PowerUnitStatusRMSVoltage_Type()
)
powerUnitStatusRMSVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitStatusRMSVoltage.setStatus("mandatory")
_PowerUnitStatusRMSCurrent_Type = DisplayString
_PowerUnitStatusRMSCurrent_Object = MibTableColumn
powerUnitStatusRMSCurrent = _PowerUnitStatusRMSCurrent_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 1, 1, 17),
    _PowerUnitStatusRMSCurrent_Type()
)
powerUnitStatusRMSCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitStatusRMSCurrent.setStatus("mandatory")
_PowerUnitStatusRMSMax_Type = DisplayString
_PowerUnitStatusRMSMax_Object = MibTableColumn
powerUnitStatusRMSMax = _PowerUnitStatusRMSMax_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 1, 1, 18),
    _PowerUnitStatusRMSMax_Type()
)
powerUnitStatusRMSMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitStatusRMSMax.setStatus("mandatory")
_PowerUnitStatusTemperature1_Type = DisplayString
_PowerUnitStatusTemperature1_Object = MibTableColumn
powerUnitStatusTemperature1 = _PowerUnitStatusTemperature1_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 1, 1, 19),
    _PowerUnitStatusTemperature1_Type()
)
powerUnitStatusTemperature1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitStatusTemperature1.setStatus("mandatory")
_PowerUnitStatusHumidity1_Type = DisplayString
_PowerUnitStatusHumidity1_Object = MibTableColumn
powerUnitStatusHumidity1 = _PowerUnitStatusHumidity1_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 1, 1, 20),
    _PowerUnitStatusHumidity1_Type()
)
powerUnitStatusHumidity1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitStatusHumidity1.setStatus("mandatory")
_PowerUnitStatusTemperature2_Type = DisplayString
_PowerUnitStatusTemperature2_Object = MibTableColumn
powerUnitStatusTemperature2 = _PowerUnitStatusTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 1, 1, 21),
    _PowerUnitStatusTemperature2_Type()
)
powerUnitStatusTemperature2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitStatusTemperature2.setStatus("mandatory")
_PowerUnitStatusHumidity2_Type = DisplayString
_PowerUnitStatusHumidity2_Object = MibTableColumn
powerUnitStatusHumidity2 = _PowerUnitStatusHumidity2_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 1, 1, 22),
    _PowerUnitStatusHumidity2_Type()
)
powerUnitStatusHumidity2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitStatusHumidity2.setStatus("mandatory")
_PowerUnitOutletTable_Object = MibTable
powerUnitOutletTable = _PowerUnitOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 2)
)
if mibBuilder.loadTexts:
    powerUnitOutletTable.setStatus("mandatory")
_PowerUnitOutletEntry_Object = MibTableRow
powerUnitOutletEntry = _PowerUnitOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 2, 1)
)
powerUnitOutletEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "powerUnitOutletIndex"),
)
if mibBuilder.loadTexts:
    powerUnitOutletEntry.setStatus("mandatory")


class _PowerUnitIndex_Type(Integer32):
    """Custom type powerUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_PowerUnitIndex_Type.__name__ = "Integer32"
_PowerUnitIndex_Object = MibTableColumn
powerUnitIndex = _PowerUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 2, 1, 11),
    _PowerUnitIndex_Type()
)
powerUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitIndex.setStatus("mandatory")


class _PowerUnitOutletIndex_Type(Integer32):
    """Custom type powerUnitOutletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_PowerUnitOutletIndex_Type.__name__ = "Integer32"
_PowerUnitOutletIndex_Object = MibTableColumn
powerUnitOutletIndex = _PowerUnitOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 2, 1, 12),
    _PowerUnitOutletIndex_Type()
)
powerUnitOutletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitOutletIndex.setStatus("mandatory")


class _PowerUnitOutletStatus_Type(Integer32):
    """Custom type powerUnitOutletStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("powered-on", 1),
          ("powered-off", 2),
          ("reboot", 3),
          ("turning-on", 4),
          ("turning-off", 5),
          ("rebooting", 6))
    )


_PowerUnitOutletStatus_Type.__name__ = "Integer32"
_PowerUnitOutletStatus_Object = MibTableColumn
powerUnitOutletStatus = _PowerUnitOutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 2, 1, 13),
    _PowerUnitOutletStatus_Type()
)
powerUnitOutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitOutletStatus.setStatus("mandatory")


class _PowerUnitOutletControl_Type(Integer32):
    """Custom type powerUnitOutletControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("power-on", 2),
          ("power-off", 3),
          ("reboot", 4))
    )


_PowerUnitOutletControl_Type.__name__ = "Integer32"
_PowerUnitOutletControl_Object = MibTableColumn
powerUnitOutletControl = _PowerUnitOutletControl_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 2, 1, 14),
    _PowerUnitOutletControl_Type()
)
powerUnitOutletControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerUnitOutletControl.setStatus("mandatory")
_PowerUnitCurrentTable_Object = MibTable
powerUnitCurrentTable = _PowerUnitCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 3)
)
if mibBuilder.loadTexts:
    powerUnitCurrentTable.setStatus("mandatory")
_PowerUnitCurrentEntry_Object = MibTableRow
powerUnitCurrentEntry = _PowerUnitCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 3, 1)
)
powerUnitCurrentEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "powerUnitCurrentIndex"),
)
if mibBuilder.loadTexts:
    powerUnitCurrentEntry.setStatus("mandatory")


class _PowerUnitCurrentIndex_Type(Integer32):
    """Custom type powerUnitCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PowerUnitCurrentIndex_Type.__name__ = "Integer32"
_PowerUnitCurrentIndex_Object = MibTableColumn
powerUnitCurrentIndex = _PowerUnitCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 3, 1, 11),
    _PowerUnitCurrentIndex_Type()
)
powerUnitCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitCurrentIndex.setStatus("mandatory")


class _PowerUnitCurrentPort_Type(Integer32):
    """Custom type powerUnitCurrentPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PowerUnitCurrentPort_Type.__name__ = "Integer32"
_PowerUnitCurrentPort_Object = MibTableColumn
powerUnitCurrentPort = _PowerUnitCurrentPort_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 3, 1, 12),
    _PowerUnitCurrentPort_Type()
)
powerUnitCurrentPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitCurrentPort.setStatus("mandatory")
_PowerUnitCurrentModel_Type = DisplayString
_PowerUnitCurrentModel_Object = MibTableColumn
powerUnitCurrentModel = _PowerUnitCurrentModel_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 3, 1, 13),
    _PowerUnitCurrentModel_Type()
)
powerUnitCurrentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitCurrentModel.setStatus("mandatory")
_PowerUnitCurrentInfeeds_Type = DisplayString
_PowerUnitCurrentInfeeds_Object = MibTableColumn
powerUnitCurrentInfeeds = _PowerUnitCurrentInfeeds_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 3, 1, 14),
    _PowerUnitCurrentInfeeds_Type()
)
powerUnitCurrentInfeeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitCurrentInfeeds.setStatus("mandatory")
_PowerUnitCurrentRMSCurrent_Type = DisplayString
_PowerUnitCurrentRMSCurrent_Object = MibTableColumn
powerUnitCurrentRMSCurrent = _PowerUnitCurrentRMSCurrent_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 3, 1, 15),
    _PowerUnitCurrentRMSCurrent_Type()
)
powerUnitCurrentRMSCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitCurrentRMSCurrent.setStatus("mandatory")
_PowerUnitCurrentRMSMax_Type = DisplayString
_PowerUnitCurrentRMSMax_Object = MibTableColumn
powerUnitCurrentRMSMax = _PowerUnitCurrentRMSMax_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 34, 3, 1, 16),
    _PowerUnitCurrentRMSMax_Type()
)
powerUnitCurrentRMSMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitCurrentRMSMax.setStatus("mandatory")
_PortGroupTable_Object = MibTable
portGroupTable = _PortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 35)
)
if mibBuilder.loadTexts:
    portGroupTable.setStatus("mandatory")
_PortGroupEntry_Object = MibTableRow
portGroupEntry = _PortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 35, 1)
)
portGroupEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "portGroupIndex"),
)
if mibBuilder.loadTexts:
    portGroupEntry.setStatus("mandatory")
_PortGroupIndex_Type = Integer32
_PortGroupIndex_Object = MibTableColumn
portGroupIndex = _PortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 35, 1, 11),
    _PortGroupIndex_Type()
)
portGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portGroupIndex.setStatus("mandatory")
_PortGroupGroupName_Type = DisplayString
_PortGroupGroupName_Object = MibTableColumn
portGroupGroupName = _PortGroupGroupName_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 35, 1, 12),
    _PortGroupGroupName_Type()
)
portGroupGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portGroupGroupName.setStatus("mandatory")
_PortGroupLoginOnEachPort_Type = Switch
_PortGroupLoginOnEachPort_Object = MibTableColumn
portGroupLoginOnEachPort = _PortGroupLoginOnEachPort_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 35, 1, 13),
    _PortGroupLoginOnEachPort_Type()
)
portGroupLoginOnEachPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portGroupLoginOnEachPort.setStatus("mandatory")
_PortGroupAddRow_Type = Action
_PortGroupAddRow_Object = MibTableColumn
portGroupAddRow = _PortGroupAddRow_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 35, 1, 15),
    _PortGroupAddRow_Type()
)
portGroupAddRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portGroupAddRow.setStatus("mandatory")
_PortGroupDelRow_Type = Action
_PortGroupDelRow_Object = MibTableColumn
portGroupDelRow = _PortGroupDelRow_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 35, 1, 16),
    _PortGroupDelRow_Type()
)
portGroupDelRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portGroupDelRow.setStatus("mandatory")
_PortAutomaticDetectionTable_Object = MibTable
portAutomaticDetectionTable = _PortAutomaticDetectionTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 36)
)
if mibBuilder.loadTexts:
    portAutomaticDetectionTable.setStatus("mandatory")
_PortAutomaticDetectionEntry_Object = MibTableRow
portAutomaticDetectionEntry = _PortAutomaticDetectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 36, 1)
)
portAutomaticDetectionEntry.setIndexNames(
    (0, "DIGI-PASSPORT-MIB", "portAutomaticDetectionIndex"),
)
if mibBuilder.loadTexts:
    portAutomaticDetectionEntry.setStatus("mandatory")
_PortAutomaticDetectionIndex_Type = Integer32
_PortAutomaticDetectionIndex_Object = MibTableColumn
portAutomaticDetectionIndex = _PortAutomaticDetectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 36, 1, 11),
    _PortAutomaticDetectionIndex_Type()
)
portAutomaticDetectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAutomaticDetectionIndex.setStatus("mandatory")


class _PortAutomaticDetectionBaud_Type(Integer32):
    """Custom type portAutomaticDetectionBaud based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              75,
              150,
              200,
              300,
              600,
              1200,
              1800,
              2400,
              4800,
              9600,
              19200,
              38400,
              57600,
              115200,
              230400)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("b75", 75),
          ("b150", 150),
          ("b200", 200),
          ("b300", 300),
          ("b600", 600),
          ("b1200", 1200),
          ("b1800", 1800),
          ("b2400", 2400),
          ("b4800", 4800),
          ("b9600", 9600),
          ("b19200", 19200),
          ("b38400", 38400),
          ("b57600", 57600),
          ("b115200", 115200),
          ("b230400", 230400))
    )


_PortAutomaticDetectionBaud_Type.__name__ = "Integer32"
_PortAutomaticDetectionBaud_Object = MibTableColumn
portAutomaticDetectionBaud = _PortAutomaticDetectionBaud_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 36, 1, 12),
    _PortAutomaticDetectionBaud_Type()
)
portAutomaticDetectionBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAutomaticDetectionBaud.setStatus("mandatory")


class _PortAutomaticDetectionDatabits_Type(Integer32):
    """Custom type portAutomaticDetectionDatabits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("seven", 7),
          ("eight", 8))
    )


_PortAutomaticDetectionDatabits_Type.__name__ = "Integer32"
_PortAutomaticDetectionDatabits_Object = MibTableColumn
portAutomaticDetectionDatabits = _PortAutomaticDetectionDatabits_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 36, 1, 13),
    _PortAutomaticDetectionDatabits_Type()
)
portAutomaticDetectionDatabits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAutomaticDetectionDatabits.setStatus("mandatory")


class _PortAutomaticDetectionParity_Type(Integer32):
    """Custom type portAutomaticDetectionParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("even", 1),
          ("odd", 2))
    )


_PortAutomaticDetectionParity_Type.__name__ = "Integer32"
_PortAutomaticDetectionParity_Object = MibTableColumn
portAutomaticDetectionParity = _PortAutomaticDetectionParity_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 36, 1, 14),
    _PortAutomaticDetectionParity_Type()
)
portAutomaticDetectionParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAutomaticDetectionParity.setStatus("mandatory")


class _PortAutomaticDetectionStopbits_Type(Integer32):
    """Custom type portAutomaticDetectionStopbits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_PortAutomaticDetectionStopbits_Type.__name__ = "Integer32"
_PortAutomaticDetectionStopbits_Object = MibTableColumn
portAutomaticDetectionStopbits = _PortAutomaticDetectionStopbits_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 36, 1, 15),
    _PortAutomaticDetectionStopbits_Type()
)
portAutomaticDetectionStopbits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAutomaticDetectionStopbits.setStatus("mandatory")
_PortAutomaticDetectionProbeStr_Type = DisplayString
_PortAutomaticDetectionProbeStr_Object = MibTableColumn
portAutomaticDetectionProbeStr = _PortAutomaticDetectionProbeStr_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 36, 1, 16),
    _PortAutomaticDetectionProbeStr_Type()
)
portAutomaticDetectionProbeStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAutomaticDetectionProbeStr.setStatus("mandatory")
_PortAutomaticDetectionWaitTime_Type = Integer32
_PortAutomaticDetectionWaitTime_Object = MibTableColumn
portAutomaticDetectionWaitTime = _PortAutomaticDetectionWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 36, 1, 17),
    _PortAutomaticDetectionWaitTime_Type()
)
portAutomaticDetectionWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAutomaticDetectionWaitTime.setStatus("mandatory")
_PortAutomaticDetectionAddRow_Type = Action
_PortAutomaticDetectionAddRow_Object = MibTableColumn
portAutomaticDetectionAddRow = _PortAutomaticDetectionAddRow_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 36, 1, 18),
    _PortAutomaticDetectionAddRow_Type()
)
portAutomaticDetectionAddRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAutomaticDetectionAddRow.setStatus("mandatory")
_PortAutomaticDetectionDelRow_Type = Action
_PortAutomaticDetectionDelRow_Object = MibTableColumn
portAutomaticDetectionDelRow = _PortAutomaticDetectionDelRow_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 36, 1, 19),
    _PortAutomaticDetectionDelRow_Type()
)
portAutomaticDetectionDelRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAutomaticDetectionDelRow.setStatus("mandatory")
_ConfigurationManagement_ObjectIdentity = ObjectIdentity
configurationManagement = _ConfigurationManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 37)
)
_Export_ObjectIdentity = ObjectIdentity
export = _Export_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 37, 11)
)


class _ExportLocation_Type(Integer32):
    """Custom type exportLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cfcard", 1),
          ("usb", 2),
          ("nfs", 3),
          ("samba", 4),
          ("userSpace", 5))
    )


_ExportLocation_Type.__name__ = "Integer32"
_ExportLocation_Object = MibScalar
exportLocation = _ExportLocation_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 37, 11, 11),
    _ExportLocation_Type()
)
exportLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exportLocation.setStatus("mandatory")


class _ExportEncrypted_Type(Integer32):
    """Custom type exportEncrypted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ExportEncrypted_Type.__name__ = "Integer32"
_ExportEncrypted_Object = MibScalar
exportEncrypted = _ExportEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 37, 11, 12),
    _ExportEncrypted_Type()
)
exportEncrypted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exportEncrypted.setStatus("mandatory")
_ExportFilename_Type = DisplayString
_ExportFilename_Object = MibScalar
exportFilename = _ExportFilename_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 37, 11, 13),
    _ExportFilename_Type()
)
exportFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exportFilename.setStatus("mandatory")
_ExportExecute_Type = Action
_ExportExecute_Object = MibScalar
exportExecute = _ExportExecute_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 37, 11, 14),
    _ExportExecute_Type()
)
exportExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exportExecute.setStatus("mandatory")
__pysmi_import_ObjectIdentity = ObjectIdentity
_pysmi_import = __pysmi_import_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 37, 12)
)


class _ImportLocation_Type(Integer32):
    """Custom type importLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cfcard", 1),
          ("usb", 2),
          ("nfs", 3),
          ("samba", 4),
          ("userSpace", 5),
          ("factorydefault", 6))
    )


_ImportLocation_Type.__name__ = "Integer32"
_ImportLocation_Object = MibScalar
importLocation = _ImportLocation_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 37, 12, 11),
    _ImportLocation_Type()
)
importLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    importLocation.setStatus("mandatory")
_ImportSelectAll_Type = Action
_ImportSelectAll_Object = MibScalar
importSelectAll = _ImportSelectAll_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 37, 12, 12),
    _ImportSelectAll_Type()
)
importSelectAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    importSelectAll.setStatus("mandatory")


class _ImportNetworkConf_Type(Integer32):
    """Custom type importNetworkConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ImportNetworkConf_Type.__name__ = "Integer32"
_ImportNetworkConf_Object = MibScalar
importNetworkConf = _ImportNetworkConf_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 37, 12, 13),
    _ImportNetworkConf_Type()
)
importNetworkConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    importNetworkConf.setStatus("mandatory")


class _ImportIncludeIpConf_Type(Integer32):
    """Custom type importIncludeIpConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ImportIncludeIpConf_Type.__name__ = "Integer32"
_ImportIncludeIpConf_Object = MibScalar
importIncludeIpConf = _ImportIncludeIpConf_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 37, 12, 14),
    _ImportIncludeIpConf_Type()
)
importIncludeIpConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    importIncludeIpConf.setStatus("mandatory")


class _ImportSerialPortConf_Type(Integer32):
    """Custom type importSerialPortConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ImportSerialPortConf_Type.__name__ = "Integer32"
_ImportSerialPortConf_Object = MibScalar
importSerialPortConf = _ImportSerialPortConf_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 37, 12, 15),
    _ImportSerialPortConf_Type()
)
importSerialPortConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    importSerialPortConf.setStatus("mandatory")


class _ImportClusterConf_Type(Integer32):
    """Custom type importClusterConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ImportClusterConf_Type.__name__ = "Integer32"
_ImportClusterConf_Object = MibScalar
importClusterConf = _ImportClusterConf_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 37, 12, 16),
    _ImportClusterConf_Type()
)
importClusterConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    importClusterConf.setStatus("mandatory")


class _ImportCustomMenuConf_Type(Integer32):
    """Custom type importCustomMenuConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ImportCustomMenuConf_Type.__name__ = "Integer32"
_ImportCustomMenuConf_Object = MibScalar
importCustomMenuConf = _ImportCustomMenuConf_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 37, 12, 17),
    _ImportCustomMenuConf_Type()
)
importCustomMenuConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    importCustomMenuConf.setStatus("mandatory")


class _ImportSystemUserConf_Type(Integer32):
    """Custom type importSystemUserConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ImportSystemUserConf_Type.__name__ = "Integer32"
_ImportSystemUserConf_Object = MibScalar
importSystemUserConf = _ImportSystemUserConf_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 37, 12, 18),
    _ImportSystemUserConf_Type()
)
importSystemUserConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    importSystemUserConf.setStatus("mandatory")


class _ImportPowerControlConf_Type(Integer32):
    """Custom type importPowerControlConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ImportPowerControlConf_Type.__name__ = "Integer32"
_ImportPowerControlConf_Object = MibScalar
importPowerControlConf = _ImportPowerControlConf_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 37, 12, 19),
    _ImportPowerControlConf_Type()
)
importPowerControlConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    importPowerControlConf.setStatus("mandatory")


class _ImportPccardConf_Type(Integer32):
    """Custom type importPccardConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ImportPccardConf_Type.__name__ = "Integer32"
_ImportPccardConf_Object = MibScalar
importPccardConf = _ImportPccardConf_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 37, 12, 20),
    _ImportPccardConf_Type()
)
importPccardConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    importPccardConf.setStatus("mandatory")


class _ImportUsbConf_Type(Integer32):
    """Custom type importUsbConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ImportUsbConf_Type.__name__ = "Integer32"
_ImportUsbConf_Object = MibScalar
importUsbConf = _ImportUsbConf_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 37, 12, 21),
    _ImportUsbConf_Type()
)
importUsbConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    importUsbConf.setStatus("mandatory")


class _ImportSystemConf_Type(Integer32):
    """Custom type importSystemConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ImportSystemConf_Type.__name__ = "Integer32"
_ImportSystemConf_Object = MibScalar
importSystemConf = _ImportSystemConf_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 37, 12, 22),
    _ImportSystemConf_Type()
)
importSystemConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    importSystemConf.setStatus("mandatory")


class _ImportPerlConf_Type(Integer32):
    """Custom type importPerlConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ImportPerlConf_Type.__name__ = "Integer32"
_ImportPerlConf_Object = MibScalar
importPerlConf = _ImportPerlConf_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 37, 12, 23),
    _ImportPerlConf_Type()
)
importPerlConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    importPerlConf.setStatus("mandatory")


class _ImportEncrypted_Type(Integer32):
    """Custom type importEncrypted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ImportEncrypted_Type.__name__ = "Integer32"
_ImportEncrypted_Object = MibScalar
importEncrypted = _ImportEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 37, 12, 24),
    _ImportEncrypted_Type()
)
importEncrypted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    importEncrypted.setStatus("mandatory")
_ImportFilename_Type = DisplayString
_ImportFilename_Object = MibScalar
importFilename = _ImportFilename_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 37, 12, 25),
    _ImportFilename_Type()
)
importFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    importFilename.setStatus("mandatory")
_ImportExecute_Type = Action
_ImportExecute_Object = MibScalar
importExecute = _ImportExecute_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 37, 12, 26),
    _ImportExecute_Type()
)
importExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    importExecute.setStatus("mandatory")
_AutoFirmUp_ObjectIdentity = ObjectIdentity
autoFirmUp = _AutoFirmUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 38)
)
_AutoFirmUpEnable_Type = Switch
_AutoFirmUpEnable_Object = MibScalar
autoFirmUpEnable = _AutoFirmUpEnable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 38, 11),
    _AutoFirmUpEnable_Type()
)
autoFirmUpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoFirmUpEnable.setStatus("mandatory")


class _AutoFirmUpProtocol_Type(Integer32):
    """Custom type autoFirmUpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("tftp", 1)
    )


_AutoFirmUpProtocol_Type.__name__ = "Integer32"
_AutoFirmUpProtocol_Object = MibScalar
autoFirmUpProtocol = _AutoFirmUpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 38, 12),
    _AutoFirmUpProtocol_Type()
)
autoFirmUpProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoFirmUpProtocol.setStatus("mandatory")
_AutoFirmUpUseDHCP_Type = Switch
_AutoFirmUpUseDHCP_Object = MibScalar
autoFirmUpUseDHCP = _AutoFirmUpUseDHCP_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 38, 13),
    _AutoFirmUpUseDHCP_Type()
)
autoFirmUpUseDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoFirmUpUseDHCP.setStatus("mandatory")
_AutoFirmUpIpAddress_Type = IpAddress
_AutoFirmUpIpAddress_Object = MibScalar
autoFirmUpIpAddress = _AutoFirmUpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 38, 14),
    _AutoFirmUpIpAddress_Type()
)
autoFirmUpIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoFirmUpIpAddress.setStatus("mandatory")
_AutoFirmUpHashFile_Type = DisplayString
_AutoFirmUpHashFile_Object = MibScalar
autoFirmUpHashFile = _AutoFirmUpHashFile_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 8, 38, 15),
    _AutoFirmUpHashFile_Type()
)
autoFirmUpHashFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoFirmUpHashFile.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGI-PASSPORT-MIB",
    **{"DisplayString": DisplayString,
       "PhysAddress": PhysAddress,
       "Switch": Switch,
       "Action": Action,
       "general": general,
       "generalModel": generalModel,
       "generalFirmwareVersion": generalFirmwareVersion,
       "generalBootcodeVersion": generalBootcodeVersion,
       "generalHWRevision": generalHWRevision,
       "generalFlashSize": generalFlashSize,
       "generalEtherAddress": generalEtherAddress,
       "generalIPAddress": generalIPAddress,
       "generalDevicename": generalDevicename,
       "generalLocating": generalLocating,
       "generalPowerStatus": generalPowerStatus,
       "generalSaveApplyConfig": generalSaveApplyConfig,
       "processor": processor,
       "processorUtilization": processorUtilization,
       "memory": memory,
       "memoryTotalMemory": memoryTotalMemory,
       "memoryAvailable": memoryAvailable,
       "time": time,
       "timeSystemCurrent": timeSystemCurrent,
       "timeNTPEnable": timeNTPEnable,
       "timeNTPAutoConfig": timeNTPAutoConfig,
       "timeNTPServer": timeNTPServer,
       "timeNTPInterval": timeNTPInterval,
       "timeNTPDHCPOptEnable": timeNTPDHCPOptEnable,
       "boot": boot,
       "bootReboot": bootReboot,
       "port": port,
       "portManageTable": portManageTable,
       "portManageEntry": portManageEntry,
       "portManageIndex": portManageIndex,
       "portsEnable": portsEnable,
       "portsRealPortEnable": portsRealPortEnable,
       "portsResetProcess": portsResetProcess,
       "portsResetToFactoryDefault": portsResetToFactoryDefault,
       "portsAddRow": portsAddRow,
       "portsDelRow": portsDelRow,
       "portsGroupName": portsGroupName,
       "portApplyAllPortsTable": portApplyAllPortsTable,
       "portApplyAllPortsEntry": portApplyAllPortsEntry,
       "portApplyAllPortsIndex": portApplyAllPortsIndex,
       "portsApplyAllPorts": portsApplyAllPorts,
       "detectionTable": detectionTable,
       "detectionEntry": detectionEntry,
       "detectIndex": detectIndex,
       "detectMethod": detectMethod,
       "detectInitDelay": detectInitDelay,
       "detectInterval": detectInterval,
       "detectTime": detectTime,
       "detectProbeStr": detectProbeStr,
       "detectedOS": detectedOS,
       "useDetectedTitle": useDetectedTitle,
       "titleNamingRule": titleNamingRule,
       "useDetectedTypeOfCS": useDetectedTypeOfCS,
       "useDetectedFreeKVM": useDetectedFreeKVM,
       "useDetectedSerialParams": useDetectedSerialParams,
       "detectDeviceVia": detectDeviceVia,
       "portTitleTable": portTitleTable,
       "portTitleEntry": portTitleEntry,
       "portTitleIndex": portTitleIndex,
       "portTitle": portTitle,
       "hostmodeTable": hostmodeTable,
       "hostmodeEntry": hostmodeEntry,
       "hostmodeIndex": hostmodeIndex,
       "hostMode": hostMode,
       "hostTypeCS": hostTypeCS,
       "hostEnableRackableCard": hostEnableRackableCard,
       "hostEnableAssignedIP": hostEnableAssignedIP,
       "hostAssignedIP": hostAssignedIP,
       "hostLocalPort": hostLocalPort,
       "hostProtocol": hostProtocol,
       "hostInactivity": hostInactivity,
       "hostEnableEscapeChar": hostEnableEscapeChar,
       "hostEscapeChar": hostEscapeChar,
       "hostBreakSeq": hostBreakSeq,
       "hostUseComment": hostUseComment,
       "hostQuickConnect": hostQuickConnect,
       "hostAppletEncode": hostAppletEncode,
       "hostTSOption": hostTSOption,
       "hostDestIP": hostDestIP,
       "hostDestPort": hostDestPort,
       "hostTSShellProgramPath": hostTSShellProgramPath,
       "hostModemInitStr": hostModemInitStr,
       "hostEnableCallback": hostEnableCallback,
       "hostCallbackNumber": hostCallbackNumber,
       "hostEnableModemTest": hostEnableModemTest,
       "hostModemTestNumber": hostModemTestNumber,
       "hostModemTestInterval": hostModemTestInterval,
       "hostServiceProcessor": hostServiceProcessor,
       "hostEnableCallbackLogin": hostEnableCallbackLogin,
       "hostEnableCallbackNumberChange": hostEnableCallbackNumberChange,
       "hostEnableAppletColumns": hostEnableAppletColumns,
       "hostEnableAppletRows": hostEnableAppletRows,
       "hostEnableDisPortInfo": hostEnableDisPortInfo,
       "hostEnableEscapeOption": hostEnableEscapeOption,
       "paramTable": paramTable,
       "paramEntry": paramEntry,
       "paramIndex": paramIndex,
       "paramType": paramType,
       "paramBaud": paramBaud,
       "paramDatabits": paramDatabits,
       "paramParity": paramParity,
       "paramStopbits": paramStopbits,
       "paramFlowctrl": paramFlowctrl,
       "paramDTROpt": paramDTROpt,
       "paramEnableDelimiter": paramEnableDelimiter,
       "paramDelimiter": paramDelimiter,
       "paramDeilmiterOption": paramDeilmiterOption,
       "paramInterCharTimeout": paramInterCharTimeout,
       "paramRemoteDestIP": paramRemoteDestIP,
       "paramRemoteDestPort": paramRemoteDestPort,
       "paramRemoteProtocol": paramRemoteProtocol,
       "paramRemoteContinuousConnect": paramRemoteContinuousConnect,
       "paramRemoteEstablishInterval": paramRemoteEstablishInterval,
       "paramRemoteOEMType": paramRemoteOEMType,
       "paramRemoteUsername": paramRemoteUsername,
       "paramRemotePassword": paramRemotePassword,
       "paramRemoteSupportProtocol": paramRemoteSupportProtocol,
       "paramRemoteAutomaticLogin": paramRemoteAutomaticLogin,
       "paramRemoteUseCustomScript": paramRemoteUseCustomScript,
       "paramFlushBuf": paramFlushBuf,
       "loggingTable": loggingTable,
       "loggingEntry": loggingEntry,
       "loggingIndex": loggingIndex,
       "loggingEnablePortLogging": loggingEnablePortLogging,
       "loggingOption": loggingOption,
       "loggingStoLoc": loggingStoLoc,
       "loggingSyslog": loggingSyslog,
       "loggingBufferSize": loggingBufferSize,
       "loggingFileByTitle": loggingFileByTitle,
       "loggingFilename": loggingFilename,
       "loggingTimeStamp": loggingTimeStamp,
       "loggingShowOnConn": loggingShowOnConn,
       "loggingStringM": loggingStringM,
       "loggingBackupOnMount": loggingBackupOnMount,
       "loggingFacility": loggingFacility,
       "loggingCharLength": loggingCharLength,
       "backupfileNumber": backupfileNumber,
       "keywordsTable": keywordsTable,
       "keywordsEntry": keywordsEntry,
       "keywordsPortIndex": keywordsPortIndex,
       "keywordIndex": keywordIndex,
       "keywordString": keywordString,
       "keywordMailEnable": keywordMailEnable,
       "keywordMailTitle": keywordMailTitle,
       "keywordMailto": keywordMailto,
       "keywordTrapEnable": keywordTrapEnable,
       "keywordTrapMsgTitle": keywordTrapMsgTitle,
       "keywordTrapToGlobal": keywordTrapToGlobal,
       "keyword1stTrapDest": keyword1stTrapDest,
       "keyword1stTrapDestComm": keyword1stTrapDestComm,
       "keyword1stTrapDestVer": keyword1stTrapDestVer,
       "keyword1stTrapUserName": keyword1stTrapUserName,
       "keyword1stTrapSecurityLevel": keyword1stTrapSecurityLevel,
       "keyword1stTrapAuthProto": keyword1stTrapAuthProto,
       "keyword1stTrapAuthPasswd": keyword1stTrapAuthPasswd,
       "keyword1stTrapPrivProto": keyword1stTrapPrivProto,
       "keyword1stTrapPrivPasswd": keyword1stTrapPrivPasswd,
       "keyword1stTrapEngineID": keyword1stTrapEngineID,
       "keyword2ndTrapDest": keyword2ndTrapDest,
       "keyword2ndTrapDestComm": keyword2ndTrapDestComm,
       "keyword2ndTrapDestVer": keyword2ndTrapDestVer,
       "keyword2ndTrapUserName": keyword2ndTrapUserName,
       "keyword2ndTrapSecurityLevel": keyword2ndTrapSecurityLevel,
       "keyword2ndTrapAuthProto": keyword2ndTrapAuthProto,
       "keyword2ndTrapAuthPasswd": keyword2ndTrapAuthPasswd,
       "keyword2ndTrapPrivProto": keyword2ndTrapPrivProto,
       "keyword2ndTrapPrivPasswd": keyword2ndTrapPrivPasswd,
       "keyword2ndTrapEngineID": keyword2ndTrapEngineID,
       "keywordCaseSensitive": keywordCaseSensitive,
       "keywordAddRow": keywordAddRow,
       "keywordDeleteRow": keywordDeleteRow,
       "authTable": authTable,
       "authEntry": authEntry,
       "authIndex": authIndex,
       "authMethod": authMethod,
       "authPrimaryIPAddress": authPrimaryIPAddress,
       "authSecondaryIPAddress": authSecondaryIPAddress,
       "authPrimaryAcctIPAddress": authPrimaryAcctIPAddress,
       "authSecondaryAcctIPAddress": authSecondaryAcctIPAddress,
       "authSecret": authSecret,
       "authTimeout": authTimeout,
       "authRetries": authRetries,
       "authLDAPSearchBase": authLDAPSearchBase,
       "authLDAPActiveDirectoryDomain": authLDAPActiveDirectoryDomain,
       "authKRBPrimaryRealm": authKRBPrimaryRealm,
       "authKRBSecondaryRealm": authKRBSecondaryRealm,
       "authAuthorService": authAuthorService,
       "authLdapSecure": authLdapSecure,
       "authPPPUser": authPPPUser,
       "usracctlTable": usracctlTable,
       "usracctlEntry": usracctlEntry,
       "usracctlIndex": usracctlIndex,
       "usracctlEveryonePortPerm": usracctlEveryonePortPerm,
       "usracctlPortPermittedUsers": usracctlPortPermittedUsers,
       "usracctlPortRestrictedUsers": usracctlPortRestrictedUsers,
       "usracctlPortPermittedLists": usracctlPortPermittedLists,
       "usracctlPortRestrictedLists": usracctlPortRestrictedLists,
       "usracctlEveryoneMonitorPerm": usracctlEveryoneMonitorPerm,
       "usracctlMonitorPermittedUsers": usracctlMonitorPermittedUsers,
       "usracctlMonitorRestrictedUsers": usracctlMonitorRestrictedUsers,
       "usracctlMonitorPermittedLists": usracctlMonitorPermittedLists,
       "usracctlMonitorRestrictedLists": usracctlMonitorRestrictedLists,
       "usracctlEveryonePowerPerm": usracctlEveryonePowerPerm,
       "usracctlPowerPermittedUsers": usracctlPowerPermittedUsers,
       "usracctlPowerRestrictedUsers": usracctlPowerRestrictedUsers,
       "usracctlPowerPermittedLists": usracctlPowerPermittedLists,
       "usracctlPowerRestrictedLists": usracctlPowerRestrictedLists,
       "usracctlEnableMultipleSession": usracctlEnableMultipleSession,
       "usracctlSessionDisplayMode": usracctlSessionDisplayMode,
       "usracctlSniffDisplayDirectionArrow": usracctlSniffDisplayDirectionArrow,
       "usracctlEveryoneLogPerm": usracctlEveryoneLogPerm,
       "usracctlLogPermittedUsers": usracctlLogPermittedUsers,
       "usracctlLogRestrictedUsers": usracctlLogRestrictedUsers,
       "usracctlLogPermittedLists": usracctlLogPermittedLists,
       "usracctlLogRestrictedLists": usracctlLogRestrictedLists,
       "usracctlEveryoneBreakPerm": usracctlEveryoneBreakPerm,
       "usracctlBreakPermittedUsers": usracctlBreakPermittedUsers,
       "usracctlBreakRestrictedUsers": usracctlBreakRestrictedUsers,
       "usracctlBreakPermittedLists": usracctlBreakPermittedLists,
       "usracctlBreakRestrictedLists": usracctlBreakRestrictedLists,
       "alertTable": alertTable,
       "alertEntry": alertEntry,
       "alertIndex": alertIndex,
       "alertLoginMail": alertLoginMail,
       "alertLoginMailTitle": alertLoginMailTitle,
       "alertLoginMailto": alertLoginMailto,
       "alertDevConnMail": alertDevConnMail,
       "alertDevConnMailTitle": alertDevConnMailTitle,
       "alertDevConnMailto": alertDevConnMailto,
       "alertDetectionMail": alertDetectionMail,
       "alertDetectionMailTitle": alertDetectionMailTitle,
       "alertDetectionMailto": alertDetectionMailto,
       "alertModemTestMail": alertModemTestMail,
       "alertModemTestMailTitle": alertModemTestMailTitle,
       "alertModemTestMailto": alertModemTestMailto,
       "alertIPMIMail": alertIPMIMail,
       "alertIPMIMailTitle": alertIPMIMailTitle,
       "alertIPMIMailto": alertIPMIMailto,
       "alertLoginTrap": alertLoginTrap,
       "alertDevConnTrap": alertDevConnTrap,
       "alertDetectionTrap": alertDetectionTrap,
       "alertModemTestTrap": alertModemTestTrap,
       "alertIPMITrap": alertIPMITrap,
       "alertToGlobalSNMP": alertToGlobalSNMP,
       "alert1stTrapRcvIP": alert1stTrapRcvIP,
       "alert1stTrapRcvComm": alert1stTrapRcvComm,
       "alert1stTrapRcvVer": alert1stTrapRcvVer,
       "alert1stTrapRcvUserName": alert1stTrapRcvUserName,
       "alert1stTrapRcvSecurityLevel": alert1stTrapRcvSecurityLevel,
       "alert1stTrapRcvAuthProto": alert1stTrapRcvAuthProto,
       "alert1stTrapRcvAuthPasswd": alert1stTrapRcvAuthPasswd,
       "alert1stTrapRcvPrivProto": alert1stTrapRcvPrivProto,
       "alert1stTrapRcvPrivPasswd": alert1stTrapRcvPrivPasswd,
       "alert1stTrapRcvEngineID": alert1stTrapRcvEngineID,
       "alert2ndTrapRcvIP": alert2ndTrapRcvIP,
       "alert2ndTrapRcvComm": alert2ndTrapRcvComm,
       "alert2ndTrapRcvVer": alert2ndTrapRcvVer,
       "alert2ndTrapRcvUserName": alert2ndTrapRcvUserName,
       "alert2ndTrapRcvSecurityLevel": alert2ndTrapRcvSecurityLevel,
       "alert2ndTrapRcvAuthProto": alert2ndTrapRcvAuthProto,
       "alert2ndTrapRcvAuthPasswd": alert2ndTrapRcvAuthPasswd,
       "alert2ndTrapRcvPrivProto": alert2ndTrapRcvPrivProto,
       "alert2ndTrapRcvPrivPasswd": alert2ndTrapRcvPrivPasswd,
       "alert2ndTrapRcvEngineID": alert2ndTrapRcvEngineID,
       "powerTable": powerTable,
       "powerEntry": powerEntry,
       "powerIndex": powerIndex,
       "powerStatus": powerStatus,
       "powerControl": powerControl,
       "ipmiConfigTable": ipmiConfigTable,
       "ipmiConfigEntry": ipmiConfigEntry,
       "ipmiConfigIndex": ipmiConfigIndex,
       "ipmiConfigUserName": ipmiConfigUserName,
       "ipmiConfigPassword": ipmiConfigPassword,
       "ipmiConfigOEMType": ipmiConfigOEMType,
       "ipmiSensorTable": ipmiSensorTable,
       "ipmiSensorEntry": ipmiSensorEntry,
       "ipmiPortIndex": ipmiPortIndex,
       "ipmiSensorIndex": ipmiSensorIndex,
       "ipmiSensorType": ipmiSensorType,
       "ipmiSensorEmailAlert": ipmiSensorEmailAlert,
       "ipmiSensorSNMPAlert": ipmiSensorSNMPAlert,
       "ipmiSensorAddRow": ipmiSensorAddRow,
       "ipmiSensorDeleteRow": ipmiSensorDeleteRow,
       "portsStatTable": portsStatTable,
       "portsStatEntry": portsStatEntry,
       "portsStatIndex": portsStatIndex,
       "portsStatBaudRate": portsStatBaudRate,
       "portsStatTx": portsStatTx,
       "portsStatRx": portsStatRx,
       "portsStatRTS": portsStatRTS,
       "portsStatCTS": portsStatCTS,
       "portsStatDTR": portsStatDTR,
       "portsStatDSR": portsStatDSR,
       "portsStatCD": portsStatCD,
       "portsStatOper": portsStatOper,
       "instantPortsParamTable": instantPortsParamTable,
       "instantPortsParamEntry": instantPortsParamEntry,
       "instantPortsParamIndex": instantPortsParamIndex,
       "instantPortsParamString": instantPortsParamString,
       "peripheral": peripheral,
       "pccard": pccard,
       "pccardType": pccardType,
       "pccardIpmode": pccardIpmode,
       "pccardIpAddress": pccardIpAddress,
       "pccardSubnet": pccardSubnet,
       "pccardGateway": pccardGateway,
       "pccardSSID": pccardSSID,
       "pccardWEPEnable": pccardWEPEnable,
       "pccardWEPMode": pccardWEPMode,
       "pccardWEPLength": pccardWEPLength,
       "pccardWEPKeyStr": pccardWEPKeyStr,
       "pccardModemInitStr": pccardModemInitStr,
       "pccardModemCallback": pccardModemCallback,
       "pccardModemCallbackNumber": pccardModemCallbackNumber,
       "pccardModemTestEnable": pccardModemTestEnable,
       "pccardModemTestNumber": pccardModemTestNumber,
       "pccardModemTestInterval": pccardModemTestInterval,
       "pccardModemTestMail": pccardModemTestMail,
       "pccardModemTestMailTitle": pccardModemTestMailTitle,
       "pccardModemTestMailto": pccardModemTestMailto,
       "pccardModemTestTrap": pccardModemTestTrap,
       "pccardTrapToGlobalSNMP": pccardTrapToGlobalSNMP,
       "pccardTrapRcvTable": pccardTrapRcvTable,
       "pccardTrapRcvEntry": pccardTrapRcvEntry,
       "pccardTrapRcvIndex": pccardTrapRcvIndex,
       "pccardTrapRcvIP": pccardTrapRcvIP,
       "pccardTrapRcvComm": pccardTrapRcvComm,
       "pccardTrapRcvVer": pccardTrapRcvVer,
       "pccardTrapRcvUserName": pccardTrapRcvUserName,
       "pccardTrapRcvSecurityLevel": pccardTrapRcvSecurityLevel,
       "pccardTrapRcvAuthProto": pccardTrapRcvAuthProto,
       "pccardTrapRcvAuthPasswd": pccardTrapRcvAuthPasswd,
       "pccardTrapRcvPrivProto": pccardTrapRcvPrivProto,
       "pccardTrapRcvPrivPasswd": pccardTrapRcvPrivPasswd,
       "pccardTrapRcvEngineID": pccardTrapRcvEngineID,
       "pccardEnableCallbackLogin": pccardEnableCallbackLogin,
       "pccardEnableCallbackNumberChange": pccardEnableCallbackNumberChange,
       "pccardIPv6Mode": pccardIPv6Mode,
       "pccardIPv6Address": pccardIPv6Address,
       "pccardIPv6Gateway": pccardIPv6Gateway,
       "pccardIPv6SecondaryIPAddress": pccardIPv6SecondaryIPAddress,
       "pccardIPv6Enable6to4tunneling": pccardIPv6Enable6to4tunneling,
       "pccardIPv6To4Relay": pccardIPv6To4Relay,
       "pccardIPv6OverwriteLocalIPV4": pccardIPv6OverwriteLocalIPV4,
       "pccardAuthMethod": pccardAuthMethod,
       "pccardPPPUser": pccardPPPUser,
       "modem": modem,
       "modemEnablePPP": modemEnablePPP,
       "modemInitString": modemInitString,
       "modemEnableCallback": modemEnableCallback,
       "modemCallbackNumber": modemCallbackNumber,
       "modemEnableModemTest": modemEnableModemTest,
       "modemTestNumber": modemTestNumber,
       "modemTestInterval": modemTestInterval,
       "modemTestMail": modemTestMail,
       "modemTestMailTitle": modemTestMailTitle,
       "modemTestMailto": modemTestMailto,
       "modemTestTrap": modemTestTrap,
       "modemTrapToGlobalSNMP": modemTrapToGlobalSNMP,
       "modemTrapRcvTable": modemTrapRcvTable,
       "modemTrapRcvEntry": modemTrapRcvEntry,
       "modemTrapRcvIndex": modemTrapRcvIndex,
       "modemTrapRcvIP": modemTrapRcvIP,
       "modemTrapRcvComm": modemTrapRcvComm,
       "modemTrapRcvVer": modemTrapRcvVer,
       "modemTrapRcvUserName": modemTrapRcvUserName,
       "modemTrapRcvSecurityLevel": modemTrapRcvSecurityLevel,
       "modemTrapRcvAuthProto": modemTrapRcvAuthProto,
       "modemTrapRcvAuthPasswd": modemTrapRcvAuthPasswd,
       "modemTrapRcvPrivProto": modemTrapRcvPrivProto,
       "modemTrapRcvPrivPasswd": modemTrapRcvPrivPasswd,
       "modemTrapRcvEngineID": modemTrapRcvEngineID,
       "modemEnableCallbackLogin": modemEnableCallbackLogin,
       "modemEnableCallbackNumberChange": modemEnableCallbackNumberChange,
       "modemSecondaryCallbackNumber": modemSecondaryCallbackNumber,
       "modemAuthMethod": modemAuthMethod,
       "modemPPPUser": modemPPPUser,
       "usb": usb,
       "usbTable": usbTable,
       "usbEntry": usbEntry,
       "usbIndex": usbIndex,
       "usbType": usbType,
       "usbModel": usbModel,
       "usbSize": usbSize,
       "usbFileSystem": usbFileSystem,
       "usbTotalSize": usbTotalSize,
       "usbIpmode": usbIpmode,
       "usbIpAddress": usbIpAddress,
       "usbSubnet": usbSubnet,
       "usbGateway": usbGateway,
       "usbSSID": usbSSID,
       "usbWEPEnable": usbWEPEnable,
       "usbWEPMode": usbWEPMode,
       "usbWEPLength": usbWEPLength,
       "usbWEPKeyStr": usbWEPKeyStr,
       "network": network,
       "netip": netip,
       "firstIPConfig": firstIPConfig,
       "firstIPv4Config": firstIPv4Config,
       "firstIPv4Mode": firstIPv4Mode,
       "firstIPv4PrimaryIPAddress": firstIPv4PrimaryIPAddress,
       "firstIPv4PrimarySubMask": firstIPv4PrimarySubMask,
       "firstIPv4PrimaryGateway": firstIPv4PrimaryGateway,
       "firstIPv4EnableSecondaryIP": firstIPv4EnableSecondaryIP,
       "firstIPv4SecondaryIPAddress": firstIPv4SecondaryIPAddress,
       "firstIPv4SecondarySubMask": firstIPv4SecondarySubMask,
       "firstIPv4SecondaryGateway": firstIPv4SecondaryGateway,
       "firstIPv6Config": firstIPv6Config,
       "firstIPv6Mode": firstIPv6Mode,
       "firstIPv6Address": firstIPv6Address,
       "firstIPv6Gateway": firstIPv6Gateway,
       "firstIPv6SecondaryIPAddress": firstIPv6SecondaryIPAddress,
       "firstIPv6Enable6to4tunneling": firstIPv6Enable6to4tunneling,
       "firstIPv6To4Relay": firstIPv6To4Relay,
       "firstIPv6OverwriteLocalIPV4": firstIPv6OverwriteLocalIPV4,
       "secondIPConfig": secondIPConfig,
       "secondIPv4Config": secondIPv4Config,
       "secondIPv4Mode": secondIPv4Mode,
       "secondIPv4PrimaryIPAddress": secondIPv4PrimaryIPAddress,
       "secondIPv4PrimarySubMask": secondIPv4PrimarySubMask,
       "secondIPv4PrimaryGateway": secondIPv4PrimaryGateway,
       "secondIPv4EnableSecondaryIP": secondIPv4EnableSecondaryIP,
       "secondIPv4SecondaryIPAddress": secondIPv4SecondaryIPAddress,
       "secondIPv4SecondarySubMask": secondIPv4SecondarySubMask,
       "secondIPv4SecondaryGateway": secondIPv4SecondaryGateway,
       "secondIPv6Config": secondIPv6Config,
       "secondIPv6Mode": secondIPv6Mode,
       "secondIPv6Address": secondIPv6Address,
       "secondIPv6Gateway": secondIPv6Gateway,
       "secondIPv6SecondaryIPAddress": secondIPv6SecondaryIPAddress,
       "secondIPv6Enable6to4tunneling": secondIPv6Enable6to4tunneling,
       "secondIPv6To4Relay": secondIPv6To4Relay,
       "secondIPv6OverwriteLocalIPV4": secondIPv6OverwriteLocalIPV4,
       "netipUseOldIPOnDHCPFailure": netipUseOldIPOnDHCPFailure,
       "netipUseManualDNS": netipUseManualDNS,
       "netipPrimaryNameServer": netipPrimaryNameServer,
       "netipSecondaryNameServer": netipSecondaryNameServer,
       "sourceBasedRouting": sourceBasedRouting,
       "snmpOther": snmpOther,
       "snmpPowerOnTraps": snmpPowerOnTraps,
       "snmpPowerOnEmails": snmpPowerOnEmails,
       "snmpAuthenTraps": snmpAuthenTraps,
       "snmpAuthenEmails": snmpAuthenEmails,
       "snmpLinkUpTraps": snmpLinkUpTraps,
       "snmpLinkUpEmails": snmpLinkUpEmails,
       "snmpLinkDownTraps": snmpLinkDownTraps,
       "snmpLinkDownEmails": snmpLinkDownEmails,
       "snmpLoginTraps": snmpLoginTraps,
       "snmpLoginEmails": snmpLoginEmails,
       "snmpMailto": snmpMailto,
       "snmpTrapRcvTable": snmpTrapRcvTable,
       "snmpTrapRcvEntry": snmpTrapRcvEntry,
       "snmpTrapRcvIndex": snmpTrapRcvIndex,
       "snmpTrapRcvIP": snmpTrapRcvIP,
       "snmpTrapRcvComm": snmpTrapRcvComm,
       "snmpTrapRcvVer": snmpTrapRcvVer,
       "snmpTrapRcvUserName": snmpTrapRcvUserName,
       "snmpTrapRcvSecurityLevel": snmpTrapRcvSecurityLevel,
       "snmpTrapRcvAuthProto": snmpTrapRcvAuthProto,
       "snmpTrapRcvAuthPasswd": snmpTrapRcvAuthPasswd,
       "snmpTrapRcvPrivProto": snmpTrapRcvPrivProto,
       "snmpTrapRcvPrivPasswd": snmpTrapRcvPrivPasswd,
       "snmpTrapRcvEngineID": snmpTrapRcvEngineID,
       "dyndns": dyndns,
       "dyndnsEnable": dyndnsEnable,
       "dyndnsDomain": dyndnsDomain,
       "dyndnsUser": dyndnsUser,
       "dyndnsPassword": dyndnsPassword,
       "dyndnsEnableCustomProgram": dyndnsEnableCustomProgram,
       "dyndnsCustomProgramPath": dyndnsCustomProgramPath,
       "dyndnsEnableKeyOpt": dyndnsEnableKeyOpt,
       "dyndnsUpdateKey": dyndnsUpdateKey,
       "dyndnsIPv4Addr": dyndnsIPv4Addr,
       "dyndnsIPv6Addr": dyndnsIPv6Addr,
       "smtp": smtp,
       "smtpPrimaryEnable": smtpPrimaryEnable,
       "smtpPrimaryAddress": smtpPrimaryAddress,
       "smtpPrimaryMode": smtpPrimaryMode,
       "smtpPrimaryUser": smtpPrimaryUser,
       "smtpPrimaryPassword": smtpPrimaryPassword,
       "smtpSecondaryEnable": smtpSecondaryEnable,
       "smtpSecondaryAddress": smtpSecondaryAddress,
       "smtpSecondaryMode": smtpSecondaryMode,
       "smtpSecondaryUser": smtpSecondaryUser,
       "smtpSecondaryPassword": smtpSecondaryPassword,
       "smtpFromAddress": smtpFromAddress,
       "ipfilter": ipfilter,
       "ipfilterTable": ipfilterTable,
       "ipfilterEntry": ipfilterEntry,
       "ipfilterIndex": ipfilterIndex,
       "ipfilterIface": ipfilterIface,
       "ipfilterOpt": ipfilterOpt,
       "ipfilterIPMask": ipfilterIPMask,
       "ipfilterPort": ipfilterPort,
       "ipfilterRule": ipfilterRule,
       "ipfilterProtocol": ipfilterProtocol,
       "ipfilterAddRow": ipfilterAddRow,
       "ipfilterDeleteRow": ipfilterDeleteRow,
       "nfs": nfs,
       "nfsPrimaryEnable": nfsPrimaryEnable,
       "nfsPrimaryAddress": nfsPrimaryAddress,
       "nfsPrimaryExported": nfsPrimaryExported,
       "nfsPrimaryTimeout": nfsPrimaryTimeout,
       "nfsPrimaryRetryInterval": nfsPrimaryRetryInterval,
       "nfsPrimaryEnableEncrypt": nfsPrimaryEnableEncrypt,
       "nfsPrimaryUser": nfsPrimaryUser,
       "nfsPrimaryPassword": nfsPrimaryPassword,
       "nfsSecondaryEnable": nfsSecondaryEnable,
       "nfsSecondaryAddress": nfsSecondaryAddress,
       "nfsSecondaryExported": nfsSecondaryExported,
       "nfsSecondaryTimeout": nfsSecondaryTimeout,
       "nfsSecondaryRetryInterval": nfsSecondaryRetryInterval,
       "nfsSecondaryEnableEncrypt": nfsSecondaryEnableEncrypt,
       "nfsSecondaryUser": nfsSecondaryUser,
       "nfsSecondaryPassword": nfsSecondaryPassword,
       "nfsMailEnable": nfsMailEnable,
       "nfsMailTitle": nfsMailTitle,
       "nfsMailto": nfsMailto,
       "nfsTrapEnable": nfsTrapEnable,
       "nfsTrapToGlobal": nfsTrapToGlobal,
       "nfsTrapRcvTable": nfsTrapRcvTable,
       "nfsTrapRcvEntry": nfsTrapRcvEntry,
       "nfsTrapRcvIndex": nfsTrapRcvIndex,
       "nfsTrapRcvIP": nfsTrapRcvIP,
       "nfsTrapRcvComm": nfsTrapRcvComm,
       "nfsTrapRcvVer": nfsTrapRcvVer,
       "nfsTrapRcvUserName": nfsTrapRcvUserName,
       "nfsTrapRcvSecurityLevel": nfsTrapRcvSecurityLevel,
       "nfsTrapRcvAuthProto": nfsTrapRcvAuthProto,
       "nfsTrapRcvAuthPasswd": nfsTrapRcvAuthPasswd,
       "nfsTrapRcvPrivProto": nfsTrapRcvPrivProto,
       "nfsTrapRcvPrivPasswd": nfsTrapRcvPrivPasswd,
       "nfsTrapRcvEngineID": nfsTrapRcvEngineID,
       "web": web,
       "webRefreshRate": webRefreshRate,
       "webLoginTimeout": webLoginTimeout,
       "webAuthMethod": webAuthMethod,
       "webAuthPrimaryIPAddress": webAuthPrimaryIPAddress,
       "webAuthSecondaryIPAddress": webAuthSecondaryIPAddress,
       "webAuthSecret": webAuthSecret,
       "webAuthTimeout": webAuthTimeout,
       "webAuthRetries": webAuthRetries,
       "webAuthLDAPSearchBase": webAuthLDAPSearchBase,
       "webAuthLDAPActiveDirectoryDomain": webAuthLDAPActiveDirectoryDomain,
       "webAuthKRBPrimaryRealm": webAuthKRBPrimaryRealm,
       "webAuthKRBSecondaryRealm": webAuthKRBSecondaryRealm,
       "webRootAccessEnable": webRootAccessEnable,
       "webSerialPortsCountsOnConnectionPage": webSerialPortsCountsOnConnectionPage,
       "webAppletOption": webAppletOption,
       "webHttpPort": webHttpPort,
       "webHttpsPort": webHttpsPort,
       "webBlockingTime": webBlockingTime,
       "webAuthAuthorService": webAuthAuthorService,
       "webAuthLdapSecure": webAuthLdapSecure,
       "ethernet": ethernet,
       "ethernetMode": ethernetMode,
       "tcpOther": tcpOther,
       "tcpOtherKeepAliveIdle": tcpOtherKeepAliveIdle,
       "tcpOtherKeepAliveProbe": tcpOtherKeepAliveProbe,
       "tcpOtherKeepAliveInterval": tcpOtherKeepAliveInterval,
       "tcpOtherReverseDNSLookup": tcpOtherReverseDNSLookup,
       "tcpOtherIPv4Forward": tcpOtherIPv4Forward,
       "ppp": ppp,
       "pppEnableDynamicPool": pppEnableDynamicPool,
       "pppIpAddr": pppIpAddr,
       "pppNumOfAddr": pppNumOfAddr,
       "pppIncommingTable": pppIncommingTable,
       "pppIncommingEntry": pppIncommingEntry,
       "pppIncommingIndex": pppIncommingIndex,
       "pppUsername": pppUsername,
       "pppPassword": pppPassword,
       "pppAuthentication": pppAuthentication,
       "pppPeerOpt": pppPeerOpt,
       "pppRemoteIP": pppRemoteIP,
       "pppAllowClientAccess": pppAllowClientAccess,
       "pppLocalPeerOpt": pppLocalPeerOpt,
       "pppLocalIP": pppLocalIP,
       "pppEnableIdleTimeout": pppEnableIdleTimeout,
       "pppTimeout": pppTimeout,
       "pppAddRow": pppAddRow,
       "pppDelRow": pppDelRow,
       "pppProccessArpRequest": pppProccessArpRequest,
       "samba": samba,
       "sambaEnableService": sambaEnableService,
       "sambaServerName": sambaServerName,
       "sambaMountPath": sambaMountPath,
       "sambaTimeout": sambaTimeout,
       "sambaInterval": sambaInterval,
       "sambaServerUser": sambaServerUser,
       "sambaServerPassword": sambaServerPassword,
       "sambaEnableEmailAlert": sambaEnableEmailAlert,
       "sambaEmailTitle": sambaEmailTitle,
       "sambaEmailTo": sambaEmailTo,
       "sambaEnableTrap": sambaEnableTrap,
       "sambaTrapToGlobal": sambaTrapToGlobal,
       "sambaTrapRcvTable": sambaTrapRcvTable,
       "sambaTrapRcvEntry": sambaTrapRcvEntry,
       "sambaTrapRcvIndex": sambaTrapRcvIndex,
       "sambaTrapRcvIP": sambaTrapRcvIP,
       "sambaTrapRcvComm": sambaTrapRcvComm,
       "sambaTrapRcvVer": sambaTrapRcvVer,
       "sambaTrapRcvUserName": sambaTrapRcvUserName,
       "sambaTrapRcvSecurityLevel": sambaTrapRcvSecurityLevel,
       "sambaTrapRcvAuthProto": sambaTrapRcvAuthProto,
       "sambaTrapRcvAuthPasswd": sambaTrapRcvAuthPasswd,
       "sambaTrapRcvPrivProto": sambaTrapRcvPrivProto,
       "sambaTrapRcvPrivPasswd": sambaTrapRcvPrivPasswd,
       "sambaTrapRcvEngineID": sambaTrapRcvEngineID,
       "systemLogging": systemLogging,
       "systemLoggingStoLoc": systemLoggingStoLoc,
       "systemLoggingBufferSize": systemLoggingBufferSize,
       "systemLoggingFilename": systemLoggingFilename,
       "systemLoggingBackupOnMount": systemLoggingBackupOnMount,
       "systemLoggingMailEnable": systemLoggingMailEnable,
       "systemLoggingMailMessageNum": systemLoggingMailMessageNum,
       "systemLoggingMailto": systemLoggingMailto,
       "accesslistTable": accesslistTable,
       "accesslistEntry": accesslistEntry,
       "accesslistIndex": accesslistIndex,
       "accesslistUserIndex": accesslistUserIndex,
       "accesslistName": accesslistName,
       "accesslistUsers": accesslistUsers,
       "accesslistAddRow": accesslistAddRow,
       "accesslistDeleteRow": accesslistDeleteRow,
       "whoTable": whoTable,
       "whoEntry": whoEntry,
       "whoIndex": whoIndex,
       "whoUser": whoUser,
       "whoTTY": whoTTY,
       "whoFrom": whoFrom,
       "whoSessions": whoSessions,
       "securityProfile": securityProfile,
       "securityProfLevel": securityProfLevel,
       "securityProfSnmpEnable": securityProfSnmpEnable,
       "securityProfDiscoverEnable": securityProfDiscoverEnable,
       "securityProfTelnetEnable": securityProfTelnetEnable,
       "securityProfSshEnable": securityProfSshEnable,
       "securityProfSSHV1Enable": securityProfSSHV1Enable,
       "securityProfHttpEnable": securityProfHttpEnable,
       "securityProfHttpsEnable": securityProfHttpsEnable,
       "securityProfAllPortsEnable": securityProfAllPortsEnable,
       "securityProfSetAllPortsTo": securityProfSetAllPortsTo,
       "securityProfStealthEnable": securityProfStealthEnable,
       "securityProfMinPasswordLength": securityProfMinPasswordLength,
       "securityProfMaxPasswordAge": securityProfMaxPasswordAge,
       "securityProfPasswordComplexity": securityProfPasswordComplexity,
       "securityProfMaxPasswordHistory": securityProfMaxPasswordHistory,
       "securityProfSnmpv1N2cEnable": securityProfSnmpv1N2cEnable,
       "securityProfSSLv2Enable": securityProfSSLv2Enable,
       "securityProfSSLv3Enable": securityProfSSLv3Enable,
       "securityProfTLSv1Enable": securityProfTLSv1Enable,
       "autoBackup": autoBackup,
       "autoBackupOption": autoBackupOption,
       "autoBackupLocation": autoBackupLocation,
       "autoBackupEncrypt": autoBackupEncrypt,
       "autoBackupFilename": autoBackupFilename,
       "autoBackupPeriod": autoBackupPeriod,
       "autoBackupMailto": autoBackupMailto,
       "syslogNGTable": syslogNGTable,
       "syslogNGEntry": syslogNGEntry,
       "syslogNGIndex": syslogNGIndex,
       "syslogNGFilter": syslogNGFilter,
       "syslogNGDestination": syslogNGDestination,
       "syslogNGLocation": syslogNGLocation,
       "syslogNGAddRow": syslogNGAddRow,
       "syslogNGDeleteRow": syslogNGDeleteRow,
       "powerUnit": powerUnit,
       "powerUnitStatusTable": powerUnitStatusTable,
       "powerUnitStatusEntry": powerUnitStatusEntry,
       "powerUnitStatusIndex": powerUnitStatusIndex,
       "powerUnitStatusModel": powerUnitStatusModel,
       "powerUnitStatusAlarm": powerUnitStatusAlarm,
       "powerUnitStatusTemperature": powerUnitStatusTemperature,
       "powerUnitStatusCircuitBreaker": powerUnitStatusCircuitBreaker,
       "powerUnitStatusRMSVoltage": powerUnitStatusRMSVoltage,
       "powerUnitStatusRMSCurrent": powerUnitStatusRMSCurrent,
       "powerUnitStatusRMSMax": powerUnitStatusRMSMax,
       "powerUnitStatusTemperature1": powerUnitStatusTemperature1,
       "powerUnitStatusHumidity1": powerUnitStatusHumidity1,
       "powerUnitStatusTemperature2": powerUnitStatusTemperature2,
       "powerUnitStatusHumidity2": powerUnitStatusHumidity2,
       "powerUnitOutletTable": powerUnitOutletTable,
       "powerUnitOutletEntry": powerUnitOutletEntry,
       "powerUnitIndex": powerUnitIndex,
       "powerUnitOutletIndex": powerUnitOutletIndex,
       "powerUnitOutletStatus": powerUnitOutletStatus,
       "powerUnitOutletControl": powerUnitOutletControl,
       "powerUnitCurrentTable": powerUnitCurrentTable,
       "powerUnitCurrentEntry": powerUnitCurrentEntry,
       "powerUnitCurrentIndex": powerUnitCurrentIndex,
       "powerUnitCurrentPort": powerUnitCurrentPort,
       "powerUnitCurrentModel": powerUnitCurrentModel,
       "powerUnitCurrentInfeeds": powerUnitCurrentInfeeds,
       "powerUnitCurrentRMSCurrent": powerUnitCurrentRMSCurrent,
       "powerUnitCurrentRMSMax": powerUnitCurrentRMSMax,
       "portGroupTable": portGroupTable,
       "portGroupEntry": portGroupEntry,
       "portGroupIndex": portGroupIndex,
       "portGroupGroupName": portGroupGroupName,
       "portGroupLoginOnEachPort": portGroupLoginOnEachPort,
       "portGroupAddRow": portGroupAddRow,
       "portGroupDelRow": portGroupDelRow,
       "portAutomaticDetectionTable": portAutomaticDetectionTable,
       "portAutomaticDetectionEntry": portAutomaticDetectionEntry,
       "portAutomaticDetectionIndex": portAutomaticDetectionIndex,
       "portAutomaticDetectionBaud": portAutomaticDetectionBaud,
       "portAutomaticDetectionDatabits": portAutomaticDetectionDatabits,
       "portAutomaticDetectionParity": portAutomaticDetectionParity,
       "portAutomaticDetectionStopbits": portAutomaticDetectionStopbits,
       "portAutomaticDetectionProbeStr": portAutomaticDetectionProbeStr,
       "portAutomaticDetectionWaitTime": portAutomaticDetectionWaitTime,
       "portAutomaticDetectionAddRow": portAutomaticDetectionAddRow,
       "portAutomaticDetectionDelRow": portAutomaticDetectionDelRow,
       "configurationManagement": configurationManagement,
       "export": export,
       "exportLocation": exportLocation,
       "exportEncrypted": exportEncrypted,
       "exportFilename": exportFilename,
       "exportExecute": exportExecute,
       "import": _pysmi_import,
       "importLocation": importLocation,
       "importSelectAll": importSelectAll,
       "importNetworkConf": importNetworkConf,
       "importIncludeIpConf": importIncludeIpConf,
       "importSerialPortConf": importSerialPortConf,
       "importClusterConf": importClusterConf,
       "importCustomMenuConf": importCustomMenuConf,
       "importSystemUserConf": importSystemUserConf,
       "importPowerControlConf": importPowerControlConf,
       "importPccardConf": importPccardConf,
       "importUsbConf": importUsbConf,
       "importSystemConf": importSystemConf,
       "importPerlConf": importPerlConf,
       "importEncrypted": importEncrypted,
       "importFilename": importFilename,
       "importExecute": importExecute,
       "autoFirmUp": autoFirmUp,
       "autoFirmUpEnable": autoFirmUpEnable,
       "autoFirmUpProtocol": autoFirmUpProtocol,
       "autoFirmUpUseDHCP": autoFirmUpUseDHCP,
       "autoFirmUpIpAddress": autoFirmUpIpAddress,
       "autoFirmUpHashFile": autoFirmUpHashFile}
)
