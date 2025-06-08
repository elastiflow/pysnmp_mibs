# SNMP MIB module (CISCO-6200-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-C6200-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:43:27 2025
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class C6200CardType(Integer32):
    """Custom type C6200CardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("none", -1),
          ("oc3si", 1),
          ("ctl", 2),
          ("cap8", 3),
          ("cap16", 4),
          ("oc3ss", 5),
          ("oc3mm", 6),
          ("stm1si", 7),
          ("stm1mm", 8),
          ("dmt8", 9))
    )





class CommandValue(Integer32):
    """Custom type CommandValue based on Integer32"""
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





class AlarmLevel(Integer32):
    """Custom type AlarmLevel based on Integer32"""
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
        *(("none", 1),
          ("minor", 2),
          ("major", 3),
          ("critical", 4),
          ("unknown", 5))
    )





class InterfaceStatus(Integer32):
    """Custom type InterfaceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )





class TestStatus(Integer32):
    """Custom type TestStatus based on Integer32"""
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
        *(("inactive", 1),
          ("active", 2),
          ("pass", 3),
          ("fail", 4),
          ("aborted", 5),
          ("waiting", 6))
    )





class TestType(Integer32):
    """Custom type TestType based on Integer32"""
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
          ("lineQuality", 1),
          ("capHardware", 2),
          ("dmtLocalTest", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cisco6200MIB_ObjectIdentity = ObjectIdentity
cisco6200MIB = _Cisco6200MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26)
)
_Cisco6200MibObjects_ObjectIdentity = ObjectIdentity
cisco6200MibObjects = _Cisco6200MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1)
)
_C62System_ObjectIdentity = ObjectIdentity
c62System = _C62System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 1)
)


class _SystemType_Type(Integer32):
    """Custom type systemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("c62OC3", 1)
    )


_SystemType_Type.__name__ = "Integer32"
_SystemType_Object = MibScalar
systemType = _SystemType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 1, 1),
    _SystemType_Type()
)
systemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemType.setStatus("mandatory")
_SystemAlarmLevel_Type = AlarmLevel
_SystemAlarmLevel_Object = MibScalar
systemAlarmLevel = _SystemAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 1, 2),
    _SystemAlarmLevel_Type()
)
systemAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemAlarmLevel.setStatus("mandatory")
_SystemAlarmLevelChngCounter_Type = Counter32
_SystemAlarmLevelChngCounter_Object = MibScalar
systemAlarmLevelChngCounter = _SystemAlarmLevelChngCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 1, 3),
    _SystemAlarmLevelChngCounter_Type()
)
systemAlarmLevelChngCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemAlarmLevelChngCounter.setStatus("mandatory")
_SystemReset_Type = CommandValue
_SystemReset_Object = MibScalar
systemReset = _SystemReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 1, 4),
    _SystemReset_Type()
)
systemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemReset.setStatus("mandatory")
_SystemSaveCnfg_Type = CommandValue
_SystemSaveCnfg_Object = MibScalar
systemSaveCnfg = _SystemSaveCnfg_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 1, 5),
    _SystemSaveCnfg_Type()
)
systemSaveCnfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSaveCnfg.setStatus("mandatory")
_SystemProvChngCounter_Type = Counter32
_SystemProvChngCounter_Object = MibScalar
systemProvChngCounter = _SystemProvChngCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 1, 6),
    _SystemProvChngCounter_Type()
)
systemProvChngCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemProvChngCounter.setStatus("mandatory")
_SystemHClockAlarmLevel_Type = AlarmLevel
_SystemHClockAlarmLevel_Object = MibScalar
systemHClockAlarmLevel = _SystemHClockAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 1, 7),
    _SystemHClockAlarmLevel_Type()
)
systemHClockAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHClockAlarmLevel.setStatus("mandatory")
_SystemFanAlarmLevel_Type = AlarmLevel
_SystemFanAlarmLevel_Object = MibScalar
systemFanAlarmLevel = _SystemFanAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 1, 8),
    _SystemFanAlarmLevel_Type()
)
systemFanAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFanAlarmLevel.setStatus("mandatory")
_SystemTemperatureAlarmLevel_Type = AlarmLevel
_SystemTemperatureAlarmLevel_Object = MibScalar
systemTemperatureAlarmLevel = _SystemTemperatureAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 1, 9),
    _SystemTemperatureAlarmLevel_Type()
)
systemTemperatureAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTemperatureAlarmLevel.setStatus("mandatory")
_SystemACO_Type = CommandValue
_SystemACO_Object = MibScalar
systemACO = _SystemACO_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 1, 10),
    _SystemACO_Type()
)
systemACO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemACO.setStatus("mandatory")
_C62Slot_ObjectIdentity = ObjectIdentity
c62Slot = _C62Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 2)
)
_SlotTable_Object = MibTable
slotTable = _SlotTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 2, 1)
)
if mibBuilder.loadTexts:
    slotTable.setStatus("mandatory")
_SlotEntry_Object = MibTableRow
slotEntry = _SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 2, 1, 1)
)
slotEntry.setIndexNames(
    (0, "CISCO-6200-MIB", "slotID"),
)
if mibBuilder.loadTexts:
    slotEntry.setStatus("mandatory")


class _SlotID_Type(Integer32):
    """Custom type slotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_SlotID_Type.__name__ = "Integer32"
_SlotID_Object = MibTableColumn
slotID = _SlotID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 2, 1, 1, 1),
    _SlotID_Type()
)
slotID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slotID.setStatus("mandatory")
_SlotType_Type = C6200CardType
_SlotType_Object = MibTableColumn
slotType = _SlotType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 2, 1, 1, 2),
    _SlotType_Type()
)
slotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotType.setStatus("mandatory")


class _SlotStatus_Type(Integer32):
    """Custom type slotStatus based on Integer32"""
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
        *(("empty", 1),
          ("notProvisioned", 2),
          ("missing", 3),
          ("mismatch", 4),
          ("match", 5))
    )


_SlotStatus_Type.__name__ = "Integer32"
_SlotStatus_Object = MibTableColumn
slotStatus = _SlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 2, 1, 1, 3),
    _SlotStatus_Type()
)
slotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatus.setStatus("mandatory")
_SlotSwVersion_Type = Integer32
_SlotSwVersion_Object = MibTableColumn
slotSwVersion = _SlotSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 2, 1, 1, 4),
    _SlotSwVersion_Type()
)
slotSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotSwVersion.setStatus("mandatory")
_SlotAlarmLevelChngCounter_Type = Counter32
_SlotAlarmLevelChngCounter_Object = MibTableColumn
slotAlarmLevelChngCounter = _SlotAlarmLevelChngCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 2, 1, 1, 5),
    _SlotAlarmLevelChngCounter_Type()
)
slotAlarmLevelChngCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotAlarmLevelChngCounter.setStatus("mandatory")
_SlotCnfType_Type = C6200CardType
_SlotCnfType_Object = MibTableColumn
slotCnfType = _SlotCnfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 2, 1, 1, 6),
    _SlotCnfType_Type()
)
slotCnfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotCnfType.setStatus("mandatory")
_SlotSubscriberChngCounter_Type = Counter32
_SlotSubscriberChngCounter_Object = MibTableColumn
slotSubscriberChngCounter = _SlotSubscriberChngCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 2, 1, 1, 7),
    _SlotSubscriberChngCounter_Type()
)
slotSubscriberChngCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotSubscriberChngCounter.setStatus("mandatory")
_SlotAlarmLevel_Type = AlarmLevel
_SlotAlarmLevel_Object = MibTableColumn
slotAlarmLevel = _SlotAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 2, 1, 1, 8),
    _SlotAlarmLevel_Type()
)
slotAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotAlarmLevel.setStatus("mandatory")


class _PortID_Type(Integer32):
    """Custom type portID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_PortID_Type.__name__ = "Integer32"
_PortID_Object = MibScalar
portID = _PortID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 2, 2),
    _PortID_Type()
)
portID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portID.setStatus("mandatory")
_C62OCInterface_ObjectIdentity = ObjectIdentity
c62OCInterface = _C62OCInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3)
)
_OCInterfaceTable_Object = MibTable
oCInterfaceTable = _OCInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1)
)
if mibBuilder.loadTexts:
    oCInterfaceTable.setStatus("mandatory")
_OCInterfaceEntry_Object = MibTableRow
oCInterfaceEntry = _OCInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1)
)
oCInterfaceEntry.setIndexNames(
    (0, "CISCO-6200-MIB", "slotID"),
    (0, "CISCO-6200-MIB", "portID"),
)
if mibBuilder.loadTexts:
    oCInterfaceEntry.setStatus("mandatory")
_OCIAlarmLevel_Type = AlarmLevel
_OCIAlarmLevel_Object = MibTableColumn
oCIAlarmLevel = _OCIAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1, 2),
    _OCIAlarmLevel_Type()
)
oCIAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCIAlarmLevel.setStatus("mandatory")
_OCIEQF_Type = AlarmLevel
_OCIEQF_Object = MibTableColumn
oCIEQF = _OCIEQF_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1, 3),
    _OCIEQF_Type()
)
oCIEQF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCIEQF.setStatus("mandatory")
_OCILOS_Type = AlarmLevel
_OCILOS_Object = MibTableColumn
oCILOS = _OCILOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1, 4),
    _OCILOS_Type()
)
oCILOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCILOS.setStatus("mandatory")
_OCILOF_Type = AlarmLevel
_OCILOF_Object = MibTableColumn
oCILOF = _OCILOF_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1, 5),
    _OCILOF_Type()
)
oCILOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCILOF.setStatus("mandatory")
_OCILAIS_Type = AlarmLevel
_OCILAIS_Object = MibTableColumn
oCILAIS = _OCILAIS_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1, 6),
    _OCILAIS_Type()
)
oCILAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCILAIS.setStatus("mandatory")
_OCILOP_Type = AlarmLevel
_OCILOP_Object = MibTableColumn
oCILOP = _OCILOP_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1, 7),
    _OCILOP_Type()
)
oCILOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCILOP.setStatus("mandatory")
_OCIPAIS_Type = AlarmLevel
_OCIPAIS_Object = MibTableColumn
oCIPAIS = _OCIPAIS_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1, 8),
    _OCIPAIS_Type()
)
oCIPAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCIPAIS.setStatus("mandatory")
_OCISLM_Type = AlarmLevel
_OCISLM_Object = MibTableColumn
oCISLM = _OCISLM_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1, 9),
    _OCISLM_Type()
)
oCISLM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCISLM.setStatus("mandatory")
_OCILRFI_Type = AlarmLevel
_OCILRFI_Object = MibTableColumn
oCILRFI = _OCILRFI_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1, 10),
    _OCILRFI_Type()
)
oCILRFI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCILRFI.setStatus("mandatory")
_OCIPRFI_Type = AlarmLevel
_OCIPRFI_Object = MibTableColumn
oCIPRFI = _OCIPRFI_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1, 11),
    _OCIPRFI_Type()
)
oCIPRFI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCIPRFI.setStatus("mandatory")
_OCILOST_Type = AlarmLevel
_OCILOST_Object = MibTableColumn
oCILOST = _OCILOST_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1, 12),
    _OCILOST_Type()
)
oCILOST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCILOST.setStatus("mandatory")
_OCILOCD_Type = AlarmLevel
_OCILOCD_Object = MibTableColumn
oCILOCD = _OCILOCD_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1, 13),
    _OCILOCD_Type()
)
oCILOCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCILOCD.setStatus("mandatory")


class _OCILoopMode_Type(Integer32):
    """Custom type oCILoopMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_OCILoopMode_Type.__name__ = "Integer32"
_OCILoopMode_Object = MibTableColumn
oCILoopMode = _OCILoopMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1, 14),
    _OCILoopMode_Type()
)
oCILoopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oCILoopMode.setStatus("mandatory")
_OCPerfTable_Object = MibTable
oCPerfTable = _OCPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 2)
)
if mibBuilder.loadTexts:
    oCPerfTable.setStatus("mandatory")
_OCPerfEntry_Object = MibTableRow
oCPerfEntry = _OCPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 2, 1)
)
oCPerfEntry.setIndexNames(
    (0, "CISCO-6200-MIB", "slotID"),
    (0, "CISCO-6200-MIB", "portID"),
)
if mibBuilder.loadTexts:
    oCPerfEntry.setStatus("mandatory")
_OCPTxCellCount_Type = Counter32
_OCPTxCellCount_Object = MibTableColumn
oCPTxCellCount = _OCPTxCellCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 2, 1, 1),
    _OCPTxCellCount_Type()
)
oCPTxCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCPTxCellCount.setStatus("mandatory")
_OCPRxCellCount_Type = Counter32
_OCPRxCellCount_Object = MibTableColumn
oCPRxCellCount = _OCPRxCellCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 2, 1, 2),
    _OCPRxCellCount_Type()
)
oCPRxCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCPRxCellCount.setStatus("mandatory")
_OCPHecErrCount_Type = Counter32
_OCPHecErrCount_Object = MibTableColumn
oCPHecErrCount = _OCPHecErrCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 2, 1, 3),
    _OCPHecErrCount_Type()
)
oCPHecErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCPHecErrCount.setStatus("mandatory")
_C62LineInterface_ObjectIdentity = ObjectIdentity
c62LineInterface = _C62LineInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4)
)
_LineInterfaceTable_Object = MibTable
lineInterfaceTable = _LineInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lineInterfaceTable.setStatus("mandatory")
_LineInterfaceEntry_Object = MibTableRow
lineInterfaceEntry = _LineInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1)
)
lineInterfaceEntry.setIndexNames(
    (0, "CISCO-6200-MIB", "slotID"),
    (0, "CISCO-6200-MIB", "portID"),
)
if mibBuilder.loadTexts:
    lineInterfaceEntry.setStatus("mandatory")
_LineAlarmLevel_Type = AlarmLevel
_LineAlarmLevel_Object = MibTableColumn
lineAlarmLevel = _LineAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 1),
    _LineAlarmLevel_Type()
)
lineAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineAlarmLevel.setStatus("mandatory")
_LineDwnSNRMargin_Type = Integer32
_LineDwnSNRMargin_Object = MibTableColumn
lineDwnSNRMargin = _LineDwnSNRMargin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 2),
    _LineDwnSNRMargin_Type()
)
lineDwnSNRMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDwnSNRMargin.setStatus("mandatory")
_LineDwnLOCD_Type = AlarmLevel
_LineDwnLOCD_Object = MibTableColumn
lineDwnLOCD = _LineDwnLOCD_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 3),
    _LineDwnLOCD_Type()
)
lineDwnLOCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDwnLOCD.setStatus("deprecated")
_LineDwnErrSecs_Type = Counter32
_LineDwnErrSecs_Object = MibTableColumn
lineDwnErrSecs = _LineDwnErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 4),
    _LineDwnErrSecs_Type()
)
lineDwnErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDwnErrSecs.setStatus("mandatory")
_LineDwnLineRate_Type = Gauge32
_LineDwnLineRate_Object = MibTableColumn
lineDwnLineRate = _LineDwnLineRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 5),
    _LineDwnLineRate_Type()
)
lineDwnLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDwnLineRate.setStatus("mandatory")
_LineUpSNRMargin_Type = Integer32
_LineUpSNRMargin_Object = MibTableColumn
lineUpSNRMargin = _LineUpSNRMargin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 6),
    _LineUpSNRMargin_Type()
)
lineUpSNRMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineUpSNRMargin.setStatus("mandatory")
_LineUpLOCD_Type = AlarmLevel
_LineUpLOCD_Object = MibTableColumn
lineUpLOCD = _LineUpLOCD_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 7),
    _LineUpLOCD_Type()
)
lineUpLOCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineUpLOCD.setStatus("mandatory")
_LineUpErrSecs_Type = Counter32
_LineUpErrSecs_Object = MibTableColumn
lineUpErrSecs = _LineUpErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 8),
    _LineUpErrSecs_Type()
)
lineUpErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineUpErrSecs.setStatus("mandatory")
_LineUpLineRate_Type = Gauge32
_LineUpLineRate_Object = MibTableColumn
lineUpLineRate = _LineUpLineRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 9),
    _LineUpLineRate_Type()
)
lineUpLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineUpLineRate.setStatus("mandatory")


class _LineRateAlarm_Type(Integer32):
    """Custom type lineRateAlarm based on Integer32"""
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
        *(("ok", 1),
          ("down", 2),
          ("up", 3),
          ("downAndUp", 4))
    )


_LineRateAlarm_Type.__name__ = "Integer32"
_LineRateAlarm_Object = MibTableColumn
lineRateAlarm = _LineRateAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 10),
    _LineRateAlarm_Type()
)
lineRateAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineRateAlarm.setStatus("mandatory")


class _LineMode_Type(Integer32):
    """Custom type lineMode based on Integer32"""
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
        *(("testing", 1),
          ("training", 2),
          ("active", 3),
          ("down", 4))
    )


_LineMode_Type.__name__ = "Integer32"
_LineMode_Object = MibTableColumn
lineMode = _LineMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 11),
    _LineMode_Type()
)
lineMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineMode.setStatus("mandatory")
_LineDMTDwnAttenuation_Type = Gauge32
_LineDMTDwnAttenuation_Object = MibTableColumn
lineDMTDwnAttenuation = _LineDMTDwnAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 12),
    _LineDMTDwnAttenuation_Type()
)
lineDMTDwnAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDMTDwnAttenuation.setStatus("mandatory")
_LineDMTUpAttenuation_Type = Gauge32
_LineDMTUpAttenuation_Object = MibTableColumn
lineDMTUpAttenuation = _LineDMTUpAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 13),
    _LineDMTUpAttenuation_Type()
)
lineDMTUpAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDMTUpAttenuation.setStatus("mandatory")
_LineDMTDwnLPR_Type = AlarmLevel
_LineDMTDwnLPR_Object = MibTableColumn
lineDMTDwnLPR = _LineDMTDwnLPR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 14),
    _LineDMTDwnLPR_Type()
)
lineDMTDwnLPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDMTDwnLPR.setStatus("mandatory")
_LineDMTUpLOS_Type = AlarmLevel
_LineDMTUpLOS_Object = MibTableColumn
lineDMTUpLOS = _LineDMTUpLOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 15),
    _LineDMTUpLOS_Type()
)
lineDMTUpLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDMTUpLOS.setStatus("mandatory")
_LineDMTUpLOF_Type = AlarmLevel
_LineDMTUpLOF_Object = MibTableColumn
lineDMTUpLOF = _LineDMTUpLOF_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 16),
    _LineDMTUpLOF_Type()
)
lineDMTUpLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDMTUpLOF.setStatus("mandatory")


class _LineDMTLoopback_Type(Integer32):
    """Custom type lineDMTLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("dslline", 2),
          ("local", 3))
    )


_LineDMTLoopback_Type.__name__ = "Integer32"
_LineDMTLoopback_Object = MibTableColumn
lineDMTLoopback = _LineDMTLoopback_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 17),
    _LineDMTLoopback_Type()
)
lineDMTLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineDMTLoopback.setStatus("mandatory")
_LinePerfTable_Object = MibTable
linePerfTable = _LinePerfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 2)
)
if mibBuilder.loadTexts:
    linePerfTable.setStatus("mandatory")
_LinePerfEntry_Object = MibTableRow
linePerfEntry = _LinePerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 2, 1)
)
linePerfEntry.setIndexNames(
    (0, "CISCO-6200-MIB", "slotID"),
    (0, "CISCO-6200-MIB", "portID"),
)
if mibBuilder.loadTexts:
    linePerfEntry.setStatus("mandatory")
_LineTxCellCount_Type = Counter32
_LineTxCellCount_Object = MibTableColumn
lineTxCellCount = _LineTxCellCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 2, 1, 1),
    _LineTxCellCount_Type()
)
lineTxCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineTxCellCount.setStatus("mandatory")
_LineRxCellCount_Type = Counter32
_LineRxCellCount_Object = MibTableColumn
lineRxCellCount = _LineRxCellCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 2, 1, 2),
    _LineRxCellCount_Type()
)
lineRxCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineRxCellCount.setStatus("mandatory")
_LineHecErrCount_Type = Counter32
_LineHecErrCount_Object = MibTableColumn
lineHecErrCount = _LineHecErrCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 2, 1, 3),
    _LineHecErrCount_Type()
)
lineHecErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineHecErrCount.setStatus("mandatory")
_LineDMTDwnFECCount_Type = Counter32
_LineDMTDwnFECCount_Object = MibTableColumn
lineDMTDwnFECCount = _LineDMTDwnFECCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 2, 1, 4),
    _LineDMTDwnFECCount_Type()
)
lineDMTDwnFECCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDMTDwnFECCount.setStatus("mandatory")
_LineDMTUpFECCount_Type = Counter32
_LineDMTUpFECCount_Object = MibTableColumn
lineDMTUpFECCount = _LineDMTUpFECCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 2, 1, 5),
    _LineDMTUpFECCount_Type()
)
lineDMTUpFECCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDMTUpFECCount.setStatus("mandatory")
_LineDMTDwnCRCCount_Type = Counter32
_LineDMTDwnCRCCount_Object = MibTableColumn
lineDMTDwnCRCCount = _LineDMTDwnCRCCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 2, 1, 6),
    _LineDMTDwnCRCCount_Type()
)
lineDMTDwnCRCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDMTDwnCRCCount.setStatus("mandatory")
_LineDMTUpCRCCount_Type = Counter32
_LineDMTUpCRCCount_Object = MibTableColumn
lineDMTUpCRCCount = _LineDMTUpCRCCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 2, 1, 7),
    _LineDMTUpCRCCount_Type()
)
lineDMTUpCRCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDMTUpCRCCount.setStatus("mandatory")
_LineDMTDwnLOSCount_Type = Counter32
_LineDMTDwnLOSCount_Object = MibTableColumn
lineDMTDwnLOSCount = _LineDMTDwnLOSCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 2, 1, 8),
    _LineDMTDwnLOSCount_Type()
)
lineDMTDwnLOSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDMTDwnLOSCount.setStatus("mandatory")
_LineDMTUpLOSCount_Type = Counter32
_LineDMTUpLOSCount_Object = MibTableColumn
lineDMTUpLOSCount = _LineDMTUpLOSCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 2, 1, 9),
    _LineDMTUpLOSCount_Type()
)
lineDMTUpLOSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDMTUpLOSCount.setStatus("mandatory")
_LineDMTDwnSEFCount_Type = Counter32
_LineDMTDwnSEFCount_Object = MibTableColumn
lineDMTDwnSEFCount = _LineDMTDwnSEFCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 2, 1, 10),
    _LineDMTDwnSEFCount_Type()
)
lineDMTDwnSEFCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDMTDwnSEFCount.setStatus("mandatory")
_LineDMTUpRDICount_Type = Counter32
_LineDMTUpRDICount_Object = MibTableColumn
lineDMTUpRDICount = _LineDMTUpRDICount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 2, 1, 11),
    _LineDMTUpRDICount_Type()
)
lineDMTUpRDICount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDMTUpRDICount.setStatus("mandatory")
_LineTestTable_Object = MibTable
lineTestTable = _LineTestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 3)
)
if mibBuilder.loadTexts:
    lineTestTable.setStatus("mandatory")
_LineTestEntry_Object = MibTableRow
lineTestEntry = _LineTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 3, 1)
)
lineTestEntry.setIndexNames(
    (0, "CISCO-6200-MIB", "slotID"),
    (0, "CISCO-6200-MIB", "portID"),
)
if mibBuilder.loadTexts:
    lineTestEntry.setStatus("mandatory")


class _LineTestTrigger_Type(Integer32):
    """Custom type lineTestTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stop", 1),
          ("start", 2),
          ("clear", 3))
    )


_LineTestTrigger_Type.__name__ = "Integer32"
_LineTestTrigger_Object = MibTableColumn
lineTestTrigger = _LineTestTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 3, 1, 1),
    _LineTestTrigger_Type()
)
lineTestTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineTestTrigger.setStatus("mandatory")
_LineTestType_Type = TestType
_LineTestType_Object = MibTableColumn
lineTestType = _LineTestType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 3, 1, 2),
    _LineTestType_Type()
)
lineTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineTestType.setStatus("mandatory")


class _LineTestTimeIntvl_Type(Integer32):
    """Custom type lineTestTimeIntvl based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_LineTestTimeIntvl_Type.__name__ = "Integer32"
_LineTestTimeIntvl_Object = MibTableColumn
lineTestTimeIntvl = _LineTestTimeIntvl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 3, 1, 3),
    _LineTestTimeIntvl_Type()
)
lineTestTimeIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineTestTimeIntvl.setStatus("mandatory")
_LineTestStatus_Type = TestStatus
_LineTestStatus_Object = MibTableColumn
lineTestStatus = _LineTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 3, 1, 4),
    _LineTestStatus_Type()
)
lineTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineTestStatus.setStatus("mandatory")
_LineTestDwnBitErrRate_Type = Integer32
_LineTestDwnBitErrRate_Object = MibTableColumn
lineTestDwnBitErrRate = _LineTestDwnBitErrRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 3, 1, 5),
    _LineTestDwnBitErrRate_Type()
)
lineTestDwnBitErrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineTestDwnBitErrRate.setStatus("mandatory")
_LineTestUpBitErrRate_Type = Integer32
_LineTestUpBitErrRate_Object = MibTableColumn
lineTestUpBitErrRate = _LineTestUpBitErrRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 3, 1, 6),
    _LineTestUpBitErrRate_Type()
)
lineTestUpBitErrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineTestUpBitErrRate.setStatus("mandatory")
_LineTestStartTime_Type = DateAndTime
_LineTestStartTime_Object = MibTableColumn
lineTestStartTime = _LineTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 3, 1, 7),
    _LineTestStartTime_Type()
)
lineTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineTestStartTime.setStatus("mandatory")
_LineTestCmplTime_Type = DateAndTime
_LineTestCmplTime_Object = MibTableColumn
lineTestCmplTime = _LineTestCmplTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 3, 1, 8),
    _LineTestCmplTime_Type()
)
lineTestCmplTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineTestCmplTime.setStatus("mandatory")


class _LineTestBitErrRateLimit_Type(Integer32):
    """Custom type lineTestBitErrRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_LineTestBitErrRateLimit_Type.__name__ = "Integer32"
_LineTestBitErrRateLimit_Object = MibTableColumn
lineTestBitErrRateLimit = _LineTestBitErrRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 3, 1, 9),
    _LineTestBitErrRateLimit_Type()
)
lineTestBitErrRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineTestBitErrRateLimit.setStatus("mandatory")
_C62Subscriber_ObjectIdentity = ObjectIdentity
c62Subscriber = _C62Subscriber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 5)
)
_SubscriberTable_Object = MibTable
subscriberTable = _SubscriberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 5, 1)
)
if mibBuilder.loadTexts:
    subscriberTable.setStatus("mandatory")
_SubscriberEntry_Object = MibTableRow
subscriberEntry = _SubscriberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 5, 1, 1)
)
subscriberEntry.setIndexNames(
    (0, "CISCO-6200-MIB", "slotID"),
    (0, "CISCO-6200-MIB", "portID"),
)
if mibBuilder.loadTexts:
    subscriberEntry.setStatus("mandatory")


class _SubscriberName_Type(DisplayString):
    """Custom type subscriberName based on DisplayString"""
    defaultValue = OctetString("DSL<slotID>/<portID>")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_SubscriberName_Type.__name__ = "DisplayString"
_SubscriberName_Object = MibTableColumn
subscriberName = _SubscriberName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 5, 1, 1, 1),
    _SubscriberName_Type()
)
subscriberName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberName.setStatus("mandatory")
_SubscriberUpLineRate_Type = Integer32
_SubscriberUpLineRate_Object = MibTableColumn
subscriberUpLineRate = _SubscriberUpLineRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 5, 1, 1, 2),
    _SubscriberUpLineRate_Type()
)
subscriberUpLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberUpLineRate.setStatus("mandatory")
_SubscriberDwnLineRate_Type = Integer32
_SubscriberDwnLineRate_Object = MibTableColumn
subscriberDwnLineRate = _SubscriberDwnLineRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 5, 1, 1, 3),
    _SubscriberDwnLineRate_Type()
)
subscriberDwnLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberDwnLineRate.setStatus("mandatory")


class _SubscriberLineState_Type(InterfaceStatus):
    """Custom type subscriberLineState based on InterfaceStatus"""
    defaultValue = 2


_SubscriberLineState_Type.__name__ = "InterfaceStatus"
_SubscriberLineState_Object = MibTableColumn
subscriberLineState = _SubscriberLineState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 5, 1, 1, 4),
    _SubscriberLineState_Type()
)
subscriberLineState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberLineState.setStatus("mandatory")


class _SubscriberDMTLOSConfig_Type(InterfaceStatus):
    """Custom type subscriberDMTLOSConfig based on InterfaceStatus"""
    defaultValue = 2


_SubscriberDMTLOSConfig_Type.__name__ = "InterfaceStatus"
_SubscriberDMTLOSConfig_Object = MibTableColumn
subscriberDMTLOSConfig = _SubscriberDMTLOSConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 5, 1, 1, 5),
    _SubscriberDMTLOSConfig_Type()
)
subscriberDMTLOSConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberDMTLOSConfig.setStatus("mandatory")
_CiscoC6200MIBConformance_ObjectIdentity = ObjectIdentity
ciscoC6200MIBConformance = _CiscoC6200MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2)
)
_CiscoC6200MIBCompliances_ObjectIdentity = ObjectIdentity
ciscoC6200MIBCompliances = _CiscoC6200MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 1)
)
_CiscoC6200MIBCompliance_ObjectIdentity = ObjectIdentity
ciscoC6200MIBCompliance = _CiscoC6200MIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 1, 1)
)
_CiscoC6200MIBCompliance2_ObjectIdentity = ObjectIdentity
ciscoC6200MIBCompliance2 = _CiscoC6200MIBCompliance2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 1, 2)
)
_CiscoC6200MIBGroups_ObjectIdentity = ObjectIdentity
ciscoC6200MIBGroups = _CiscoC6200MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2)
)
_CiscoC6200SystemGroup_ObjectIdentity = ObjectIdentity
ciscoC6200SystemGroup = _CiscoC6200SystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 1)
)
_CiscoC6200SlotGroup_ObjectIdentity = ObjectIdentity
ciscoC6200SlotGroup = _CiscoC6200SlotGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 2)
)
_CiscoC6200oCIGroup_ObjectIdentity = ObjectIdentity
ciscoC6200oCIGroup = _CiscoC6200oCIGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 3)
)
_CiscoC6200oCIPerfGroup_ObjectIdentity = ObjectIdentity
ciscoC6200oCIPerfGroup = _CiscoC6200oCIPerfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 4)
)
_CiscoC6200lineGroup_ObjectIdentity = ObjectIdentity
ciscoC6200lineGroup = _CiscoC6200lineGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 5)
)
_CiscoC6200linePerfGroup_ObjectIdentity = ObjectIdentity
ciscoC6200linePerfGroup = _CiscoC6200linePerfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 6)
)
_CiscoC6200lineTestGroup_ObjectIdentity = ObjectIdentity
ciscoC6200lineTestGroup = _CiscoC6200lineTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 7)
)
_CiscoC6200subscriberGroup_ObjectIdentity = ObjectIdentity
ciscoC6200subscriberGroup = _CiscoC6200subscriberGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 8)
)
_CiscoC6200SystemGroup2_ObjectIdentity = ObjectIdentity
ciscoC6200SystemGroup2 = _CiscoC6200SystemGroup2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 9)
)
_CiscoC6200SlotGroup2_ObjectIdentity = ObjectIdentity
ciscoC6200SlotGroup2 = _CiscoC6200SlotGroup2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 10)
)
_CiscoC6200oCIGroup2_ObjectIdentity = ObjectIdentity
ciscoC6200oCIGroup2 = _CiscoC6200oCIGroup2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 11)
)
_CiscoC6200oCIPerfGroup2_ObjectIdentity = ObjectIdentity
ciscoC6200oCIPerfGroup2 = _CiscoC6200oCIPerfGroup2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 12)
)
_CiscoC6200lineGroup2_ObjectIdentity = ObjectIdentity
ciscoC6200lineGroup2 = _CiscoC6200lineGroup2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 13)
)
_CiscoC6200linePerfGroup2_ObjectIdentity = ObjectIdentity
ciscoC6200linePerfGroup2 = _CiscoC6200linePerfGroup2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 14)
)
_CiscoC6200lineTestGroup2_ObjectIdentity = ObjectIdentity
ciscoC6200lineTestGroup2 = _CiscoC6200lineTestGroup2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 15)
)
_CiscoC6200subscriberGroup2_ObjectIdentity = ObjectIdentity
ciscoC6200subscriberGroup2 = _CiscoC6200subscriberGroup2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 16)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-6200-MIB",
    **{"C6200CardType": C6200CardType,
       "CommandValue": CommandValue,
       "AlarmLevel": AlarmLevel,
       "InterfaceStatus": InterfaceStatus,
       "TestStatus": TestStatus,
       "TestType": TestType,
       "cisco6200MIB": cisco6200MIB,
       "cisco6200MibObjects": cisco6200MibObjects,
       "c62System": c62System,
       "systemType": systemType,
       "systemAlarmLevel": systemAlarmLevel,
       "systemAlarmLevelChngCounter": systemAlarmLevelChngCounter,
       "systemReset": systemReset,
       "systemSaveCnfg": systemSaveCnfg,
       "systemProvChngCounter": systemProvChngCounter,
       "systemHClockAlarmLevel": systemHClockAlarmLevel,
       "systemFanAlarmLevel": systemFanAlarmLevel,
       "systemTemperatureAlarmLevel": systemTemperatureAlarmLevel,
       "systemACO": systemACO,
       "c62Slot": c62Slot,
       "slotTable": slotTable,
       "slotEntry": slotEntry,
       "slotID": slotID,
       "slotType": slotType,
       "slotStatus": slotStatus,
       "slotSwVersion": slotSwVersion,
       "slotAlarmLevelChngCounter": slotAlarmLevelChngCounter,
       "slotCnfType": slotCnfType,
       "slotSubscriberChngCounter": slotSubscriberChngCounter,
       "slotAlarmLevel": slotAlarmLevel,
       "portID": portID,
       "c62OCInterface": c62OCInterface,
       "oCInterfaceTable": oCInterfaceTable,
       "oCInterfaceEntry": oCInterfaceEntry,
       "oCIAlarmLevel": oCIAlarmLevel,
       "oCIEQF": oCIEQF,
       "oCILOS": oCILOS,
       "oCILOF": oCILOF,
       "oCILAIS": oCILAIS,
       "oCILOP": oCILOP,
       "oCIPAIS": oCIPAIS,
       "oCISLM": oCISLM,
       "oCILRFI": oCILRFI,
       "oCIPRFI": oCIPRFI,
       "oCILOST": oCILOST,
       "oCILOCD": oCILOCD,
       "oCILoopMode": oCILoopMode,
       "oCPerfTable": oCPerfTable,
       "oCPerfEntry": oCPerfEntry,
       "oCPTxCellCount": oCPTxCellCount,
       "oCPRxCellCount": oCPRxCellCount,
       "oCPHecErrCount": oCPHecErrCount,
       "c62LineInterface": c62LineInterface,
       "lineInterfaceTable": lineInterfaceTable,
       "lineInterfaceEntry": lineInterfaceEntry,
       "lineAlarmLevel": lineAlarmLevel,
       "lineDwnSNRMargin": lineDwnSNRMargin,
       "lineDwnLOCD": lineDwnLOCD,
       "lineDwnErrSecs": lineDwnErrSecs,
       "lineDwnLineRate": lineDwnLineRate,
       "lineUpSNRMargin": lineUpSNRMargin,
       "lineUpLOCD": lineUpLOCD,
       "lineUpErrSecs": lineUpErrSecs,
       "lineUpLineRate": lineUpLineRate,
       "lineRateAlarm": lineRateAlarm,
       "lineMode": lineMode,
       "lineDMTDwnAttenuation": lineDMTDwnAttenuation,
       "lineDMTUpAttenuation": lineDMTUpAttenuation,
       "lineDMTDwnLPR": lineDMTDwnLPR,
       "lineDMTUpLOS": lineDMTUpLOS,
       "lineDMTUpLOF": lineDMTUpLOF,
       "lineDMTLoopback": lineDMTLoopback,
       "linePerfTable": linePerfTable,
       "linePerfEntry": linePerfEntry,
       "lineTxCellCount": lineTxCellCount,
       "lineRxCellCount": lineRxCellCount,
       "lineHecErrCount": lineHecErrCount,
       "lineDMTDwnFECCount": lineDMTDwnFECCount,
       "lineDMTUpFECCount": lineDMTUpFECCount,
       "lineDMTDwnCRCCount": lineDMTDwnCRCCount,
       "lineDMTUpCRCCount": lineDMTUpCRCCount,
       "lineDMTDwnLOSCount": lineDMTDwnLOSCount,
       "lineDMTUpLOSCount": lineDMTUpLOSCount,
       "lineDMTDwnSEFCount": lineDMTDwnSEFCount,
       "lineDMTUpRDICount": lineDMTUpRDICount,
       "lineTestTable": lineTestTable,
       "lineTestEntry": lineTestEntry,
       "lineTestTrigger": lineTestTrigger,
       "lineTestType": lineTestType,
       "lineTestTimeIntvl": lineTestTimeIntvl,
       "lineTestStatus": lineTestStatus,
       "lineTestDwnBitErrRate": lineTestDwnBitErrRate,
       "lineTestUpBitErrRate": lineTestUpBitErrRate,
       "lineTestStartTime": lineTestStartTime,
       "lineTestCmplTime": lineTestCmplTime,
       "lineTestBitErrRateLimit": lineTestBitErrRateLimit,
       "c62Subscriber": c62Subscriber,
       "subscriberTable": subscriberTable,
       "subscriberEntry": subscriberEntry,
       "subscriberName": subscriberName,
       "subscriberUpLineRate": subscriberUpLineRate,
       "subscriberDwnLineRate": subscriberDwnLineRate,
       "subscriberLineState": subscriberLineState,
       "subscriberDMTLOSConfig": subscriberDMTLOSConfig,
       "ciscoC6200MIBConformance": ciscoC6200MIBConformance,
       "ciscoC6200MIBCompliances": ciscoC6200MIBCompliances,
       "ciscoC6200MIBCompliance": ciscoC6200MIBCompliance,
       "ciscoC6200MIBCompliance2": ciscoC6200MIBCompliance2,
       "ciscoC6200MIBGroups": ciscoC6200MIBGroups,
       "ciscoC6200SystemGroup": ciscoC6200SystemGroup,
       "ciscoC6200SlotGroup": ciscoC6200SlotGroup,
       "ciscoC6200oCIGroup": ciscoC6200oCIGroup,
       "ciscoC6200oCIPerfGroup": ciscoC6200oCIPerfGroup,
       "ciscoC6200lineGroup": ciscoC6200lineGroup,
       "ciscoC6200linePerfGroup": ciscoC6200linePerfGroup,
       "ciscoC6200lineTestGroup": ciscoC6200lineTestGroup,
       "ciscoC6200subscriberGroup": ciscoC6200subscriberGroup,
       "ciscoC6200SystemGroup2": ciscoC6200SystemGroup2,
       "ciscoC6200SlotGroup2": ciscoC6200SlotGroup2,
       "ciscoC6200oCIGroup2": ciscoC6200oCIGroup2,
       "ciscoC6200oCIPerfGroup2": ciscoC6200oCIPerfGroup2,
       "ciscoC6200lineGroup2": ciscoC6200lineGroup2,
       "ciscoC6200linePerfGroup2": ciscoC6200linePerfGroup2,
       "ciscoC6200lineTestGroup2": ciscoC6200lineTestGroup2,
       "ciscoC6200subscriberGroup2": ciscoC6200subscriberGroup2}
)
