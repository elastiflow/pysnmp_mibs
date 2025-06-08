# SNMP MIB module (ME1200-PTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-PTP-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:31 2025
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

(me1200SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCOME1200-MIB",
    "me1200SwitchMgmt")

(ME1200Integer16,
 ME1200Integer64,
 ME1200InterfaceIndex,
 ME1200RowEditorState,
 ME1200Unsigned16,
 ME1200Unsigned64,
 ME1200Unsigned8) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200Integer16",
    "ME1200Integer64",
    "ME1200InterfaceIndex",
    "ME1200RowEditorState",
    "ME1200Unsigned16",
    "ME1200Unsigned64",
    "ME1200Unsigned8")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

me1200PtpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65)
)
if mibBuilder.loadTexts:
    me1200PtpMib.setRevisions(
        ("2015-07-06 00:00",
         "2015-03-26 00:00",
         "2014-04-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200ptpClockPortState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("initializing", 0),
          ("faulty", 1),
          ("disabled", 2),
          ("listening", 3),
          ("preMaster", 4),
          ("master", 5),
          ("passive", 6),
          ("uncalibrated", 7),
          ("slave", 8),
          ("p2pTransparent", 9),
          ("e2eTransparent", 10))
    )



class ME1200ptpDestAdrType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("linkLocal", 1))
    )



class ME1200ptpDeviceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ordBound", 1),
          ("p2pTransparent", 2),
          ("e2eTransparent", 3),
          ("masterOnly", 4),
          ("slaveOnly", 5))
    )



class ME1200ptpExtClock1pps(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onePpsDisable", 0),
          ("onePpsOutput", 1),
          ("onePpsInput", 2))
    )



class ME1200ptpPreferredAdj(TextualConvention, Integer32):
    status = "current"
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
        *(("preferredAdjLtc", 0),
          ("preferredAdjSyncE", 1),
          ("preferredAdjXO", 2),
          ("preferredAdjLtcPhase", 3))
    )



class ME1200ptpProfile(TextualConvention, Integer32):
    status = "current"
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
        *(("noProfile", 0),
          ("ieee1588", 1),
          ("g8265", 2),
          ("g8275", 3))
    )



class ME1200ptpProtocol(TextualConvention, Integer32):
    status = "current"
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
        *(("ethernet", 0),
          ("ethernetMixed", 1),
          ("ip4multi", 2),
          ("ip4mixed", 3),
          ("ip4uni", 4),
          ("oam", 5),
          ("onePps", 6))
    )



class ME1200ptpServoClockOption(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clockFree", 0),
          ("clockSyncE", 1))
    )



class ME1200ptpSlaveClockState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("slaveClockStateFreerun", 0),
          ("slaveClockStateFreqLocking", 1),
          ("slaveClockStatePhaseLocking", 2),
          ("slaveClockStateLocked", 3),
          ("slaveClockStateHoldover", 4),
          ("slaveClockStateInvalid", 5))
    )



class ME1200ptpSystemTimeSyncMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("systemTimeNoSync", 0),
          ("systemTimeSyncGet", 1),
          ("systemTimeSyncSet", 2))
    )



class ME1200ptpUcCommState(TextualConvention, Integer32):
    status = "current"
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
        *(("idle", 0),
          ("initializing", 1),
          ("connected", 2),
          ("selected", 3),
          ("synced", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200PtpMibObjects_ObjectIdentity = ObjectIdentity
me1200PtpMibObjects = _Me1200PtpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1)
)
_Me1200PtpCapabilities_ObjectIdentity = ObjectIdentity
me1200PtpCapabilities = _Me1200PtpCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 1)
)
_Me1200PtpCapabilitiesGlobals_ObjectIdentity = ObjectIdentity
me1200PtpCapabilitiesGlobals = _Me1200PtpCapabilitiesGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 1, 1)
)
_Me1200PtpCapabilitiesGlobalsClockCount_Type = Unsigned32
_Me1200PtpCapabilitiesGlobalsClockCount_Object = MibScalar
me1200PtpCapabilitiesGlobalsClockCount = _Me1200PtpCapabilitiesGlobalsClockCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 1, 1, 1),
    _Me1200PtpCapabilitiesGlobalsClockCount_Type()
)
me1200PtpCapabilitiesGlobalsClockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpCapabilitiesGlobalsClockCount.setStatus("current")
_Me1200PtpConfig_ObjectIdentity = ObjectIdentity
me1200PtpConfig = _Me1200PtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2)
)
_Me1200PtpConfigGlobals_ObjectIdentity = ObjectIdentity
me1200PtpConfigGlobals = _Me1200PtpConfigGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 1)
)
_Me1200PtpConfigGlobalsExternalClockMode_ObjectIdentity = ObjectIdentity
me1200PtpConfigGlobalsExternalClockMode = _Me1200PtpConfigGlobalsExternalClockMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 1, 1)
)
_Me1200PtpConfigGlobalsExternalClockModeOnePpsMode_Type = ME1200ptpExtClock1pps
_Me1200PtpConfigGlobalsExternalClockModeOnePpsMode_Object = MibScalar
me1200PtpConfigGlobalsExternalClockModeOnePpsMode = _Me1200PtpConfigGlobalsExternalClockModeOnePpsMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 1, 1, 1),
    _Me1200PtpConfigGlobalsExternalClockModeOnePpsMode_Type()
)
me1200PtpConfigGlobalsExternalClockModeOnePpsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigGlobalsExternalClockModeOnePpsMode.setStatus("current")
_Me1200PtpConfigGlobalsExternalClockModeExternalEnable_Type = TruthValue
_Me1200PtpConfigGlobalsExternalClockModeExternalEnable_Object = MibScalar
me1200PtpConfigGlobalsExternalClockModeExternalEnable = _Me1200PtpConfigGlobalsExternalClockModeExternalEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 1, 1, 2),
    _Me1200PtpConfigGlobalsExternalClockModeExternalEnable_Type()
)
me1200PtpConfigGlobalsExternalClockModeExternalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigGlobalsExternalClockModeExternalEnable.setStatus("current")
_Me1200PtpConfigGlobalsExternalClockModeAdjustMethod_Type = ME1200ptpPreferredAdj
_Me1200PtpConfigGlobalsExternalClockModeAdjustMethod_Object = MibScalar
me1200PtpConfigGlobalsExternalClockModeAdjustMethod = _Me1200PtpConfigGlobalsExternalClockModeAdjustMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 1, 1, 3),
    _Me1200PtpConfigGlobalsExternalClockModeAdjustMethod_Type()
)
me1200PtpConfigGlobalsExternalClockModeAdjustMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigGlobalsExternalClockModeAdjustMethod.setStatus("current")
_Me1200PtpConfigGlobalsExternalClockModeClockFrequency_Type = Unsigned32
_Me1200PtpConfigGlobalsExternalClockModeClockFrequency_Object = MibScalar
me1200PtpConfigGlobalsExternalClockModeClockFrequency = _Me1200PtpConfigGlobalsExternalClockModeClockFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 1, 1, 4),
    _Me1200PtpConfigGlobalsExternalClockModeClockFrequency_Type()
)
me1200PtpConfigGlobalsExternalClockModeClockFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigGlobalsExternalClockModeClockFrequency.setStatus("current")
_Me1200PtpConfigGlobalsSystemTimeSyncMode_ObjectIdentity = ObjectIdentity
me1200PtpConfigGlobalsSystemTimeSyncMode = _Me1200PtpConfigGlobalsSystemTimeSyncMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 1, 2)
)
_Me1200PtpConfigGlobalsSystemTimeSyncModeMode_Type = ME1200ptpSystemTimeSyncMode
_Me1200PtpConfigGlobalsSystemTimeSyncModeMode_Object = MibScalar
me1200PtpConfigGlobalsSystemTimeSyncModeMode = _Me1200PtpConfigGlobalsSystemTimeSyncModeMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 1, 2, 1),
    _Me1200PtpConfigGlobalsSystemTimeSyncModeMode_Type()
)
me1200PtpConfigGlobalsSystemTimeSyncModeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigGlobalsSystemTimeSyncModeMode.setStatus("current")
_Me1200PtpConfigClocks_ObjectIdentity = ObjectIdentity
me1200PtpConfigClocks = _Me1200PtpConfigClocks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2)
)
_Me1200PtpConfigClocksDefaultDsTable_Object = MibTable
me1200PtpConfigClocksDefaultDsTable = _Me1200PtpConfigClocksDefaultDsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsTable.setStatus("current")
_Me1200PtpConfigClocksDefaultDsEntry_Object = MibTableRow
me1200PtpConfigClocksDefaultDsEntry = _Me1200PtpConfigClocksDefaultDsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 1, 1)
)
me1200PtpConfigClocksDefaultDsEntry.setIndexNames(
    (0, "ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsClockId"),
)
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsEntry.setStatus("current")


class _Me1200PtpConfigClocksDefaultDsClockId_Type(Integer32):
    """Custom type me1200PtpConfigClocksDefaultDsClockId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Me1200PtpConfigClocksDefaultDsClockId_Type.__name__ = "Integer32"
_Me1200PtpConfigClocksDefaultDsClockId_Object = MibTableColumn
me1200PtpConfigClocksDefaultDsClockId = _Me1200PtpConfigClocksDefaultDsClockId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 1, 1, 1),
    _Me1200PtpConfigClocksDefaultDsClockId_Type()
)
me1200PtpConfigClocksDefaultDsClockId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsClockId.setStatus("current")
_Me1200PtpConfigClocksDefaultDsDeviceType_Type = ME1200ptpDeviceType
_Me1200PtpConfigClocksDefaultDsDeviceType_Object = MibTableColumn
me1200PtpConfigClocksDefaultDsDeviceType = _Me1200PtpConfigClocksDefaultDsDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 1, 1, 2),
    _Me1200PtpConfigClocksDefaultDsDeviceType_Type()
)
me1200PtpConfigClocksDefaultDsDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsDeviceType.setStatus("current")
_Me1200PtpConfigClocksDefaultDsTwoStepFlag_Type = TruthValue
_Me1200PtpConfigClocksDefaultDsTwoStepFlag_Object = MibTableColumn
me1200PtpConfigClocksDefaultDsTwoStepFlag = _Me1200PtpConfigClocksDefaultDsTwoStepFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 1, 1, 3),
    _Me1200PtpConfigClocksDefaultDsTwoStepFlag_Type()
)
me1200PtpConfigClocksDefaultDsTwoStepFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsTwoStepFlag.setStatus("current")
_Me1200PtpConfigClocksDefaultDsPriority1_Type = ME1200Unsigned8
_Me1200PtpConfigClocksDefaultDsPriority1_Object = MibTableColumn
me1200PtpConfigClocksDefaultDsPriority1 = _Me1200PtpConfigClocksDefaultDsPriority1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 1, 1, 4),
    _Me1200PtpConfigClocksDefaultDsPriority1_Type()
)
me1200PtpConfigClocksDefaultDsPriority1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsPriority1.setStatus("current")
_Me1200PtpConfigClocksDefaultDsPriority2_Type = ME1200Unsigned8
_Me1200PtpConfigClocksDefaultDsPriority2_Object = MibTableColumn
me1200PtpConfigClocksDefaultDsPriority2 = _Me1200PtpConfigClocksDefaultDsPriority2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 1, 1, 5),
    _Me1200PtpConfigClocksDefaultDsPriority2_Type()
)
me1200PtpConfigClocksDefaultDsPriority2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsPriority2.setStatus("current")
_Me1200PtpConfigClocksDefaultDsOneWay_Type = TruthValue
_Me1200PtpConfigClocksDefaultDsOneWay_Object = MibTableColumn
me1200PtpConfigClocksDefaultDsOneWay = _Me1200PtpConfigClocksDefaultDsOneWay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 1, 1, 6),
    _Me1200PtpConfigClocksDefaultDsOneWay_Type()
)
me1200PtpConfigClocksDefaultDsOneWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsOneWay.setStatus("current")
_Me1200PtpConfigClocksDefaultDsDomainNumber_Type = ME1200Unsigned8
_Me1200PtpConfigClocksDefaultDsDomainNumber_Object = MibTableColumn
me1200PtpConfigClocksDefaultDsDomainNumber = _Me1200PtpConfigClocksDefaultDsDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 1, 1, 7),
    _Me1200PtpConfigClocksDefaultDsDomainNumber_Type()
)
me1200PtpConfigClocksDefaultDsDomainNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsDomainNumber.setStatus("current")
_Me1200PtpConfigClocksDefaultDsProtocol_Type = ME1200ptpProtocol
_Me1200PtpConfigClocksDefaultDsProtocol_Object = MibTableColumn
me1200PtpConfigClocksDefaultDsProtocol = _Me1200PtpConfigClocksDefaultDsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 1, 1, 8),
    _Me1200PtpConfigClocksDefaultDsProtocol_Type()
)
me1200PtpConfigClocksDefaultDsProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsProtocol.setStatus("current")
_Me1200PtpConfigClocksDefaultDsVlanTagEnable_Type = TruthValue
_Me1200PtpConfigClocksDefaultDsVlanTagEnable_Object = MibTableColumn
me1200PtpConfigClocksDefaultDsVlanTagEnable = _Me1200PtpConfigClocksDefaultDsVlanTagEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 1, 1, 9),
    _Me1200PtpConfigClocksDefaultDsVlanTagEnable_Type()
)
me1200PtpConfigClocksDefaultDsVlanTagEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsVlanTagEnable.setStatus("current")
_Me1200PtpConfigClocksDefaultDsVid_Type = ME1200Unsigned16
_Me1200PtpConfigClocksDefaultDsVid_Object = MibTableColumn
me1200PtpConfigClocksDefaultDsVid = _Me1200PtpConfigClocksDefaultDsVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 1, 1, 10),
    _Me1200PtpConfigClocksDefaultDsVid_Type()
)
me1200PtpConfigClocksDefaultDsVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsVid.setStatus("current")
_Me1200PtpConfigClocksDefaultDsPcp_Type = ME1200Unsigned8
_Me1200PtpConfigClocksDefaultDsPcp_Object = MibTableColumn
me1200PtpConfigClocksDefaultDsPcp = _Me1200PtpConfigClocksDefaultDsPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 1, 1, 11),
    _Me1200PtpConfigClocksDefaultDsPcp_Type()
)
me1200PtpConfigClocksDefaultDsPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsPcp.setStatus("current")
_Me1200PtpConfigClocksDefaultDsMep_Type = Integer32
_Me1200PtpConfigClocksDefaultDsMep_Object = MibTableColumn
me1200PtpConfigClocksDefaultDsMep = _Me1200PtpConfigClocksDefaultDsMep_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 1, 1, 12),
    _Me1200PtpConfigClocksDefaultDsMep_Type()
)
me1200PtpConfigClocksDefaultDsMep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsMep.setStatus("current")
_Me1200PtpConfigClocksDefaultDsClkDom_Type = Unsigned32
_Me1200PtpConfigClocksDefaultDsClkDom_Object = MibTableColumn
me1200PtpConfigClocksDefaultDsClkDom = _Me1200PtpConfigClocksDefaultDsClkDom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 1, 1, 13),
    _Me1200PtpConfigClocksDefaultDsClkDom_Type()
)
me1200PtpConfigClocksDefaultDsClkDom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsClkDom.setStatus("current")
_Me1200PtpConfigClocksDefaultDsDscp_Type = ME1200Unsigned8
_Me1200PtpConfigClocksDefaultDsDscp_Object = MibTableColumn
me1200PtpConfigClocksDefaultDsDscp = _Me1200PtpConfigClocksDefaultDsDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 1, 1, 14),
    _Me1200PtpConfigClocksDefaultDsDscp_Type()
)
me1200PtpConfigClocksDefaultDsDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsDscp.setStatus("current")
_Me1200PtpConfigClocksDefaultDsProfile_Type = ME1200ptpProfile
_Me1200PtpConfigClocksDefaultDsProfile_Object = MibTableColumn
me1200PtpConfigClocksDefaultDsProfile = _Me1200PtpConfigClocksDefaultDsProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 1, 1, 15),
    _Me1200PtpConfigClocksDefaultDsProfile_Type()
)
me1200PtpConfigClocksDefaultDsProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsProfile.setStatus("current")
_Me1200PtpConfigClocksDefaultDsLocalPriority_Type = ME1200Unsigned8
_Me1200PtpConfigClocksDefaultDsLocalPriority_Object = MibTableColumn
me1200PtpConfigClocksDefaultDsLocalPriority = _Me1200PtpConfigClocksDefaultDsLocalPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 1, 1, 16),
    _Me1200PtpConfigClocksDefaultDsLocalPriority_Type()
)
me1200PtpConfigClocksDefaultDsLocalPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsLocalPriority.setStatus("current")
_Me1200PtpConfigClocksDefaultDsAction_Type = ME1200RowEditorState
_Me1200PtpConfigClocksDefaultDsAction_Object = MibTableColumn
me1200PtpConfigClocksDefaultDsAction = _Me1200PtpConfigClocksDefaultDsAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 1, 1, 100),
    _Me1200PtpConfigClocksDefaultDsAction_Type()
)
me1200PtpConfigClocksDefaultDsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsAction.setStatus("current")
_Me1200PtpConfigClocksDefaultDsTableRowEditor_ObjectIdentity = ObjectIdentity
me1200PtpConfigClocksDefaultDsTableRowEditor = _Me1200PtpConfigClocksDefaultDsTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 2)
)


class _Me1200PtpConfigClocksDefaultDsTableRowEditorClockId_Type(Integer32):
    """Custom type me1200PtpConfigClocksDefaultDsTableRowEditorClockId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Me1200PtpConfigClocksDefaultDsTableRowEditorClockId_Type.__name__ = "Integer32"
_Me1200PtpConfigClocksDefaultDsTableRowEditorClockId_Object = MibScalar
me1200PtpConfigClocksDefaultDsTableRowEditorClockId = _Me1200PtpConfigClocksDefaultDsTableRowEditorClockId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 2, 1),
    _Me1200PtpConfigClocksDefaultDsTableRowEditorClockId_Type()
)
me1200PtpConfigClocksDefaultDsTableRowEditorClockId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsTableRowEditorClockId.setStatus("current")
_Me1200PtpConfigClocksDefaultDsTableRowEditorDeviceType_Type = ME1200ptpDeviceType
_Me1200PtpConfigClocksDefaultDsTableRowEditorDeviceType_Object = MibScalar
me1200PtpConfigClocksDefaultDsTableRowEditorDeviceType = _Me1200PtpConfigClocksDefaultDsTableRowEditorDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 2, 2),
    _Me1200PtpConfigClocksDefaultDsTableRowEditorDeviceType_Type()
)
me1200PtpConfigClocksDefaultDsTableRowEditorDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsTableRowEditorDeviceType.setStatus("current")
_Me1200PtpConfigClocksDefaultDsTableRowEditorTwoStepFlag_Type = TruthValue
_Me1200PtpConfigClocksDefaultDsTableRowEditorTwoStepFlag_Object = MibScalar
me1200PtpConfigClocksDefaultDsTableRowEditorTwoStepFlag = _Me1200PtpConfigClocksDefaultDsTableRowEditorTwoStepFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 2, 3),
    _Me1200PtpConfigClocksDefaultDsTableRowEditorTwoStepFlag_Type()
)
me1200PtpConfigClocksDefaultDsTableRowEditorTwoStepFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsTableRowEditorTwoStepFlag.setStatus("current")
_Me1200PtpConfigClocksDefaultDsTableRowEditorPriority1_Type = ME1200Unsigned8
_Me1200PtpConfigClocksDefaultDsTableRowEditorPriority1_Object = MibScalar
me1200PtpConfigClocksDefaultDsTableRowEditorPriority1 = _Me1200PtpConfigClocksDefaultDsTableRowEditorPriority1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 2, 4),
    _Me1200PtpConfigClocksDefaultDsTableRowEditorPriority1_Type()
)
me1200PtpConfigClocksDefaultDsTableRowEditorPriority1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsTableRowEditorPriority1.setStatus("current")
_Me1200PtpConfigClocksDefaultDsTableRowEditorPriority2_Type = ME1200Unsigned8
_Me1200PtpConfigClocksDefaultDsTableRowEditorPriority2_Object = MibScalar
me1200PtpConfigClocksDefaultDsTableRowEditorPriority2 = _Me1200PtpConfigClocksDefaultDsTableRowEditorPriority2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 2, 5),
    _Me1200PtpConfigClocksDefaultDsTableRowEditorPriority2_Type()
)
me1200PtpConfigClocksDefaultDsTableRowEditorPriority2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsTableRowEditorPriority2.setStatus("current")
_Me1200PtpConfigClocksDefaultDsTableRowEditorOneWay_Type = TruthValue
_Me1200PtpConfigClocksDefaultDsTableRowEditorOneWay_Object = MibScalar
me1200PtpConfigClocksDefaultDsTableRowEditorOneWay = _Me1200PtpConfigClocksDefaultDsTableRowEditorOneWay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 2, 6),
    _Me1200PtpConfigClocksDefaultDsTableRowEditorOneWay_Type()
)
me1200PtpConfigClocksDefaultDsTableRowEditorOneWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsTableRowEditorOneWay.setStatus("current")
_Me1200PtpConfigClocksDefaultDsTableRowEditorDomainNumber_Type = ME1200Unsigned8
_Me1200PtpConfigClocksDefaultDsTableRowEditorDomainNumber_Object = MibScalar
me1200PtpConfigClocksDefaultDsTableRowEditorDomainNumber = _Me1200PtpConfigClocksDefaultDsTableRowEditorDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 2, 7),
    _Me1200PtpConfigClocksDefaultDsTableRowEditorDomainNumber_Type()
)
me1200PtpConfigClocksDefaultDsTableRowEditorDomainNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsTableRowEditorDomainNumber.setStatus("current")
_Me1200PtpConfigClocksDefaultDsTableRowEditorProtocol_Type = ME1200ptpProtocol
_Me1200PtpConfigClocksDefaultDsTableRowEditorProtocol_Object = MibScalar
me1200PtpConfigClocksDefaultDsTableRowEditorProtocol = _Me1200PtpConfigClocksDefaultDsTableRowEditorProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 2, 8),
    _Me1200PtpConfigClocksDefaultDsTableRowEditorProtocol_Type()
)
me1200PtpConfigClocksDefaultDsTableRowEditorProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsTableRowEditorProtocol.setStatus("current")
_Me1200PtpConfigClocksDefaultDsTableRowEditorVlanTagEnable_Type = TruthValue
_Me1200PtpConfigClocksDefaultDsTableRowEditorVlanTagEnable_Object = MibScalar
me1200PtpConfigClocksDefaultDsTableRowEditorVlanTagEnable = _Me1200PtpConfigClocksDefaultDsTableRowEditorVlanTagEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 2, 9),
    _Me1200PtpConfigClocksDefaultDsTableRowEditorVlanTagEnable_Type()
)
me1200PtpConfigClocksDefaultDsTableRowEditorVlanTagEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsTableRowEditorVlanTagEnable.setStatus("current")
_Me1200PtpConfigClocksDefaultDsTableRowEditorVid_Type = ME1200Unsigned16
_Me1200PtpConfigClocksDefaultDsTableRowEditorVid_Object = MibScalar
me1200PtpConfigClocksDefaultDsTableRowEditorVid = _Me1200PtpConfigClocksDefaultDsTableRowEditorVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 2, 10),
    _Me1200PtpConfigClocksDefaultDsTableRowEditorVid_Type()
)
me1200PtpConfigClocksDefaultDsTableRowEditorVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsTableRowEditorVid.setStatus("current")
_Me1200PtpConfigClocksDefaultDsTableRowEditorPcp_Type = ME1200Unsigned8
_Me1200PtpConfigClocksDefaultDsTableRowEditorPcp_Object = MibScalar
me1200PtpConfigClocksDefaultDsTableRowEditorPcp = _Me1200PtpConfigClocksDefaultDsTableRowEditorPcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 2, 11),
    _Me1200PtpConfigClocksDefaultDsTableRowEditorPcp_Type()
)
me1200PtpConfigClocksDefaultDsTableRowEditorPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsTableRowEditorPcp.setStatus("current")
_Me1200PtpConfigClocksDefaultDsTableRowEditorMep_Type = Integer32
_Me1200PtpConfigClocksDefaultDsTableRowEditorMep_Object = MibScalar
me1200PtpConfigClocksDefaultDsTableRowEditorMep = _Me1200PtpConfigClocksDefaultDsTableRowEditorMep_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 2, 12),
    _Me1200PtpConfigClocksDefaultDsTableRowEditorMep_Type()
)
me1200PtpConfigClocksDefaultDsTableRowEditorMep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsTableRowEditorMep.setStatus("current")
_Me1200PtpConfigClocksDefaultDsTableRowEditorClkDom_Type = Unsigned32
_Me1200PtpConfigClocksDefaultDsTableRowEditorClkDom_Object = MibScalar
me1200PtpConfigClocksDefaultDsTableRowEditorClkDom = _Me1200PtpConfigClocksDefaultDsTableRowEditorClkDom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 2, 13),
    _Me1200PtpConfigClocksDefaultDsTableRowEditorClkDom_Type()
)
me1200PtpConfigClocksDefaultDsTableRowEditorClkDom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsTableRowEditorClkDom.setStatus("current")
_Me1200PtpConfigClocksDefaultDsTableRowEditorDscp_Type = ME1200Unsigned8
_Me1200PtpConfigClocksDefaultDsTableRowEditorDscp_Object = MibScalar
me1200PtpConfigClocksDefaultDsTableRowEditorDscp = _Me1200PtpConfigClocksDefaultDsTableRowEditorDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 2, 14),
    _Me1200PtpConfigClocksDefaultDsTableRowEditorDscp_Type()
)
me1200PtpConfigClocksDefaultDsTableRowEditorDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsTableRowEditorDscp.setStatus("current")
_Me1200PtpConfigClocksDefaultDsTableRowEditorProfile_Type = ME1200ptpProfile
_Me1200PtpConfigClocksDefaultDsTableRowEditorProfile_Object = MibScalar
me1200PtpConfigClocksDefaultDsTableRowEditorProfile = _Me1200PtpConfigClocksDefaultDsTableRowEditorProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 2, 15),
    _Me1200PtpConfigClocksDefaultDsTableRowEditorProfile_Type()
)
me1200PtpConfigClocksDefaultDsTableRowEditorProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsTableRowEditorProfile.setStatus("current")
_Me1200PtpConfigClocksDefaultDsTableRowEditorLocalPriority_Type = ME1200Unsigned8
_Me1200PtpConfigClocksDefaultDsTableRowEditorLocalPriority_Object = MibScalar
me1200PtpConfigClocksDefaultDsTableRowEditorLocalPriority = _Me1200PtpConfigClocksDefaultDsTableRowEditorLocalPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 2, 16),
    _Me1200PtpConfigClocksDefaultDsTableRowEditorLocalPriority_Type()
)
me1200PtpConfigClocksDefaultDsTableRowEditorLocalPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsTableRowEditorLocalPriority.setStatus("current")
_Me1200PtpConfigClocksDefaultDsTableRowEditorAction_Type = ME1200RowEditorState
_Me1200PtpConfigClocksDefaultDsTableRowEditorAction_Object = MibScalar
me1200PtpConfigClocksDefaultDsTableRowEditorAction = _Me1200PtpConfigClocksDefaultDsTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 2, 100),
    _Me1200PtpConfigClocksDefaultDsTableRowEditorAction_Type()
)
me1200PtpConfigClocksDefaultDsTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsTableRowEditorAction.setStatus("current")
_Me1200PtpConfigClocksTimePropertiesDsTable_Object = MibTable
me1200PtpConfigClocksTimePropertiesDsTable = _Me1200PtpConfigClocksTimePropertiesDsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    me1200PtpConfigClocksTimePropertiesDsTable.setStatus("current")
_Me1200PtpConfigClocksTimePropertiesDsEntry_Object = MibTableRow
me1200PtpConfigClocksTimePropertiesDsEntry = _Me1200PtpConfigClocksTimePropertiesDsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 3, 1)
)
me1200PtpConfigClocksTimePropertiesDsEntry.setIndexNames(
    (0, "ME1200-PTP-MIB", "me1200PtpConfigClocksTimePropertiesDsClockId"),
)
if mibBuilder.loadTexts:
    me1200PtpConfigClocksTimePropertiesDsEntry.setStatus("current")


class _Me1200PtpConfigClocksTimePropertiesDsClockId_Type(Integer32):
    """Custom type me1200PtpConfigClocksTimePropertiesDsClockId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Me1200PtpConfigClocksTimePropertiesDsClockId_Type.__name__ = "Integer32"
_Me1200PtpConfigClocksTimePropertiesDsClockId_Object = MibTableColumn
me1200PtpConfigClocksTimePropertiesDsClockId = _Me1200PtpConfigClocksTimePropertiesDsClockId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 3, 1, 1),
    _Me1200PtpConfigClocksTimePropertiesDsClockId_Type()
)
me1200PtpConfigClocksTimePropertiesDsClockId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksTimePropertiesDsClockId.setStatus("current")
_Me1200PtpConfigClocksTimePropertiesDsCurrentUtcOffset_Type = ME1200Integer16
_Me1200PtpConfigClocksTimePropertiesDsCurrentUtcOffset_Object = MibTableColumn
me1200PtpConfigClocksTimePropertiesDsCurrentUtcOffset = _Me1200PtpConfigClocksTimePropertiesDsCurrentUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 3, 1, 2),
    _Me1200PtpConfigClocksTimePropertiesDsCurrentUtcOffset_Type()
)
me1200PtpConfigClocksTimePropertiesDsCurrentUtcOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksTimePropertiesDsCurrentUtcOffset.setStatus("current")
_Me1200PtpConfigClocksTimePropertiesDsCurrentUtcOffsetValid_Type = TruthValue
_Me1200PtpConfigClocksTimePropertiesDsCurrentUtcOffsetValid_Object = MibTableColumn
me1200PtpConfigClocksTimePropertiesDsCurrentUtcOffsetValid = _Me1200PtpConfigClocksTimePropertiesDsCurrentUtcOffsetValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 3, 1, 3),
    _Me1200PtpConfigClocksTimePropertiesDsCurrentUtcOffsetValid_Type()
)
me1200PtpConfigClocksTimePropertiesDsCurrentUtcOffsetValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksTimePropertiesDsCurrentUtcOffsetValid.setStatus("current")
_Me1200PtpConfigClocksTimePropertiesDsLeap59_Type = TruthValue
_Me1200PtpConfigClocksTimePropertiesDsLeap59_Object = MibTableColumn
me1200PtpConfigClocksTimePropertiesDsLeap59 = _Me1200PtpConfigClocksTimePropertiesDsLeap59_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 3, 1, 4),
    _Me1200PtpConfigClocksTimePropertiesDsLeap59_Type()
)
me1200PtpConfigClocksTimePropertiesDsLeap59.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksTimePropertiesDsLeap59.setStatus("current")
_Me1200PtpConfigClocksTimePropertiesDsLeap61_Type = TruthValue
_Me1200PtpConfigClocksTimePropertiesDsLeap61_Object = MibTableColumn
me1200PtpConfigClocksTimePropertiesDsLeap61 = _Me1200PtpConfigClocksTimePropertiesDsLeap61_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 3, 1, 5),
    _Me1200PtpConfigClocksTimePropertiesDsLeap61_Type()
)
me1200PtpConfigClocksTimePropertiesDsLeap61.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksTimePropertiesDsLeap61.setStatus("current")
_Me1200PtpConfigClocksTimePropertiesDsTimeTraceable_Type = TruthValue
_Me1200PtpConfigClocksTimePropertiesDsTimeTraceable_Object = MibTableColumn
me1200PtpConfigClocksTimePropertiesDsTimeTraceable = _Me1200PtpConfigClocksTimePropertiesDsTimeTraceable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 3, 1, 6),
    _Me1200PtpConfigClocksTimePropertiesDsTimeTraceable_Type()
)
me1200PtpConfigClocksTimePropertiesDsTimeTraceable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksTimePropertiesDsTimeTraceable.setStatus("current")
_Me1200PtpConfigClocksTimePropertiesDsFrequencyTraceable_Type = TruthValue
_Me1200PtpConfigClocksTimePropertiesDsFrequencyTraceable_Object = MibTableColumn
me1200PtpConfigClocksTimePropertiesDsFrequencyTraceable = _Me1200PtpConfigClocksTimePropertiesDsFrequencyTraceable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 3, 1, 7),
    _Me1200PtpConfigClocksTimePropertiesDsFrequencyTraceable_Type()
)
me1200PtpConfigClocksTimePropertiesDsFrequencyTraceable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksTimePropertiesDsFrequencyTraceable.setStatus("current")
_Me1200PtpConfigClocksTimePropertiesDsPtpTimescale_Type = TruthValue
_Me1200PtpConfigClocksTimePropertiesDsPtpTimescale_Object = MibTableColumn
me1200PtpConfigClocksTimePropertiesDsPtpTimescale = _Me1200PtpConfigClocksTimePropertiesDsPtpTimescale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 3, 1, 8),
    _Me1200PtpConfigClocksTimePropertiesDsPtpTimescale_Type()
)
me1200PtpConfigClocksTimePropertiesDsPtpTimescale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksTimePropertiesDsPtpTimescale.setStatus("current")
_Me1200PtpConfigClocksTimePropertiesDsTimeSource_Type = ME1200Unsigned8
_Me1200PtpConfigClocksTimePropertiesDsTimeSource_Object = MibTableColumn
me1200PtpConfigClocksTimePropertiesDsTimeSource = _Me1200PtpConfigClocksTimePropertiesDsTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 3, 1, 9),
    _Me1200PtpConfigClocksTimePropertiesDsTimeSource_Type()
)
me1200PtpConfigClocksTimePropertiesDsTimeSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksTimePropertiesDsTimeSource.setStatus("current")
_Me1200PtpConfigClocksFilterParametersTable_Object = MibTable
me1200PtpConfigClocksFilterParametersTable = _Me1200PtpConfigClocksFilterParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    me1200PtpConfigClocksFilterParametersTable.setStatus("current")
_Me1200PtpConfigClocksFilterParametersEntry_Object = MibTableRow
me1200PtpConfigClocksFilterParametersEntry = _Me1200PtpConfigClocksFilterParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 4, 1)
)
me1200PtpConfigClocksFilterParametersEntry.setIndexNames(
    (0, "ME1200-PTP-MIB", "me1200PtpConfigClocksFilterParametersClockId"),
)
if mibBuilder.loadTexts:
    me1200PtpConfigClocksFilterParametersEntry.setStatus("current")


class _Me1200PtpConfigClocksFilterParametersClockId_Type(Integer32):
    """Custom type me1200PtpConfigClocksFilterParametersClockId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Me1200PtpConfigClocksFilterParametersClockId_Type.__name__ = "Integer32"
_Me1200PtpConfigClocksFilterParametersClockId_Object = MibTableColumn
me1200PtpConfigClocksFilterParametersClockId = _Me1200PtpConfigClocksFilterParametersClockId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 4, 1, 1),
    _Me1200PtpConfigClocksFilterParametersClockId_Type()
)
me1200PtpConfigClocksFilterParametersClockId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksFilterParametersClockId.setStatus("current")
_Me1200PtpConfigClocksFilterParametersDelayFilter_Type = Unsigned32
_Me1200PtpConfigClocksFilterParametersDelayFilter_Object = MibTableColumn
me1200PtpConfigClocksFilterParametersDelayFilter = _Me1200PtpConfigClocksFilterParametersDelayFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 4, 1, 2),
    _Me1200PtpConfigClocksFilterParametersDelayFilter_Type()
)
me1200PtpConfigClocksFilterParametersDelayFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksFilterParametersDelayFilter.setStatus("current")
_Me1200PtpConfigClocksFilterParametersFilterType_Type = Unsigned32
_Me1200PtpConfigClocksFilterParametersFilterType_Object = MibTableColumn
me1200PtpConfigClocksFilterParametersFilterType = _Me1200PtpConfigClocksFilterParametersFilterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 4, 1, 3),
    _Me1200PtpConfigClocksFilterParametersFilterType_Type()
)
me1200PtpConfigClocksFilterParametersFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksFilterParametersFilterType.setStatus("current")
_Me1200PtpConfigClocksFilterParametersPeriod_Type = Unsigned32
_Me1200PtpConfigClocksFilterParametersPeriod_Object = MibTableColumn
me1200PtpConfigClocksFilterParametersPeriod = _Me1200PtpConfigClocksFilterParametersPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 4, 1, 4),
    _Me1200PtpConfigClocksFilterParametersPeriod_Type()
)
me1200PtpConfigClocksFilterParametersPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksFilterParametersPeriod.setStatus("current")
_Me1200PtpConfigClocksFilterParametersDist_Type = Unsigned32
_Me1200PtpConfigClocksFilterParametersDist_Object = MibTableColumn
me1200PtpConfigClocksFilterParametersDist = _Me1200PtpConfigClocksFilterParametersDist_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 4, 1, 5),
    _Me1200PtpConfigClocksFilterParametersDist_Type()
)
me1200PtpConfigClocksFilterParametersDist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksFilterParametersDist.setStatus("current")
_Me1200PtpConfigClocksServoParametersTable_Object = MibTable
me1200PtpConfigClocksServoParametersTable = _Me1200PtpConfigClocksServoParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    me1200PtpConfigClocksServoParametersTable.setStatus("current")
_Me1200PtpConfigClocksServoParametersEntry_Object = MibTableRow
me1200PtpConfigClocksServoParametersEntry = _Me1200PtpConfigClocksServoParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 5, 1)
)
me1200PtpConfigClocksServoParametersEntry.setIndexNames(
    (0, "ME1200-PTP-MIB", "me1200PtpConfigClocksServoParametersClockId"),
)
if mibBuilder.loadTexts:
    me1200PtpConfigClocksServoParametersEntry.setStatus("current")


class _Me1200PtpConfigClocksServoParametersClockId_Type(Integer32):
    """Custom type me1200PtpConfigClocksServoParametersClockId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Me1200PtpConfigClocksServoParametersClockId_Type.__name__ = "Integer32"
_Me1200PtpConfigClocksServoParametersClockId_Object = MibTableColumn
me1200PtpConfigClocksServoParametersClockId = _Me1200PtpConfigClocksServoParametersClockId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 5, 1, 1),
    _Me1200PtpConfigClocksServoParametersClockId_Type()
)
me1200PtpConfigClocksServoParametersClockId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksServoParametersClockId.setStatus("current")
_Me1200PtpConfigClocksServoParametersDisplay_Type = TruthValue
_Me1200PtpConfigClocksServoParametersDisplay_Object = MibTableColumn
me1200PtpConfigClocksServoParametersDisplay = _Me1200PtpConfigClocksServoParametersDisplay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 5, 1, 2),
    _Me1200PtpConfigClocksServoParametersDisplay_Type()
)
me1200PtpConfigClocksServoParametersDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksServoParametersDisplay.setStatus("current")
_Me1200PtpConfigClocksServoParametersPEnable_Type = TruthValue
_Me1200PtpConfigClocksServoParametersPEnable_Object = MibTableColumn
me1200PtpConfigClocksServoParametersPEnable = _Me1200PtpConfigClocksServoParametersPEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 5, 1, 3),
    _Me1200PtpConfigClocksServoParametersPEnable_Type()
)
me1200PtpConfigClocksServoParametersPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksServoParametersPEnable.setStatus("current")
_Me1200PtpConfigClocksServoParametersIEnable_Type = TruthValue
_Me1200PtpConfigClocksServoParametersIEnable_Object = MibTableColumn
me1200PtpConfigClocksServoParametersIEnable = _Me1200PtpConfigClocksServoParametersIEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 5, 1, 4),
    _Me1200PtpConfigClocksServoParametersIEnable_Type()
)
me1200PtpConfigClocksServoParametersIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksServoParametersIEnable.setStatus("current")
_Me1200PtpConfigClocksServoParametersDEnable_Type = TruthValue
_Me1200PtpConfigClocksServoParametersDEnable_Object = MibTableColumn
me1200PtpConfigClocksServoParametersDEnable = _Me1200PtpConfigClocksServoParametersDEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 5, 1, 5),
    _Me1200PtpConfigClocksServoParametersDEnable_Type()
)
me1200PtpConfigClocksServoParametersDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksServoParametersDEnable.setStatus("current")
_Me1200PtpConfigClocksServoParametersPval_Type = Unsigned32
_Me1200PtpConfigClocksServoParametersPval_Object = MibTableColumn
me1200PtpConfigClocksServoParametersPval = _Me1200PtpConfigClocksServoParametersPval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 5, 1, 6),
    _Me1200PtpConfigClocksServoParametersPval_Type()
)
me1200PtpConfigClocksServoParametersPval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksServoParametersPval.setStatus("current")
_Me1200PtpConfigClocksServoParametersIval_Type = Unsigned32
_Me1200PtpConfigClocksServoParametersIval_Object = MibTableColumn
me1200PtpConfigClocksServoParametersIval = _Me1200PtpConfigClocksServoParametersIval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 5, 1, 7),
    _Me1200PtpConfigClocksServoParametersIval_Type()
)
me1200PtpConfigClocksServoParametersIval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksServoParametersIval.setStatus("current")
_Me1200PtpConfigClocksServoParametersDval_Type = Unsigned32
_Me1200PtpConfigClocksServoParametersDval_Object = MibTableColumn
me1200PtpConfigClocksServoParametersDval = _Me1200PtpConfigClocksServoParametersDval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 5, 1, 8),
    _Me1200PtpConfigClocksServoParametersDval_Type()
)
me1200PtpConfigClocksServoParametersDval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksServoParametersDval.setStatus("current")
_Me1200PtpConfigClocksServoParametersSrvOption_Type = ME1200ptpServoClockOption
_Me1200PtpConfigClocksServoParametersSrvOption_Object = MibTableColumn
me1200PtpConfigClocksServoParametersSrvOption = _Me1200PtpConfigClocksServoParametersSrvOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 5, 1, 9),
    _Me1200PtpConfigClocksServoParametersSrvOption_Type()
)
me1200PtpConfigClocksServoParametersSrvOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksServoParametersSrvOption.setStatus("current")
_Me1200PtpConfigClocksServoParametersSynceThreshold_Type = Unsigned32
_Me1200PtpConfigClocksServoParametersSynceThreshold_Object = MibTableColumn
me1200PtpConfigClocksServoParametersSynceThreshold = _Me1200PtpConfigClocksServoParametersSynceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 5, 1, 10),
    _Me1200PtpConfigClocksServoParametersSynceThreshold_Type()
)
me1200PtpConfigClocksServoParametersSynceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksServoParametersSynceThreshold.setStatus("current")
_Me1200PtpConfigClocksServoParametersSynceAp_Type = Unsigned32
_Me1200PtpConfigClocksServoParametersSynceAp_Object = MibTableColumn
me1200PtpConfigClocksServoParametersSynceAp = _Me1200PtpConfigClocksServoParametersSynceAp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 5, 1, 11),
    _Me1200PtpConfigClocksServoParametersSynceAp_Type()
)
me1200PtpConfigClocksServoParametersSynceAp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksServoParametersSynceAp.setStatus("current")
_Me1200PtpConfigClocksServoParametersHoFilter_Type = Integer32
_Me1200PtpConfigClocksServoParametersHoFilter_Object = MibTableColumn
me1200PtpConfigClocksServoParametersHoFilter = _Me1200PtpConfigClocksServoParametersHoFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 5, 1, 12),
    _Me1200PtpConfigClocksServoParametersHoFilter_Type()
)
me1200PtpConfigClocksServoParametersHoFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksServoParametersHoFilter.setStatus("current")
_Me1200PtpConfigClocksServoParametersStableAdjThreshold_Type = ME1200Unsigned64
_Me1200PtpConfigClocksServoParametersStableAdjThreshold_Object = MibTableColumn
me1200PtpConfigClocksServoParametersStableAdjThreshold = _Me1200PtpConfigClocksServoParametersStableAdjThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 5, 1, 13),
    _Me1200PtpConfigClocksServoParametersStableAdjThreshold_Type()
)
me1200PtpConfigClocksServoParametersStableAdjThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksServoParametersStableAdjThreshold.setStatus("current")
_Me1200PtpConfigClocksSlaveConfigTable_Object = MibTable
me1200PtpConfigClocksSlaveConfigTable = _Me1200PtpConfigClocksSlaveConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    me1200PtpConfigClocksSlaveConfigTable.setStatus("current")
_Me1200PtpConfigClocksSlaveConfigEntry_Object = MibTableRow
me1200PtpConfigClocksSlaveConfigEntry = _Me1200PtpConfigClocksSlaveConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 6, 1)
)
me1200PtpConfigClocksSlaveConfigEntry.setIndexNames(
    (0, "ME1200-PTP-MIB", "me1200PtpConfigClocksSlaveConfigClockId"),
)
if mibBuilder.loadTexts:
    me1200PtpConfigClocksSlaveConfigEntry.setStatus("current")


class _Me1200PtpConfigClocksSlaveConfigClockId_Type(Integer32):
    """Custom type me1200PtpConfigClocksSlaveConfigClockId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Me1200PtpConfigClocksSlaveConfigClockId_Type.__name__ = "Integer32"
_Me1200PtpConfigClocksSlaveConfigClockId_Object = MibTableColumn
me1200PtpConfigClocksSlaveConfigClockId = _Me1200PtpConfigClocksSlaveConfigClockId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 6, 1, 1),
    _Me1200PtpConfigClocksSlaveConfigClockId_Type()
)
me1200PtpConfigClocksSlaveConfigClockId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksSlaveConfigClockId.setStatus("current")
_Me1200PtpConfigClocksSlaveConfigStableOffset_Type = Unsigned32
_Me1200PtpConfigClocksSlaveConfigStableOffset_Object = MibTableColumn
me1200PtpConfigClocksSlaveConfigStableOffset = _Me1200PtpConfigClocksSlaveConfigStableOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 6, 1, 2),
    _Me1200PtpConfigClocksSlaveConfigStableOffset_Type()
)
me1200PtpConfigClocksSlaveConfigStableOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksSlaveConfigStableOffset.setStatus("current")
_Me1200PtpConfigClocksSlaveConfigOffsetOk_Type = Unsigned32
_Me1200PtpConfigClocksSlaveConfigOffsetOk_Object = MibTableColumn
me1200PtpConfigClocksSlaveConfigOffsetOk = _Me1200PtpConfigClocksSlaveConfigOffsetOk_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 6, 1, 3),
    _Me1200PtpConfigClocksSlaveConfigOffsetOk_Type()
)
me1200PtpConfigClocksSlaveConfigOffsetOk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksSlaveConfigOffsetOk.setStatus("current")
_Me1200PtpConfigClocksSlaveConfigOffsetFail_Type = Unsigned32
_Me1200PtpConfigClocksSlaveConfigOffsetFail_Object = MibTableColumn
me1200PtpConfigClocksSlaveConfigOffsetFail = _Me1200PtpConfigClocksSlaveConfigOffsetFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 6, 1, 4),
    _Me1200PtpConfigClocksSlaveConfigOffsetFail_Type()
)
me1200PtpConfigClocksSlaveConfigOffsetFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksSlaveConfigOffsetFail.setStatus("current")
_Me1200PtpConfigClocksUnicastSlaveConfigTable_Object = MibTable
me1200PtpConfigClocksUnicastSlaveConfigTable = _Me1200PtpConfigClocksUnicastSlaveConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 7)
)
if mibBuilder.loadTexts:
    me1200PtpConfigClocksUnicastSlaveConfigTable.setStatus("current")
_Me1200PtpConfigClocksUnicastSlaveConfigEntry_Object = MibTableRow
me1200PtpConfigClocksUnicastSlaveConfigEntry = _Me1200PtpConfigClocksUnicastSlaveConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 7, 1)
)
me1200PtpConfigClocksUnicastSlaveConfigEntry.setIndexNames(
    (0, "ME1200-PTP-MIB", "me1200PtpConfigClocksUnicastSlaveConfigClockId"),
    (0, "ME1200-PTP-MIB", "me1200PtpConfigClocksUnicastSlaveConfigMasterId"),
)
if mibBuilder.loadTexts:
    me1200PtpConfigClocksUnicastSlaveConfigEntry.setStatus("current")


class _Me1200PtpConfigClocksUnicastSlaveConfigClockId_Type(Integer32):
    """Custom type me1200PtpConfigClocksUnicastSlaveConfigClockId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Me1200PtpConfigClocksUnicastSlaveConfigClockId_Type.__name__ = "Integer32"
_Me1200PtpConfigClocksUnicastSlaveConfigClockId_Object = MibTableColumn
me1200PtpConfigClocksUnicastSlaveConfigClockId = _Me1200PtpConfigClocksUnicastSlaveConfigClockId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 7, 1, 1),
    _Me1200PtpConfigClocksUnicastSlaveConfigClockId_Type()
)
me1200PtpConfigClocksUnicastSlaveConfigClockId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksUnicastSlaveConfigClockId.setStatus("current")


class _Me1200PtpConfigClocksUnicastSlaveConfigMasterId_Type(Integer32):
    """Custom type me1200PtpConfigClocksUnicastSlaveConfigMasterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Me1200PtpConfigClocksUnicastSlaveConfigMasterId_Type.__name__ = "Integer32"
_Me1200PtpConfigClocksUnicastSlaveConfigMasterId_Object = MibTableColumn
me1200PtpConfigClocksUnicastSlaveConfigMasterId = _Me1200PtpConfigClocksUnicastSlaveConfigMasterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 7, 1, 2),
    _Me1200PtpConfigClocksUnicastSlaveConfigMasterId_Type()
)
me1200PtpConfigClocksUnicastSlaveConfigMasterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksUnicastSlaveConfigMasterId.setStatus("current")
_Me1200PtpConfigClocksUnicastSlaveConfigDuration_Type = Unsigned32
_Me1200PtpConfigClocksUnicastSlaveConfigDuration_Object = MibTableColumn
me1200PtpConfigClocksUnicastSlaveConfigDuration = _Me1200PtpConfigClocksUnicastSlaveConfigDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 7, 1, 3),
    _Me1200PtpConfigClocksUnicastSlaveConfigDuration_Type()
)
me1200PtpConfigClocksUnicastSlaveConfigDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksUnicastSlaveConfigDuration.setStatus("current")
_Me1200PtpConfigClocksUnicastSlaveConfigIpAddress_Type = IpAddress
_Me1200PtpConfigClocksUnicastSlaveConfigIpAddress_Object = MibTableColumn
me1200PtpConfigClocksUnicastSlaveConfigIpAddress = _Me1200PtpConfigClocksUnicastSlaveConfigIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 7, 1, 4),
    _Me1200PtpConfigClocksUnicastSlaveConfigIpAddress_Type()
)
me1200PtpConfigClocksUnicastSlaveConfigIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksUnicastSlaveConfigIpAddress.setStatus("current")
_Me1200PtpConfigClocksPortDsTable_Object = MibTable
me1200PtpConfigClocksPortDsTable = _Me1200PtpConfigClocksPortDsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 8)
)
if mibBuilder.loadTexts:
    me1200PtpConfigClocksPortDsTable.setStatus("current")
_Me1200PtpConfigClocksPortDsEntry_Object = MibTableRow
me1200PtpConfigClocksPortDsEntry = _Me1200PtpConfigClocksPortDsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 8, 1)
)
me1200PtpConfigClocksPortDsEntry.setIndexNames(
    (0, "ME1200-PTP-MIB", "me1200PtpConfigClocksPortDsClockId"),
    (0, "ME1200-PTP-MIB", "me1200PtpConfigClocksPortDsPortId"),
)
if mibBuilder.loadTexts:
    me1200PtpConfigClocksPortDsEntry.setStatus("current")


class _Me1200PtpConfigClocksPortDsClockId_Type(Integer32):
    """Custom type me1200PtpConfigClocksPortDsClockId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Me1200PtpConfigClocksPortDsClockId_Type.__name__ = "Integer32"
_Me1200PtpConfigClocksPortDsClockId_Object = MibTableColumn
me1200PtpConfigClocksPortDsClockId = _Me1200PtpConfigClocksPortDsClockId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 8, 1, 1),
    _Me1200PtpConfigClocksPortDsClockId_Type()
)
me1200PtpConfigClocksPortDsClockId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksPortDsClockId.setStatus("current")


class _Me1200PtpConfigClocksPortDsPortId_Type(ME1200InterfaceIndex):
    """Custom type me1200PtpConfigClocksPortDsPortId based on ME1200InterfaceIndex"""
    subtypeSpec = ME1200InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Me1200PtpConfigClocksPortDsPortId_Type.__name__ = "ME1200InterfaceIndex"
_Me1200PtpConfigClocksPortDsPortId_Object = MibTableColumn
me1200PtpConfigClocksPortDsPortId = _Me1200PtpConfigClocksPortDsPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 8, 1, 2),
    _Me1200PtpConfigClocksPortDsPortId_Type()
)
me1200PtpConfigClocksPortDsPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksPortDsPortId.setStatus("current")
_Me1200PtpConfigClocksPortDsEnabled_Type = ME1200Unsigned8
_Me1200PtpConfigClocksPortDsEnabled_Object = MibTableColumn
me1200PtpConfigClocksPortDsEnabled = _Me1200PtpConfigClocksPortDsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 8, 1, 3),
    _Me1200PtpConfigClocksPortDsEnabled_Type()
)
me1200PtpConfigClocksPortDsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksPortDsEnabled.setStatus("current")
_Me1200PtpConfigClocksPortDsLogAnnounceInterval_Type = ME1200Integer16
_Me1200PtpConfigClocksPortDsLogAnnounceInterval_Object = MibTableColumn
me1200PtpConfigClocksPortDsLogAnnounceInterval = _Me1200PtpConfigClocksPortDsLogAnnounceInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 8, 1, 4),
    _Me1200PtpConfigClocksPortDsLogAnnounceInterval_Type()
)
me1200PtpConfigClocksPortDsLogAnnounceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksPortDsLogAnnounceInterval.setStatus("current")
_Me1200PtpConfigClocksPortDsAnnounceReceiptTimeout_Type = ME1200Unsigned8
_Me1200PtpConfigClocksPortDsAnnounceReceiptTimeout_Object = MibTableColumn
me1200PtpConfigClocksPortDsAnnounceReceiptTimeout = _Me1200PtpConfigClocksPortDsAnnounceReceiptTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 8, 1, 5),
    _Me1200PtpConfigClocksPortDsAnnounceReceiptTimeout_Type()
)
me1200PtpConfigClocksPortDsAnnounceReceiptTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksPortDsAnnounceReceiptTimeout.setStatus("current")
_Me1200PtpConfigClocksPortDsLogSyncInterval_Type = ME1200Integer16
_Me1200PtpConfigClocksPortDsLogSyncInterval_Object = MibTableColumn
me1200PtpConfigClocksPortDsLogSyncInterval = _Me1200PtpConfigClocksPortDsLogSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 8, 1, 6),
    _Me1200PtpConfigClocksPortDsLogSyncInterval_Type()
)
me1200PtpConfigClocksPortDsLogSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksPortDsLogSyncInterval.setStatus("current")
_Me1200PtpConfigClocksPortDsDelayMechanism_Type = ME1200Unsigned8
_Me1200PtpConfigClocksPortDsDelayMechanism_Object = MibTableColumn
me1200PtpConfigClocksPortDsDelayMechanism = _Me1200PtpConfigClocksPortDsDelayMechanism_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 8, 1, 7),
    _Me1200PtpConfigClocksPortDsDelayMechanism_Type()
)
me1200PtpConfigClocksPortDsDelayMechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksPortDsDelayMechanism.setStatus("current")
_Me1200PtpConfigClocksPortDsLogMinPdelayReqInterval_Type = ME1200Integer16
_Me1200PtpConfigClocksPortDsLogMinPdelayReqInterval_Object = MibTableColumn
me1200PtpConfigClocksPortDsLogMinPdelayReqInterval = _Me1200PtpConfigClocksPortDsLogMinPdelayReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 8, 1, 8),
    _Me1200PtpConfigClocksPortDsLogMinPdelayReqInterval_Type()
)
me1200PtpConfigClocksPortDsLogMinPdelayReqInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksPortDsLogMinPdelayReqInterval.setStatus("current")
_Me1200PtpConfigClocksPortDsDelayAsymmetry_Type = ME1200Integer64
_Me1200PtpConfigClocksPortDsDelayAsymmetry_Object = MibTableColumn
me1200PtpConfigClocksPortDsDelayAsymmetry = _Me1200PtpConfigClocksPortDsDelayAsymmetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 8, 1, 9),
    _Me1200PtpConfigClocksPortDsDelayAsymmetry_Type()
)
me1200PtpConfigClocksPortDsDelayAsymmetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksPortDsDelayAsymmetry.setStatus("current")
_Me1200PtpConfigClocksPortDsIngressLatency_Type = ME1200Integer64
_Me1200PtpConfigClocksPortDsIngressLatency_Object = MibTableColumn
me1200PtpConfigClocksPortDsIngressLatency = _Me1200PtpConfigClocksPortDsIngressLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 8, 1, 10),
    _Me1200PtpConfigClocksPortDsIngressLatency_Type()
)
me1200PtpConfigClocksPortDsIngressLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksPortDsIngressLatency.setStatus("current")
_Me1200PtpConfigClocksPortDsEgressLatency_Type = ME1200Integer64
_Me1200PtpConfigClocksPortDsEgressLatency_Object = MibTableColumn
me1200PtpConfigClocksPortDsEgressLatency = _Me1200PtpConfigClocksPortDsEgressLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 8, 1, 11),
    _Me1200PtpConfigClocksPortDsEgressLatency_Type()
)
me1200PtpConfigClocksPortDsEgressLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksPortDsEgressLatency.setStatus("current")
_Me1200PtpConfigClocksPortDsPortInternal_Type = TruthValue
_Me1200PtpConfigClocksPortDsPortInternal_Object = MibTableColumn
me1200PtpConfigClocksPortDsPortInternal = _Me1200PtpConfigClocksPortDsPortInternal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 8, 1, 12),
    _Me1200PtpConfigClocksPortDsPortInternal_Type()
)
me1200PtpConfigClocksPortDsPortInternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksPortDsPortInternal.setStatus("current")
_Me1200PtpConfigClocksPortDsVersionNumber_Type = ME1200Unsigned16
_Me1200PtpConfigClocksPortDsVersionNumber_Object = MibTableColumn
me1200PtpConfigClocksPortDsVersionNumber = _Me1200PtpConfigClocksPortDsVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 8, 1, 13),
    _Me1200PtpConfigClocksPortDsVersionNumber_Type()
)
me1200PtpConfigClocksPortDsVersionNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksPortDsVersionNumber.setStatus("current")
_Me1200PtpConfigClocksPortDsMcastAddr_Type = ME1200ptpDestAdrType
_Me1200PtpConfigClocksPortDsMcastAddr_Object = MibTableColumn
me1200PtpConfigClocksPortDsMcastAddr = _Me1200PtpConfigClocksPortDsMcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 8, 1, 14),
    _Me1200PtpConfigClocksPortDsMcastAddr_Type()
)
me1200PtpConfigClocksPortDsMcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksPortDsMcastAddr.setStatus("current")
_Me1200PtpConfigClocksPortDsNotSlave_Type = TruthValue
_Me1200PtpConfigClocksPortDsNotSlave_Object = MibTableColumn
me1200PtpConfigClocksPortDsNotSlave = _Me1200PtpConfigClocksPortDsNotSlave_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 8, 1, 15),
    _Me1200PtpConfigClocksPortDsNotSlave_Type()
)
me1200PtpConfigClocksPortDsNotSlave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksPortDsNotSlave.setStatus("current")
_Me1200PtpConfigClocksPortDsLocalPriority_Type = ME1200Unsigned8
_Me1200PtpConfigClocksPortDsLocalPriority_Object = MibTableColumn
me1200PtpConfigClocksPortDsLocalPriority = _Me1200PtpConfigClocksPortDsLocalPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 2, 2, 8, 1, 16),
    _Me1200PtpConfigClocksPortDsLocalPriority_Type()
)
me1200PtpConfigClocksPortDsLocalPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpConfigClocksPortDsLocalPriority.setStatus("current")
_Me1200PtpStatus_ObjectIdentity = ObjectIdentity
me1200PtpStatus = _Me1200PtpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3)
)
_Me1200PtpStatusClocks_ObjectIdentity = ObjectIdentity
me1200PtpStatusClocks = _Me1200PtpStatusClocks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1)
)
_Me1200PtpStatusClocksDefaultDsTable_Object = MibTable
me1200PtpStatusClocksDefaultDsTable = _Me1200PtpStatusClocksDefaultDsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    me1200PtpStatusClocksDefaultDsTable.setStatus("current")
_Me1200PtpStatusClocksDefaultDsEntry_Object = MibTableRow
me1200PtpStatusClocksDefaultDsEntry = _Me1200PtpStatusClocksDefaultDsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 1, 1)
)
me1200PtpStatusClocksDefaultDsEntry.setIndexNames(
    (0, "ME1200-PTP-MIB", "me1200PtpStatusClocksDefaultDsClockId"),
)
if mibBuilder.loadTexts:
    me1200PtpStatusClocksDefaultDsEntry.setStatus("current")


class _Me1200PtpStatusClocksDefaultDsClockId_Type(Integer32):
    """Custom type me1200PtpStatusClocksDefaultDsClockId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Me1200PtpStatusClocksDefaultDsClockId_Type.__name__ = "Integer32"
_Me1200PtpStatusClocksDefaultDsClockId_Object = MibTableColumn
me1200PtpStatusClocksDefaultDsClockId = _Me1200PtpStatusClocksDefaultDsClockId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 1, 1, 1),
    _Me1200PtpStatusClocksDefaultDsClockId_Type()
)
me1200PtpStatusClocksDefaultDsClockId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksDefaultDsClockId.setStatus("current")


class _Me1200PtpStatusClocksDefaultDsClockIdentity_Type(OctetString):
    """Custom type me1200PtpStatusClocksDefaultDsClockIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_Me1200PtpStatusClocksDefaultDsClockIdentity_Type.__name__ = "OctetString"
_Me1200PtpStatusClocksDefaultDsClockIdentity_Object = MibTableColumn
me1200PtpStatusClocksDefaultDsClockIdentity = _Me1200PtpStatusClocksDefaultDsClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 1, 1, 2),
    _Me1200PtpStatusClocksDefaultDsClockIdentity_Type()
)
me1200PtpStatusClocksDefaultDsClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksDefaultDsClockIdentity.setStatus("current")
_Me1200PtpStatusClocksDefaultDsClockQualityClockClass_Type = ME1200Unsigned8
_Me1200PtpStatusClocksDefaultDsClockQualityClockClass_Object = MibTableColumn
me1200PtpStatusClocksDefaultDsClockQualityClockClass = _Me1200PtpStatusClocksDefaultDsClockQualityClockClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 1, 1, 3),
    _Me1200PtpStatusClocksDefaultDsClockQualityClockClass_Type()
)
me1200PtpStatusClocksDefaultDsClockQualityClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksDefaultDsClockQualityClockClass.setStatus("current")
_Me1200PtpStatusClocksDefaultDsClockQualityClockAccuracy_Type = ME1200Unsigned8
_Me1200PtpStatusClocksDefaultDsClockQualityClockAccuracy_Object = MibTableColumn
me1200PtpStatusClocksDefaultDsClockQualityClockAccuracy = _Me1200PtpStatusClocksDefaultDsClockQualityClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 1, 1, 4),
    _Me1200PtpStatusClocksDefaultDsClockQualityClockAccuracy_Type()
)
me1200PtpStatusClocksDefaultDsClockQualityClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksDefaultDsClockQualityClockAccuracy.setStatus("current")
_Me1200PtpStatusClocksDefaultDsClockQualityOffsetScaledLogVar_Type = ME1200Unsigned16
_Me1200PtpStatusClocksDefaultDsClockQualityOffsetScaledLogVar_Object = MibTableColumn
me1200PtpStatusClocksDefaultDsClockQualityOffsetScaledLogVar = _Me1200PtpStatusClocksDefaultDsClockQualityOffsetScaledLogVar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 1, 1, 5),
    _Me1200PtpStatusClocksDefaultDsClockQualityOffsetScaledLogVar_Type()
)
me1200PtpStatusClocksDefaultDsClockQualityOffsetScaledLogVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksDefaultDsClockQualityOffsetScaledLogVar.setStatus("current")
_Me1200PtpStatusClocksCurrentDsTable_Object = MibTable
me1200PtpStatusClocksCurrentDsTable = _Me1200PtpStatusClocksCurrentDsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    me1200PtpStatusClocksCurrentDsTable.setStatus("current")
_Me1200PtpStatusClocksCurrentDsEntry_Object = MibTableRow
me1200PtpStatusClocksCurrentDsEntry = _Me1200PtpStatusClocksCurrentDsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 2, 1)
)
me1200PtpStatusClocksCurrentDsEntry.setIndexNames(
    (0, "ME1200-PTP-MIB", "me1200PtpStatusClocksCurrentDsClockId"),
)
if mibBuilder.loadTexts:
    me1200PtpStatusClocksCurrentDsEntry.setStatus("current")


class _Me1200PtpStatusClocksCurrentDsClockId_Type(Integer32):
    """Custom type me1200PtpStatusClocksCurrentDsClockId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Me1200PtpStatusClocksCurrentDsClockId_Type.__name__ = "Integer32"
_Me1200PtpStatusClocksCurrentDsClockId_Object = MibTableColumn
me1200PtpStatusClocksCurrentDsClockId = _Me1200PtpStatusClocksCurrentDsClockId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 2, 1, 1),
    _Me1200PtpStatusClocksCurrentDsClockId_Type()
)
me1200PtpStatusClocksCurrentDsClockId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksCurrentDsClockId.setStatus("current")
_Me1200PtpStatusClocksCurrentDsStepsRemoved_Type = ME1200Unsigned16
_Me1200PtpStatusClocksCurrentDsStepsRemoved_Object = MibTableColumn
me1200PtpStatusClocksCurrentDsStepsRemoved = _Me1200PtpStatusClocksCurrentDsStepsRemoved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 2, 1, 2),
    _Me1200PtpStatusClocksCurrentDsStepsRemoved_Type()
)
me1200PtpStatusClocksCurrentDsStepsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksCurrentDsStepsRemoved.setStatus("current")
_Me1200PtpStatusClocksCurrentDsOffsetFromMaster_Type = ME1200Integer64
_Me1200PtpStatusClocksCurrentDsOffsetFromMaster_Object = MibTableColumn
me1200PtpStatusClocksCurrentDsOffsetFromMaster = _Me1200PtpStatusClocksCurrentDsOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 2, 1, 3),
    _Me1200PtpStatusClocksCurrentDsOffsetFromMaster_Type()
)
me1200PtpStatusClocksCurrentDsOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksCurrentDsOffsetFromMaster.setStatus("current")
_Me1200PtpStatusClocksCurrentDsMeanPathDelay_Type = ME1200Integer64
_Me1200PtpStatusClocksCurrentDsMeanPathDelay_Object = MibTableColumn
me1200PtpStatusClocksCurrentDsMeanPathDelay = _Me1200PtpStatusClocksCurrentDsMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 2, 1, 4),
    _Me1200PtpStatusClocksCurrentDsMeanPathDelay_Type()
)
me1200PtpStatusClocksCurrentDsMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksCurrentDsMeanPathDelay.setStatus("current")
_Me1200PtpStatusClocksParentDsTable_Object = MibTable
me1200PtpStatusClocksParentDsTable = _Me1200PtpStatusClocksParentDsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    me1200PtpStatusClocksParentDsTable.setStatus("current")
_Me1200PtpStatusClocksParentDsEntry_Object = MibTableRow
me1200PtpStatusClocksParentDsEntry = _Me1200PtpStatusClocksParentDsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 3, 1)
)
me1200PtpStatusClocksParentDsEntry.setIndexNames(
    (0, "ME1200-PTP-MIB", "me1200PtpStatusClocksParentDsClockId"),
)
if mibBuilder.loadTexts:
    me1200PtpStatusClocksParentDsEntry.setStatus("current")


class _Me1200PtpStatusClocksParentDsClockId_Type(Integer32):
    """Custom type me1200PtpStatusClocksParentDsClockId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Me1200PtpStatusClocksParentDsClockId_Type.__name__ = "Integer32"
_Me1200PtpStatusClocksParentDsClockId_Object = MibTableColumn
me1200PtpStatusClocksParentDsClockId = _Me1200PtpStatusClocksParentDsClockId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 3, 1, 1),
    _Me1200PtpStatusClocksParentDsClockId_Type()
)
me1200PtpStatusClocksParentDsClockId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksParentDsClockId.setStatus("current")


class _Me1200PtpStatusClocksParentDsParentPortIdentityClockIdentity_Type(OctetString):
    """Custom type me1200PtpStatusClocksParentDsParentPortIdentityClockIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_Me1200PtpStatusClocksParentDsParentPortIdentityClockIdentity_Type.__name__ = "OctetString"
_Me1200PtpStatusClocksParentDsParentPortIdentityClockIdentity_Object = MibTableColumn
me1200PtpStatusClocksParentDsParentPortIdentityClockIdentity = _Me1200PtpStatusClocksParentDsParentPortIdentityClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 3, 1, 2),
    _Me1200PtpStatusClocksParentDsParentPortIdentityClockIdentity_Type()
)
me1200PtpStatusClocksParentDsParentPortIdentityClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksParentDsParentPortIdentityClockIdentity.setStatus("current")
_Me1200PtpStatusClocksParentDsParentPortIdentityPortNumber_Type = ME1200Unsigned16
_Me1200PtpStatusClocksParentDsParentPortIdentityPortNumber_Object = MibTableColumn
me1200PtpStatusClocksParentDsParentPortIdentityPortNumber = _Me1200PtpStatusClocksParentDsParentPortIdentityPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 3, 1, 3),
    _Me1200PtpStatusClocksParentDsParentPortIdentityPortNumber_Type()
)
me1200PtpStatusClocksParentDsParentPortIdentityPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksParentDsParentPortIdentityPortNumber.setStatus("current")
_Me1200PtpStatusClocksParentDsParentStats_Type = TruthValue
_Me1200PtpStatusClocksParentDsParentStats_Object = MibTableColumn
me1200PtpStatusClocksParentDsParentStats = _Me1200PtpStatusClocksParentDsParentStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 3, 1, 4),
    _Me1200PtpStatusClocksParentDsParentStats_Type()
)
me1200PtpStatusClocksParentDsParentStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksParentDsParentStats.setStatus("current")
_Me1200PtpStatusClocksParentDsObservedParentOffsetScaledLogVar_Type = ME1200Unsigned16
_Me1200PtpStatusClocksParentDsObservedParentOffsetScaledLogVar_Object = MibTableColumn
me1200PtpStatusClocksParentDsObservedParentOffsetScaledLogVar = _Me1200PtpStatusClocksParentDsObservedParentOffsetScaledLogVar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 3, 1, 5),
    _Me1200PtpStatusClocksParentDsObservedParentOffsetScaledLogVar_Type()
)
me1200PtpStatusClocksParentDsObservedParentOffsetScaledLogVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksParentDsObservedParentOffsetScaledLogVar.setStatus("current")
_Me1200PtpStatusClocksParentDsObservedParentClockPhaseChangeRate_Type = Integer32
_Me1200PtpStatusClocksParentDsObservedParentClockPhaseChangeRate_Object = MibTableColumn
me1200PtpStatusClocksParentDsObservedParentClockPhaseChangeRate = _Me1200PtpStatusClocksParentDsObservedParentClockPhaseChangeRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 3, 1, 6),
    _Me1200PtpStatusClocksParentDsObservedParentClockPhaseChangeRate_Type()
)
me1200PtpStatusClocksParentDsObservedParentClockPhaseChangeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksParentDsObservedParentClockPhaseChangeRate.setStatus("current")


class _Me1200PtpStatusClocksParentDsGrmstrIdentity_Type(OctetString):
    """Custom type me1200PtpStatusClocksParentDsGrmstrIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_Me1200PtpStatusClocksParentDsGrmstrIdentity_Type.__name__ = "OctetString"
_Me1200PtpStatusClocksParentDsGrmstrIdentity_Object = MibTableColumn
me1200PtpStatusClocksParentDsGrmstrIdentity = _Me1200PtpStatusClocksParentDsGrmstrIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 3, 1, 7),
    _Me1200PtpStatusClocksParentDsGrmstrIdentity_Type()
)
me1200PtpStatusClocksParentDsGrmstrIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksParentDsGrmstrIdentity.setStatus("current")
_Me1200PtpStatusClocksParentDsGrmstrClkQualClockClass_Type = ME1200Unsigned8
_Me1200PtpStatusClocksParentDsGrmstrClkQualClockClass_Object = MibTableColumn
me1200PtpStatusClocksParentDsGrmstrClkQualClockClass = _Me1200PtpStatusClocksParentDsGrmstrClkQualClockClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 3, 1, 8),
    _Me1200PtpStatusClocksParentDsGrmstrClkQualClockClass_Type()
)
me1200PtpStatusClocksParentDsGrmstrClkQualClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksParentDsGrmstrClkQualClockClass.setStatus("current")
_Me1200PtpStatusClocksParentDsGmstrClkQualClockAccuracy_Type = ME1200Unsigned8
_Me1200PtpStatusClocksParentDsGmstrClkQualClockAccuracy_Object = MibTableColumn
me1200PtpStatusClocksParentDsGmstrClkQualClockAccuracy = _Me1200PtpStatusClocksParentDsGmstrClkQualClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 3, 1, 9),
    _Me1200PtpStatusClocksParentDsGmstrClkQualClockAccuracy_Type()
)
me1200PtpStatusClocksParentDsGmstrClkQualClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksParentDsGmstrClkQualClockAccuracy.setStatus("current")
_Me1200PtpStatusClocksParentDsGmstrClkQualOffsetScaledLogVar_Type = ME1200Unsigned16
_Me1200PtpStatusClocksParentDsGmstrClkQualOffsetScaledLogVar_Object = MibTableColumn
me1200PtpStatusClocksParentDsGmstrClkQualOffsetScaledLogVar = _Me1200PtpStatusClocksParentDsGmstrClkQualOffsetScaledLogVar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 3, 1, 10),
    _Me1200PtpStatusClocksParentDsGmstrClkQualOffsetScaledLogVar_Type()
)
me1200PtpStatusClocksParentDsGmstrClkQualOffsetScaledLogVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksParentDsGmstrClkQualOffsetScaledLogVar.setStatus("current")
_Me1200PtpStatusClocksParentDsGmstrPriority1_Type = ME1200Unsigned8
_Me1200PtpStatusClocksParentDsGmstrPriority1_Object = MibTableColumn
me1200PtpStatusClocksParentDsGmstrPriority1 = _Me1200PtpStatusClocksParentDsGmstrPriority1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 3, 1, 11),
    _Me1200PtpStatusClocksParentDsGmstrPriority1_Type()
)
me1200PtpStatusClocksParentDsGmstrPriority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksParentDsGmstrPriority1.setStatus("current")
_Me1200PtpStatusClocksParentDsGmstrPriority2_Type = ME1200Unsigned8
_Me1200PtpStatusClocksParentDsGmstrPriority2_Object = MibTableColumn
me1200PtpStatusClocksParentDsGmstrPriority2 = _Me1200PtpStatusClocksParentDsGmstrPriority2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 3, 1, 12),
    _Me1200PtpStatusClocksParentDsGmstrPriority2_Type()
)
me1200PtpStatusClocksParentDsGmstrPriority2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksParentDsGmstrPriority2.setStatus("current")
_Me1200PtpStatusClocksTimePropertiesDsTable_Object = MibTable
me1200PtpStatusClocksTimePropertiesDsTable = _Me1200PtpStatusClocksTimePropertiesDsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    me1200PtpStatusClocksTimePropertiesDsTable.setStatus("current")
_Me1200PtpStatusClocksTimePropertiesDsEntry_Object = MibTableRow
me1200PtpStatusClocksTimePropertiesDsEntry = _Me1200PtpStatusClocksTimePropertiesDsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 4, 1)
)
me1200PtpStatusClocksTimePropertiesDsEntry.setIndexNames(
    (0, "ME1200-PTP-MIB", "me1200PtpStatusClocksTimePropertiesDsClockId"),
)
if mibBuilder.loadTexts:
    me1200PtpStatusClocksTimePropertiesDsEntry.setStatus("current")


class _Me1200PtpStatusClocksTimePropertiesDsClockId_Type(Integer32):
    """Custom type me1200PtpStatusClocksTimePropertiesDsClockId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Me1200PtpStatusClocksTimePropertiesDsClockId_Type.__name__ = "Integer32"
_Me1200PtpStatusClocksTimePropertiesDsClockId_Object = MibTableColumn
me1200PtpStatusClocksTimePropertiesDsClockId = _Me1200PtpStatusClocksTimePropertiesDsClockId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 4, 1, 1),
    _Me1200PtpStatusClocksTimePropertiesDsClockId_Type()
)
me1200PtpStatusClocksTimePropertiesDsClockId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksTimePropertiesDsClockId.setStatus("current")
_Me1200PtpStatusClocksTimePropertiesDsCurrentUtcOffset_Type = ME1200Integer16
_Me1200PtpStatusClocksTimePropertiesDsCurrentUtcOffset_Object = MibTableColumn
me1200PtpStatusClocksTimePropertiesDsCurrentUtcOffset = _Me1200PtpStatusClocksTimePropertiesDsCurrentUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 4, 1, 2),
    _Me1200PtpStatusClocksTimePropertiesDsCurrentUtcOffset_Type()
)
me1200PtpStatusClocksTimePropertiesDsCurrentUtcOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksTimePropertiesDsCurrentUtcOffset.setStatus("current")
_Me1200PtpStatusClocksTimePropertiesDsCurrentUtcOffsetValid_Type = TruthValue
_Me1200PtpStatusClocksTimePropertiesDsCurrentUtcOffsetValid_Object = MibTableColumn
me1200PtpStatusClocksTimePropertiesDsCurrentUtcOffsetValid = _Me1200PtpStatusClocksTimePropertiesDsCurrentUtcOffsetValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 4, 1, 3),
    _Me1200PtpStatusClocksTimePropertiesDsCurrentUtcOffsetValid_Type()
)
me1200PtpStatusClocksTimePropertiesDsCurrentUtcOffsetValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksTimePropertiesDsCurrentUtcOffsetValid.setStatus("current")
_Me1200PtpStatusClocksTimePropertiesDsLeap59_Type = TruthValue
_Me1200PtpStatusClocksTimePropertiesDsLeap59_Object = MibTableColumn
me1200PtpStatusClocksTimePropertiesDsLeap59 = _Me1200PtpStatusClocksTimePropertiesDsLeap59_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 4, 1, 4),
    _Me1200PtpStatusClocksTimePropertiesDsLeap59_Type()
)
me1200PtpStatusClocksTimePropertiesDsLeap59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksTimePropertiesDsLeap59.setStatus("current")
_Me1200PtpStatusClocksTimePropertiesDsLeap61_Type = TruthValue
_Me1200PtpStatusClocksTimePropertiesDsLeap61_Object = MibTableColumn
me1200PtpStatusClocksTimePropertiesDsLeap61 = _Me1200PtpStatusClocksTimePropertiesDsLeap61_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 4, 1, 5),
    _Me1200PtpStatusClocksTimePropertiesDsLeap61_Type()
)
me1200PtpStatusClocksTimePropertiesDsLeap61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksTimePropertiesDsLeap61.setStatus("current")
_Me1200PtpStatusClocksTimePropertiesDsTimeTraceable_Type = TruthValue
_Me1200PtpStatusClocksTimePropertiesDsTimeTraceable_Object = MibTableColumn
me1200PtpStatusClocksTimePropertiesDsTimeTraceable = _Me1200PtpStatusClocksTimePropertiesDsTimeTraceable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 4, 1, 6),
    _Me1200PtpStatusClocksTimePropertiesDsTimeTraceable_Type()
)
me1200PtpStatusClocksTimePropertiesDsTimeTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksTimePropertiesDsTimeTraceable.setStatus("current")
_Me1200PtpStatusClocksTimePropertiesDsFrequencyTraceable_Type = TruthValue
_Me1200PtpStatusClocksTimePropertiesDsFrequencyTraceable_Object = MibTableColumn
me1200PtpStatusClocksTimePropertiesDsFrequencyTraceable = _Me1200PtpStatusClocksTimePropertiesDsFrequencyTraceable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 4, 1, 7),
    _Me1200PtpStatusClocksTimePropertiesDsFrequencyTraceable_Type()
)
me1200PtpStatusClocksTimePropertiesDsFrequencyTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksTimePropertiesDsFrequencyTraceable.setStatus("current")
_Me1200PtpStatusClocksTimePropertiesDsPtpTimescale_Type = TruthValue
_Me1200PtpStatusClocksTimePropertiesDsPtpTimescale_Object = MibTableColumn
me1200PtpStatusClocksTimePropertiesDsPtpTimescale = _Me1200PtpStatusClocksTimePropertiesDsPtpTimescale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 4, 1, 8),
    _Me1200PtpStatusClocksTimePropertiesDsPtpTimescale_Type()
)
me1200PtpStatusClocksTimePropertiesDsPtpTimescale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksTimePropertiesDsPtpTimescale.setStatus("current")
_Me1200PtpStatusClocksTimePropertiesDsTimeSource_Type = ME1200Unsigned8
_Me1200PtpStatusClocksTimePropertiesDsTimeSource_Object = MibTableColumn
me1200PtpStatusClocksTimePropertiesDsTimeSource = _Me1200PtpStatusClocksTimePropertiesDsTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 4, 1, 9),
    _Me1200PtpStatusClocksTimePropertiesDsTimeSource_Type()
)
me1200PtpStatusClocksTimePropertiesDsTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksTimePropertiesDsTimeSource.setStatus("current")
_Me1200PtpStatusClocksSlaveDsTable_Object = MibTable
me1200PtpStatusClocksSlaveDsTable = _Me1200PtpStatusClocksSlaveDsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 5)
)
if mibBuilder.loadTexts:
    me1200PtpStatusClocksSlaveDsTable.setStatus("current")
_Me1200PtpStatusClocksSlaveDsEntry_Object = MibTableRow
me1200PtpStatusClocksSlaveDsEntry = _Me1200PtpStatusClocksSlaveDsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 5, 1)
)
me1200PtpStatusClocksSlaveDsEntry.setIndexNames(
    (0, "ME1200-PTP-MIB", "me1200PtpStatusClocksSlaveDsClockId"),
)
if mibBuilder.loadTexts:
    me1200PtpStatusClocksSlaveDsEntry.setStatus("current")


class _Me1200PtpStatusClocksSlaveDsClockId_Type(Integer32):
    """Custom type me1200PtpStatusClocksSlaveDsClockId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Me1200PtpStatusClocksSlaveDsClockId_Type.__name__ = "Integer32"
_Me1200PtpStatusClocksSlaveDsClockId_Object = MibTableColumn
me1200PtpStatusClocksSlaveDsClockId = _Me1200PtpStatusClocksSlaveDsClockId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 5, 1, 1),
    _Me1200PtpStatusClocksSlaveDsClockId_Type()
)
me1200PtpStatusClocksSlaveDsClockId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksSlaveDsClockId.setStatus("current")
_Me1200PtpStatusClocksSlaveDsSlavePort_Type = ME1200Unsigned16
_Me1200PtpStatusClocksSlaveDsSlavePort_Object = MibTableColumn
me1200PtpStatusClocksSlaveDsSlavePort = _Me1200PtpStatusClocksSlaveDsSlavePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 5, 1, 2),
    _Me1200PtpStatusClocksSlaveDsSlavePort_Type()
)
me1200PtpStatusClocksSlaveDsSlavePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksSlaveDsSlavePort.setStatus("current")
_Me1200PtpStatusClocksSlaveDsSlaveState_Type = ME1200ptpSlaveClockState
_Me1200PtpStatusClocksSlaveDsSlaveState_Object = MibTableColumn
me1200PtpStatusClocksSlaveDsSlaveState = _Me1200PtpStatusClocksSlaveDsSlaveState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 5, 1, 3),
    _Me1200PtpStatusClocksSlaveDsSlaveState_Type()
)
me1200PtpStatusClocksSlaveDsSlaveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksSlaveDsSlaveState.setStatus("current")
_Me1200PtpStatusClocksSlaveDsHoldoverStable_Type = ME1200Unsigned8
_Me1200PtpStatusClocksSlaveDsHoldoverStable_Object = MibTableColumn
me1200PtpStatusClocksSlaveDsHoldoverStable = _Me1200PtpStatusClocksSlaveDsHoldoverStable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 5, 1, 4),
    _Me1200PtpStatusClocksSlaveDsHoldoverStable_Type()
)
me1200PtpStatusClocksSlaveDsHoldoverStable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksSlaveDsHoldoverStable.setStatus("current")
_Me1200PtpStatusClocksSlaveDsHoldoverAdj_Type = ME1200Integer64
_Me1200PtpStatusClocksSlaveDsHoldoverAdj_Object = MibTableColumn
me1200PtpStatusClocksSlaveDsHoldoverAdj = _Me1200PtpStatusClocksSlaveDsHoldoverAdj_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 5, 1, 5),
    _Me1200PtpStatusClocksSlaveDsHoldoverAdj_Type()
)
me1200PtpStatusClocksSlaveDsHoldoverAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksSlaveDsHoldoverAdj.setStatus("current")
_Me1200PtpStatusClocksUnicastMasterTable_Object = MibTable
me1200PtpStatusClocksUnicastMasterTable = _Me1200PtpStatusClocksUnicastMasterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 6)
)
if mibBuilder.loadTexts:
    me1200PtpStatusClocksUnicastMasterTable.setStatus("current")
_Me1200PtpStatusClocksUnicastMasterEntry_Object = MibTableRow
me1200PtpStatusClocksUnicastMasterEntry = _Me1200PtpStatusClocksUnicastMasterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 6, 1)
)
me1200PtpStatusClocksUnicastMasterEntry.setIndexNames(
    (0, "ME1200-PTP-MIB", "me1200PtpStatusClocksUnicastMasterClockId"),
    (0, "ME1200-PTP-MIB", "me1200PtpStatusClocksUnicastMasterSlaveIp"),
)
if mibBuilder.loadTexts:
    me1200PtpStatusClocksUnicastMasterEntry.setStatus("current")


class _Me1200PtpStatusClocksUnicastMasterClockId_Type(Integer32):
    """Custom type me1200PtpStatusClocksUnicastMasterClockId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Me1200PtpStatusClocksUnicastMasterClockId_Type.__name__ = "Integer32"
_Me1200PtpStatusClocksUnicastMasterClockId_Object = MibTableColumn
me1200PtpStatusClocksUnicastMasterClockId = _Me1200PtpStatusClocksUnicastMasterClockId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 6, 1, 1),
    _Me1200PtpStatusClocksUnicastMasterClockId_Type()
)
me1200PtpStatusClocksUnicastMasterClockId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksUnicastMasterClockId.setStatus("current")
_Me1200PtpStatusClocksUnicastMasterSlaveIp_Type = IpAddress
_Me1200PtpStatusClocksUnicastMasterSlaveIp_Object = MibTableColumn
me1200PtpStatusClocksUnicastMasterSlaveIp = _Me1200PtpStatusClocksUnicastMasterSlaveIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 6, 1, 2),
    _Me1200PtpStatusClocksUnicastMasterSlaveIp_Type()
)
me1200PtpStatusClocksUnicastMasterSlaveIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksUnicastMasterSlaveIp.setStatus("current")
_Me1200PtpStatusClocksUnicastMasterSlaveMac_Type = MacAddress
_Me1200PtpStatusClocksUnicastMasterSlaveMac_Object = MibTableColumn
me1200PtpStatusClocksUnicastMasterSlaveMac = _Me1200PtpStatusClocksUnicastMasterSlaveMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 6, 1, 3),
    _Me1200PtpStatusClocksUnicastMasterSlaveMac_Type()
)
me1200PtpStatusClocksUnicastMasterSlaveMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksUnicastMasterSlaveMac.setStatus("current")
_Me1200PtpStatusClocksUnicastMasterPort_Type = ME1200Unsigned16
_Me1200PtpStatusClocksUnicastMasterPort_Object = MibTableColumn
me1200PtpStatusClocksUnicastMasterPort = _Me1200PtpStatusClocksUnicastMasterPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 6, 1, 4),
    _Me1200PtpStatusClocksUnicastMasterPort_Type()
)
me1200PtpStatusClocksUnicastMasterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksUnicastMasterPort.setStatus("current")
_Me1200PtpStatusClocksUnicastMasterAnnLogMsgPeriod_Type = ME1200Integer16
_Me1200PtpStatusClocksUnicastMasterAnnLogMsgPeriod_Object = MibTableColumn
me1200PtpStatusClocksUnicastMasterAnnLogMsgPeriod = _Me1200PtpStatusClocksUnicastMasterAnnLogMsgPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 6, 1, 5),
    _Me1200PtpStatusClocksUnicastMasterAnnLogMsgPeriod_Type()
)
me1200PtpStatusClocksUnicastMasterAnnLogMsgPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksUnicastMasterAnnLogMsgPeriod.setStatus("current")
_Me1200PtpStatusClocksUnicastMasterAnn_Type = TruthValue
_Me1200PtpStatusClocksUnicastMasterAnn_Object = MibTableColumn
me1200PtpStatusClocksUnicastMasterAnn = _Me1200PtpStatusClocksUnicastMasterAnn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 6, 1, 6),
    _Me1200PtpStatusClocksUnicastMasterAnn_Type()
)
me1200PtpStatusClocksUnicastMasterAnn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksUnicastMasterAnn.setStatus("current")
_Me1200PtpStatusClocksUnicastMasterLogMsgPeriod_Type = ME1200Integer16
_Me1200PtpStatusClocksUnicastMasterLogMsgPeriod_Object = MibTableColumn
me1200PtpStatusClocksUnicastMasterLogMsgPeriod = _Me1200PtpStatusClocksUnicastMasterLogMsgPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 6, 1, 7),
    _Me1200PtpStatusClocksUnicastMasterLogMsgPeriod_Type()
)
me1200PtpStatusClocksUnicastMasterLogMsgPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksUnicastMasterLogMsgPeriod.setStatus("current")
_Me1200PtpStatusClocksUnicastMasterSync_Type = TruthValue
_Me1200PtpStatusClocksUnicastMasterSync_Object = MibTableColumn
me1200PtpStatusClocksUnicastMasterSync = _Me1200PtpStatusClocksUnicastMasterSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 6, 1, 8),
    _Me1200PtpStatusClocksUnicastMasterSync_Type()
)
me1200PtpStatusClocksUnicastMasterSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksUnicastMasterSync.setStatus("current")
_Me1200PtpStatusClocksUnicastSlaveTable_Object = MibTable
me1200PtpStatusClocksUnicastSlaveTable = _Me1200PtpStatusClocksUnicastSlaveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 7)
)
if mibBuilder.loadTexts:
    me1200PtpStatusClocksUnicastSlaveTable.setStatus("current")
_Me1200PtpStatusClocksUnicastSlaveEntry_Object = MibTableRow
me1200PtpStatusClocksUnicastSlaveEntry = _Me1200PtpStatusClocksUnicastSlaveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 7, 1)
)
me1200PtpStatusClocksUnicastSlaveEntry.setIndexNames(
    (0, "ME1200-PTP-MIB", "me1200PtpStatusClocksUnicastSlaveClockId"),
    (0, "ME1200-PTP-MIB", "me1200PtpStatusClocksUnicastSlaveMasterId"),
)
if mibBuilder.loadTexts:
    me1200PtpStatusClocksUnicastSlaveEntry.setStatus("current")


class _Me1200PtpStatusClocksUnicastSlaveClockId_Type(Integer32):
    """Custom type me1200PtpStatusClocksUnicastSlaveClockId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Me1200PtpStatusClocksUnicastSlaveClockId_Type.__name__ = "Integer32"
_Me1200PtpStatusClocksUnicastSlaveClockId_Object = MibTableColumn
me1200PtpStatusClocksUnicastSlaveClockId = _Me1200PtpStatusClocksUnicastSlaveClockId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 7, 1, 1),
    _Me1200PtpStatusClocksUnicastSlaveClockId_Type()
)
me1200PtpStatusClocksUnicastSlaveClockId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksUnicastSlaveClockId.setStatus("current")


class _Me1200PtpStatusClocksUnicastSlaveMasterId_Type(Integer32):
    """Custom type me1200PtpStatusClocksUnicastSlaveMasterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Me1200PtpStatusClocksUnicastSlaveMasterId_Type.__name__ = "Integer32"
_Me1200PtpStatusClocksUnicastSlaveMasterId_Object = MibTableColumn
me1200PtpStatusClocksUnicastSlaveMasterId = _Me1200PtpStatusClocksUnicastSlaveMasterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 7, 1, 2),
    _Me1200PtpStatusClocksUnicastSlaveMasterId_Type()
)
me1200PtpStatusClocksUnicastSlaveMasterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksUnicastSlaveMasterId.setStatus("current")
_Me1200PtpStatusClocksUnicastSlaveMasterIp_Type = IpAddress
_Me1200PtpStatusClocksUnicastSlaveMasterIp_Object = MibTableColumn
me1200PtpStatusClocksUnicastSlaveMasterIp = _Me1200PtpStatusClocksUnicastSlaveMasterIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 7, 1, 3),
    _Me1200PtpStatusClocksUnicastSlaveMasterIp_Type()
)
me1200PtpStatusClocksUnicastSlaveMasterIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksUnicastSlaveMasterIp.setStatus("current")
_Me1200PtpStatusClocksUnicastSlaveMasterMac_Type = MacAddress
_Me1200PtpStatusClocksUnicastSlaveMasterMac_Object = MibTableColumn
me1200PtpStatusClocksUnicastSlaveMasterMac = _Me1200PtpStatusClocksUnicastSlaveMasterMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 7, 1, 4),
    _Me1200PtpStatusClocksUnicastSlaveMasterMac_Type()
)
me1200PtpStatusClocksUnicastSlaveMasterMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksUnicastSlaveMasterMac.setStatus("current")


class _Me1200PtpStatusClocksUnicastSlaveSourcePortIdentityClockIdentity_Type(OctetString):
    """Custom type me1200PtpStatusClocksUnicastSlaveSourcePortIdentityClockIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_Me1200PtpStatusClocksUnicastSlaveSourcePortIdentityClockIdentity_Type.__name__ = "OctetString"
_Me1200PtpStatusClocksUnicastSlaveSourcePortIdentityClockIdentity_Object = MibTableColumn
me1200PtpStatusClocksUnicastSlaveSourcePortIdentityClockIdentity = _Me1200PtpStatusClocksUnicastSlaveSourcePortIdentityClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 7, 1, 5),
    _Me1200PtpStatusClocksUnicastSlaveSourcePortIdentityClockIdentity_Type()
)
me1200PtpStatusClocksUnicastSlaveSourcePortIdentityClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksUnicastSlaveSourcePortIdentityClockIdentity.setStatus("current")
_Me1200PtpStatusClocksUnicastSlaveSourcePortIdentityPortNumber_Type = ME1200Unsigned16
_Me1200PtpStatusClocksUnicastSlaveSourcePortIdentityPortNumber_Object = MibTableColumn
me1200PtpStatusClocksUnicastSlaveSourcePortIdentityPortNumber = _Me1200PtpStatusClocksUnicastSlaveSourcePortIdentityPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 7, 1, 6),
    _Me1200PtpStatusClocksUnicastSlaveSourcePortIdentityPortNumber_Type()
)
me1200PtpStatusClocksUnicastSlaveSourcePortIdentityPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksUnicastSlaveSourcePortIdentityPortNumber.setStatus("current")
_Me1200PtpStatusClocksUnicastSlavePort_Type = ME1200Unsigned16
_Me1200PtpStatusClocksUnicastSlavePort_Object = MibTableColumn
me1200PtpStatusClocksUnicastSlavePort = _Me1200PtpStatusClocksUnicastSlavePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 7, 1, 7),
    _Me1200PtpStatusClocksUnicastSlavePort_Type()
)
me1200PtpStatusClocksUnicastSlavePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksUnicastSlavePort.setStatus("current")
_Me1200PtpStatusClocksUnicastSlaveLogMsgPeriod_Type = ME1200Integer16
_Me1200PtpStatusClocksUnicastSlaveLogMsgPeriod_Object = MibTableColumn
me1200PtpStatusClocksUnicastSlaveLogMsgPeriod = _Me1200PtpStatusClocksUnicastSlaveLogMsgPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 7, 1, 8),
    _Me1200PtpStatusClocksUnicastSlaveLogMsgPeriod_Type()
)
me1200PtpStatusClocksUnicastSlaveLogMsgPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksUnicastSlaveLogMsgPeriod.setStatus("current")
_Me1200PtpStatusClocksUnicastSlaveCommState_Type = ME1200ptpUcCommState
_Me1200PtpStatusClocksUnicastSlaveCommState_Object = MibTableColumn
me1200PtpStatusClocksUnicastSlaveCommState = _Me1200PtpStatusClocksUnicastSlaveCommState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 7, 1, 9),
    _Me1200PtpStatusClocksUnicastSlaveCommState_Type()
)
me1200PtpStatusClocksUnicastSlaveCommState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksUnicastSlaveCommState.setStatus("current")
_Me1200PtpStatusClocksUnicastSlaveConfMasterIp_Type = IpAddress
_Me1200PtpStatusClocksUnicastSlaveConfMasterIp_Object = MibTableColumn
me1200PtpStatusClocksUnicastSlaveConfMasterIp = _Me1200PtpStatusClocksUnicastSlaveConfMasterIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 7, 1, 10),
    _Me1200PtpStatusClocksUnicastSlaveConfMasterIp_Type()
)
me1200PtpStatusClocksUnicastSlaveConfMasterIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksUnicastSlaveConfMasterIp.setStatus("current")
_Me1200PtpStatusClocksPortsDsTable_Object = MibTable
me1200PtpStatusClocksPortsDsTable = _Me1200PtpStatusClocksPortsDsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 8)
)
if mibBuilder.loadTexts:
    me1200PtpStatusClocksPortsDsTable.setStatus("current")
_Me1200PtpStatusClocksPortsDsEntry_Object = MibTableRow
me1200PtpStatusClocksPortsDsEntry = _Me1200PtpStatusClocksPortsDsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 8, 1)
)
me1200PtpStatusClocksPortsDsEntry.setIndexNames(
    (0, "ME1200-PTP-MIB", "me1200PtpStatusClocksPortsDsClockId"),
    (0, "ME1200-PTP-MIB", "me1200PtpStatusClocksPortsDsPortId"),
)
if mibBuilder.loadTexts:
    me1200PtpStatusClocksPortsDsEntry.setStatus("current")


class _Me1200PtpStatusClocksPortsDsClockId_Type(Integer32):
    """Custom type me1200PtpStatusClocksPortsDsClockId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Me1200PtpStatusClocksPortsDsClockId_Type.__name__ = "Integer32"
_Me1200PtpStatusClocksPortsDsClockId_Object = MibTableColumn
me1200PtpStatusClocksPortsDsClockId = _Me1200PtpStatusClocksPortsDsClockId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 8, 1, 1),
    _Me1200PtpStatusClocksPortsDsClockId_Type()
)
me1200PtpStatusClocksPortsDsClockId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksPortsDsClockId.setStatus("current")


class _Me1200PtpStatusClocksPortsDsPortId_Type(ME1200InterfaceIndex):
    """Custom type me1200PtpStatusClocksPortsDsPortId based on ME1200InterfaceIndex"""
    subtypeSpec = ME1200InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Me1200PtpStatusClocksPortsDsPortId_Type.__name__ = "ME1200InterfaceIndex"
_Me1200PtpStatusClocksPortsDsPortId_Object = MibTableColumn
me1200PtpStatusClocksPortsDsPortId = _Me1200PtpStatusClocksPortsDsPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 8, 1, 2),
    _Me1200PtpStatusClocksPortsDsPortId_Type()
)
me1200PtpStatusClocksPortsDsPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksPortsDsPortId.setStatus("current")
_Me1200PtpStatusClocksPortsDsPortState_Type = ME1200ptpClockPortState
_Me1200PtpStatusClocksPortsDsPortState_Object = MibTableColumn
me1200PtpStatusClocksPortsDsPortState = _Me1200PtpStatusClocksPortsDsPortState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 8, 1, 3),
    _Me1200PtpStatusClocksPortsDsPortState_Type()
)
me1200PtpStatusClocksPortsDsPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksPortsDsPortState.setStatus("current")
_Me1200PtpStatusClocksPortsDsLogMinDelayReqInterval_Type = ME1200Integer16
_Me1200PtpStatusClocksPortsDsLogMinDelayReqInterval_Object = MibTableColumn
me1200PtpStatusClocksPortsDsLogMinDelayReqInterval = _Me1200PtpStatusClocksPortsDsLogMinDelayReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 8, 1, 4),
    _Me1200PtpStatusClocksPortsDsLogMinDelayReqInterval_Type()
)
me1200PtpStatusClocksPortsDsLogMinDelayReqInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksPortsDsLogMinDelayReqInterval.setStatus("current")
_Me1200PtpStatusClocksPortsDsPeerMeanPathDelay_Type = ME1200Integer64
_Me1200PtpStatusClocksPortsDsPeerMeanPathDelay_Object = MibTableColumn
me1200PtpStatusClocksPortsDsPeerMeanPathDelay = _Me1200PtpStatusClocksPortsDsPeerMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 8, 1, 5),
    _Me1200PtpStatusClocksPortsDsPeerMeanPathDelay_Type()
)
me1200PtpStatusClocksPortsDsPeerMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksPortsDsPeerMeanPathDelay.setStatus("current")
_Me1200PtpStatusClocksPortsDsPeerDelayOk_Type = TruthValue
_Me1200PtpStatusClocksPortsDsPeerDelayOk_Object = MibTableColumn
me1200PtpStatusClocksPortsDsPeerDelayOk = _Me1200PtpStatusClocksPortsDsPeerDelayOk_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 3, 1, 8, 1, 6),
    _Me1200PtpStatusClocksPortsDsPeerDelayOk_Type()
)
me1200PtpStatusClocksPortsDsPeerDelayOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PtpStatusClocksPortsDsPeerDelayOk.setStatus("current")
_Me1200PtpControl_ObjectIdentity = ObjectIdentity
me1200PtpControl = _Me1200PtpControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 4)
)
_Me1200PtpControlClocksTable_Object = MibTable
me1200PtpControlClocksTable = _Me1200PtpControlClocksTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 4, 1)
)
if mibBuilder.loadTexts:
    me1200PtpControlClocksTable.setStatus("current")
_Me1200PtpControlClocksEntry_Object = MibTableRow
me1200PtpControlClocksEntry = _Me1200PtpControlClocksEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 4, 1, 1)
)
me1200PtpControlClocksEntry.setIndexNames(
    (0, "ME1200-PTP-MIB", "me1200PtpControlClocksClockId"),
)
if mibBuilder.loadTexts:
    me1200PtpControlClocksEntry.setStatus("current")


class _Me1200PtpControlClocksClockId_Type(Integer32):
    """Custom type me1200PtpControlClocksClockId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Me1200PtpControlClocksClockId_Type.__name__ = "Integer32"
_Me1200PtpControlClocksClockId_Object = MibTableColumn
me1200PtpControlClocksClockId = _Me1200PtpControlClocksClockId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 4, 1, 1, 1),
    _Me1200PtpControlClocksClockId_Type()
)
me1200PtpControlClocksClockId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PtpControlClocksClockId.setStatus("current")
_Me1200PtpControlClocksSyncToSystemClock_Type = ME1200Unsigned8
_Me1200PtpControlClocksSyncToSystemClock_Object = MibTableColumn
me1200PtpControlClocksSyncToSystemClock = _Me1200PtpControlClocksSyncToSystemClock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 4, 1, 1, 2),
    _Me1200PtpControlClocksSyncToSystemClock_Type()
)
me1200PtpControlClocksSyncToSystemClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PtpControlClocksSyncToSystemClock.setStatus("current")
_Me1200PtpStatistics_ObjectIdentity = ObjectIdentity
me1200PtpStatistics = _Me1200PtpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 5)
)
_Me1200PtpNotifs_ObjectIdentity = ObjectIdentity
me1200PtpNotifs = _Me1200PtpNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 6)
)
_Me1200PtpMibConformance_ObjectIdentity = ObjectIdentity
me1200PtpMibConformance = _Me1200PtpMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 2)
)
_Me1200PtpMibCompliances_ObjectIdentity = ObjectIdentity
me1200PtpMibCompliances = _Me1200PtpMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 2, 1)
)
_Me1200PtpMibGroups_ObjectIdentity = ObjectIdentity
me1200PtpMibGroups = _Me1200PtpMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 2, 2)
)

# Managed Objects groups

me1200PtpCapabilitiesGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 2, 2, 1)
)
me1200PtpCapabilitiesGlobalsInfoGroup.setObjects(
    ("ME1200-PTP-MIB", "me1200PtpCapabilitiesGlobalsClockCount")
)
if mibBuilder.loadTexts:
    me1200PtpCapabilitiesGlobalsInfoGroup.setStatus("current")

me1200PtpConfigGlobalsExternalClockModeInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 2, 2, 2)
)
me1200PtpConfigGlobalsExternalClockModeInfoGroup.setObjects(
      *(("ME1200-PTP-MIB", "me1200PtpConfigGlobalsExternalClockModeOnePpsMode"),
        ("ME1200-PTP-MIB", "me1200PtpConfigGlobalsExternalClockModeExternalEnable"),
        ("ME1200-PTP-MIB", "me1200PtpConfigGlobalsExternalClockModeAdjustMethod"),
        ("ME1200-PTP-MIB", "me1200PtpConfigGlobalsExternalClockModeClockFrequency"))
)
if mibBuilder.loadTexts:
    me1200PtpConfigGlobalsExternalClockModeInfoGroup.setStatus("current")

me1200PtpConfigGlobalsSystemTimeSyncModeInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 2, 2, 3)
)
me1200PtpConfigGlobalsSystemTimeSyncModeInfoGroup.setObjects(
    ("ME1200-PTP-MIB", "me1200PtpConfigGlobalsSystemTimeSyncModeMode")
)
if mibBuilder.loadTexts:
    me1200PtpConfigGlobalsSystemTimeSyncModeInfoGroup.setStatus("current")

me1200PtpConfigClocksDefaultDsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 2, 2, 4)
)
me1200PtpConfigClocksDefaultDsTableInfoGroup.setObjects(
      *(("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsDeviceType"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsTwoStepFlag"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsPriority1"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsPriority2"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsOneWay"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsDomainNumber"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsProtocol"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsVlanTagEnable"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsVid"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsPcp"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsMep"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsClkDom"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsDscp"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsProfile"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsLocalPriority"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsAction"))
)
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsTableInfoGroup.setStatus("current")

me1200PtpConfigClocksDefaultDsTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 2, 2, 5)
)
me1200PtpConfigClocksDefaultDsTableRowEditorInfoGroup.setObjects(
      *(("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsTableRowEditorClockId"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsTableRowEditorDeviceType"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsTableRowEditorTwoStepFlag"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsTableRowEditorPriority1"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsTableRowEditorPriority2"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsTableRowEditorOneWay"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsTableRowEditorDomainNumber"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsTableRowEditorProtocol"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsTableRowEditorVlanTagEnable"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsTableRowEditorVid"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsTableRowEditorPcp"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsTableRowEditorMep"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsTableRowEditorClkDom"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsTableRowEditorDscp"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsTableRowEditorProfile"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsTableRowEditorLocalPriority"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200PtpConfigClocksDefaultDsTableRowEditorInfoGroup.setStatus("current")

me1200PtpConfigClocksTimePropertiesDsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 2, 2, 6)
)
me1200PtpConfigClocksTimePropertiesDsTableInfoGroup.setObjects(
      *(("ME1200-PTP-MIB", "me1200PtpConfigClocksTimePropertiesDsCurrentUtcOffset"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksTimePropertiesDsCurrentUtcOffsetValid"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksTimePropertiesDsLeap59"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksTimePropertiesDsLeap61"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksTimePropertiesDsTimeTraceable"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksTimePropertiesDsFrequencyTraceable"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksTimePropertiesDsPtpTimescale"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksTimePropertiesDsTimeSource"))
)
if mibBuilder.loadTexts:
    me1200PtpConfigClocksTimePropertiesDsTableInfoGroup.setStatus("current")

me1200PtpConfigClocksFilterParametersTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 2, 2, 7)
)
me1200PtpConfigClocksFilterParametersTableInfoGroup.setObjects(
      *(("ME1200-PTP-MIB", "me1200PtpConfigClocksFilterParametersDelayFilter"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksFilterParametersFilterType"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksFilterParametersPeriod"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksFilterParametersDist"))
)
if mibBuilder.loadTexts:
    me1200PtpConfigClocksFilterParametersTableInfoGroup.setStatus("current")

me1200PtpConfigClocksServoParametersTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 2, 2, 8)
)
me1200PtpConfigClocksServoParametersTableInfoGroup.setObjects(
      *(("ME1200-PTP-MIB", "me1200PtpConfigClocksServoParametersDisplay"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksServoParametersPEnable"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksServoParametersIEnable"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksServoParametersDEnable"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksServoParametersPval"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksServoParametersIval"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksServoParametersDval"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksServoParametersSrvOption"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksServoParametersSynceThreshold"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksServoParametersSynceAp"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksServoParametersHoFilter"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksServoParametersStableAdjThreshold"))
)
if mibBuilder.loadTexts:
    me1200PtpConfigClocksServoParametersTableInfoGroup.setStatus("current")

me1200PtpConfigClocksSlaveConfigTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 2, 2, 9)
)
me1200PtpConfigClocksSlaveConfigTableInfoGroup.setObjects(
      *(("ME1200-PTP-MIB", "me1200PtpConfigClocksSlaveConfigStableOffset"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksSlaveConfigOffsetOk"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksSlaveConfigOffsetFail"))
)
if mibBuilder.loadTexts:
    me1200PtpConfigClocksSlaveConfigTableInfoGroup.setStatus("current")

me1200PtpConfigClocksUnicastSlaveConfigTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 2, 2, 10)
)
me1200PtpConfigClocksUnicastSlaveConfigTableInfoGroup.setObjects(
      *(("ME1200-PTP-MIB", "me1200PtpConfigClocksUnicastSlaveConfigDuration"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksUnicastSlaveConfigIpAddress"))
)
if mibBuilder.loadTexts:
    me1200PtpConfigClocksUnicastSlaveConfigTableInfoGroup.setStatus("current")

me1200PtpConfigClocksPortDsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 2, 2, 11)
)
me1200PtpConfigClocksPortDsTableInfoGroup.setObjects(
      *(("ME1200-PTP-MIB", "me1200PtpConfigClocksPortDsEnabled"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksPortDsLogAnnounceInterval"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksPortDsAnnounceReceiptTimeout"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksPortDsLogSyncInterval"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksPortDsDelayMechanism"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksPortDsLogMinPdelayReqInterval"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksPortDsDelayAsymmetry"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksPortDsIngressLatency"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksPortDsEgressLatency"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksPortDsPortInternal"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksPortDsVersionNumber"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksPortDsMcastAddr"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksPortDsNotSlave"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksPortDsLocalPriority"))
)
if mibBuilder.loadTexts:
    me1200PtpConfigClocksPortDsTableInfoGroup.setStatus("current")

me1200PtpStatusClocksDefaultDsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 2, 2, 12)
)
me1200PtpStatusClocksDefaultDsTableInfoGroup.setObjects(
      *(("ME1200-PTP-MIB", "me1200PtpStatusClocksDefaultDsClockIdentity"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksDefaultDsClockQualityClockClass"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksDefaultDsClockQualityClockAccuracy"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksDefaultDsClockQualityOffsetScaledLogVar"))
)
if mibBuilder.loadTexts:
    me1200PtpStatusClocksDefaultDsTableInfoGroup.setStatus("current")

me1200PtpStatusClocksCurrentDsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 2, 2, 13)
)
me1200PtpStatusClocksCurrentDsTableInfoGroup.setObjects(
      *(("ME1200-PTP-MIB", "me1200PtpStatusClocksCurrentDsStepsRemoved"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksCurrentDsOffsetFromMaster"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksCurrentDsMeanPathDelay"))
)
if mibBuilder.loadTexts:
    me1200PtpStatusClocksCurrentDsTableInfoGroup.setStatus("current")

me1200PtpStatusClocksParentDsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 2, 2, 14)
)
me1200PtpStatusClocksParentDsTableInfoGroup.setObjects(
      *(("ME1200-PTP-MIB", "me1200PtpStatusClocksParentDsParentPortIdentityClockIdentity"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksParentDsParentPortIdentityPortNumber"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksParentDsParentStats"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksParentDsObservedParentOffsetScaledLogVar"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksParentDsObservedParentClockPhaseChangeRate"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksParentDsGrmstrIdentity"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksParentDsGrmstrClkQualClockClass"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksParentDsGmstrClkQualClockAccuracy"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksParentDsGmstrClkQualOffsetScaledLogVar"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksParentDsGmstrPriority1"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksParentDsGmstrPriority2"))
)
if mibBuilder.loadTexts:
    me1200PtpStatusClocksParentDsTableInfoGroup.setStatus("current")

me1200PtpStatusClocksTimePropertiesDsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 2, 2, 15)
)
me1200PtpStatusClocksTimePropertiesDsTableInfoGroup.setObjects(
      *(("ME1200-PTP-MIB", "me1200PtpStatusClocksTimePropertiesDsCurrentUtcOffset"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksTimePropertiesDsCurrentUtcOffsetValid"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksTimePropertiesDsLeap59"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksTimePropertiesDsLeap61"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksTimePropertiesDsTimeTraceable"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksTimePropertiesDsFrequencyTraceable"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksTimePropertiesDsPtpTimescale"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksTimePropertiesDsTimeSource"))
)
if mibBuilder.loadTexts:
    me1200PtpStatusClocksTimePropertiesDsTableInfoGroup.setStatus("current")

me1200PtpStatusClocksSlaveDsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 2, 2, 16)
)
me1200PtpStatusClocksSlaveDsTableInfoGroup.setObjects(
      *(("ME1200-PTP-MIB", "me1200PtpStatusClocksSlaveDsSlavePort"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksSlaveDsSlaveState"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksSlaveDsHoldoverStable"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksSlaveDsHoldoverAdj"))
)
if mibBuilder.loadTexts:
    me1200PtpStatusClocksSlaveDsTableInfoGroup.setStatus("current")

me1200PtpStatusClocksUnicastMasterTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 2, 2, 17)
)
me1200PtpStatusClocksUnicastMasterTableInfoGroup.setObjects(
      *(("ME1200-PTP-MIB", "me1200PtpStatusClocksUnicastMasterSlaveMac"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksUnicastMasterPort"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksUnicastMasterAnnLogMsgPeriod"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksUnicastMasterAnn"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksUnicastMasterLogMsgPeriod"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksUnicastMasterSync"))
)
if mibBuilder.loadTexts:
    me1200PtpStatusClocksUnicastMasterTableInfoGroup.setStatus("current")

me1200PtpStatusClocksUnicastSlaveTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 2, 2, 18)
)
me1200PtpStatusClocksUnicastSlaveTableInfoGroup.setObjects(
      *(("ME1200-PTP-MIB", "me1200PtpStatusClocksUnicastSlaveMasterIp"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksUnicastSlaveMasterMac"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksUnicastSlaveSourcePortIdentityClockIdentity"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksUnicastSlaveSourcePortIdentityPortNumber"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksUnicastSlavePort"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksUnicastSlaveLogMsgPeriod"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksUnicastSlaveCommState"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksUnicastSlaveConfMasterIp"))
)
if mibBuilder.loadTexts:
    me1200PtpStatusClocksUnicastSlaveTableInfoGroup.setStatus("current")

me1200PtpStatusClocksPortsDsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 2, 2, 19)
)
me1200PtpStatusClocksPortsDsTableInfoGroup.setObjects(
      *(("ME1200-PTP-MIB", "me1200PtpStatusClocksPortsDsPortState"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksPortsDsLogMinDelayReqInterval"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksPortsDsPeerMeanPathDelay"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksPortsDsPeerDelayOk"))
)
if mibBuilder.loadTexts:
    me1200PtpStatusClocksPortsDsTableInfoGroup.setStatus("current")

me1200PtpControlClocksTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 2, 2, 20)
)
me1200PtpControlClocksTableInfoGroup.setObjects(
    ("ME1200-PTP-MIB", "me1200PtpControlClocksSyncToSystemClock")
)
if mibBuilder.loadTexts:
    me1200PtpControlClocksTableInfoGroup.setStatus("current")


# Notification objects

me1200PtpNotifsPortStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 6, 1)
)
me1200PtpNotifsPortStateChange.setObjects(
      *(("ME1200-PTP-MIB", "me1200PtpStatusClocksPortsDsPortId"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksPortsDsPortState"))
)
if mibBuilder.loadTexts:
    me1200PtpNotifsPortStateChange.setStatus(
        "current"
    )

me1200PtpNotifsClockSlaveStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 6, 2)
)
me1200PtpNotifsClockSlaveStateChange.setObjects(
      *(("ME1200-PTP-MIB", "me1200PtpStatusClocksSlaveDsClockId"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksSlaveDsSlaveState"))
)
if mibBuilder.loadTexts:
    me1200PtpNotifsClockSlaveStateChange.setStatus(
        "current"
    )

me1200PtpNotifsUnicastCommunicationStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 6, 3)
)
me1200PtpNotifsUnicastCommunicationStateChange.setObjects(
    ("ME1200-PTP-MIB", "me1200PtpStatusClocksUnicastSlaveCommState")
)
if mibBuilder.loadTexts:
    me1200PtpNotifsUnicastCommunicationStateChange.setStatus(
        "current"
    )

me1200PtpNotifsUnicastSlaveAppears = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 6, 4)
)
me1200PtpNotifsUnicastSlaveAppears.setObjects(
    ("ME1200-PTP-MIB", "me1200PtpStatusClocksUnicastMasterSlaveIp")
)
if mibBuilder.loadTexts:
    me1200PtpNotifsUnicastSlaveAppears.setStatus(
        "current"
    )

me1200PtpNotifsUnicastSlaveDisappears = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 1, 6, 5)
)
me1200PtpNotifsUnicastSlaveDisappears.setObjects(
    ("ME1200-PTP-MIB", "me1200PtpStatusClocksUnicastMasterSlaveIp")
)
if mibBuilder.loadTexts:
    me1200PtpNotifsUnicastSlaveDisappears.setStatus(
        "current"
    )


# Notifications groups

me1200PtpNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 2, 2, 21)
)
me1200PtpNotifsGroup.setObjects(
      *(("ME1200-PTP-MIB", "me1200PtpNotifsPortStateChange"),
        ("ME1200-PTP-MIB", "me1200PtpNotifsClockSlaveStateChange"),
        ("ME1200-PTP-MIB", "me1200PtpNotifsUnicastCommunicationStateChange"),
        ("ME1200-PTP-MIB", "me1200PtpNotifsUnicastSlaveAppears"),
        ("ME1200-PTP-MIB", "me1200PtpNotifsUnicastSlaveDisappears"))
)
if mibBuilder.loadTexts:
    me1200PtpNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

me1200PtpMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 65, 2, 1, 1)
)
me1200PtpMibCompliance.setObjects(
      *(("ME1200-PTP-MIB", "me1200PtpCapabilitiesGlobalsInfoGroup"),
        ("ME1200-PTP-MIB", "me1200PtpConfigGlobalsExternalClockModeInfoGroup"),
        ("ME1200-PTP-MIB", "me1200PtpConfigGlobalsSystemTimeSyncModeInfoGroup"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsTableInfoGroup"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksDefaultDsTableRowEditorInfoGroup"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksTimePropertiesDsTableInfoGroup"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksFilterParametersTableInfoGroup"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksServoParametersTableInfoGroup"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksSlaveConfigTableInfoGroup"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksUnicastSlaveConfigTableInfoGroup"),
        ("ME1200-PTP-MIB", "me1200PtpConfigClocksPortDsTableInfoGroup"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksDefaultDsTableInfoGroup"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksCurrentDsTableInfoGroup"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksParentDsTableInfoGroup"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksTimePropertiesDsTableInfoGroup"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksSlaveDsTableInfoGroup"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksUnicastMasterTableInfoGroup"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksUnicastSlaveTableInfoGroup"),
        ("ME1200-PTP-MIB", "me1200PtpStatusClocksPortsDsTableInfoGroup"),
        ("ME1200-PTP-MIB", "me1200PtpControlClocksTableInfoGroup"),
        ("ME1200-PTP-MIB", "me1200PtpNotifsGroup"))
)
if mibBuilder.loadTexts:
    me1200PtpMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-PTP-MIB",
    **{"ME1200ptpClockPortState": ME1200ptpClockPortState,
       "ME1200ptpDestAdrType": ME1200ptpDestAdrType,
       "ME1200ptpDeviceType": ME1200ptpDeviceType,
       "ME1200ptpExtClock1pps": ME1200ptpExtClock1pps,
       "ME1200ptpPreferredAdj": ME1200ptpPreferredAdj,
       "ME1200ptpProfile": ME1200ptpProfile,
       "ME1200ptpProtocol": ME1200ptpProtocol,
       "ME1200ptpServoClockOption": ME1200ptpServoClockOption,
       "ME1200ptpSlaveClockState": ME1200ptpSlaveClockState,
       "ME1200ptpSystemTimeSyncMode": ME1200ptpSystemTimeSyncMode,
       "ME1200ptpUcCommState": ME1200ptpUcCommState,
       "me1200PtpMib": me1200PtpMib,
       "me1200PtpMibObjects": me1200PtpMibObjects,
       "me1200PtpCapabilities": me1200PtpCapabilities,
       "me1200PtpCapabilitiesGlobals": me1200PtpCapabilitiesGlobals,
       "me1200PtpCapabilitiesGlobalsClockCount": me1200PtpCapabilitiesGlobalsClockCount,
       "me1200PtpConfig": me1200PtpConfig,
       "me1200PtpConfigGlobals": me1200PtpConfigGlobals,
       "me1200PtpConfigGlobalsExternalClockMode": me1200PtpConfigGlobalsExternalClockMode,
       "me1200PtpConfigGlobalsExternalClockModeOnePpsMode": me1200PtpConfigGlobalsExternalClockModeOnePpsMode,
       "me1200PtpConfigGlobalsExternalClockModeExternalEnable": me1200PtpConfigGlobalsExternalClockModeExternalEnable,
       "me1200PtpConfigGlobalsExternalClockModeAdjustMethod": me1200PtpConfigGlobalsExternalClockModeAdjustMethod,
       "me1200PtpConfigGlobalsExternalClockModeClockFrequency": me1200PtpConfigGlobalsExternalClockModeClockFrequency,
       "me1200PtpConfigGlobalsSystemTimeSyncMode": me1200PtpConfigGlobalsSystemTimeSyncMode,
       "me1200PtpConfigGlobalsSystemTimeSyncModeMode": me1200PtpConfigGlobalsSystemTimeSyncModeMode,
       "me1200PtpConfigClocks": me1200PtpConfigClocks,
       "me1200PtpConfigClocksDefaultDsTable": me1200PtpConfigClocksDefaultDsTable,
       "me1200PtpConfigClocksDefaultDsEntry": me1200PtpConfigClocksDefaultDsEntry,
       "me1200PtpConfigClocksDefaultDsClockId": me1200PtpConfigClocksDefaultDsClockId,
       "me1200PtpConfigClocksDefaultDsDeviceType": me1200PtpConfigClocksDefaultDsDeviceType,
       "me1200PtpConfigClocksDefaultDsTwoStepFlag": me1200PtpConfigClocksDefaultDsTwoStepFlag,
       "me1200PtpConfigClocksDefaultDsPriority1": me1200PtpConfigClocksDefaultDsPriority1,
       "me1200PtpConfigClocksDefaultDsPriority2": me1200PtpConfigClocksDefaultDsPriority2,
       "me1200PtpConfigClocksDefaultDsOneWay": me1200PtpConfigClocksDefaultDsOneWay,
       "me1200PtpConfigClocksDefaultDsDomainNumber": me1200PtpConfigClocksDefaultDsDomainNumber,
       "me1200PtpConfigClocksDefaultDsProtocol": me1200PtpConfigClocksDefaultDsProtocol,
       "me1200PtpConfigClocksDefaultDsVlanTagEnable": me1200PtpConfigClocksDefaultDsVlanTagEnable,
       "me1200PtpConfigClocksDefaultDsVid": me1200PtpConfigClocksDefaultDsVid,
       "me1200PtpConfigClocksDefaultDsPcp": me1200PtpConfigClocksDefaultDsPcp,
       "me1200PtpConfigClocksDefaultDsMep": me1200PtpConfigClocksDefaultDsMep,
       "me1200PtpConfigClocksDefaultDsClkDom": me1200PtpConfigClocksDefaultDsClkDom,
       "me1200PtpConfigClocksDefaultDsDscp": me1200PtpConfigClocksDefaultDsDscp,
       "me1200PtpConfigClocksDefaultDsProfile": me1200PtpConfigClocksDefaultDsProfile,
       "me1200PtpConfigClocksDefaultDsLocalPriority": me1200PtpConfigClocksDefaultDsLocalPriority,
       "me1200PtpConfigClocksDefaultDsAction": me1200PtpConfigClocksDefaultDsAction,
       "me1200PtpConfigClocksDefaultDsTableRowEditor": me1200PtpConfigClocksDefaultDsTableRowEditor,
       "me1200PtpConfigClocksDefaultDsTableRowEditorClockId": me1200PtpConfigClocksDefaultDsTableRowEditorClockId,
       "me1200PtpConfigClocksDefaultDsTableRowEditorDeviceType": me1200PtpConfigClocksDefaultDsTableRowEditorDeviceType,
       "me1200PtpConfigClocksDefaultDsTableRowEditorTwoStepFlag": me1200PtpConfigClocksDefaultDsTableRowEditorTwoStepFlag,
       "me1200PtpConfigClocksDefaultDsTableRowEditorPriority1": me1200PtpConfigClocksDefaultDsTableRowEditorPriority1,
       "me1200PtpConfigClocksDefaultDsTableRowEditorPriority2": me1200PtpConfigClocksDefaultDsTableRowEditorPriority2,
       "me1200PtpConfigClocksDefaultDsTableRowEditorOneWay": me1200PtpConfigClocksDefaultDsTableRowEditorOneWay,
       "me1200PtpConfigClocksDefaultDsTableRowEditorDomainNumber": me1200PtpConfigClocksDefaultDsTableRowEditorDomainNumber,
       "me1200PtpConfigClocksDefaultDsTableRowEditorProtocol": me1200PtpConfigClocksDefaultDsTableRowEditorProtocol,
       "me1200PtpConfigClocksDefaultDsTableRowEditorVlanTagEnable": me1200PtpConfigClocksDefaultDsTableRowEditorVlanTagEnable,
       "me1200PtpConfigClocksDefaultDsTableRowEditorVid": me1200PtpConfigClocksDefaultDsTableRowEditorVid,
       "me1200PtpConfigClocksDefaultDsTableRowEditorPcp": me1200PtpConfigClocksDefaultDsTableRowEditorPcp,
       "me1200PtpConfigClocksDefaultDsTableRowEditorMep": me1200PtpConfigClocksDefaultDsTableRowEditorMep,
       "me1200PtpConfigClocksDefaultDsTableRowEditorClkDom": me1200PtpConfigClocksDefaultDsTableRowEditorClkDom,
       "me1200PtpConfigClocksDefaultDsTableRowEditorDscp": me1200PtpConfigClocksDefaultDsTableRowEditorDscp,
       "me1200PtpConfigClocksDefaultDsTableRowEditorProfile": me1200PtpConfigClocksDefaultDsTableRowEditorProfile,
       "me1200PtpConfigClocksDefaultDsTableRowEditorLocalPriority": me1200PtpConfigClocksDefaultDsTableRowEditorLocalPriority,
       "me1200PtpConfigClocksDefaultDsTableRowEditorAction": me1200PtpConfigClocksDefaultDsTableRowEditorAction,
       "me1200PtpConfigClocksTimePropertiesDsTable": me1200PtpConfigClocksTimePropertiesDsTable,
       "me1200PtpConfigClocksTimePropertiesDsEntry": me1200PtpConfigClocksTimePropertiesDsEntry,
       "me1200PtpConfigClocksTimePropertiesDsClockId": me1200PtpConfigClocksTimePropertiesDsClockId,
       "me1200PtpConfigClocksTimePropertiesDsCurrentUtcOffset": me1200PtpConfigClocksTimePropertiesDsCurrentUtcOffset,
       "me1200PtpConfigClocksTimePropertiesDsCurrentUtcOffsetValid": me1200PtpConfigClocksTimePropertiesDsCurrentUtcOffsetValid,
       "me1200PtpConfigClocksTimePropertiesDsLeap59": me1200PtpConfigClocksTimePropertiesDsLeap59,
       "me1200PtpConfigClocksTimePropertiesDsLeap61": me1200PtpConfigClocksTimePropertiesDsLeap61,
       "me1200PtpConfigClocksTimePropertiesDsTimeTraceable": me1200PtpConfigClocksTimePropertiesDsTimeTraceable,
       "me1200PtpConfigClocksTimePropertiesDsFrequencyTraceable": me1200PtpConfigClocksTimePropertiesDsFrequencyTraceable,
       "me1200PtpConfigClocksTimePropertiesDsPtpTimescale": me1200PtpConfigClocksTimePropertiesDsPtpTimescale,
       "me1200PtpConfigClocksTimePropertiesDsTimeSource": me1200PtpConfigClocksTimePropertiesDsTimeSource,
       "me1200PtpConfigClocksFilterParametersTable": me1200PtpConfigClocksFilterParametersTable,
       "me1200PtpConfigClocksFilterParametersEntry": me1200PtpConfigClocksFilterParametersEntry,
       "me1200PtpConfigClocksFilterParametersClockId": me1200PtpConfigClocksFilterParametersClockId,
       "me1200PtpConfigClocksFilterParametersDelayFilter": me1200PtpConfigClocksFilterParametersDelayFilter,
       "me1200PtpConfigClocksFilterParametersFilterType": me1200PtpConfigClocksFilterParametersFilterType,
       "me1200PtpConfigClocksFilterParametersPeriod": me1200PtpConfigClocksFilterParametersPeriod,
       "me1200PtpConfigClocksFilterParametersDist": me1200PtpConfigClocksFilterParametersDist,
       "me1200PtpConfigClocksServoParametersTable": me1200PtpConfigClocksServoParametersTable,
       "me1200PtpConfigClocksServoParametersEntry": me1200PtpConfigClocksServoParametersEntry,
       "me1200PtpConfigClocksServoParametersClockId": me1200PtpConfigClocksServoParametersClockId,
       "me1200PtpConfigClocksServoParametersDisplay": me1200PtpConfigClocksServoParametersDisplay,
       "me1200PtpConfigClocksServoParametersPEnable": me1200PtpConfigClocksServoParametersPEnable,
       "me1200PtpConfigClocksServoParametersIEnable": me1200PtpConfigClocksServoParametersIEnable,
       "me1200PtpConfigClocksServoParametersDEnable": me1200PtpConfigClocksServoParametersDEnable,
       "me1200PtpConfigClocksServoParametersPval": me1200PtpConfigClocksServoParametersPval,
       "me1200PtpConfigClocksServoParametersIval": me1200PtpConfigClocksServoParametersIval,
       "me1200PtpConfigClocksServoParametersDval": me1200PtpConfigClocksServoParametersDval,
       "me1200PtpConfigClocksServoParametersSrvOption": me1200PtpConfigClocksServoParametersSrvOption,
       "me1200PtpConfigClocksServoParametersSynceThreshold": me1200PtpConfigClocksServoParametersSynceThreshold,
       "me1200PtpConfigClocksServoParametersSynceAp": me1200PtpConfigClocksServoParametersSynceAp,
       "me1200PtpConfigClocksServoParametersHoFilter": me1200PtpConfigClocksServoParametersHoFilter,
       "me1200PtpConfigClocksServoParametersStableAdjThreshold": me1200PtpConfigClocksServoParametersStableAdjThreshold,
       "me1200PtpConfigClocksSlaveConfigTable": me1200PtpConfigClocksSlaveConfigTable,
       "me1200PtpConfigClocksSlaveConfigEntry": me1200PtpConfigClocksSlaveConfigEntry,
       "me1200PtpConfigClocksSlaveConfigClockId": me1200PtpConfigClocksSlaveConfigClockId,
       "me1200PtpConfigClocksSlaveConfigStableOffset": me1200PtpConfigClocksSlaveConfigStableOffset,
       "me1200PtpConfigClocksSlaveConfigOffsetOk": me1200PtpConfigClocksSlaveConfigOffsetOk,
       "me1200PtpConfigClocksSlaveConfigOffsetFail": me1200PtpConfigClocksSlaveConfigOffsetFail,
       "me1200PtpConfigClocksUnicastSlaveConfigTable": me1200PtpConfigClocksUnicastSlaveConfigTable,
       "me1200PtpConfigClocksUnicastSlaveConfigEntry": me1200PtpConfigClocksUnicastSlaveConfigEntry,
       "me1200PtpConfigClocksUnicastSlaveConfigClockId": me1200PtpConfigClocksUnicastSlaveConfigClockId,
       "me1200PtpConfigClocksUnicastSlaveConfigMasterId": me1200PtpConfigClocksUnicastSlaveConfigMasterId,
       "me1200PtpConfigClocksUnicastSlaveConfigDuration": me1200PtpConfigClocksUnicastSlaveConfigDuration,
       "me1200PtpConfigClocksUnicastSlaveConfigIpAddress": me1200PtpConfigClocksUnicastSlaveConfigIpAddress,
       "me1200PtpConfigClocksPortDsTable": me1200PtpConfigClocksPortDsTable,
       "me1200PtpConfigClocksPortDsEntry": me1200PtpConfigClocksPortDsEntry,
       "me1200PtpConfigClocksPortDsClockId": me1200PtpConfigClocksPortDsClockId,
       "me1200PtpConfigClocksPortDsPortId": me1200PtpConfigClocksPortDsPortId,
       "me1200PtpConfigClocksPortDsEnabled": me1200PtpConfigClocksPortDsEnabled,
       "me1200PtpConfigClocksPortDsLogAnnounceInterval": me1200PtpConfigClocksPortDsLogAnnounceInterval,
       "me1200PtpConfigClocksPortDsAnnounceReceiptTimeout": me1200PtpConfigClocksPortDsAnnounceReceiptTimeout,
       "me1200PtpConfigClocksPortDsLogSyncInterval": me1200PtpConfigClocksPortDsLogSyncInterval,
       "me1200PtpConfigClocksPortDsDelayMechanism": me1200PtpConfigClocksPortDsDelayMechanism,
       "me1200PtpConfigClocksPortDsLogMinPdelayReqInterval": me1200PtpConfigClocksPortDsLogMinPdelayReqInterval,
       "me1200PtpConfigClocksPortDsDelayAsymmetry": me1200PtpConfigClocksPortDsDelayAsymmetry,
       "me1200PtpConfigClocksPortDsIngressLatency": me1200PtpConfigClocksPortDsIngressLatency,
       "me1200PtpConfigClocksPortDsEgressLatency": me1200PtpConfigClocksPortDsEgressLatency,
       "me1200PtpConfigClocksPortDsPortInternal": me1200PtpConfigClocksPortDsPortInternal,
       "me1200PtpConfigClocksPortDsVersionNumber": me1200PtpConfigClocksPortDsVersionNumber,
       "me1200PtpConfigClocksPortDsMcastAddr": me1200PtpConfigClocksPortDsMcastAddr,
       "me1200PtpConfigClocksPortDsNotSlave": me1200PtpConfigClocksPortDsNotSlave,
       "me1200PtpConfigClocksPortDsLocalPriority": me1200PtpConfigClocksPortDsLocalPriority,
       "me1200PtpStatus": me1200PtpStatus,
       "me1200PtpStatusClocks": me1200PtpStatusClocks,
       "me1200PtpStatusClocksDefaultDsTable": me1200PtpStatusClocksDefaultDsTable,
       "me1200PtpStatusClocksDefaultDsEntry": me1200PtpStatusClocksDefaultDsEntry,
       "me1200PtpStatusClocksDefaultDsClockId": me1200PtpStatusClocksDefaultDsClockId,
       "me1200PtpStatusClocksDefaultDsClockIdentity": me1200PtpStatusClocksDefaultDsClockIdentity,
       "me1200PtpStatusClocksDefaultDsClockQualityClockClass": me1200PtpStatusClocksDefaultDsClockQualityClockClass,
       "me1200PtpStatusClocksDefaultDsClockQualityClockAccuracy": me1200PtpStatusClocksDefaultDsClockQualityClockAccuracy,
       "me1200PtpStatusClocksDefaultDsClockQualityOffsetScaledLogVar": me1200PtpStatusClocksDefaultDsClockQualityOffsetScaledLogVar,
       "me1200PtpStatusClocksCurrentDsTable": me1200PtpStatusClocksCurrentDsTable,
       "me1200PtpStatusClocksCurrentDsEntry": me1200PtpStatusClocksCurrentDsEntry,
       "me1200PtpStatusClocksCurrentDsClockId": me1200PtpStatusClocksCurrentDsClockId,
       "me1200PtpStatusClocksCurrentDsStepsRemoved": me1200PtpStatusClocksCurrentDsStepsRemoved,
       "me1200PtpStatusClocksCurrentDsOffsetFromMaster": me1200PtpStatusClocksCurrentDsOffsetFromMaster,
       "me1200PtpStatusClocksCurrentDsMeanPathDelay": me1200PtpStatusClocksCurrentDsMeanPathDelay,
       "me1200PtpStatusClocksParentDsTable": me1200PtpStatusClocksParentDsTable,
       "me1200PtpStatusClocksParentDsEntry": me1200PtpStatusClocksParentDsEntry,
       "me1200PtpStatusClocksParentDsClockId": me1200PtpStatusClocksParentDsClockId,
       "me1200PtpStatusClocksParentDsParentPortIdentityClockIdentity": me1200PtpStatusClocksParentDsParentPortIdentityClockIdentity,
       "me1200PtpStatusClocksParentDsParentPortIdentityPortNumber": me1200PtpStatusClocksParentDsParentPortIdentityPortNumber,
       "me1200PtpStatusClocksParentDsParentStats": me1200PtpStatusClocksParentDsParentStats,
       "me1200PtpStatusClocksParentDsObservedParentOffsetScaledLogVar": me1200PtpStatusClocksParentDsObservedParentOffsetScaledLogVar,
       "me1200PtpStatusClocksParentDsObservedParentClockPhaseChangeRate": me1200PtpStatusClocksParentDsObservedParentClockPhaseChangeRate,
       "me1200PtpStatusClocksParentDsGrmstrIdentity": me1200PtpStatusClocksParentDsGrmstrIdentity,
       "me1200PtpStatusClocksParentDsGrmstrClkQualClockClass": me1200PtpStatusClocksParentDsGrmstrClkQualClockClass,
       "me1200PtpStatusClocksParentDsGmstrClkQualClockAccuracy": me1200PtpStatusClocksParentDsGmstrClkQualClockAccuracy,
       "me1200PtpStatusClocksParentDsGmstrClkQualOffsetScaledLogVar": me1200PtpStatusClocksParentDsGmstrClkQualOffsetScaledLogVar,
       "me1200PtpStatusClocksParentDsGmstrPriority1": me1200PtpStatusClocksParentDsGmstrPriority1,
       "me1200PtpStatusClocksParentDsGmstrPriority2": me1200PtpStatusClocksParentDsGmstrPriority2,
       "me1200PtpStatusClocksTimePropertiesDsTable": me1200PtpStatusClocksTimePropertiesDsTable,
       "me1200PtpStatusClocksTimePropertiesDsEntry": me1200PtpStatusClocksTimePropertiesDsEntry,
       "me1200PtpStatusClocksTimePropertiesDsClockId": me1200PtpStatusClocksTimePropertiesDsClockId,
       "me1200PtpStatusClocksTimePropertiesDsCurrentUtcOffset": me1200PtpStatusClocksTimePropertiesDsCurrentUtcOffset,
       "me1200PtpStatusClocksTimePropertiesDsCurrentUtcOffsetValid": me1200PtpStatusClocksTimePropertiesDsCurrentUtcOffsetValid,
       "me1200PtpStatusClocksTimePropertiesDsLeap59": me1200PtpStatusClocksTimePropertiesDsLeap59,
       "me1200PtpStatusClocksTimePropertiesDsLeap61": me1200PtpStatusClocksTimePropertiesDsLeap61,
       "me1200PtpStatusClocksTimePropertiesDsTimeTraceable": me1200PtpStatusClocksTimePropertiesDsTimeTraceable,
       "me1200PtpStatusClocksTimePropertiesDsFrequencyTraceable": me1200PtpStatusClocksTimePropertiesDsFrequencyTraceable,
       "me1200PtpStatusClocksTimePropertiesDsPtpTimescale": me1200PtpStatusClocksTimePropertiesDsPtpTimescale,
       "me1200PtpStatusClocksTimePropertiesDsTimeSource": me1200PtpStatusClocksTimePropertiesDsTimeSource,
       "me1200PtpStatusClocksSlaveDsTable": me1200PtpStatusClocksSlaveDsTable,
       "me1200PtpStatusClocksSlaveDsEntry": me1200PtpStatusClocksSlaveDsEntry,
       "me1200PtpStatusClocksSlaveDsClockId": me1200PtpStatusClocksSlaveDsClockId,
       "me1200PtpStatusClocksSlaveDsSlavePort": me1200PtpStatusClocksSlaveDsSlavePort,
       "me1200PtpStatusClocksSlaveDsSlaveState": me1200PtpStatusClocksSlaveDsSlaveState,
       "me1200PtpStatusClocksSlaveDsHoldoverStable": me1200PtpStatusClocksSlaveDsHoldoverStable,
       "me1200PtpStatusClocksSlaveDsHoldoverAdj": me1200PtpStatusClocksSlaveDsHoldoverAdj,
       "me1200PtpStatusClocksUnicastMasterTable": me1200PtpStatusClocksUnicastMasterTable,
       "me1200PtpStatusClocksUnicastMasterEntry": me1200PtpStatusClocksUnicastMasterEntry,
       "me1200PtpStatusClocksUnicastMasterClockId": me1200PtpStatusClocksUnicastMasterClockId,
       "me1200PtpStatusClocksUnicastMasterSlaveIp": me1200PtpStatusClocksUnicastMasterSlaveIp,
       "me1200PtpStatusClocksUnicastMasterSlaveMac": me1200PtpStatusClocksUnicastMasterSlaveMac,
       "me1200PtpStatusClocksUnicastMasterPort": me1200PtpStatusClocksUnicastMasterPort,
       "me1200PtpStatusClocksUnicastMasterAnnLogMsgPeriod": me1200PtpStatusClocksUnicastMasterAnnLogMsgPeriod,
       "me1200PtpStatusClocksUnicastMasterAnn": me1200PtpStatusClocksUnicastMasterAnn,
       "me1200PtpStatusClocksUnicastMasterLogMsgPeriod": me1200PtpStatusClocksUnicastMasterLogMsgPeriod,
       "me1200PtpStatusClocksUnicastMasterSync": me1200PtpStatusClocksUnicastMasterSync,
       "me1200PtpStatusClocksUnicastSlaveTable": me1200PtpStatusClocksUnicastSlaveTable,
       "me1200PtpStatusClocksUnicastSlaveEntry": me1200PtpStatusClocksUnicastSlaveEntry,
       "me1200PtpStatusClocksUnicastSlaveClockId": me1200PtpStatusClocksUnicastSlaveClockId,
       "me1200PtpStatusClocksUnicastSlaveMasterId": me1200PtpStatusClocksUnicastSlaveMasterId,
       "me1200PtpStatusClocksUnicastSlaveMasterIp": me1200PtpStatusClocksUnicastSlaveMasterIp,
       "me1200PtpStatusClocksUnicastSlaveMasterMac": me1200PtpStatusClocksUnicastSlaveMasterMac,
       "me1200PtpStatusClocksUnicastSlaveSourcePortIdentityClockIdentity": me1200PtpStatusClocksUnicastSlaveSourcePortIdentityClockIdentity,
       "me1200PtpStatusClocksUnicastSlaveSourcePortIdentityPortNumber": me1200PtpStatusClocksUnicastSlaveSourcePortIdentityPortNumber,
       "me1200PtpStatusClocksUnicastSlavePort": me1200PtpStatusClocksUnicastSlavePort,
       "me1200PtpStatusClocksUnicastSlaveLogMsgPeriod": me1200PtpStatusClocksUnicastSlaveLogMsgPeriod,
       "me1200PtpStatusClocksUnicastSlaveCommState": me1200PtpStatusClocksUnicastSlaveCommState,
       "me1200PtpStatusClocksUnicastSlaveConfMasterIp": me1200PtpStatusClocksUnicastSlaveConfMasterIp,
       "me1200PtpStatusClocksPortsDsTable": me1200PtpStatusClocksPortsDsTable,
       "me1200PtpStatusClocksPortsDsEntry": me1200PtpStatusClocksPortsDsEntry,
       "me1200PtpStatusClocksPortsDsClockId": me1200PtpStatusClocksPortsDsClockId,
       "me1200PtpStatusClocksPortsDsPortId": me1200PtpStatusClocksPortsDsPortId,
       "me1200PtpStatusClocksPortsDsPortState": me1200PtpStatusClocksPortsDsPortState,
       "me1200PtpStatusClocksPortsDsLogMinDelayReqInterval": me1200PtpStatusClocksPortsDsLogMinDelayReqInterval,
       "me1200PtpStatusClocksPortsDsPeerMeanPathDelay": me1200PtpStatusClocksPortsDsPeerMeanPathDelay,
       "me1200PtpStatusClocksPortsDsPeerDelayOk": me1200PtpStatusClocksPortsDsPeerDelayOk,
       "me1200PtpControl": me1200PtpControl,
       "me1200PtpControlClocksTable": me1200PtpControlClocksTable,
       "me1200PtpControlClocksEntry": me1200PtpControlClocksEntry,
       "me1200PtpControlClocksClockId": me1200PtpControlClocksClockId,
       "me1200PtpControlClocksSyncToSystemClock": me1200PtpControlClocksSyncToSystemClock,
       "me1200PtpStatistics": me1200PtpStatistics,
       "me1200PtpNotifs": me1200PtpNotifs,
       "me1200PtpNotifsPortStateChange": me1200PtpNotifsPortStateChange,
       "me1200PtpNotifsClockSlaveStateChange": me1200PtpNotifsClockSlaveStateChange,
       "me1200PtpNotifsUnicastCommunicationStateChange": me1200PtpNotifsUnicastCommunicationStateChange,
       "me1200PtpNotifsUnicastSlaveAppears": me1200PtpNotifsUnicastSlaveAppears,
       "me1200PtpNotifsUnicastSlaveDisappears": me1200PtpNotifsUnicastSlaveDisappears,
       "me1200PtpMibConformance": me1200PtpMibConformance,
       "me1200PtpMibCompliances": me1200PtpMibCompliances,
       "me1200PtpMibCompliance": me1200PtpMibCompliance,
       "me1200PtpMibGroups": me1200PtpMibGroups,
       "me1200PtpCapabilitiesGlobalsInfoGroup": me1200PtpCapabilitiesGlobalsInfoGroup,
       "me1200PtpConfigGlobalsExternalClockModeInfoGroup": me1200PtpConfigGlobalsExternalClockModeInfoGroup,
       "me1200PtpConfigGlobalsSystemTimeSyncModeInfoGroup": me1200PtpConfigGlobalsSystemTimeSyncModeInfoGroup,
       "me1200PtpConfigClocksDefaultDsTableInfoGroup": me1200PtpConfigClocksDefaultDsTableInfoGroup,
       "me1200PtpConfigClocksDefaultDsTableRowEditorInfoGroup": me1200PtpConfigClocksDefaultDsTableRowEditorInfoGroup,
       "me1200PtpConfigClocksTimePropertiesDsTableInfoGroup": me1200PtpConfigClocksTimePropertiesDsTableInfoGroup,
       "me1200PtpConfigClocksFilterParametersTableInfoGroup": me1200PtpConfigClocksFilterParametersTableInfoGroup,
       "me1200PtpConfigClocksServoParametersTableInfoGroup": me1200PtpConfigClocksServoParametersTableInfoGroup,
       "me1200PtpConfigClocksSlaveConfigTableInfoGroup": me1200PtpConfigClocksSlaveConfigTableInfoGroup,
       "me1200PtpConfigClocksUnicastSlaveConfigTableInfoGroup": me1200PtpConfigClocksUnicastSlaveConfigTableInfoGroup,
       "me1200PtpConfigClocksPortDsTableInfoGroup": me1200PtpConfigClocksPortDsTableInfoGroup,
       "me1200PtpStatusClocksDefaultDsTableInfoGroup": me1200PtpStatusClocksDefaultDsTableInfoGroup,
       "me1200PtpStatusClocksCurrentDsTableInfoGroup": me1200PtpStatusClocksCurrentDsTableInfoGroup,
       "me1200PtpStatusClocksParentDsTableInfoGroup": me1200PtpStatusClocksParentDsTableInfoGroup,
       "me1200PtpStatusClocksTimePropertiesDsTableInfoGroup": me1200PtpStatusClocksTimePropertiesDsTableInfoGroup,
       "me1200PtpStatusClocksSlaveDsTableInfoGroup": me1200PtpStatusClocksSlaveDsTableInfoGroup,
       "me1200PtpStatusClocksUnicastMasterTableInfoGroup": me1200PtpStatusClocksUnicastMasterTableInfoGroup,
       "me1200PtpStatusClocksUnicastSlaveTableInfoGroup": me1200PtpStatusClocksUnicastSlaveTableInfoGroup,
       "me1200PtpStatusClocksPortsDsTableInfoGroup": me1200PtpStatusClocksPortsDsTableInfoGroup,
       "me1200PtpControlClocksTableInfoGroup": me1200PtpControlClocksTableInfoGroup,
       "me1200PtpNotifsGroup": me1200PtpNotifsGroup}
)
