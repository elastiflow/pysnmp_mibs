# SNMP MIB module (CIENA-MIBv2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_1271/CIENA-MIBv2.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:39:47 2025
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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



class MwSeverityLevel(Integer32):
    """Custom type MwSeverityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2048,
              2050,
              2052,
              2053,
              2054,
              2055,
              2056)
        )
    )
    namedValues = NamedValues(
        *(("mwNormal", 2048),
          ("mwInhibited", 2050),
          ("mwInformational", 2052),
          ("mwWarning", 2053),
          ("mwMinor", 2054),
          ("mwMajor", 2055),
          ("mwCritical", 2056))
    )





class MwAttributeId(Integer32):
    """Custom type MwAttributeId based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              256,
              257,
              258,
              259,
              260,
              261,
              262,
              263,
              264,
              265,
              266,
              267,
              268,
              269,
              270,
              271,
              512,
              513,
              514,
              515,
              516,
              517,
              518,
              519,
              520,
              521,
              522,
              523,
              524,
              525,
              768,
              769,
              770,
              771,
              772,
              1024,
              1025,
              1026,
              1027,
              1028,
              1280,
              1281,
              1282,
              1283,
              1536,
              1537,
              1538,
              1539,
              1792,
              1793,
              1794,
              1795,
              1796,
              1797,
              1798,
              1799,
              1800,
              1801,
              1802,
              1803,
              1804,
              2048,
              2050,
              2052,
              2053,
              2054,
              2055,
              2056,
              1000000)
        )
    )
    namedValues = NamedValues(
        *(("moduleState", 1),
          ("moduleStatus", 2),
          ("measurementInterval", 3),
          ("reportingInterval", 4),
          ("moduleConfig", 5),
          ("resetModule", 6),
          ("moduleQuiesce", 7),
          ("modulePartId", 8),
          ("modulePartNumber", 9),
          ("moduleSerialId", 10),
          ("moduleRevisionId", 11),
          ("moduleSoftwareImage", 12),
          ("moduleMaintenanceMode", 13),
          ("moduleResetAccum", 14),
          ("moduleType", 15),
          ("moduleSlotsLeft", 16),
          ("moduleSlotsRight", 17),
          ("led0Sp", 256),
          ("led1Sp", 257),
          ("led2Sp", 258),
          ("led3Sp", 259),
          ("led4Sp", 260),
          ("led5Sp", 261),
          ("led6Sp", 262),
          ("led7Sp", 263),
          ("led0Mp", 264),
          ("led1Mp", 265),
          ("led2Mp", 266),
          ("led3Mp", 267),
          ("led4Mp", 268),
          ("led5Mp", 269),
          ("led6Mp", 270),
          ("led7Mp", 271),
          ("precisionLaserPower", 512),
          ("precisionLaserTemp", 513),
          ("precisionLaserCurrent", 514),
          ("precisionLaserTECCurrent", 515),
          ("precisionLaserHeatSinkTemp", 516),
          ("precisionLaserOpMode", 517),
          ("precisionLaserCurrentLimit", 518),
          ("precisionLaserSpPower", 519),
          ("precisionLaserSpCurrent", 520),
          ("precisionLaserSpTemp", 521),
          ("precisionLaserSpInterlock", 522),
          ("precisionLaserState", 523),
          ("precisionLaserWavelength", 524),
          ("precisionLaserSpConfigState", 525),
          ("remodGratingTemp", 768),
          ("remodInputSignal", 769),
          ("remodOutputSignal", 770),
          ("remodDitherEnable", 771),
          ("remodFrequencyTrack", 772),
          ("selectorFrequencyA", 1024),
          ("selectorFrequencyB", 1025),
          ("selectorGratingTemp", 1026),
          ("selectorSigLevelA", 1027),
          ("selectorSigLevelB", 1028),
          ("fiberAmpTopInput", 1280),
          ("fiberAmpBottomInput", 1281),
          ("fiberAmpTopOutput", 1282),
          ("fiberAmpBottomOutput", 1283),
          ("powerSource1Fail", 1536),
          ("powerSource2Fail", 1537),
          ("powerSummaryFail", 1538),
          ("powerBackplaneTemp", 1539),
          ("ncpSoftware", 1792),
          ("ncpEms", 1793),
          ("ncpTftpHost", 1794),
          ("ncpNodeName", 1795),
          ("ncpNodeIpAddress", 1796),
          ("ncpSpOkLed", 1797),
          ("ncpSpMajorLed", 1798),
          ("ncpSpMinorLed", 1799),
          ("ncpSpMaintLed", 1800),
          ("ncpMpOkLed", 1801),
          ("ncpMpMajorLed", 1802),
          ("ncpMpMinorLed", 1803),
          ("ncpMpMaintLed", 1804),
          ("alarmNormal", 2048),
          ("alarmInhibited", 2050),
          ("alarmInformational", 2052),
          ("alarmWarning", 2053),
          ("alarmMinor", 2054),
          ("alarmMajor", 2055),
          ("alarmCritical", 2056),
          ("attributeUndefined", 1000000))
    )





class MwMonitorPointId(Integer32):
    """Custom type MwMonitorPointId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(512,
              513,
              514,
              515,
              516,
              768,
              769,
              770,
              1026,
              1027,
              1028,
              1029,
              1280,
              1281,
              1282,
              1283,
              2568,
              3840,
              3841,
              3842,
              3843,
              4100,
              4101,
              4102,
              4103,
              4354,
              4355,
              4356,
              4357,
              4358,
              4359,
              4360,
              4361,
              4370,
              4371)
        )
    )
    namedValues = NamedValues(
        *(("precisionLaserPower", 512),
          ("precisionLaserTemp", 513),
          ("precisionLaserCurrent", 514),
          ("precisionLaserTECCurrent", 515),
          ("precisionLaserHeatSinkTemp", 516),
          ("remodGratingTemperature", 768),
          ("remodInputSignal", 769),
          ("remodOutputSignal", 770),
          ("selectorGratingTempA", 1026),
          ("selectorSignalLevelA", 1027),
          ("selectorSignalLevelB", 1028),
          ("selectorGratingTempB", 1029),
          ("fiberAmpTopInput", 1280),
          ("fiberAmpBottomInput", 1281),
          ("fiberAmpTopOutput", 1282),
          ("fiberAmpBottomOutput", 1283),
          ("scmInputSignal", 2568),
          ("scimTopInput", 3840),
          ("scimBottomInput", 3841),
          ("scimTopOutput", 3842),
          ("scimBottomOutput", 3843),
          ("adm1Heater", 4100),
          ("adm2Heater", 4101),
          ("adm3Heater", 4102),
          ("adm4Heater", 4103),
          ("admaTopAdmInput", 4354),
          ("admaBottomAdmInput", 4355),
          ("admaTopCombinerInput", 4356),
          ("admaBottomCombinerInput", 4357),
          ("admaTopInput", 4358),
          ("admaBottomInput", 4359),
          ("admaBottomOutput", 4360),
          ("admaTopOutput", 4361),
          ("admaTopPreampOutput", 4370),
          ("admaBottomPreampOutput", 4371))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ciena_ObjectIdentity = ObjectIdentity
ciena = _Ciena_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271)
)
_MultiwaveMgmt_ObjectIdentity = ObjectIdentity
multiwaveMgmt = _MultiwaveMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1, 1)
)
_NcpModuleInfo_ObjectIdentity = ObjectIdentity
ncpModuleInfo = _NcpModuleInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1, 1, 1)
)


class _NodeType_Type(Integer32):
    """Custom type nodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("terminal", 1),
          ("opticalLineAmplifer", 2))
    )


_NodeType_Type.__name__ = "Integer32"
_NodeType_Object = MibScalar
nodeType = _NodeType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 1, 1, 4),
    _NodeType_Type()
)
nodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeType.setStatus("mandatory")
_NodeName_Type = DisplayString
_NodeName_Object = MibScalar
nodeName = _NodeName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 1, 1, 5),
    _NodeName_Type()
)
nodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeName.setStatus("mandatory")


class _NodeOKLED_Type(Integer32):
    """Custom type nodeOKLED based on Integer32"""
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


_NodeOKLED_Type.__name__ = "Integer32"
_NodeOKLED_Object = MibScalar
nodeOKLED = _NodeOKLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 1, 1, 10),
    _NodeOKLED_Type()
)
nodeOKLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeOKLED.setStatus("mandatory")


class _NodeMajorLED_Type(Integer32):
    """Custom type nodeMajorLED based on Integer32"""
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


_NodeMajorLED_Type.__name__ = "Integer32"
_NodeMajorLED_Object = MibScalar
nodeMajorLED = _NodeMajorLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 1, 1, 11),
    _NodeMajorLED_Type()
)
nodeMajorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeMajorLED.setStatus("mandatory")


class _NodeMinorLED_Type(Integer32):
    """Custom type nodeMinorLED based on Integer32"""
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


_NodeMinorLED_Type.__name__ = "Integer32"
_NodeMinorLED_Object = MibScalar
nodeMinorLED = _NodeMinorLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 1, 1, 12),
    _NodeMinorLED_Type()
)
nodeMinorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeMinorLED.setStatus("mandatory")


class _NodeMaintenanceLED_Type(Integer32):
    """Custom type nodeMaintenanceLED based on Integer32"""
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


_NodeMaintenanceLED_Type.__name__ = "Integer32"
_NodeMaintenanceLED_Object = MibScalar
nodeMaintenanceLED = _NodeMaintenanceLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 1, 1, 13),
    _NodeMaintenanceLED_Type()
)
nodeMaintenanceLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeMaintenanceLED.setStatus("mandatory")


class _NCPOkLED_Type(Integer32):
    """Custom type nCPOkLED based on Integer32"""
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


_NCPOkLED_Type.__name__ = "Integer32"
_NCPOkLED_Object = MibScalar
nCPOkLED = _NCPOkLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 1, 1, 18),
    _NCPOkLED_Type()
)
nCPOkLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nCPOkLED.setStatus("mandatory")


class _NcpMajorLED_Type(Integer32):
    """Custom type ncpMajorLED based on Integer32"""
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


_NcpMajorLED_Type.__name__ = "Integer32"
_NcpMajorLED_Object = MibScalar
ncpMajorLED = _NcpMajorLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 1, 1, 19),
    _NcpMajorLED_Type()
)
ncpMajorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncpMajorLED.setStatus("mandatory")


class _NcpMinorLED_Type(Integer32):
    """Custom type ncpMinorLED based on Integer32"""
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


_NcpMinorLED_Type.__name__ = "Integer32"
_NcpMinorLED_Object = MibScalar
ncpMinorLED = _NcpMinorLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 1, 1, 20),
    _NcpMinorLED_Type()
)
ncpMinorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncpMinorLED.setStatus("mandatory")


class _NcpMaintenanceLED_Type(Integer32):
    """Custom type ncpMaintenanceLED based on Integer32"""
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


_NcpMaintenanceLED_Type.__name__ = "Integer32"
_NcpMaintenanceLED_Object = MibScalar
ncpMaintenanceLED = _NcpMaintenanceLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 1, 1, 21),
    _NcpMaintenanceLED_Type()
)
ncpMaintenanceLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncpMaintenanceLED.setStatus("mandatory")
_NcpTime_Type = Integer32
_NcpTime_Object = MibScalar
ncpTime = _NcpTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 1, 1, 22),
    _NcpTime_Type()
)
ncpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncpTime.setStatus("mandatory")
_NodeTypeStr_Type = DisplayString
_NodeTypeStr_Object = MibScalar
nodeTypeStr = _NodeTypeStr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 1, 1, 23),
    _NodeTypeStr_Type()
)
nodeTypeStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeTypeStr.setStatus("mandatory")
_NodeAddr_Type = IpAddress
_NodeAddr_Object = MibScalar
nodeAddr = _NodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 1, 1, 24),
    _NodeAddr_Type()
)
nodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeAddr.setStatus("mandatory")


class _NcpCrashDumpPresent_Type(Integer32):
    """Custom type ncpCrashDumpPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("present", 1),
          ("not-present", 2))
    )


_NcpCrashDumpPresent_Type.__name__ = "Integer32"
_NcpCrashDumpPresent_Object = MibScalar
ncpCrashDumpPresent = _NcpCrashDumpPresent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 1, 1, 25),
    _NcpCrashDumpPresent_Type()
)
ncpCrashDumpPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncpCrashDumpPresent.setStatus("mandatory")
_Equipment_ObjectIdentity = ObjectIdentity
equipment = _Equipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1, 2)
)
_Multiwave_ObjectIdentity = ObjectIdentity
multiwave = _Multiwave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3)
)
_ModuleTable_Object = MibTable
moduleTable = _ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 1)
)
if mibBuilder.loadTexts:
    moduleTable.setStatus("mandatory")
_ModEntry_Object = MibTableRow
modEntry = _ModEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 1, 1)
)
modEntry.setIndexNames(
    (0, "CIENA-MIBv2", "shelfId"),
    (0, "CIENA-MIBv2", "slotId"),
)
if mibBuilder.loadTexts:
    modEntry.setStatus("mandatory")
_ShelfId_Type = Integer32
_ShelfId_Object = MibTableColumn
shelfId = _ShelfId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 1, 1, 1),
    _ShelfId_Type()
)
shelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfId.setStatus("mandatory")
_SlotId_Type = Integer32
_SlotId_Object = MibTableColumn
slotId = _SlotId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 1, 1, 2),
    _SlotId_Type()
)
slotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotId.setStatus("mandatory")
_PartId_Type = DisplayString
_PartId_Object = MibTableColumn
partId = _PartId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 1, 1, 3),
    _PartId_Type()
)
partId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partId.setStatus("mandatory")
_PartNumber_Type = DisplayString
_PartNumber_Object = MibTableColumn
partNumber = _PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 1, 1, 4),
    _PartNumber_Type()
)
partNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partNumber.setStatus("mandatory")
_SerialId_Type = DisplayString
_SerialId_Object = MibTableColumn
serialId = _SerialId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 1, 1, 5),
    _SerialId_Type()
)
serialId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialId.setStatus("mandatory")
_RevisionId_Type = DisplayString
_RevisionId_Object = MibTableColumn
revisionId = _RevisionId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 1, 1, 6),
    _RevisionId_Type()
)
revisionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    revisionId.setStatus("mandatory")


class _ModuleType_Type(Integer32):
    """Custom type moduleType based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29)
        )
    )
    namedValues = NamedValues(
        *(("remodulator", 1),
          ("pump", 2),
          ("fiberAmplifier", 3),
          ("splitter", 4),
          ("combiner", 5),
          ("serviceChannelModem", 6),
          ("nodalControlProcessor", 7),
          ("selector", 8),
          ("auxilliaryModule", 9),
          ("shelfPowerModule", 10),
          ("unknown", 11),
          ("orderWire", 12),
          ("dualSplitter", 13),
          ("dualCombiner", 14),
          ("scim", 15),
          ("addDropMux", 16),
          ("splitterCombiner", 17),
          ("addDropMuxAmp", 18),
          ("receiver", 19),
          ("transmitter", 20),
          ("fireflyIo", 21),
          ("fireflyMuxDem", 22),
          ("fireflyTransceiver", 23),
          ("unused", 24),
          ("fireflyScm", 25),
          ("fireflyPower", 26),
          ("busExtender", 27),
          ("router40", 28),
          ("auxiliaryModuleR2", 29))
    )


_ModuleType_Type.__name__ = "Integer32"
_ModuleType_Object = MibTableColumn
moduleType = _ModuleType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 1, 1, 7),
    _ModuleType_Type()
)
moduleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleType.setStatus("mandatory")


class _ModuleState_Type(Integer32):
    """Custom type moduleState based on Integer32"""
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
        *(("present", 1),
          ("notPresent", 2),
          ("operational", 3),
          ("timedOut", 4),
          ("notInitialized", 5),
          ("resetting", 6),
          ("notPresentConfigured", 7))
    )


_ModuleState_Type.__name__ = "Integer32"
_ModuleState_Object = MibTableColumn
moduleState = _ModuleState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 1, 1, 9),
    _ModuleState_Type()
)
moduleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleState.setStatus("mandatory")
_ModuleStatus_Type = MwSeverityLevel
_ModuleStatus_Object = MibTableColumn
moduleStatus = _ModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 1, 1, 10),
    _ModuleStatus_Type()
)
moduleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleStatus.setStatus("mandatory")


class _CpResetModule_Type(Integer32):
    """Custom type cpResetModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("operational", 2))
    )


_CpResetModule_Type.__name__ = "Integer32"
_CpResetModule_Object = MibTableColumn
cpResetModule = _CpResetModule_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 1, 1, 11),
    _CpResetModule_Type()
)
cpResetModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpResetModule.setStatus("mandatory")


class _IsInMaintenanceMode_Type(Integer32):
    """Custom type isInMaintenanceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inMaintMode", 1),
          ("notInMaintMode", 2))
    )


_IsInMaintenanceMode_Type.__name__ = "Integer32"
_IsInMaintenanceMode_Object = MibTableColumn
isInMaintenanceMode = _IsInMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 1, 1, 16),
    _IsInMaintenanceMode_Type()
)
isInMaintenanceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isInMaintenanceMode.setStatus("mandatory")


class _CpResetAccumulators_Type(Integer32):
    """Custom type cpResetAccumulators based on Integer32"""
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


_CpResetAccumulators_Type.__name__ = "Integer32"
_CpResetAccumulators_Object = MibTableColumn
cpResetAccumulators = _CpResetAccumulators_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 1, 1, 17),
    _CpResetAccumulators_Type()
)
cpResetAccumulators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpResetAccumulators.setStatus("mandatory")
_SlotsLeft_Type = Integer32
_SlotsLeft_Object = MibTableColumn
slotsLeft = _SlotsLeft_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 1, 1, 18),
    _SlotsLeft_Type()
)
slotsLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotsLeft.setStatus("mandatory")
_SlotsRight_Type = Integer32
_SlotsRight_Object = MibTableColumn
slotsRight = _SlotsRight_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 1, 1, 19),
    _SlotsRight_Type()
)
slotsRight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotsRight.setStatus("mandatory")
_ModuleTypeStr_Type = DisplayString
_ModuleTypeStr_Object = MibTableColumn
moduleTypeStr = _ModuleTypeStr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 1, 1, 20),
    _ModuleTypeStr_Type()
)
moduleTypeStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleTypeStr.setStatus("mandatory")
_RemodTable_Object = MibTable
remodTable = _RemodTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2)
)
if mibBuilder.loadTexts:
    remodTable.setStatus("mandatory")
_RemodEntry_Object = MibTableRow
remodEntry = _RemodEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2, 1)
)
remodEntry.setIndexNames(
    (0, "CIENA-MIBv2", "shelfId"),
    (0, "CIENA-MIBv2", "slotId"),
)
if mibBuilder.loadTexts:
    remodEntry.setStatus("mandatory")
_MpRemodGratingTemperature_Type = Integer32
_MpRemodGratingTemperature_Object = MibTableColumn
mpRemodGratingTemperature = _MpRemodGratingTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2, 1, 3),
    _MpRemodGratingTemperature_Type()
)
mpRemodGratingTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRemodGratingTemperature.setStatus("mandatory")


class _MpInputSignalLevel_Type(Integer32):
    """Custom type mpInputSignalLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("present", 2))
    )


_MpInputSignalLevel_Type.__name__ = "Integer32"
_MpInputSignalLevel_Object = MibTableColumn
mpInputSignalLevel = _MpInputSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2, 1, 4),
    _MpInputSignalLevel_Type()
)
mpInputSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpInputSignalLevel.setStatus("mandatory")


class _SpDitherEnable_Type(Integer32):
    """Custom type spDitherEnable based on Integer32"""
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


_SpDitherEnable_Type.__name__ = "Integer32"
_SpDitherEnable_Object = MibTableColumn
spDitherEnable = _SpDitherEnable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2, 1, 6),
    _SpDitherEnable_Type()
)
spDitherEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spDitherEnable.setStatus("mandatory")


class _SpFreqTrack_Type(Integer32):
    """Custom type spFreqTrack based on Integer32"""
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


_SpFreqTrack_Type.__name__ = "Integer32"
_SpFreqTrack_Object = MibTableColumn
spFreqTrack = _SpFreqTrack_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2, 1, 7),
    _SpFreqTrack_Type()
)
spFreqTrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spFreqTrack.setStatus("mandatory")
_MpRemodLaserPower_Type = Integer32
_MpRemodLaserPower_Object = MibTableColumn
mpRemodLaserPower = _MpRemodLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2, 1, 8),
    _MpRemodLaserPower_Type()
)
mpRemodLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRemodLaserPower.setStatus("mandatory")
_MpRemodLaserTemp_Type = Integer32
_MpRemodLaserTemp_Object = MibTableColumn
mpRemodLaserTemp = _MpRemodLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2, 1, 9),
    _MpRemodLaserTemp_Type()
)
mpRemodLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRemodLaserTemp.setStatus("mandatory")
_MpRemodLaserCurrent_Type = Integer32
_MpRemodLaserCurrent_Object = MibTableColumn
mpRemodLaserCurrent = _MpRemodLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2, 1, 10),
    _MpRemodLaserCurrent_Type()
)
mpRemodLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRemodLaserCurrent.setStatus("mandatory")
_MpRemodTECCurrent_Type = Integer32
_MpRemodTECCurrent_Object = MibTableColumn
mpRemodTECCurrent = _MpRemodTECCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2, 1, 11),
    _MpRemodTECCurrent_Type()
)
mpRemodTECCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRemodTECCurrent.setStatus("mandatory")
_MpRemodHeatSinkTemperature_Type = Integer32
_MpRemodHeatSinkTemperature_Object = MibTableColumn
mpRemodHeatSinkTemperature = _MpRemodHeatSinkTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2, 1, 12),
    _MpRemodHeatSinkTemperature_Type()
)
mpRemodHeatSinkTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRemodHeatSinkTemperature.setStatus("mandatory")


class _SpRemodOperatingMode_Type(Integer32):
    """Custom type spRemodOperatingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("constantPower", 1),
          ("constantPurrent", 2))
    )


_SpRemodOperatingMode_Type.__name__ = "Integer32"
_SpRemodOperatingMode_Object = MibTableColumn
spRemodOperatingMode = _SpRemodOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2, 1, 13),
    _SpRemodOperatingMode_Type()
)
spRemodOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spRemodOperatingMode.setStatus("mandatory")


class _MpRemodCurrentLimited_Type(Integer32):
    """Custom type mpRemodCurrentLimited based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_MpRemodCurrentLimited_Type.__name__ = "Integer32"
_MpRemodCurrentLimited_Object = MibTableColumn
mpRemodCurrentLimited = _MpRemodCurrentLimited_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2, 1, 14),
    _MpRemodCurrentLimited_Type()
)
mpRemodCurrentLimited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRemodCurrentLimited.setStatus("mandatory")
_SpRemodLaserPower_Type = Integer32
_SpRemodLaserPower_Object = MibTableColumn
spRemodLaserPower = _SpRemodLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2, 1, 15),
    _SpRemodLaserPower_Type()
)
spRemodLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spRemodLaserPower.setStatus("mandatory")
_SpRemodLaserTemperature_Type = Integer32
_SpRemodLaserTemperature_Object = MibTableColumn
spRemodLaserTemperature = _SpRemodLaserTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2, 1, 17),
    _SpRemodLaserTemperature_Type()
)
spRemodLaserTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spRemodLaserTemperature.setStatus("mandatory")


class _MpRemodLaserState_Type(Integer32):
    """Custom type mpRemodLaserState based on Integer32"""
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
        *(("off", 1),
          ("preheat", 2),
          ("on", 3),
          ("tracking", 4),
          ("locked", 5),
          ("safetyShutdown", 6))
    )


_MpRemodLaserState_Type.__name__ = "Integer32"
_MpRemodLaserState_Object = MibTableColumn
mpRemodLaserState = _MpRemodLaserState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2, 1, 19),
    _MpRemodLaserState_Type()
)
mpRemodLaserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRemodLaserState.setStatus("mandatory")
_FcRemodWavelength_Type = Integer32
_FcRemodWavelength_Object = MibTableColumn
fcRemodWavelength = _FcRemodWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2, 1, 20),
    _FcRemodWavelength_Type()
)
fcRemodWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcRemodWavelength.setStatus("mandatory")


class _SpRemodConfiguredState_Type(Integer32):
    """Custom type spRemodConfiguredState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("deactivated", 2),
          ("shutdown", 3))
    )


_SpRemodConfiguredState_Type.__name__ = "Integer32"
_SpRemodConfiguredState_Object = MibTableColumn
spRemodConfiguredState = _SpRemodConfiguredState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2, 1, 21),
    _SpRemodConfiguredState_Type()
)
spRemodConfiguredState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spRemodConfiguredState.setStatus("mandatory")


class _RemodOKLED_Type(Integer32):
    """Custom type remodOKLED based on Integer32"""
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


_RemodOKLED_Type.__name__ = "Integer32"
_RemodOKLED_Object = MibTableColumn
remodOKLED = _RemodOKLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2, 1, 26),
    _RemodOKLED_Type()
)
remodOKLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remodOKLED.setStatus("mandatory")


class _RemodMajorLED_Type(Integer32):
    """Custom type remodMajorLED based on Integer32"""
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


_RemodMajorLED_Type.__name__ = "Integer32"
_RemodMajorLED_Object = MibTableColumn
remodMajorLED = _RemodMajorLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2, 1, 27),
    _RemodMajorLED_Type()
)
remodMajorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remodMajorLED.setStatus("mandatory")


class _RemodMinorLED_Type(Integer32):
    """Custom type remodMinorLED based on Integer32"""
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


_RemodMinorLED_Type.__name__ = "Integer32"
_RemodMinorLED_Object = MibTableColumn
remodMinorLED = _RemodMinorLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2, 1, 28),
    _RemodMinorLED_Type()
)
remodMinorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remodMinorLED.setStatus("mandatory")


class _RemodMaintenanceLED_Type(Integer32):
    """Custom type remodMaintenanceLED based on Integer32"""
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


_RemodMaintenanceLED_Type.__name__ = "Integer32"
_RemodMaintenanceLED_Object = MibTableColumn
remodMaintenanceLED = _RemodMaintenanceLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2, 1, 29),
    _RemodMaintenanceLED_Type()
)
remodMaintenanceLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remodMaintenanceLED.setStatus("mandatory")


class _TerminalType_Type(Integer32):
    """Custom type terminalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("async", 1),
          ("sonet", 2))
    )


_TerminalType_Type.__name__ = "Integer32"
_TerminalType_Object = MibTableColumn
terminalType = _TerminalType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2, 1, 30),
    _TerminalType_Type()
)
terminalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terminalType.setStatus("mandatory")
_SpGratingTemp_Type = Integer32
_SpGratingTemp_Object = MibTableColumn
spGratingTemp = _SpGratingTemp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2, 1, 31),
    _SpGratingTemp_Type()
)
spGratingTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spGratingTemp.setStatus("mandatory")
_RemodChannelTag1_Type = OctetString
_RemodChannelTag1_Object = MibTableColumn
remodChannelTag1 = _RemodChannelTag1_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2, 1, 32),
    _RemodChannelTag1_Type()
)
remodChannelTag1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remodChannelTag1.setStatus("mandatory")
_RemodChannelTag2_Type = OctetString
_RemodChannelTag2_Object = MibTableColumn
remodChannelTag2 = _RemodChannelTag2_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2, 1, 33),
    _RemodChannelTag2_Type()
)
remodChannelTag2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remodChannelTag2.setStatus("mandatory")
_PumpTable_Object = MibTable
pumpTable = _PumpTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 3)
)
if mibBuilder.loadTexts:
    pumpTable.setStatus("mandatory")
_PumpEntry_Object = MibTableRow
pumpEntry = _PumpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 3, 1)
)
pumpEntry.setIndexNames(
    (0, "CIENA-MIBv2", "shelfId"),
    (0, "CIENA-MIBv2", "slotId"),
)
if mibBuilder.loadTexts:
    pumpEntry.setStatus("mandatory")
_MpPumpLaserPower_Type = Integer32
_MpPumpLaserPower_Object = MibTableColumn
mpPumpLaserPower = _MpPumpLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 3, 1, 3),
    _MpPumpLaserPower_Type()
)
mpPumpLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpPumpLaserPower.setStatus("mandatory")
_MpPumpLaserTemp_Type = Integer32
_MpPumpLaserTemp_Object = MibTableColumn
mpPumpLaserTemp = _MpPumpLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 3, 1, 4),
    _MpPumpLaserTemp_Type()
)
mpPumpLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpPumpLaserTemp.setStatus("mandatory")
_MpPumpLaserCurrent_Type = Integer32
_MpPumpLaserCurrent_Object = MibTableColumn
mpPumpLaserCurrent = _MpPumpLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 3, 1, 5),
    _MpPumpLaserCurrent_Type()
)
mpPumpLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpPumpLaserCurrent.setStatus("mandatory")
_MpPumpTECCurrent_Type = Integer32
_MpPumpTECCurrent_Object = MibTableColumn
mpPumpTECCurrent = _MpPumpTECCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 3, 1, 6),
    _MpPumpTECCurrent_Type()
)
mpPumpTECCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpPumpTECCurrent.setStatus("mandatory")
_MpPumpHeatSinkTemperature_Type = Integer32
_MpPumpHeatSinkTemperature_Object = MibTableColumn
mpPumpHeatSinkTemperature = _MpPumpHeatSinkTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 3, 1, 7),
    _MpPumpHeatSinkTemperature_Type()
)
mpPumpHeatSinkTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpPumpHeatSinkTemperature.setStatus("mandatory")


class _SpPumpOperatingMode_Type(Integer32):
    """Custom type spPumpOperatingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("constantPower", 1),
          ("constantPurrent", 2))
    )


_SpPumpOperatingMode_Type.__name__ = "Integer32"
_SpPumpOperatingMode_Object = MibTableColumn
spPumpOperatingMode = _SpPumpOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 3, 1, 8),
    _SpPumpOperatingMode_Type()
)
spPumpOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spPumpOperatingMode.setStatus("mandatory")


class _MpPumpCurrentLimited_Type(Integer32):
    """Custom type mpPumpCurrentLimited based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_MpPumpCurrentLimited_Type.__name__ = "Integer32"
_MpPumpCurrentLimited_Object = MibTableColumn
mpPumpCurrentLimited = _MpPumpCurrentLimited_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 3, 1, 9),
    _MpPumpCurrentLimited_Type()
)
mpPumpCurrentLimited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpPumpCurrentLimited.setStatus("mandatory")
_SpPumpLaserPower_Type = Integer32
_SpPumpLaserPower_Object = MibTableColumn
spPumpLaserPower = _SpPumpLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 3, 1, 10),
    _SpPumpLaserPower_Type()
)
spPumpLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spPumpLaserPower.setStatus("mandatory")
_SpPumpLaserCurrent_Type = Integer32
_SpPumpLaserCurrent_Object = MibTableColumn
spPumpLaserCurrent = _SpPumpLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 3, 1, 11),
    _SpPumpLaserCurrent_Type()
)
spPumpLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spPumpLaserCurrent.setStatus("mandatory")
_SpPumpLaserTemp_Type = Integer32
_SpPumpLaserTemp_Object = MibTableColumn
spPumpLaserTemp = _SpPumpLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 3, 1, 12),
    _SpPumpLaserTemp_Type()
)
spPumpLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spPumpLaserTemp.setStatus("mandatory")


class _MpPumpLaserState_Type(Integer32):
    """Custom type mpPumpLaserState based on Integer32"""
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
        *(("off", 1),
          ("preheat", 2),
          ("on", 3),
          ("tracking", 4),
          ("locked", 5))
    )


_MpPumpLaserState_Type.__name__ = "Integer32"
_MpPumpLaserState_Object = MibTableColumn
mpPumpLaserState = _MpPumpLaserState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 3, 1, 14),
    _MpPumpLaserState_Type()
)
mpPumpLaserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpPumpLaserState.setStatus("mandatory")
_FcPumpWavelength_Type = Integer32
_FcPumpWavelength_Object = MibTableColumn
fcPumpWavelength = _FcPumpWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 3, 1, 15),
    _FcPumpWavelength_Type()
)
fcPumpWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPumpWavelength.setStatus("mandatory")


class _PumpOKLED_Type(Integer32):
    """Custom type pumpOKLED based on Integer32"""
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


_PumpOKLED_Type.__name__ = "Integer32"
_PumpOKLED_Object = MibTableColumn
pumpOKLED = _PumpOKLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 3, 1, 20),
    _PumpOKLED_Type()
)
pumpOKLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pumpOKLED.setStatus("mandatory")


class _PumpMajorLED_Type(Integer32):
    """Custom type pumpMajorLED based on Integer32"""
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


_PumpMajorLED_Type.__name__ = "Integer32"
_PumpMajorLED_Object = MibTableColumn
pumpMajorLED = _PumpMajorLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 3, 1, 21),
    _PumpMajorLED_Type()
)
pumpMajorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pumpMajorLED.setStatus("mandatory")


class _PumpMinorLED_Type(Integer32):
    """Custom type pumpMinorLED based on Integer32"""
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


_PumpMinorLED_Type.__name__ = "Integer32"
_PumpMinorLED_Object = MibTableColumn
pumpMinorLED = _PumpMinorLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 3, 1, 22),
    _PumpMinorLED_Type()
)
pumpMinorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pumpMinorLED.setStatus("mandatory")


class _PumpMaintenanceLED_Type(Integer32):
    """Custom type pumpMaintenanceLED based on Integer32"""
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


_PumpMaintenanceLED_Type.__name__ = "Integer32"
_PumpMaintenanceLED_Object = MibTableColumn
pumpMaintenanceLED = _PumpMaintenanceLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 3, 1, 23),
    _PumpMaintenanceLED_Type()
)
pumpMaintenanceLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pumpMaintenanceLED.setStatus("mandatory")


class _SpPumpConfiguredState_Type(Integer32):
    """Custom type spPumpConfiguredState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("deactivated", 2))
    )


_SpPumpConfiguredState_Type.__name__ = "Integer32"
_SpPumpConfiguredState_Object = MibTableColumn
spPumpConfiguredState = _SpPumpConfiguredState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 3, 1, 24),
    _SpPumpConfiguredState_Type()
)
spPumpConfiguredState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spPumpConfiguredState.setStatus("mandatory")
_SelectorTable_Object = MibTable
selectorTable = _SelectorTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 4)
)
if mibBuilder.loadTexts:
    selectorTable.setStatus("mandatory")
_SelectorEntry_Object = MibTableRow
selectorEntry = _SelectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 4, 1)
)
selectorEntry.setIndexNames(
    (0, "CIENA-MIBv2", "shelfId"),
    (0, "CIENA-MIBv2", "slotId"),
)
if mibBuilder.loadTexts:
    selectorEntry.setStatus("mandatory")
_FcSelectorWavelengthTop_Type = Integer32
_FcSelectorWavelengthTop_Object = MibTableColumn
fcSelectorWavelengthTop = _FcSelectorWavelengthTop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 4, 1, 3),
    _FcSelectorWavelengthTop_Type()
)
fcSelectorWavelengthTop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcSelectorWavelengthTop.setStatus("mandatory")
_FcSelectorWavelengthBottom_Type = Integer32
_FcSelectorWavelengthBottom_Object = MibTableColumn
fcSelectorWavelengthBottom = _FcSelectorWavelengthBottom_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 4, 1, 4),
    _FcSelectorWavelengthBottom_Type()
)
fcSelectorWavelengthBottom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcSelectorWavelengthBottom.setStatus("mandatory")
_MpSignalLevelTop_Type = Integer32
_MpSignalLevelTop_Object = MibTableColumn
mpSignalLevelTop = _MpSignalLevelTop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 4, 1, 6),
    _MpSignalLevelTop_Type()
)
mpSignalLevelTop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpSignalLevelTop.setStatus("mandatory")
_MpSignalLevelBottom_Type = Integer32
_MpSignalLevelBottom_Object = MibTableColumn
mpSignalLevelBottom = _MpSignalLevelBottom_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 4, 1, 7),
    _MpSignalLevelBottom_Type()
)
mpSignalLevelBottom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpSignalLevelBottom.setStatus("mandatory")


class _SelectorOKLedTop_Type(Integer32):
    """Custom type selectorOKLedTop based on Integer32"""
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


_SelectorOKLedTop_Type.__name__ = "Integer32"
_SelectorOKLedTop_Object = MibTableColumn
selectorOKLedTop = _SelectorOKLedTop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 4, 1, 12),
    _SelectorOKLedTop_Type()
)
selectorOKLedTop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selectorOKLedTop.setStatus("mandatory")


class _SelectorMajorLedTop_Type(Integer32):
    """Custom type selectorMajorLedTop based on Integer32"""
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


_SelectorMajorLedTop_Type.__name__ = "Integer32"
_SelectorMajorLedTop_Object = MibTableColumn
selectorMajorLedTop = _SelectorMajorLedTop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 4, 1, 13),
    _SelectorMajorLedTop_Type()
)
selectorMajorLedTop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selectorMajorLedTop.setStatus("mandatory")


class _SelectorMinorLedTop_Type(Integer32):
    """Custom type selectorMinorLedTop based on Integer32"""
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


_SelectorMinorLedTop_Type.__name__ = "Integer32"
_SelectorMinorLedTop_Object = MibTableColumn
selectorMinorLedTop = _SelectorMinorLedTop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 4, 1, 14),
    _SelectorMinorLedTop_Type()
)
selectorMinorLedTop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selectorMinorLedTop.setStatus("mandatory")


class _SelectorMaintenanceLedTop_Type(Integer32):
    """Custom type selectorMaintenanceLedTop based on Integer32"""
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


_SelectorMaintenanceLedTop_Type.__name__ = "Integer32"
_SelectorMaintenanceLedTop_Object = MibTableColumn
selectorMaintenanceLedTop = _SelectorMaintenanceLedTop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 4, 1, 15),
    _SelectorMaintenanceLedTop_Type()
)
selectorMaintenanceLedTop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selectorMaintenanceLedTop.setStatus("mandatory")


class _SelectorOKLedBottom_Type(Integer32):
    """Custom type selectorOKLedBottom based on Integer32"""
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


_SelectorOKLedBottom_Type.__name__ = "Integer32"
_SelectorOKLedBottom_Object = MibTableColumn
selectorOKLedBottom = _SelectorOKLedBottom_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 4, 1, 20),
    _SelectorOKLedBottom_Type()
)
selectorOKLedBottom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selectorOKLedBottom.setStatus("mandatory")


class _SelectorMajorLedBottom_Type(Integer32):
    """Custom type selectorMajorLedBottom based on Integer32"""
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


_SelectorMajorLedBottom_Type.__name__ = "Integer32"
_SelectorMajorLedBottom_Object = MibTableColumn
selectorMajorLedBottom = _SelectorMajorLedBottom_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 4, 1, 21),
    _SelectorMajorLedBottom_Type()
)
selectorMajorLedBottom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selectorMajorLedBottom.setStatus("mandatory")


class _SelectorMinorLedBottom_Type(Integer32):
    """Custom type selectorMinorLedBottom based on Integer32"""
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


_SelectorMinorLedBottom_Type.__name__ = "Integer32"
_SelectorMinorLedBottom_Object = MibTableColumn
selectorMinorLedBottom = _SelectorMinorLedBottom_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 4, 1, 22),
    _SelectorMinorLedBottom_Type()
)
selectorMinorLedBottom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selectorMinorLedBottom.setStatus("mandatory")


class _SelectorMaintenanceLedBottom_Type(Integer32):
    """Custom type selectorMaintenanceLedBottom based on Integer32"""
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


_SelectorMaintenanceLedBottom_Type.__name__ = "Integer32"
_SelectorMaintenanceLedBottom_Object = MibTableColumn
selectorMaintenanceLedBottom = _SelectorMaintenanceLedBottom_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 4, 1, 23),
    _SelectorMaintenanceLedBottom_Type()
)
selectorMaintenanceLedBottom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selectorMaintenanceLedBottom.setStatus("mandatory")
_MpGratingTopTemp_Type = Integer32
_MpGratingTopTemp_Object = MibTableColumn
mpGratingTopTemp = _MpGratingTopTemp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 4, 1, 24),
    _MpGratingTopTemp_Type()
)
mpGratingTopTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGratingTopTemp.setStatus("mandatory")
_MpGratingBottomTemp_Type = Integer32
_MpGratingBottomTemp_Object = MibTableColumn
mpGratingBottomTemp = _MpGratingBottomTemp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 4, 1, 25),
    _MpGratingBottomTemp_Type()
)
mpGratingBottomTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGratingBottomTemp.setStatus("mandatory")
_SpGratingTopTemp_Type = Integer32
_SpGratingTopTemp_Object = MibTableColumn
spGratingTopTemp = _SpGratingTopTemp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 4, 1, 26),
    _SpGratingTopTemp_Type()
)
spGratingTopTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spGratingTopTemp.setStatus("mandatory")
_SpGratingBottomTemp_Type = Integer32
_SpGratingBottomTemp_Object = MibTableColumn
spGratingBottomTemp = _SpGratingBottomTemp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 4, 1, 27),
    _SpGratingBottomTemp_Type()
)
spGratingBottomTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spGratingBottomTemp.setStatus("mandatory")
_SelectorChannelTagA1_Type = OctetString
_SelectorChannelTagA1_Object = MibTableColumn
selectorChannelTagA1 = _SelectorChannelTagA1_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 4, 1, 28),
    _SelectorChannelTagA1_Type()
)
selectorChannelTagA1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selectorChannelTagA1.setStatus("mandatory")
_SelectorChannelTagA2_Type = OctetString
_SelectorChannelTagA2_Object = MibTableColumn
selectorChannelTagA2 = _SelectorChannelTagA2_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 4, 1, 29),
    _SelectorChannelTagA2_Type()
)
selectorChannelTagA2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selectorChannelTagA2.setStatus("mandatory")
_SelectorChannelTagB1_Type = OctetString
_SelectorChannelTagB1_Object = MibTableColumn
selectorChannelTagB1 = _SelectorChannelTagB1_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 4, 1, 30),
    _SelectorChannelTagB1_Type()
)
selectorChannelTagB1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selectorChannelTagB1.setStatus("mandatory")
_SelectorChannelTagB2_Type = OctetString
_SelectorChannelTagB2_Object = MibTableColumn
selectorChannelTagB2 = _SelectorChannelTagB2_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 4, 1, 31),
    _SelectorChannelTagB2_Type()
)
selectorChannelTagB2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selectorChannelTagB2.setStatus("mandatory")
_FiberAmpTable_Object = MibTable
fiberAmpTable = _FiberAmpTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 5)
)
if mibBuilder.loadTexts:
    fiberAmpTable.setStatus("mandatory")
_FiberAmpEntry_Object = MibTableRow
fiberAmpEntry = _FiberAmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 5, 1)
)
fiberAmpEntry.setIndexNames(
    (0, "CIENA-MIBv2", "shelfId"),
    (0, "CIENA-MIBv2", "slotId"),
)
if mibBuilder.loadTexts:
    fiberAmpEntry.setStatus("mandatory")
_FiberAmpTopInputSignalLevel_Type = Integer32
_FiberAmpTopInputSignalLevel_Object = MibTableColumn
fiberAmpTopInputSignalLevel = _FiberAmpTopInputSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 5, 1, 3),
    _FiberAmpTopInputSignalLevel_Type()
)
fiberAmpTopInputSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberAmpTopInputSignalLevel.setStatus("mandatory")
_FiberAmpTopOutputSignalLevel_Type = Integer32
_FiberAmpTopOutputSignalLevel_Object = MibTableColumn
fiberAmpTopOutputSignalLevel = _FiberAmpTopOutputSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 5, 1, 4),
    _FiberAmpTopOutputSignalLevel_Type()
)
fiberAmpTopOutputSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberAmpTopOutputSignalLevel.setStatus("mandatory")
_FiberAmpBottomInputSignalLevel_Type = Integer32
_FiberAmpBottomInputSignalLevel_Object = MibTableColumn
fiberAmpBottomInputSignalLevel = _FiberAmpBottomInputSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 5, 1, 5),
    _FiberAmpBottomInputSignalLevel_Type()
)
fiberAmpBottomInputSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberAmpBottomInputSignalLevel.setStatus("mandatory")
_FiberAmpBottomOutputSignalLevel_Type = Integer32
_FiberAmpBottomOutputSignalLevel_Object = MibTableColumn
fiberAmpBottomOutputSignalLevel = _FiberAmpBottomOutputSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 5, 1, 6),
    _FiberAmpBottomOutputSignalLevel_Type()
)
fiberAmpBottomOutputSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberAmpBottomOutputSignalLevel.setStatus("mandatory")


class _FiberAmpTopOKLed_Type(Integer32):
    """Custom type fiberAmpTopOKLed based on Integer32"""
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


_FiberAmpTopOKLed_Type.__name__ = "Integer32"
_FiberAmpTopOKLed_Object = MibTableColumn
fiberAmpTopOKLed = _FiberAmpTopOKLed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 5, 1, 11),
    _FiberAmpTopOKLed_Type()
)
fiberAmpTopOKLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberAmpTopOKLed.setStatus("mandatory")


class _FiberAmpTopMajorLed_Type(Integer32):
    """Custom type fiberAmpTopMajorLed based on Integer32"""
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


_FiberAmpTopMajorLed_Type.__name__ = "Integer32"
_FiberAmpTopMajorLed_Object = MibTableColumn
fiberAmpTopMajorLed = _FiberAmpTopMajorLed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 5, 1, 12),
    _FiberAmpTopMajorLed_Type()
)
fiberAmpTopMajorLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberAmpTopMajorLed.setStatus("mandatory")


class _FiberAmpTopMinorLed_Type(Integer32):
    """Custom type fiberAmpTopMinorLed based on Integer32"""
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


_FiberAmpTopMinorLed_Type.__name__ = "Integer32"
_FiberAmpTopMinorLed_Object = MibTableColumn
fiberAmpTopMinorLed = _FiberAmpTopMinorLed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 5, 1, 13),
    _FiberAmpTopMinorLed_Type()
)
fiberAmpTopMinorLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberAmpTopMinorLed.setStatus("mandatory")


class _FiberAmpTopMaintenanceLed_Type(Integer32):
    """Custom type fiberAmpTopMaintenanceLed based on Integer32"""
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


_FiberAmpTopMaintenanceLed_Type.__name__ = "Integer32"
_FiberAmpTopMaintenanceLed_Object = MibTableColumn
fiberAmpTopMaintenanceLed = _FiberAmpTopMaintenanceLed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 5, 1, 14),
    _FiberAmpTopMaintenanceLed_Type()
)
fiberAmpTopMaintenanceLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberAmpTopMaintenanceLed.setStatus("mandatory")


class _FiberAmpBottomOKLed_Type(Integer32):
    """Custom type fiberAmpBottomOKLed based on Integer32"""
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


_FiberAmpBottomOKLed_Type.__name__ = "Integer32"
_FiberAmpBottomOKLed_Object = MibTableColumn
fiberAmpBottomOKLed = _FiberAmpBottomOKLed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 5, 1, 19),
    _FiberAmpBottomOKLed_Type()
)
fiberAmpBottomOKLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberAmpBottomOKLed.setStatus("mandatory")


class _FiberAmpBottomMajorLed_Type(Integer32):
    """Custom type fiberAmpBottomMajorLed based on Integer32"""
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


_FiberAmpBottomMajorLed_Type.__name__ = "Integer32"
_FiberAmpBottomMajorLed_Object = MibTableColumn
fiberAmpBottomMajorLed = _FiberAmpBottomMajorLed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 5, 1, 20),
    _FiberAmpBottomMajorLed_Type()
)
fiberAmpBottomMajorLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberAmpBottomMajorLed.setStatus("mandatory")


class _FiberAmpBottomMinorLed_Type(Integer32):
    """Custom type fiberAmpBottomMinorLed based on Integer32"""
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


_FiberAmpBottomMinorLed_Type.__name__ = "Integer32"
_FiberAmpBottomMinorLed_Object = MibTableColumn
fiberAmpBottomMinorLed = _FiberAmpBottomMinorLed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 5, 1, 21),
    _FiberAmpBottomMinorLed_Type()
)
fiberAmpBottomMinorLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberAmpBottomMinorLed.setStatus("mandatory")


class _FiberAmpBottomMaintenanceLed_Type(Integer32):
    """Custom type fiberAmpBottomMaintenanceLed based on Integer32"""
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


_FiberAmpBottomMaintenanceLed_Type.__name__ = "Integer32"
_FiberAmpBottomMaintenanceLed_Object = MibTableColumn
fiberAmpBottomMaintenanceLed = _FiberAmpBottomMaintenanceLed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 5, 1, 22),
    _FiberAmpBottomMaintenanceLed_Type()
)
fiberAmpBottomMaintenanceLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberAmpBottomMaintenanceLed.setStatus("mandatory")
_ShelfPowerTable_Object = MibTable
shelfPowerTable = _ShelfPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 6)
)
if mibBuilder.loadTexts:
    shelfPowerTable.setStatus("mandatory")
_ShelfPowerEntry_Object = MibTableRow
shelfPowerEntry = _ShelfPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 6, 1)
)
shelfPowerEntry.setIndexNames(
    (0, "CIENA-MIBv2", "shelfId"),
    (0, "CIENA-MIBv2", "slotId"),
)
if mibBuilder.loadTexts:
    shelfPowerEntry.setStatus("mandatory")


class _ShelfPowerSource1Fail_Type(Integer32):
    """Custom type shelfPowerSource1Fail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("ok", 2))
    )


_ShelfPowerSource1Fail_Type.__name__ = "Integer32"
_ShelfPowerSource1Fail_Object = MibTableColumn
shelfPowerSource1Fail = _ShelfPowerSource1Fail_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 6, 1, 3),
    _ShelfPowerSource1Fail_Type()
)
shelfPowerSource1Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfPowerSource1Fail.setStatus("mandatory")


class _ShelfPowerSource2Fail_Type(Integer32):
    """Custom type shelfPowerSource2Fail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("ok", 2))
    )


_ShelfPowerSource2Fail_Type.__name__ = "Integer32"
_ShelfPowerSource2Fail_Object = MibTableColumn
shelfPowerSource2Fail = _ShelfPowerSource2Fail_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 6, 1, 4),
    _ShelfPowerSource2Fail_Type()
)
shelfPowerSource2Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfPowerSource2Fail.setStatus("mandatory")


class _ShelfPowerSummaryFail_Type(Integer32):
    """Custom type shelfPowerSummaryFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("ok", 2))
    )


_ShelfPowerSummaryFail_Type.__name__ = "Integer32"
_ShelfPowerSummaryFail_Object = MibTableColumn
shelfPowerSummaryFail = _ShelfPowerSummaryFail_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 6, 1, 5),
    _ShelfPowerSummaryFail_Type()
)
shelfPowerSummaryFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfPowerSummaryFail.setStatus("mandatory")
_ShelfPowerTemperature_Type = Integer32
_ShelfPowerTemperature_Object = MibTableColumn
shelfPowerTemperature = _ShelfPowerTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 6, 1, 6),
    _ShelfPowerTemperature_Type()
)
shelfPowerTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfPowerTemperature.setStatus("mandatory")


class _ShelfPowerFan1Fail_Type(Integer32):
    """Custom type shelfPowerFan1Fail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("ok", 2))
    )


_ShelfPowerFan1Fail_Type.__name__ = "Integer32"
_ShelfPowerFan1Fail_Object = MibTableColumn
shelfPowerFan1Fail = _ShelfPowerFan1Fail_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 6, 1, 7),
    _ShelfPowerFan1Fail_Type()
)
shelfPowerFan1Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfPowerFan1Fail.setStatus("mandatory")


class _ShelfPowerFan2Fail_Type(Integer32):
    """Custom type shelfPowerFan2Fail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("ok", 2))
    )


_ShelfPowerFan2Fail_Type.__name__ = "Integer32"
_ShelfPowerFan2Fail_Object = MibTableColumn
shelfPowerFan2Fail = _ShelfPowerFan2Fail_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 6, 1, 8),
    _ShelfPowerFan2Fail_Type()
)
shelfPowerFan2Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfPowerFan2Fail.setStatus("mandatory")
_MonitorPointTable_Object = MibTable
monitorPointTable = _MonitorPointTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 7)
)
if mibBuilder.loadTexts:
    monitorPointTable.setStatus("mandatory")
_MonitorPointEntry_Object = MibTableRow
monitorPointEntry = _MonitorPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 7, 1)
)
monitorPointEntry.setIndexNames(
    (0, "CIENA-MIBv2", "monitorPointShelfId"),
    (0, "CIENA-MIBv2", "monitorPointSlotId"),
    (0, "CIENA-MIBv2", "monitorPointUnitId"),
    (0, "CIENA-MIBv2", "monitorPointAttributeId"),
)
if mibBuilder.loadTexts:
    monitorPointEntry.setStatus("mandatory")
_MonitorPointShelfId_Type = Integer32
_MonitorPointShelfId_Object = MibTableColumn
monitorPointShelfId = _MonitorPointShelfId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 7, 1, 1),
    _MonitorPointShelfId_Type()
)
monitorPointShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPointShelfId.setStatus("mandatory")
_MonitorPointSlotId_Type = Integer32
_MonitorPointSlotId_Object = MibTableColumn
monitorPointSlotId = _MonitorPointSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 7, 1, 2),
    _MonitorPointSlotId_Type()
)
monitorPointSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPointSlotId.setStatus("mandatory")
_MonitorPointUnitId_Type = Integer32
_MonitorPointUnitId_Object = MibTableColumn
monitorPointUnitId = _MonitorPointUnitId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 7, 1, 3),
    _MonitorPointUnitId_Type()
)
monitorPointUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPointUnitId.setStatus("mandatory")
_MonitorPointAttributeId_Type = MwMonitorPointId
_MonitorPointAttributeId_Object = MibTableColumn
monitorPointAttributeId = _MonitorPointAttributeId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 7, 1, 4),
    _MonitorPointAttributeId_Type()
)
monitorPointAttributeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPointAttributeId.setStatus("mandatory")
_MeasuredValue_Type = Integer32
_MeasuredValue_Object = MibTableColumn
measuredValue = _MeasuredValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 7, 1, 5),
    _MeasuredValue_Type()
)
measuredValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measuredValue.setStatus("mandatory")
_HighValueLatch_Type = Integer32
_HighValueLatch_Object = MibTableColumn
highValueLatch = _HighValueLatch_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 7, 1, 6),
    _HighValueLatch_Type()
)
highValueLatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highValueLatch.setStatus("mandatory")
_LowValueLatch_Type = Integer32
_LowValueLatch_Object = MibTableColumn
lowValueLatch = _LowValueLatch_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 7, 1, 7),
    _LowValueLatch_Type()
)
lowValueLatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowValueLatch.setStatus("mandatory")
_AverageValue_Type = Integer32
_AverageValue_Object = MibTableColumn
averageValue = _AverageValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 7, 1, 8),
    _AverageValue_Type()
)
averageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    averageValue.setStatus("mandatory")
_AverageSamplesQty_Type = Integer32
_AverageSamplesQty_Object = MibTableColumn
averageSamplesQty = _AverageSamplesQty_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 7, 1, 9),
    _AverageSamplesQty_Type()
)
averageSamplesQty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    averageSamplesQty.setStatus("mandatory")
_HiMajorThreshold_Type = Integer32
_HiMajorThreshold_Object = MibTableColumn
hiMajorThreshold = _HiMajorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 7, 1, 10),
    _HiMajorThreshold_Type()
)
hiMajorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiMajorThreshold.setStatus("mandatory")
_HiMinorThreshold_Type = Integer32
_HiMinorThreshold_Object = MibTableColumn
hiMinorThreshold = _HiMinorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 7, 1, 11),
    _HiMinorThreshold_Type()
)
hiMinorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiMinorThreshold.setStatus("mandatory")
_LoMinorThreshold_Type = Integer32
_LoMinorThreshold_Object = MibTableColumn
loMinorThreshold = _LoMinorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 7, 1, 12),
    _LoMinorThreshold_Type()
)
loMinorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loMinorThreshold.setStatus("mandatory")
_LoMajorThreshold_Type = Integer32
_LoMajorThreshold_Object = MibTableColumn
loMajorThreshold = _LoMajorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 7, 1, 13),
    _LoMajorThreshold_Type()
)
loMajorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loMajorThreshold.setStatus("mandatory")


class _HiMajorThresholdMode_Type(Integer32):
    """Custom type hiMajorThresholdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2),
          ("not-supported", 3))
    )


_HiMajorThresholdMode_Type.__name__ = "Integer32"
_HiMajorThresholdMode_Object = MibTableColumn
hiMajorThresholdMode = _HiMajorThresholdMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 7, 1, 14),
    _HiMajorThresholdMode_Type()
)
hiMajorThresholdMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiMajorThresholdMode.setStatus("mandatory")


class _HiMinorThresholdMode_Type(Integer32):
    """Custom type hiMinorThresholdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2),
          ("not-supported", 3))
    )


_HiMinorThresholdMode_Type.__name__ = "Integer32"
_HiMinorThresholdMode_Object = MibTableColumn
hiMinorThresholdMode = _HiMinorThresholdMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 7, 1, 15),
    _HiMinorThresholdMode_Type()
)
hiMinorThresholdMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiMinorThresholdMode.setStatus("mandatory")


class _LoMinorThresholdMode_Type(Integer32):
    """Custom type loMinorThresholdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2),
          ("not-supported", 3))
    )


_LoMinorThresholdMode_Type.__name__ = "Integer32"
_LoMinorThresholdMode_Object = MibTableColumn
loMinorThresholdMode = _LoMinorThresholdMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 7, 1, 16),
    _LoMinorThresholdMode_Type()
)
loMinorThresholdMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loMinorThresholdMode.setStatus("mandatory")


class _LoMajorThresholdMode_Type(Integer32):
    """Custom type loMajorThresholdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2),
          ("not-supported", 3))
    )


_LoMajorThresholdMode_Type.__name__ = "Integer32"
_LoMajorThresholdMode_Object = MibTableColumn
loMajorThresholdMode = _LoMajorThresholdMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 7, 1, 17),
    _LoMajorThresholdMode_Type()
)
loMajorThresholdMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loMajorThresholdMode.setStatus("mandatory")


class _ThresholdSource_Type(Integer32):
    """Custom type thresholdSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("currentValue", 1),
          ("averageValue", 2))
    )


_ThresholdSource_Type.__name__ = "Integer32"
_ThresholdSource_Object = MibTableColumn
thresholdSource = _ThresholdSource_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 7, 1, 18),
    _ThresholdSource_Type()
)
thresholdSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdSource.setStatus("mandatory")


class _AverageMethod_Type(Integer32):
    """Custom type averageMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("twoPoint", 1),
          ("cumulative", 2))
    )


_AverageMethod_Type.__name__ = "Integer32"
_AverageMethod_Object = MibTableColumn
averageMethod = _AverageMethod_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 7, 1, 19),
    _AverageMethod_Type()
)
averageMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    averageMethod.setStatus("mandatory")


class _CpResetAccumulator_Type(Integer32):
    """Custom type cpResetAccumulator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_CpResetAccumulator_Type.__name__ = "Integer32"
_CpResetAccumulator_Object = MibTableColumn
cpResetAccumulator = _CpResetAccumulator_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 7, 1, 20),
    _CpResetAccumulator_Type()
)
cpResetAccumulator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpResetAccumulator.setStatus("mandatory")
_MaxValue_Type = Integer32
_MaxValue_Object = MibTableColumn
maxValue = _MaxValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 7, 1, 21),
    _MaxValue_Type()
)
maxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxValue.setStatus("mandatory")
_MinValue_Type = Integer32
_MinValue_Object = MibTableColumn
minValue = _MinValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 7, 1, 22),
    _MinValue_Type()
)
minValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minValue.setStatus("mandatory")


class _Units_Type(Integer32):
    """Custom type units based on Integer32"""
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
        *(("tenths-of-microwatt", 1),
          ("tenths-of-milliwatt", 2),
          ("tenths-of-degree-celcius", 3),
          ("milliamps", 4),
          ("millivolts", 5))
    )


_Units_Type.__name__ = "Integer32"
_Units_Object = MibTableColumn
units = _Units_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 7, 1, 23),
    _Units_Type()
)
units.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    units.setStatus("mandatory")


class _ThresholdCompareMode_Type(Integer32):
    """Custom type thresholdCompareMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("delta", 2))
    )


_ThresholdCompareMode_Type.__name__ = "Integer32"
_ThresholdCompareMode_Object = MibTableColumn
thresholdCompareMode = _ThresholdCompareMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 7, 1, 24),
    _ThresholdCompareMode_Type()
)
thresholdCompareMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdCompareMode.setStatus("mandatory")
_MwSupportingEMSGroup_ObjectIdentity = ObjectIdentity
mwSupportingEMSGroup = _MwSupportingEMSGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 8)
)
_MwSupportEMSTableSize_Type = Integer32
_MwSupportEMSTableSize_Object = MibScalar
mwSupportEMSTableSize = _MwSupportEMSTableSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 8, 1),
    _MwSupportEMSTableSize_Type()
)
mwSupportEMSTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSupportEMSTableSize.setStatus("mandatory")
_MwSupportEMSTable_Object = MibTable
mwSupportEMSTable = _MwSupportEMSTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 8, 2)
)
if mibBuilder.loadTexts:
    mwSupportEMSTable.setStatus("mandatory")
_MwSupportEMSEntry_Object = MibTableRow
mwSupportEMSEntry = _MwSupportEMSEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 8, 2, 1)
)
mwSupportEMSEntry.setIndexNames(
    (0, "CIENA-MIBv2", "mwEMSNum"),
)
if mibBuilder.loadTexts:
    mwSupportEMSEntry.setStatus("mandatory")
_MwEMSNum_Type = Integer32
_MwEMSNum_Object = MibTableColumn
mwEMSNum = _MwEMSNum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 8, 2, 1, 1),
    _MwEMSNum_Type()
)
mwEMSNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwEMSNum.setStatus("mandatory")


class _MwEMSAddrType_Type(Integer32):
    """Custom type mwEMSAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("mwUdpIp", 1)
    )


_MwEMSAddrType_Type.__name__ = "Integer32"
_MwEMSAddrType_Object = MibTableColumn
mwEMSAddrType = _MwEMSAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 8, 2, 1, 2),
    _MwEMSAddrType_Type()
)
mwEMSAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwEMSAddrType.setStatus("mandatory")
_MwEMSAddr_Type = OctetString
_MwEMSAddr_Object = MibTableColumn
mwEMSAddr = _MwEMSAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 8, 2, 1, 3),
    _MwEMSAddr_Type()
)
mwEMSAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwEMSAddr.setStatus("mandatory")
_MwEMSName_Type = DisplayString
_MwEMSName_Object = MibTableColumn
mwEMSName = _MwEMSName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 8, 2, 1, 4),
    _MwEMSName_Type()
)
mwEMSName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwEMSName.setStatus("mandatory")
_MwEMSVersion_Type = Integer32
_MwEMSVersion_Object = MibTableColumn
mwEMSVersion = _MwEMSVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 8, 2, 1, 5),
    _MwEMSVersion_Type()
)
mwEMSVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwEMSVersion.setStatus("mandatory")
_AlarmTable_Object = MibTable
alarmTable = _AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 9)
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("deprecated")
_OldAlarmEntry_Object = MibTableRow
oldAlarmEntry = _OldAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 9, 1)
)
oldAlarmEntry.setIndexNames(
    (0, "CIENA-MIBv2", "shelfId"),
    (0, "CIENA-MIBv2", "slotId"),
    (0, "CIENA-MIBv2", "alarmCriticality"),
    (0, "CIENA-MIBv2", "alarmTerm"),
    (0, "CIENA-MIBv2", "alarmAttrIx"),
)
if mibBuilder.loadTexts:
    oldAlarmEntry.setStatus("deprecated")


class _AlarmSeverity_Type(Integer32):
    """Custom type alarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2048,
              2050,
              2052,
              2053,
              2054,
              2055,
              2056)
        )
    )
    namedValues = NamedValues(
        *(("alarmNormal", 2048),
          ("alarmInhibited", 2050),
          ("alarmInformational", 2052),
          ("alarmWarning", 2053),
          ("alarmMinor", 2054),
          ("alarmMajor", 2055),
          ("alarmCritical", 2056))
    )


_AlarmSeverity_Type.__name__ = "Integer32"
_AlarmSeverity_Object = MibTableColumn
alarmSeverity = _AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 9, 1, 3),
    _AlarmSeverity_Type()
)
alarmSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmSeverity.setStatus("deprecated")
_AlarmTerm_Type = Integer32
_AlarmTerm_Object = MibTableColumn
alarmTerm = _AlarmTerm_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 9, 1, 4),
    _AlarmTerm_Type()
)
alarmTerm.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmTerm.setStatus("deprecated")
_AlarmAttrIx_Type = Integer32
_AlarmAttrIx_Object = MibTableColumn
alarmAttrIx = _AlarmAttrIx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 9, 1, 5),
    _AlarmAttrIx_Type()
)
alarmAttrIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmAttrIx.setStatus("deprecated")
_AlarmAttrId_Type = Integer32
_AlarmAttrId_Object = MibTableColumn
alarmAttrId = _AlarmAttrId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 9, 1, 6),
    _AlarmAttrId_Type()
)
alarmAttrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmAttrId.setStatus("deprecated")
_MwDSModuleGroup_ObjectIdentity = ObjectIdentity
mwDSModuleGroup = _MwDSModuleGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 10)
)
_MwDSModuleTable_Object = MibTable
mwDSModuleTable = _MwDSModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 10, 1)
)
if mibBuilder.loadTexts:
    mwDSModuleTable.setStatus("mandatory")
_MwDSModuleEntry_Object = MibTableRow
mwDSModuleEntry = _MwDSModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 10, 1, 1)
)
mwDSModuleEntry.setIndexNames(
    (0, "CIENA-MIBv2", "shelfId"),
    (0, "CIENA-MIBv2", "slotId"),
    (0, "CIENA-MIBv2", "mwDSType"),
    (0, "CIENA-MIBv2", "mwDSNum"),
)
if mibBuilder.loadTexts:
    mwDSModuleEntry.setStatus("mandatory")


class _MwDSType_Type(Integer32):
    """Custom type mwDSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mwDsInput", 1),
          ("mwDsOutput", 2))
    )


_MwDSType_Type.__name__ = "Integer32"
_MwDSType_Object = MibTableColumn
mwDSType = _MwDSType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 10, 1, 1, 1),
    _MwDSType_Type()
)
mwDSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwDSType.setStatus("mandatory")
_MwDSNum_Type = Integer32
_MwDSNum_Object = MibTableColumn
mwDSNum = _MwDSNum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 10, 1, 1, 2),
    _MwDSNum_Type()
)
mwDSNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwDSNum.setStatus("mandatory")
_MwDSignalName_Type = DisplayString
_MwDSignalName_Object = MibTableColumn
mwDSignalName = _MwDSignalName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 10, 1, 1, 3),
    _MwDSignalName_Type()
)
mwDSignalName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwDSignalName.setStatus("mandatory")


class _MwDSignalState_Type(Integer32):
    """Custom type mwDSignalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mwDiscreteOpen", 1),
          ("mwDiscreteClosed", 2))
    )


_MwDSignalState_Type.__name__ = "Integer32"
_MwDSignalState_Object = MibTableColumn
mwDSignalState = _MwDSignalState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 10, 1, 1, 4),
    _MwDSignalState_Type()
)
mwDSignalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwDSignalState.setStatus("mandatory")
_MwDSignalOffStateName_Type = DisplayString
_MwDSignalOffStateName_Object = MibTableColumn
mwDSignalOffStateName = _MwDSignalOffStateName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 10, 1, 1, 5),
    _MwDSignalOffStateName_Type()
)
mwDSignalOffStateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwDSignalOffStateName.setStatus("mandatory")
_MwDSignalOnStateName_Type = DisplayString
_MwDSignalOnStateName_Object = MibTableColumn
mwDSignalOnStateName = _MwDSignalOnStateName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 10, 1, 1, 6),
    _MwDSignalOnStateName_Type()
)
mwDSignalOnStateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwDSignalOnStateName.setStatus("mandatory")
_MwDSCriticality_Type = MwSeverityLevel
_MwDSCriticality_Object = MibTableColumn
mwDSCriticality = _MwDSCriticality_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 10, 1, 1, 7),
    _MwDSCriticality_Type()
)
mwDSCriticality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwDSCriticality.setStatus("mandatory")


class _MwDSAlarmState_Type(Integer32):
    """Custom type mwDSAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mwDiscreteOn", 1),
          ("mwDiscreteOff", 2))
    )


_MwDSAlarmState_Type.__name__ = "Integer32"
_MwDSAlarmState_Object = MibTableColumn
mwDSAlarmState = _MwDSAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 10, 1, 1, 8),
    _MwDSAlarmState_Type()
)
mwDSAlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwDSAlarmState.setStatus("mandatory")
_MwNeighborModuleGroup_ObjectIdentity = ObjectIdentity
mwNeighborModuleGroup = _MwNeighborModuleGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 11)
)
_MwNeighborTable_Object = MibTable
mwNeighborTable = _MwNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 11, 1)
)
if mibBuilder.loadTexts:
    mwNeighborTable.setStatus("mandatory")
_MwNeighborEntry_Object = MibTableRow
mwNeighborEntry = _MwNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 11, 1, 1)
)
mwNeighborEntry.setIndexNames(
    (0, "CIENA-MIBv2", "mwNeighborDirection"),
    (0, "CIENA-MIBv2", "mwNeighborDistance"),
)
if mibBuilder.loadTexts:
    mwNeighborEntry.setStatus("mandatory")


class _MwNeighborDirection_Type(Integer32):
    """Custom type mwNeighborDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mwFromWest", 1),
          ("mwFromEast", 2))
    )


_MwNeighborDirection_Type.__name__ = "Integer32"
_MwNeighborDirection_Object = MibTableColumn
mwNeighborDirection = _MwNeighborDirection_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 11, 1, 1, 1),
    _MwNeighborDirection_Type()
)
mwNeighborDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwNeighborDirection.setStatus("mandatory")
_MwNeighborDistance_Type = Integer32
_MwNeighborDistance_Object = MibTableColumn
mwNeighborDistance = _MwNeighborDistance_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 11, 1, 1, 2),
    _MwNeighborDistance_Type()
)
mwNeighborDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwNeighborDistance.setStatus("mandatory")


class _MwAddrType_Type(Integer32):
    """Custom type mwAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("mwIpAddr", 1)
    )


_MwAddrType_Type.__name__ = "Integer32"
_MwAddrType_Object = MibTableColumn
mwAddrType = _MwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 11, 1, 1, 3),
    _MwAddrType_Type()
)
mwAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAddrType.setStatus("mandatory")
_MwNeighborAddr_Type = OctetString
_MwNeighborAddr_Object = MibTableColumn
mwNeighborAddr = _MwNeighborAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 11, 1, 1, 4),
    _MwNeighborAddr_Type()
)
mwNeighborAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwNeighborAddr.setStatus("mandatory")
_MwAlarmTable_Object = MibTable
mwAlarmTable = _MwAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 12)
)
if mibBuilder.loadTexts:
    mwAlarmTable.setStatus("mandatory")
_MwAlarmEntry_Object = MibTableRow
mwAlarmEntry = _MwAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 12, 1)
)
mwAlarmEntry.setIndexNames(
    (0, "CIENA-MIBv2", "shelfId"),
    (0, "CIENA-MIBv2", "slotId"),
    (0, "CIENA-MIBv2", "alarmCriticality"),
    (0, "CIENA-MIBv2", "alarmSequence"),
)
if mibBuilder.loadTexts:
    mwAlarmEntry.setStatus("mandatory")
_AlarmSequence_Type = Integer32
_AlarmSequence_Object = MibTableColumn
alarmSequence = _AlarmSequence_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 12, 1, 1),
    _AlarmSequence_Type()
)
alarmSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSequence.setStatus("mandatory")
_AlarmTime_Type = Integer32
_AlarmTime_Object = MibTableColumn
alarmTime = _AlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 12, 1, 2),
    _AlarmTime_Type()
)
alarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTime.setStatus("mandatory")
_AlarmCriticality_Type = MwSeverityLevel
_AlarmCriticality_Object = MibTableColumn
alarmCriticality = _AlarmCriticality_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 12, 1, 3),
    _AlarmCriticality_Type()
)
alarmCriticality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCriticality.setStatus("mandatory")
_AlarmAttribute1_Type = MwAttributeId
_AlarmAttribute1_Object = MibTableColumn
alarmAttribute1 = _AlarmAttribute1_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 12, 1, 4),
    _AlarmAttribute1_Type()
)
alarmAttribute1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmAttribute1.setStatus("mandatory")
_AlarmAttrSubCode1_Type = Integer32
_AlarmAttrSubCode1_Object = MibTableColumn
alarmAttrSubCode1 = _AlarmAttrSubCode1_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 12, 1, 5),
    _AlarmAttrSubCode1_Type()
)
alarmAttrSubCode1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmAttrSubCode1.setStatus("mandatory")
_AlarmAttribute2_Type = MwAttributeId
_AlarmAttribute2_Object = MibTableColumn
alarmAttribute2 = _AlarmAttribute2_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 12, 1, 6),
    _AlarmAttribute2_Type()
)
alarmAttribute2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmAttribute2.setStatus("mandatory")
_AlarmAttrSubCode2_Type = Integer32
_AlarmAttrSubCode2_Object = MibTableColumn
alarmAttrSubCode2 = _AlarmAttrSubCode2_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 12, 1, 7),
    _AlarmAttrSubCode2_Type()
)
alarmAttrSubCode2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmAttrSubCode2.setStatus("mandatory")
_AlarmAttribute3_Type = MwAttributeId
_AlarmAttribute3_Object = MibTableColumn
alarmAttribute3 = _AlarmAttribute3_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 12, 1, 8),
    _AlarmAttribute3_Type()
)
alarmAttribute3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmAttribute3.setStatus("mandatory")
_AlarmAttrSubCode3_Type = Integer32
_AlarmAttrSubCode3_Object = MibTableColumn
alarmAttrSubCode3 = _AlarmAttrSubCode3_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 12, 1, 9),
    _AlarmAttrSubCode3_Type()
)
alarmAttrSubCode3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmAttrSubCode3.setStatus("mandatory")
_AlarmAttribute4_Type = MwAttributeId
_AlarmAttribute4_Object = MibTableColumn
alarmAttribute4 = _AlarmAttribute4_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 12, 1, 10),
    _AlarmAttribute4_Type()
)
alarmAttribute4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmAttribute4.setStatus("mandatory")
_AlarmAttrSubCode4_Type = Integer32
_AlarmAttrSubCode4_Object = MibTableColumn
alarmAttrSubCode4 = _AlarmAttrSubCode4_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 12, 1, 11),
    _AlarmAttrSubCode4_Type()
)
alarmAttrSubCode4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmAttrSubCode4.setStatus("mandatory")
_AlarmCondition_Type = DisplayString
_AlarmCondition_Object = MibTableColumn
alarmCondition = _AlarmCondition_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 12, 1, 12),
    _AlarmCondition_Type()
)
alarmCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCondition.setStatus("mandatory")
_MwUsersGroup_ObjectIdentity = ObjectIdentity
mwUsersGroup = _MwUsersGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 13)
)
_MwUsersLoggedInTable_Object = MibTable
mwUsersLoggedInTable = _MwUsersLoggedInTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 13, 1)
)
if mibBuilder.loadTexts:
    mwUsersLoggedInTable.setStatus("mandatory")
_MwUsersLoggedInEntry_Object = MibTableRow
mwUsersLoggedInEntry = _MwUsersLoggedInEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 13, 1, 1)
)
mwUsersLoggedInEntry.setIndexNames(
    (0, "CIENA-MIBv2", "mwLoginNum"),
)
if mibBuilder.loadTexts:
    mwUsersLoggedInEntry.setStatus("mandatory")
_MwLoginNum_Type = Integer32
_MwLoginNum_Object = MibTableColumn
mwLoginNum = _MwLoginNum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 13, 1, 1, 1),
    _MwLoginNum_Type()
)
mwLoginNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwLoginNum.setStatus("mandatory")
_MwUserNum_Type = Integer32
_MwUserNum_Object = MibTableColumn
mwUserNum = _MwUserNum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 13, 1, 1, 2),
    _MwUserNum_Type()
)
mwUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwUserNum.setStatus("mandatory")
_MwLoggedInFrom_Type = DisplayString
_MwLoggedInFrom_Object = MibTableColumn
mwLoggedInFrom = _MwLoggedInFrom_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 13, 1, 1, 3),
    _MwLoggedInFrom_Type()
)
mwLoggedInFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwLoggedInFrom.setStatus("mandatory")
_MwElapsedLoginTime_Type = Integer32
_MwElapsedLoginTime_Object = MibTableColumn
mwElapsedLoginTime = _MwElapsedLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 13, 1, 1, 4),
    _MwElapsedLoginTime_Type()
)
mwElapsedLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwElapsedLoginTime.setStatus("mandatory")
_MwChangeGroup_ObjectIdentity = ObjectIdentity
mwChangeGroup = _MwChangeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 14)
)
_MwChangeTable_Object = MibTable
mwChangeTable = _MwChangeTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 14, 2)
)
if mibBuilder.loadTexts:
    mwChangeTable.setStatus("mandatory")
_MwChangeEntry_Object = MibTableRow
mwChangeEntry = _MwChangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 14, 2, 1)
)
mwChangeEntry.setIndexNames(
    (0, "CIENA-MIBv2", "mwChangeNumber"),
)
if mibBuilder.loadTexts:
    mwChangeEntry.setStatus("mandatory")
_MwChangeNumber_Type = Integer32
_MwChangeNumber_Object = MibTableColumn
mwChangeNumber = _MwChangeNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 14, 2, 1, 1),
    _MwChangeNumber_Type()
)
mwChangeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwChangeNumber.setStatus("mandatory")
_MwLastChangeTime_Type = TimeTicks
_MwLastChangeTime_Object = MibTableColumn
mwLastChangeTime = _MwLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 14, 2, 1, 2),
    _MwLastChangeTime_Type()
)
mwLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwLastChangeTime.setStatus("mandatory")
_MwTableId_Type = ObjectIdentifier
_MwTableId_Object = MibTableColumn
mwTableId = _MwTableId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 14, 2, 1, 3),
    _MwTableId_Type()
)
mwTableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTableId.setStatus("mandatory")
_ScmTable_Object = MibTable
scmTable = _ScmTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 15)
)
if mibBuilder.loadTexts:
    scmTable.setStatus("mandatory")
_ScmEntry_Object = MibTableRow
scmEntry = _ScmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 15, 1)
)
scmEntry.setIndexNames(
    (0, "CIENA-MIBv2", "shelfId"),
    (0, "CIENA-MIBv2", "slotId"),
)
if mibBuilder.loadTexts:
    scmEntry.setStatus("mandatory")
_ScmLaserPower_Type = Integer32
_ScmLaserPower_Object = MibTableColumn
scmLaserPower = _ScmLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 15, 1, 1),
    _ScmLaserPower_Type()
)
scmLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmLaserPower.setStatus("mandatory")
_ScmLaserTemperature_Type = Integer32
_ScmLaserTemperature_Object = MibTableColumn
scmLaserTemperature = _ScmLaserTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 15, 1, 2),
    _ScmLaserTemperature_Type()
)
scmLaserTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmLaserTemperature.setStatus("mandatory")
_ScmLaserCurrent_Type = Integer32
_ScmLaserCurrent_Object = MibTableColumn
scmLaserCurrent = _ScmLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 15, 1, 3),
    _ScmLaserCurrent_Type()
)
scmLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmLaserCurrent.setStatus("mandatory")
_ScmLaserTECCurrent_Type = Integer32
_ScmLaserTECCurrent_Object = MibTableColumn
scmLaserTECCurrent = _ScmLaserTECCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 15, 1, 4),
    _ScmLaserTECCurrent_Type()
)
scmLaserTECCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmLaserTECCurrent.setStatus("mandatory")
_ScmLaserHeatSinkTemperature_Type = Integer32
_ScmLaserHeatSinkTemperature_Object = MibTableColumn
scmLaserHeatSinkTemperature = _ScmLaserHeatSinkTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 15, 1, 5),
    _ScmLaserHeatSinkTemperature_Type()
)
scmLaserHeatSinkTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmLaserHeatSinkTemperature.setStatus("mandatory")


class _ScmLaserState_Type(Integer32):
    """Custom type scmLaserState based on Integer32"""
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
        *(("off", 1),
          ("preheat", 2),
          ("on", 3),
          ("tracking", 4),
          ("locked", 5))
    )


_ScmLaserState_Type.__name__ = "Integer32"
_ScmLaserState_Object = MibTableColumn
scmLaserState = _ScmLaserState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 15, 1, 6),
    _ScmLaserState_Type()
)
scmLaserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmLaserState.setStatus("mandatory")
_ScmLaserWavelength_Type = Integer32
_ScmLaserWavelength_Object = MibTableColumn
scmLaserWavelength = _ScmLaserWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 15, 1, 7),
    _ScmLaserWavelength_Type()
)
scmLaserWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmLaserWavelength.setStatus("mandatory")


class _ScmLaserInputSignalAbsent_Type(Integer32):
    """Custom type scmLaserInputSignalAbsent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-present", 1),
          ("present", 2))
    )


_ScmLaserInputSignalAbsent_Type.__name__ = "Integer32"
_ScmLaserInputSignalAbsent_Object = MibTableColumn
scmLaserInputSignalAbsent = _ScmLaserInputSignalAbsent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 15, 1, 8),
    _ScmLaserInputSignalAbsent_Type()
)
scmLaserInputSignalAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmLaserInputSignalAbsent.setStatus("mandatory")


class _ScmEastLinkStat_Type(Integer32):
    """Custom type scmEastLinkStat based on Integer32"""
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
        *(("down", 1),
          ("degraded", 2),
          ("up", 3),
          ("connect-error", 4),
          ("framing", 5),
          ("deactivated", 6))
    )


_ScmEastLinkStat_Type.__name__ = "Integer32"
_ScmEastLinkStat_Object = MibTableColumn
scmEastLinkStat = _ScmEastLinkStat_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 15, 1, 9),
    _ScmEastLinkStat_Type()
)
scmEastLinkStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmEastLinkStat.setStatus("mandatory")


class _ScmWestLinkStat_Type(Integer32):
    """Custom type scmWestLinkStat based on Integer32"""
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
        *(("down", 1),
          ("degraded", 2),
          ("up", 3),
          ("connect-error", 4),
          ("framing", 5),
          ("deactivated", 6))
    )


_ScmWestLinkStat_Type.__name__ = "Integer32"
_ScmWestLinkStat_Object = MibTableColumn
scmWestLinkStat = _ScmWestLinkStat_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 15, 1, 10),
    _ScmWestLinkStat_Type()
)
scmWestLinkStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmWestLinkStat.setStatus("mandatory")


class _ScmFramingMode_Type(Integer32):
    """Custom type scmFramingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("regen", 2))
    )


_ScmFramingMode_Type.__name__ = "Integer32"
_ScmFramingMode_Object = MibTableColumn
scmFramingMode = _ScmFramingMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 15, 1, 11),
    _ScmFramingMode_Type()
)
scmFramingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmFramingMode.setStatus("mandatory")


class _ScmNodeType_Type(Integer32):
    """Custom type scmNodeType based on Integer32"""
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
        *(("east-end", 1),
          ("west-end", 2),
          ("intermediate", 3),
          ("east-crosslink", 4),
          ("west-crosslink", 5))
    )


_ScmNodeType_Type.__name__ = "Integer32"
_ScmNodeType_Object = MibTableColumn
scmNodeType = _ScmNodeType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 15, 1, 12),
    _ScmNodeType_Type()
)
scmNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmNodeType.setStatus("mandatory")


class _ScmSlave_Type(Integer32):
    """Custom type scmSlave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("slave", 1),
          ("master", 2))
    )


_ScmSlave_Type.__name__ = "Integer32"
_ScmSlave_Object = MibTableColumn
scmSlave = _ScmSlave_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 15, 1, 13),
    _ScmSlave_Type()
)
scmSlave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmSlave.setStatus("mandatory")


class _ScmOkLED_Type(Integer32):
    """Custom type scmOkLED based on Integer32"""
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


_ScmOkLED_Type.__name__ = "Integer32"
_ScmOkLED_Object = MibTableColumn
scmOkLED = _ScmOkLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 15, 1, 14),
    _ScmOkLED_Type()
)
scmOkLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmOkLED.setStatus("mandatory")


class _ScmMajorLED_Type(Integer32):
    """Custom type scmMajorLED based on Integer32"""
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


_ScmMajorLED_Type.__name__ = "Integer32"
_ScmMajorLED_Object = MibTableColumn
scmMajorLED = _ScmMajorLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 15, 1, 15),
    _ScmMajorLED_Type()
)
scmMajorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmMajorLED.setStatus("mandatory")


class _ScmMinorLED_Type(Integer32):
    """Custom type scmMinorLED based on Integer32"""
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


_ScmMinorLED_Type.__name__ = "Integer32"
_ScmMinorLED_Object = MibTableColumn
scmMinorLED = _ScmMinorLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 15, 1, 16),
    _ScmMinorLED_Type()
)
scmMinorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmMinorLED.setStatus("mandatory")


class _ScmMaintenanceLED_Type(Integer32):
    """Custom type scmMaintenanceLED based on Integer32"""
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


_ScmMaintenanceLED_Type.__name__ = "Integer32"
_ScmMaintenanceLED_Object = MibTableColumn
scmMaintenanceLED = _ScmMaintenanceLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 15, 1, 17),
    _ScmMaintenanceLED_Type()
)
scmMaintenanceLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmMaintenanceLED.setStatus("mandatory")
_ScimTable_Object = MibTable
scimTable = _ScimTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 16)
)
if mibBuilder.loadTexts:
    scimTable.setStatus("mandatory")
_ScimEntry_Object = MibTableRow
scimEntry = _ScimEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 16, 1)
)
scimEntry.setIndexNames(
    (0, "CIENA-MIBv2", "shelfId"),
    (0, "CIENA-MIBv2", "slotId"),
)
if mibBuilder.loadTexts:
    scimEntry.setStatus("mandatory")
_ScimTopInput_Type = Integer32
_ScimTopInput_Object = MibTableColumn
scimTopInput = _ScimTopInput_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 16, 1, 1),
    _ScimTopInput_Type()
)
scimTopInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scimTopInput.setStatus("mandatory")
_ScimBottomInput_Type = Integer32
_ScimBottomInput_Object = MibTableColumn
scimBottomInput = _ScimBottomInput_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 16, 1, 2),
    _ScimBottomInput_Type()
)
scimBottomInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scimBottomInput.setStatus("mandatory")
_ScimTopOutput_Type = Integer32
_ScimTopOutput_Object = MibTableColumn
scimTopOutput = _ScimTopOutput_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 16, 1, 3),
    _ScimTopOutput_Type()
)
scimTopOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scimTopOutput.setStatus("mandatory")
_ScimBottomOutput_Type = Integer32
_ScimBottomOutput_Object = MibTableColumn
scimBottomOutput = _ScimBottomOutput_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 16, 1, 4),
    _ScimBottomOutput_Type()
)
scimBottomOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scimBottomOutput.setStatus("mandatory")


class _ScimTopOkLED_Type(Integer32):
    """Custom type scimTopOkLED based on Integer32"""
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


_ScimTopOkLED_Type.__name__ = "Integer32"
_ScimTopOkLED_Object = MibTableColumn
scimTopOkLED = _ScimTopOkLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 16, 1, 5),
    _ScimTopOkLED_Type()
)
scimTopOkLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scimTopOkLED.setStatus("mandatory")


class _ScimTopMajorLED_Type(Integer32):
    """Custom type scimTopMajorLED based on Integer32"""
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


_ScimTopMajorLED_Type.__name__ = "Integer32"
_ScimTopMajorLED_Object = MibTableColumn
scimTopMajorLED = _ScimTopMajorLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 16, 1, 6),
    _ScimTopMajorLED_Type()
)
scimTopMajorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scimTopMajorLED.setStatus("mandatory")


class _ScimTopMinorLED_Type(Integer32):
    """Custom type scimTopMinorLED based on Integer32"""
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


_ScimTopMinorLED_Type.__name__ = "Integer32"
_ScimTopMinorLED_Object = MibTableColumn
scimTopMinorLED = _ScimTopMinorLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 16, 1, 7),
    _ScimTopMinorLED_Type()
)
scimTopMinorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scimTopMinorLED.setStatus("mandatory")


class _ScimTopMaintenanceLED_Type(Integer32):
    """Custom type scimTopMaintenanceLED based on Integer32"""
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


_ScimTopMaintenanceLED_Type.__name__ = "Integer32"
_ScimTopMaintenanceLED_Object = MibTableColumn
scimTopMaintenanceLED = _ScimTopMaintenanceLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 16, 1, 8),
    _ScimTopMaintenanceLED_Type()
)
scimTopMaintenanceLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scimTopMaintenanceLED.setStatus("mandatory")


class _ScimBottomOkLED_Type(Integer32):
    """Custom type scimBottomOkLED based on Integer32"""
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


_ScimBottomOkLED_Type.__name__ = "Integer32"
_ScimBottomOkLED_Object = MibTableColumn
scimBottomOkLED = _ScimBottomOkLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 16, 1, 9),
    _ScimBottomOkLED_Type()
)
scimBottomOkLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scimBottomOkLED.setStatus("mandatory")


class _ScimBottomMajorLED_Type(Integer32):
    """Custom type scimBottomMajorLED based on Integer32"""
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


_ScimBottomMajorLED_Type.__name__ = "Integer32"
_ScimBottomMajorLED_Object = MibTableColumn
scimBottomMajorLED = _ScimBottomMajorLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 16, 1, 10),
    _ScimBottomMajorLED_Type()
)
scimBottomMajorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scimBottomMajorLED.setStatus("mandatory")


class _ScimBottomMinorLED_Type(Integer32):
    """Custom type scimBottomMinorLED based on Integer32"""
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


_ScimBottomMinorLED_Type.__name__ = "Integer32"
_ScimBottomMinorLED_Object = MibTableColumn
scimBottomMinorLED = _ScimBottomMinorLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 16, 1, 11),
    _ScimBottomMinorLED_Type()
)
scimBottomMinorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scimBottomMinorLED.setStatus("mandatory")


class _ScimBottomMaintenanceLED_Type(Integer32):
    """Custom type scimBottomMaintenanceLED based on Integer32"""
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


_ScimBottomMaintenanceLED_Type.__name__ = "Integer32"
_ScimBottomMaintenanceLED_Object = MibTableColumn
scimBottomMaintenanceLED = _ScimBottomMaintenanceLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 16, 1, 12),
    _ScimBottomMaintenanceLED_Type()
)
scimBottomMaintenanceLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scimBottomMaintenanceLED.setStatus("mandatory")


class _ScimTopMaintMode_Type(Integer32):
    """Custom type scimTopMaintMode based on Integer32"""
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


_ScimTopMaintMode_Type.__name__ = "Integer32"
_ScimTopMaintMode_Object = MibTableColumn
scimTopMaintMode = _ScimTopMaintMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 16, 1, 13),
    _ScimTopMaintMode_Type()
)
scimTopMaintMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scimTopMaintMode.setStatus("mandatory")


class _ScimBottomMaintMode_Type(Integer32):
    """Custom type scimBottomMaintMode based on Integer32"""
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


_ScimBottomMaintMode_Type.__name__ = "Integer32"
_ScimBottomMaintMode_Object = MibTableColumn
scimBottomMaintMode = _ScimBottomMaintMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 16, 1, 14),
    _ScimBottomMaintMode_Type()
)
scimBottomMaintMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scimBottomMaintMode.setStatus("mandatory")
_AdmTable_Object = MibTable
admTable = _AdmTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 17)
)
if mibBuilder.loadTexts:
    admTable.setStatus("mandatory")
_AdmEntry_Object = MibTableRow
admEntry = _AdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 17, 1)
)
admEntry.setIndexNames(
    (0, "CIENA-MIBv2", "shelfId"),
    (0, "CIENA-MIBv2", "slotId"),
)
if mibBuilder.loadTexts:
    admEntry.setStatus("mandatory")
_Adm1Heater_Type = Integer32
_Adm1Heater_Object = MibTableColumn
adm1Heater = _Adm1Heater_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 17, 1, 1),
    _Adm1Heater_Type()
)
adm1Heater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adm1Heater.setStatus("mandatory")
_Adm1Wavelength_Type = Integer32
_Adm1Wavelength_Object = MibTableColumn
adm1Wavelength = _Adm1Wavelength_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 17, 1, 2),
    _Adm1Wavelength_Type()
)
adm1Wavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adm1Wavelength.setStatus("mandatory")
_Adm1HeaterReference_Type = Integer32
_Adm1HeaterReference_Object = MibTableColumn
adm1HeaterReference = _Adm1HeaterReference_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 17, 1, 3),
    _Adm1HeaterReference_Type()
)
adm1HeaterReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adm1HeaterReference.setStatus("mandatory")


class _Adm1HeaterStatus_Type(Integer32):
    """Custom type adm1HeaterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("degraded", 2),
          ("failed", 3))
    )


_Adm1HeaterStatus_Type.__name__ = "Integer32"
_Adm1HeaterStatus_Object = MibTableColumn
adm1HeaterStatus = _Adm1HeaterStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 17, 1, 4),
    _Adm1HeaterStatus_Type()
)
adm1HeaterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adm1HeaterStatus.setStatus("mandatory")
_Adm2Heater_Type = Integer32
_Adm2Heater_Object = MibTableColumn
adm2Heater = _Adm2Heater_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 17, 1, 5),
    _Adm2Heater_Type()
)
adm2Heater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adm2Heater.setStatus("mandatory")
_Adm2Wavelength_Type = Integer32
_Adm2Wavelength_Object = MibTableColumn
adm2Wavelength = _Adm2Wavelength_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 17, 1, 6),
    _Adm2Wavelength_Type()
)
adm2Wavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adm2Wavelength.setStatus("mandatory")
_Adm2HeaterReference_Type = Integer32
_Adm2HeaterReference_Object = MibTableColumn
adm2HeaterReference = _Adm2HeaterReference_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 17, 1, 7),
    _Adm2HeaterReference_Type()
)
adm2HeaterReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adm2HeaterReference.setStatus("mandatory")


class _Adm2HeaterStatus_Type(Integer32):
    """Custom type adm2HeaterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("degraded", 2),
          ("failed", 3))
    )


_Adm2HeaterStatus_Type.__name__ = "Integer32"
_Adm2HeaterStatus_Object = MibTableColumn
adm2HeaterStatus = _Adm2HeaterStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 17, 1, 8),
    _Adm2HeaterStatus_Type()
)
adm2HeaterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adm2HeaterStatus.setStatus("mandatory")
_Adm3Heater_Type = Integer32
_Adm3Heater_Object = MibTableColumn
adm3Heater = _Adm3Heater_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 17, 1, 9),
    _Adm3Heater_Type()
)
adm3Heater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adm3Heater.setStatus("mandatory")
_Adm3Wavelength_Type = Integer32
_Adm3Wavelength_Object = MibTableColumn
adm3Wavelength = _Adm3Wavelength_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 17, 1, 10),
    _Adm3Wavelength_Type()
)
adm3Wavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adm3Wavelength.setStatus("mandatory")
_Adm3HeaterReference_Type = Integer32
_Adm3HeaterReference_Object = MibTableColumn
adm3HeaterReference = _Adm3HeaterReference_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 17, 1, 11),
    _Adm3HeaterReference_Type()
)
adm3HeaterReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adm3HeaterReference.setStatus("mandatory")


class _Adm3HeaterStatus_Type(Integer32):
    """Custom type adm3HeaterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("degraded", 2),
          ("failed", 3))
    )


_Adm3HeaterStatus_Type.__name__ = "Integer32"
_Adm3HeaterStatus_Object = MibTableColumn
adm3HeaterStatus = _Adm3HeaterStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 17, 1, 12),
    _Adm3HeaterStatus_Type()
)
adm3HeaterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adm3HeaterStatus.setStatus("mandatory")
_Adm4Heater_Type = Integer32
_Adm4Heater_Object = MibTableColumn
adm4Heater = _Adm4Heater_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 17, 1, 13),
    _Adm4Heater_Type()
)
adm4Heater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adm4Heater.setStatus("mandatory")
_Adm4Wavelength_Type = Integer32
_Adm4Wavelength_Object = MibTableColumn
adm4Wavelength = _Adm4Wavelength_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 17, 1, 14),
    _Adm4Wavelength_Type()
)
adm4Wavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adm4Wavelength.setStatus("mandatory")
_Adm4HeaterReference_Type = Integer32
_Adm4HeaterReference_Object = MibTableColumn
adm4HeaterReference = _Adm4HeaterReference_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 17, 1, 15),
    _Adm4HeaterReference_Type()
)
adm4HeaterReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adm4HeaterReference.setStatus("mandatory")


class _Adm4HeaterStatus_Type(Integer32):
    """Custom type adm4HeaterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("degraded", 2),
          ("failed", 3))
    )


_Adm4HeaterStatus_Type.__name__ = "Integer32"
_Adm4HeaterStatus_Object = MibTableColumn
adm4HeaterStatus = _Adm4HeaterStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 17, 1, 16),
    _Adm4HeaterStatus_Type()
)
adm4HeaterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adm4HeaterStatus.setStatus("mandatory")


class _AdmOkLED_Type(Integer32):
    """Custom type admOkLED based on Integer32"""
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


_AdmOkLED_Type.__name__ = "Integer32"
_AdmOkLED_Object = MibTableColumn
admOkLED = _AdmOkLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 17, 1, 17),
    _AdmOkLED_Type()
)
admOkLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admOkLED.setStatus("mandatory")


class _AdmMajorLED_Type(Integer32):
    """Custom type admMajorLED based on Integer32"""
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


_AdmMajorLED_Type.__name__ = "Integer32"
_AdmMajorLED_Object = MibTableColumn
admMajorLED = _AdmMajorLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 17, 1, 18),
    _AdmMajorLED_Type()
)
admMajorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admMajorLED.setStatus("mandatory")


class _AdmMinorLED_Type(Integer32):
    """Custom type admMinorLED based on Integer32"""
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


_AdmMinorLED_Type.__name__ = "Integer32"
_AdmMinorLED_Object = MibTableColumn
admMinorLED = _AdmMinorLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 17, 1, 19),
    _AdmMinorLED_Type()
)
admMinorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admMinorLED.setStatus("mandatory")


class _AdmMaintLED_Type(Integer32):
    """Custom type admMaintLED based on Integer32"""
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


_AdmMaintLED_Type.__name__ = "Integer32"
_AdmMaintLED_Object = MibTableColumn
admMaintLED = _AdmMaintLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 17, 1, 20),
    _AdmMaintLED_Type()
)
admMaintLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admMaintLED.setStatus("mandatory")
_OwTable_Object = MibTable
owTable = _OwTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 18)
)
if mibBuilder.loadTexts:
    owTable.setStatus("mandatory")
_OwEntry_Object = MibTableRow
owEntry = _OwEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 18, 1)
)
owEntry.setIndexNames(
    (0, "CIENA-MIBv2", "shelfId"),
    (0, "CIENA-MIBv2", "slotId"),
)
if mibBuilder.loadTexts:
    owEntry.setStatus("mandatory")


class _OwLine1OffHook_Type(Integer32):
    """Custom type owLine1OffHook based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off-hook", 1),
          ("on-hook", 2))
    )


_OwLine1OffHook_Type.__name__ = "Integer32"
_OwLine1OffHook_Object = MibTableColumn
owLine1OffHook = _OwLine1OffHook_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 18, 1, 1),
    _OwLine1OffHook_Type()
)
owLine1OffHook.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owLine1OffHook.setStatus("mandatory")


class _OwLine2OffHook_Type(Integer32):
    """Custom type owLine2OffHook based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off-hook", 1),
          ("on-hook", 2))
    )


_OwLine2OffHook_Type.__name__ = "Integer32"
_OwLine2OffHook_Object = MibTableColumn
owLine2OffHook = _OwLine2OffHook_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 18, 1, 2),
    _OwLine2OffHook_Type()
)
owLine2OffHook.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owLine2OffHook.setStatus("mandatory")
_AdmaTable_Object = MibTable
admaTable = _AdmaTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 19)
)
if mibBuilder.loadTexts:
    admaTable.setStatus("mandatory")
_AdmaEntry_Object = MibTableRow
admaEntry = _AdmaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 19, 1)
)
admaEntry.setIndexNames(
    (0, "CIENA-MIBv2", "shelfId"),
    (0, "CIENA-MIBv2", "slotId"),
)
if mibBuilder.loadTexts:
    admaEntry.setStatus("mandatory")
_AdmaTopInput_Type = Integer32
_AdmaTopInput_Object = MibTableColumn
admaTopInput = _AdmaTopInput_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 19, 1, 1),
    _AdmaTopInput_Type()
)
admaTopInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admaTopInput.setStatus("mandatory")
_AdmaBottomInput_Type = Integer32
_AdmaBottomInput_Object = MibTableColumn
admaBottomInput = _AdmaBottomInput_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 19, 1, 2),
    _AdmaBottomInput_Type()
)
admaBottomInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admaBottomInput.setStatus("mandatory")
_AdmaTopOutput_Type = Integer32
_AdmaTopOutput_Object = MibTableColumn
admaTopOutput = _AdmaTopOutput_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 19, 1, 3),
    _AdmaTopOutput_Type()
)
admaTopOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admaTopOutput.setStatus("mandatory")
_AdmaBottomOutput_Type = Integer32
_AdmaBottomOutput_Object = MibTableColumn
admaBottomOutput = _AdmaBottomOutput_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 19, 1, 4),
    _AdmaBottomOutput_Type()
)
admaBottomOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admaBottomOutput.setStatus("mandatory")


class _AdmaTopPreampOutput_Type(Integer32):
    """Custom type admaTopPreampOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("present", 1),
          ("not-present", 2))
    )


_AdmaTopPreampOutput_Type.__name__ = "Integer32"
_AdmaTopPreampOutput_Object = MibTableColumn
admaTopPreampOutput = _AdmaTopPreampOutput_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 19, 1, 5),
    _AdmaTopPreampOutput_Type()
)
admaTopPreampOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admaTopPreampOutput.setStatus("mandatory")


class _AdmaBottomPreampOutput_Type(Integer32):
    """Custom type admaBottomPreampOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("present", 1),
          ("not-present", 2))
    )


_AdmaBottomPreampOutput_Type.__name__ = "Integer32"
_AdmaBottomPreampOutput_Object = MibTableColumn
admaBottomPreampOutput = _AdmaBottomPreampOutput_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 19, 1, 6),
    _AdmaBottomPreampOutput_Type()
)
admaBottomPreampOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admaBottomPreampOutput.setStatus("mandatory")
_AdmaTopAdmInput_Type = Integer32
_AdmaTopAdmInput_Object = MibTableColumn
admaTopAdmInput = _AdmaTopAdmInput_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 19, 1, 7),
    _AdmaTopAdmInput_Type()
)
admaTopAdmInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admaTopAdmInput.setStatus("mandatory")
_AdmaBottomAdmInput_Type = Integer32
_AdmaBottomAdmInput_Object = MibTableColumn
admaBottomAdmInput = _AdmaBottomAdmInput_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 19, 1, 8),
    _AdmaBottomAdmInput_Type()
)
admaBottomAdmInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admaBottomAdmInput.setStatus("mandatory")
_AdmaTopCombinerInput_Type = Integer32
_AdmaTopCombinerInput_Object = MibTableColumn
admaTopCombinerInput = _AdmaTopCombinerInput_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 19, 1, 9),
    _AdmaTopCombinerInput_Type()
)
admaTopCombinerInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admaTopCombinerInput.setStatus("mandatory")
_AdmaBottomCombinerInput_Type = Integer32
_AdmaBottomCombinerInput_Object = MibTableColumn
admaBottomCombinerInput = _AdmaBottomCombinerInput_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 19, 1, 10),
    _AdmaBottomCombinerInput_Type()
)
admaBottomCombinerInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admaBottomCombinerInput.setStatus("mandatory")


class _AdmaTopOkLED_Type(Integer32):
    """Custom type admaTopOkLED based on Integer32"""
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


_AdmaTopOkLED_Type.__name__ = "Integer32"
_AdmaTopOkLED_Object = MibTableColumn
admaTopOkLED = _AdmaTopOkLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 19, 1, 11),
    _AdmaTopOkLED_Type()
)
admaTopOkLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admaTopOkLED.setStatus("mandatory")


class _AdmaTopMajorLED_Type(Integer32):
    """Custom type admaTopMajorLED based on Integer32"""
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


_AdmaTopMajorLED_Type.__name__ = "Integer32"
_AdmaTopMajorLED_Object = MibTableColumn
admaTopMajorLED = _AdmaTopMajorLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 19, 1, 12),
    _AdmaTopMajorLED_Type()
)
admaTopMajorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admaTopMajorLED.setStatus("mandatory")


class _AdmaTopMinorLED_Type(Integer32):
    """Custom type admaTopMinorLED based on Integer32"""
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


_AdmaTopMinorLED_Type.__name__ = "Integer32"
_AdmaTopMinorLED_Object = MibTableColumn
admaTopMinorLED = _AdmaTopMinorLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 19, 1, 13),
    _AdmaTopMinorLED_Type()
)
admaTopMinorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admaTopMinorLED.setStatus("mandatory")


class _AdmaTopMaintenanceLED_Type(Integer32):
    """Custom type admaTopMaintenanceLED based on Integer32"""
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


_AdmaTopMaintenanceLED_Type.__name__ = "Integer32"
_AdmaTopMaintenanceLED_Object = MibTableColumn
admaTopMaintenanceLED = _AdmaTopMaintenanceLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 19, 1, 14),
    _AdmaTopMaintenanceLED_Type()
)
admaTopMaintenanceLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admaTopMaintenanceLED.setStatus("mandatory")


class _AdmaBottomOkLED_Type(Integer32):
    """Custom type admaBottomOkLED based on Integer32"""
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


_AdmaBottomOkLED_Type.__name__ = "Integer32"
_AdmaBottomOkLED_Object = MibTableColumn
admaBottomOkLED = _AdmaBottomOkLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 19, 1, 15),
    _AdmaBottomOkLED_Type()
)
admaBottomOkLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admaBottomOkLED.setStatus("mandatory")


class _AdmaBottomMajorLED_Type(Integer32):
    """Custom type admaBottomMajorLED based on Integer32"""
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


_AdmaBottomMajorLED_Type.__name__ = "Integer32"
_AdmaBottomMajorLED_Object = MibTableColumn
admaBottomMajorLED = _AdmaBottomMajorLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 19, 1, 16),
    _AdmaBottomMajorLED_Type()
)
admaBottomMajorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admaBottomMajorLED.setStatus("mandatory")


class _AdmaBottomMinorLED_Type(Integer32):
    """Custom type admaBottomMinorLED based on Integer32"""
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


_AdmaBottomMinorLED_Type.__name__ = "Integer32"
_AdmaBottomMinorLED_Object = MibTableColumn
admaBottomMinorLED = _AdmaBottomMinorLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 19, 1, 17),
    _AdmaBottomMinorLED_Type()
)
admaBottomMinorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admaBottomMinorLED.setStatus("mandatory")


class _AdmaBottomMaintenanceLED_Type(Integer32):
    """Custom type admaBottomMaintenanceLED based on Integer32"""
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


_AdmaBottomMaintenanceLED_Type.__name__ = "Integer32"
_AdmaBottomMaintenanceLED_Object = MibTableColumn
admaBottomMaintenanceLED = _AdmaBottomMaintenanceLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 19, 1, 18),
    _AdmaBottomMaintenanceLED_Type()
)
admaBottomMaintenanceLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admaBottomMaintenanceLED.setStatus("mandatory")


class _AdmaTopMaintMode_Type(Integer32):
    """Custom type admaTopMaintMode based on Integer32"""
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


_AdmaTopMaintMode_Type.__name__ = "Integer32"
_AdmaTopMaintMode_Object = MibTableColumn
admaTopMaintMode = _AdmaTopMaintMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 19, 1, 19),
    _AdmaTopMaintMode_Type()
)
admaTopMaintMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admaTopMaintMode.setStatus("mandatory")


class _AdmaBottomMaintMode_Type(Integer32):
    """Custom type admaBottomMaintMode based on Integer32"""
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


_AdmaBottomMaintMode_Type.__name__ = "Integer32"
_AdmaBottomMaintMode_Object = MibTableColumn
admaBottomMaintMode = _AdmaBottomMaintMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 19, 1, 20),
    _AdmaBottomMaintMode_Type()
)
admaBottomMaintMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admaBottomMaintMode.setStatus("mandatory")
_MwLoadedImagesGroup_ObjectIdentity = ObjectIdentity
mwLoadedImagesGroup = _MwLoadedImagesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 20)
)
_MwAvailableImagesTable_Object = MibTable
mwAvailableImagesTable = _MwAvailableImagesTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 20, 1)
)
if mibBuilder.loadTexts:
    mwAvailableImagesTable.setStatus("mandatory")
_MwAvailableImageEntry_Object = MibTableRow
mwAvailableImageEntry = _MwAvailableImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 20, 1, 1)
)
mwAvailableImageEntry.setIndexNames(
    (0, "CIENA-MIBv2", "shelfId"),
    (0, "CIENA-MIBv2", "slotId"),
)
if mibBuilder.loadTexts:
    mwAvailableImageEntry.setStatus("mandatory")
_MwRunningImage_Type = DisplayString
_MwRunningImage_Object = MibTableColumn
mwRunningImage = _MwRunningImage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 20, 1, 1, 1),
    _MwRunningImage_Type()
)
mwRunningImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRunningImage.setStatus("mandatory")


class _MwImageControl_Type(Integer32):
    """Custom type mwImageControl based on Integer32"""
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
        *(("mwLoadImage", 1),
          ("mwDeleteSecondaryImage", 2),
          ("mwDeletePrimaryImage", 3),
          ("mwDuplicateImage", 4),
          ("mwSwapImage", 5),
          ("mwCommitImage", 6),
          ("mwRestartModule", 7))
    )


_MwImageControl_Type.__name__ = "Integer32"
_MwImageControl_Object = MibTableColumn
mwImageControl = _MwImageControl_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 20, 1, 1, 2),
    _MwImageControl_Type()
)
mwImageControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwImageControl.setStatus("mandatory")


class _MwPrimaryImageStatus_Type(Integer32):
    """Custom type mwPrimaryImageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mwLoadingImage", 1),
          ("mwImagePresent", 2),
          ("mwNoImage", 3))
    )


_MwPrimaryImageStatus_Type.__name__ = "Integer32"
_MwPrimaryImageStatus_Object = MibTableColumn
mwPrimaryImageStatus = _MwPrimaryImageStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 20, 1, 1, 3),
    _MwPrimaryImageStatus_Type()
)
mwPrimaryImageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPrimaryImageStatus.setStatus("mandatory")
_MwPrimaryImageName_Type = DisplayString
_MwPrimaryImageName_Object = MibTableColumn
mwPrimaryImageName = _MwPrimaryImageName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 20, 1, 1, 4),
    _MwPrimaryImageName_Type()
)
mwPrimaryImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPrimaryImageName.setStatus("mandatory")


class _MwSecondaryImageStatus_Type(Integer32):
    """Custom type mwSecondaryImageStatus based on Integer32"""
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
        *(("mwImagePresent", 1),
          ("mwImageLoadFailed", 2),
          ("mwLoadingImage", 3),
          ("mwNoImage", 4))
    )


_MwSecondaryImageStatus_Type.__name__ = "Integer32"
_MwSecondaryImageStatus_Object = MibTableColumn
mwSecondaryImageStatus = _MwSecondaryImageStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 20, 1, 1, 6),
    _MwSecondaryImageStatus_Type()
)
mwSecondaryImageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSecondaryImageStatus.setStatus("mandatory")
_MwSecondaryImageName_Type = DisplayString
_MwSecondaryImageName_Object = MibTableColumn
mwSecondaryImageName = _MwSecondaryImageName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 20, 1, 1, 7),
    _MwSecondaryImageName_Type()
)
mwSecondaryImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSecondaryImageName.setStatus("mandatory")
_MwImageLoadFrom_Type = DisplayString
_MwImageLoadFrom_Object = MibTableColumn
mwImageLoadFrom = _MwImageLoadFrom_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 20, 1, 1, 8),
    _MwImageLoadFrom_Type()
)
mwImageLoadFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwImageLoadFrom.setStatus("mandatory")
_MwImageLastStatus_Type = Integer32
_MwImageLastStatus_Object = MibTableColumn
mwImageLastStatus = _MwImageLastStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 20, 1, 1, 9),
    _MwImageLastStatus_Type()
)
mwImageLastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwImageLastStatus.setStatus("mandatory")
_TxcvrTable_Object = MibTable
txcvrTable = _TxcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21)
)
if mibBuilder.loadTexts:
    txcvrTable.setStatus("mandatory")
_TxcvrEntry_Object = MibTableRow
txcvrEntry = _TxcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1)
)
txcvrEntry.setIndexNames(
    (0, "CIENA-MIBv2", "shelfId"),
    (0, "CIENA-MIBv2", "slotId"),
)
if mibBuilder.loadTexts:
    txcvrEntry.setStatus("mandatory")
_MpTxcvrGratingTemperature_Type = Integer32
_MpTxcvrGratingTemperature_Object = MibTableColumn
mpTxcvrGratingTemperature = _MpTxcvrGratingTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 1),
    _MpTxcvrGratingTemperature_Type()
)
mpTxcvrGratingTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTxcvrGratingTemperature.setStatus("mandatory")
_MpTxcvrSrLaserPower_Type = Integer32
_MpTxcvrSrLaserPower_Object = MibTableColumn
mpTxcvrSrLaserPower = _MpTxcvrSrLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 2),
    _MpTxcvrSrLaserPower_Type()
)
mpTxcvrSrLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTxcvrSrLaserPower.setStatus("mandatory")
_SpTxcvrSrLaserPower_Type = Integer32
_SpTxcvrSrLaserPower_Object = MibTableColumn
spTxcvrSrLaserPower = _SpTxcvrSrLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 3),
    _SpTxcvrSrLaserPower_Type()
)
spTxcvrSrLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTxcvrSrLaserPower.setStatus("mandatory")
_MpTxcvrSrLaserCurrent_Type = Integer32
_MpTxcvrSrLaserCurrent_Object = MibTableColumn
mpTxcvrSrLaserCurrent = _MpTxcvrSrLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 4),
    _MpTxcvrSrLaserCurrent_Type()
)
mpTxcvrSrLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTxcvrSrLaserCurrent.setStatus("mandatory")
_MpTxcvrSrInputSignalLevel_Type = Integer32
_MpTxcvrSrInputSignalLevel_Object = MibTableColumn
mpTxcvrSrInputSignalLevel = _MpTxcvrSrInputSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 5),
    _MpTxcvrSrInputSignalLevel_Type()
)
mpTxcvrSrInputSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTxcvrSrInputSignalLevel.setStatus("mandatory")


class _SpTxcvrSrLaserConfiguredState_Type(Integer32):
    """Custom type spTxcvrSrLaserConfiguredState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("deactivated", 2),
          ("shutdown", 3))
    )


_SpTxcvrSrLaserConfiguredState_Type.__name__ = "Integer32"
_SpTxcvrSrLaserConfiguredState_Object = MibTableColumn
spTxcvrSrLaserConfiguredState = _SpTxcvrSrLaserConfiguredState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 6),
    _SpTxcvrSrLaserConfiguredState_Type()
)
spTxcvrSrLaserConfiguredState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTxcvrSrLaserConfiguredState.setStatus("mandatory")


class _MpTxcvrSrLaserState_Type(Integer32):
    """Custom type mpTxcvrSrLaserState based on Integer32"""
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
        *(("off", 1),
          ("preheat", 2),
          ("on", 3),
          ("tracking", 4),
          ("locked", 5),
          ("safetyShutdown", 6))
    )


_MpTxcvrSrLaserState_Type.__name__ = "Integer32"
_MpTxcvrSrLaserState_Object = MibTableColumn
mpTxcvrSrLaserState = _MpTxcvrSrLaserState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 7),
    _MpTxcvrSrLaserState_Type()
)
mpTxcvrSrLaserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTxcvrSrLaserState.setStatus("mandatory")


class _MpTxcvrSrLaserShutdownCause_Type(Integer32):
    """Custom type mpTxcvrSrLaserShutdownCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              9)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("noInputSignal", 2),
          ("noSonetLock", 3),
          ("sonetLof", 4),
          ("noModEnergy", 5),
          ("unknown", 9))
    )


_MpTxcvrSrLaserShutdownCause_Type.__name__ = "Integer32"
_MpTxcvrSrLaserShutdownCause_Object = MibTableColumn
mpTxcvrSrLaserShutdownCause = _MpTxcvrSrLaserShutdownCause_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 8),
    _MpTxcvrSrLaserShutdownCause_Type()
)
mpTxcvrSrLaserShutdownCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTxcvrSrLaserShutdownCause.setStatus("mandatory")
_SpTxcvrSrLosThreshold_Type = Integer32
_SpTxcvrSrLosThreshold_Object = MibTableColumn
spTxcvrSrLosThreshold = _SpTxcvrSrLosThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 9),
    _SpTxcvrSrLosThreshold_Type()
)
spTxcvrSrLosThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTxcvrSrLosThreshold.setStatus("mandatory")


class _SpTxcvrRxMaintenance_Type(Integer32):
    """Custom type spTxcvrRxMaintenance based on Integer32"""
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


_SpTxcvrRxMaintenance_Type.__name__ = "Integer32"
_SpTxcvrRxMaintenance_Object = MibTableColumn
spTxcvrRxMaintenance = _SpTxcvrRxMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 10),
    _SpTxcvrRxMaintenance_Type()
)
spTxcvrRxMaintenance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTxcvrRxMaintenance.setStatus("mandatory")


class _SpTxcvrSrAutoShutdown_Type(Integer32):
    """Custom type spTxcvrSrAutoShutdown based on Integer32"""
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


_SpTxcvrSrAutoShutdown_Type.__name__ = "Integer32"
_SpTxcvrSrAutoShutdown_Object = MibTableColumn
spTxcvrSrAutoShutdown = _SpTxcvrSrAutoShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 11),
    _SpTxcvrSrAutoShutdown_Type()
)
spTxcvrSrAutoShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTxcvrSrAutoShutdown.setStatus("mandatory")


class _MpTxcvrSrCurrentLimited_Type(Integer32):
    """Custom type mpTxcvrSrCurrentLimited based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_MpTxcvrSrCurrentLimited_Type.__name__ = "Integer32"
_MpTxcvrSrCurrentLimited_Object = MibTableColumn
mpTxcvrSrCurrentLimited = _MpTxcvrSrCurrentLimited_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 12),
    _MpTxcvrSrCurrentLimited_Type()
)
mpTxcvrSrCurrentLimited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTxcvrSrCurrentLimited.setStatus("mandatory")
_MpTxcvrDfbLaserPower_Type = Integer32
_MpTxcvrDfbLaserPower_Object = MibTableColumn
mpTxcvrDfbLaserPower = _MpTxcvrDfbLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 13),
    _MpTxcvrDfbLaserPower_Type()
)
mpTxcvrDfbLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTxcvrDfbLaserPower.setStatus("mandatory")
_SpTxcvrDfbLaserPower_Type = Integer32
_SpTxcvrDfbLaserPower_Object = MibTableColumn
spTxcvrDfbLaserPower = _SpTxcvrDfbLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 14),
    _SpTxcvrDfbLaserPower_Type()
)
spTxcvrDfbLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTxcvrDfbLaserPower.setStatus("mandatory")
_MpTxcvrDfbLaserCurrent_Type = Integer32
_MpTxcvrDfbLaserCurrent_Object = MibTableColumn
mpTxcvrDfbLaserCurrent = _MpTxcvrDfbLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 15),
    _MpTxcvrDfbLaserCurrent_Type()
)
mpTxcvrDfbLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTxcvrDfbLaserCurrent.setStatus("mandatory")
_MpTxcvrDfbLaserTemp_Type = Integer32
_MpTxcvrDfbLaserTemp_Object = MibTableColumn
mpTxcvrDfbLaserTemp = _MpTxcvrDfbLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 16),
    _MpTxcvrDfbLaserTemp_Type()
)
mpTxcvrDfbLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTxcvrDfbLaserTemp.setStatus("mandatory")
_SpTxcvrDfbLaserTemp_Type = Integer32
_SpTxcvrDfbLaserTemp_Object = MibTableColumn
spTxcvrDfbLaserTemp = _SpTxcvrDfbLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 17),
    _SpTxcvrDfbLaserTemp_Type()
)
spTxcvrDfbLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTxcvrDfbLaserTemp.setStatus("mandatory")


class _SpTxcvrDfbLaserConfiguredState_Type(Integer32):
    """Custom type spTxcvrDfbLaserConfiguredState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("deactivated", 2),
          ("shutdown", 3))
    )


_SpTxcvrDfbLaserConfiguredState_Type.__name__ = "Integer32"
_SpTxcvrDfbLaserConfiguredState_Object = MibTableColumn
spTxcvrDfbLaserConfiguredState = _SpTxcvrDfbLaserConfiguredState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 18),
    _SpTxcvrDfbLaserConfiguredState_Type()
)
spTxcvrDfbLaserConfiguredState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTxcvrDfbLaserConfiguredState.setStatus("mandatory")


class _MpTxcvrDfbLaserState_Type(Integer32):
    """Custom type mpTxcvrDfbLaserState based on Integer32"""
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
        *(("off", 1),
          ("preheat", 2),
          ("on", 3),
          ("tracking", 4),
          ("locked", 5),
          ("safetyShutdown", 6))
    )


_MpTxcvrDfbLaserState_Type.__name__ = "Integer32"
_MpTxcvrDfbLaserState_Object = MibTableColumn
mpTxcvrDfbLaserState = _MpTxcvrDfbLaserState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 19),
    _MpTxcvrDfbLaserState_Type()
)
mpTxcvrDfbLaserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTxcvrDfbLaserState.setStatus("mandatory")


class _SpTxcvrDfbSubcarrier_Type(Integer32):
    """Custom type spTxcvrDfbSubcarrier based on Integer32"""
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


_SpTxcvrDfbSubcarrier_Type.__name__ = "Integer32"
_SpTxcvrDfbSubcarrier_Object = MibTableColumn
spTxcvrDfbSubcarrier = _SpTxcvrDfbSubcarrier_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 20),
    _SpTxcvrDfbSubcarrier_Type()
)
spTxcvrDfbSubcarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTxcvrDfbSubcarrier.setStatus("mandatory")


class _SpTxcvrTxMaintenance_Type(Integer32):
    """Custom type spTxcvrTxMaintenance based on Integer32"""
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


_SpTxcvrTxMaintenance_Type.__name__ = "Integer32"
_SpTxcvrTxMaintenance_Object = MibTableColumn
spTxcvrTxMaintenance = _SpTxcvrTxMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 21),
    _SpTxcvrTxMaintenance_Type()
)
spTxcvrTxMaintenance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTxcvrTxMaintenance.setStatus("mandatory")


class _MpTxcvrDfbCurrentLimited_Type(Integer32):
    """Custom type mpTxcvrDfbCurrentLimited based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_MpTxcvrDfbCurrentLimited_Type.__name__ = "Integer32"
_MpTxcvrDfbCurrentLimited_Object = MibTableColumn
mpTxcvrDfbCurrentLimited = _MpTxcvrDfbCurrentLimited_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 22),
    _MpTxcvrDfbCurrentLimited_Type()
)
mpTxcvrDfbCurrentLimited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTxcvrDfbCurrentLimited.setStatus("mandatory")


class _MpTxcvrDfbLaserShutdownCause_Type(Integer32):
    """Custom type mpTxcvrDfbLaserShutdownCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("gratingTempUnstable", 7),
          ("laserTempUnstable", 8),
          ("unknown", 9))
    )


_MpTxcvrDfbLaserShutdownCause_Type.__name__ = "Integer32"
_MpTxcvrDfbLaserShutdownCause_Object = MibTableColumn
mpTxcvrDfbLaserShutdownCause = _MpTxcvrDfbLaserShutdownCause_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 23),
    _MpTxcvrDfbLaserShutdownCause_Type()
)
mpTxcvrDfbLaserShutdownCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTxcvrDfbLaserShutdownCause.setStatus("mandatory")


class _MpTxcvrDfbAutoShutdownEnable_Type(Integer32):
    """Custom type mpTxcvrDfbAutoShutdownEnable based on Integer32"""
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


_MpTxcvrDfbAutoShutdownEnable_Type.__name__ = "Integer32"
_MpTxcvrDfbAutoShutdownEnable_Object = MibTableColumn
mpTxcvrDfbAutoShutdownEnable = _MpTxcvrDfbAutoShutdownEnable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 24),
    _MpTxcvrDfbAutoShutdownEnable_Type()
)
mpTxcvrDfbAutoShutdownEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTxcvrDfbAutoShutdownEnable.setStatus("mandatory")
_MpTxcvrApdInputSignalLevel_Type = Integer32
_MpTxcvrApdInputSignalLevel_Object = MibTableColumn
mpTxcvrApdInputSignalLevel = _MpTxcvrApdInputSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 25),
    _MpTxcvrApdInputSignalLevel_Type()
)
mpTxcvrApdInputSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTxcvrApdInputSignalLevel.setStatus("mandatory")
_MpTxcvrHeatSinkTemperature_Type = Integer32
_MpTxcvrHeatSinkTemperature_Object = MibTableColumn
mpTxcvrHeatSinkTemperature = _MpTxcvrHeatSinkTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 26),
    _MpTxcvrHeatSinkTemperature_Type()
)
mpTxcvrHeatSinkTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTxcvrHeatSinkTemperature.setStatus("mandatory")
_MpTxcvrTECCurrent_Type = Integer32
_MpTxcvrTECCurrent_Object = MibTableColumn
mpTxcvrTECCurrent = _MpTxcvrTECCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 27),
    _MpTxcvrTECCurrent_Type()
)
mpTxcvrTECCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTxcvrTECCurrent.setStatus("mandatory")


class _MpTxcvrTECHeaterStatus_Type(Integer32):
    """Custom type mpTxcvrTECHeaterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("failed", 2))
    )


_MpTxcvrTECHeaterStatus_Type.__name__ = "Integer32"
_MpTxcvrTECHeaterStatus_Object = MibTableColumn
mpTxcvrTECHeaterStatus = _MpTxcvrTECHeaterStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 28),
    _MpTxcvrTECHeaterStatus_Type()
)
mpTxcvrTECHeaterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTxcvrTECHeaterStatus.setStatus("mandatory")


class _MpTxcvrGratingHeaterStatus_Type(Integer32):
    """Custom type mpTxcvrGratingHeaterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("degraded", 2),
          ("failed", 3))
    )


_MpTxcvrGratingHeaterStatus_Type.__name__ = "Integer32"
_MpTxcvrGratingHeaterStatus_Object = MibTableColumn
mpTxcvrGratingHeaterStatus = _MpTxcvrGratingHeaterStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 29),
    _MpTxcvrGratingHeaterStatus_Type()
)
mpTxcvrGratingHeaterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTxcvrGratingHeaterStatus.setStatus("mandatory")
_FcTxcvrWavelength_Type = Integer32
_FcTxcvrWavelength_Object = MibTableColumn
fcTxcvrWavelength = _FcTxcvrWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 30),
    _FcTxcvrWavelength_Type()
)
fcTxcvrWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcTxcvrWavelength.setStatus("mandatory")


class _TxcvrOKLED_Type(Integer32):
    """Custom type txcvrOKLED based on Integer32"""
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


_TxcvrOKLED_Type.__name__ = "Integer32"
_TxcvrOKLED_Object = MibTableColumn
txcvrOKLED = _TxcvrOKLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 31),
    _TxcvrOKLED_Type()
)
txcvrOKLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txcvrOKLED.setStatus("mandatory")


class _TxcvrMajorLED_Type(Integer32):
    """Custom type txcvrMajorLED based on Integer32"""
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


_TxcvrMajorLED_Type.__name__ = "Integer32"
_TxcvrMajorLED_Object = MibTableColumn
txcvrMajorLED = _TxcvrMajorLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 32),
    _TxcvrMajorLED_Type()
)
txcvrMajorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txcvrMajorLED.setStatus("mandatory")


class _TxcvrMinorLED_Type(Integer32):
    """Custom type txcvrMinorLED based on Integer32"""
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


_TxcvrMinorLED_Type.__name__ = "Integer32"
_TxcvrMinorLED_Object = MibTableColumn
txcvrMinorLED = _TxcvrMinorLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 33),
    _TxcvrMinorLED_Type()
)
txcvrMinorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txcvrMinorLED.setStatus("mandatory")


class _TxcvrMaintenanceLED_Type(Integer32):
    """Custom type txcvrMaintenanceLED based on Integer32"""
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


_TxcvrMaintenanceLED_Type.__name__ = "Integer32"
_TxcvrMaintenanceLED_Object = MibTableColumn
txcvrMaintenanceLED = _TxcvrMaintenanceLED_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 34),
    _TxcvrMaintenanceLED_Type()
)
txcvrMaintenanceLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txcvrMaintenanceLED.setStatus("mandatory")
_TxcvrChannelTag1_Type = OctetString
_TxcvrChannelTag1_Object = MibTableColumn
txcvrChannelTag1 = _TxcvrChannelTag1_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 35),
    _TxcvrChannelTag1_Type()
)
txcvrChannelTag1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txcvrChannelTag1.setStatus("mandatory")
_TxcvrChannelTag2_Type = OctetString
_TxcvrChannelTag2_Object = MibTableColumn
txcvrChannelTag2 = _TxcvrChannelTag2_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 21, 1, 36),
    _TxcvrChannelTag2_Type()
)
txcvrChannelTag2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txcvrChannelTag2.setStatus("mandatory")
_FfIoTable_Object = MibTable
ffIoTable = _FfIoTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 22)
)
if mibBuilder.loadTexts:
    ffIoTable.setStatus("mandatory")
_FfIoEntry_Object = MibTableRow
ffIoEntry = _FfIoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 22, 1)
)
ffIoEntry.setIndexNames(
    (0, "CIENA-MIBv2", "shelfId"),
    (0, "CIENA-MIBv2", "slotId"),
)
if mibBuilder.loadTexts:
    ffIoEntry.setStatus("mandatory")
_MpFfIoAmbientTemperature_Type = Integer32
_MpFfIoAmbientTemperature_Object = MibTableColumn
mpFfIoAmbientTemperature = _MpFfIoAmbientTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 22, 1, 1),
    _MpFfIoAmbientTemperature_Type()
)
mpFfIoAmbientTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFfIoAmbientTemperature.setStatus("mandatory")
_MpFfIoFanPresent_Type = Integer32
_MpFfIoFanPresent_Object = MibTableColumn
mpFfIoFanPresent = _MpFfIoFanPresent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 22, 1, 2),
    _MpFfIoFanPresent_Type()
)
mpFfIoFanPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFfIoFanPresent.setStatus("mandatory")
_MpFfIoFanFail_Type = Integer32
_MpFfIoFanFail_Object = MibTableColumn
mpFfIoFanFail = _MpFfIoFanFail_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 22, 1, 3),
    _MpFfIoFanFail_Type()
)
mpFfIoFanFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFfIoFanFail.setStatus("mandatory")
_MpFfIoFuseFail_Type = Integer32
_MpFfIoFuseFail_Object = MibTableColumn
mpFfIoFuseFail = _MpFfIoFuseFail_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 22, 1, 4),
    _MpFfIoFuseFail_Type()
)
mpFfIoFuseFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFfIoFuseFail.setStatus("mandatory")
_SpFfIoResetModule_Type = Integer32
_SpFfIoResetModule_Object = MibTableColumn
spFfIoResetModule = _SpFfIoResetModule_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 22, 1, 5),
    _SpFfIoResetModule_Type()
)
spFfIoResetModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spFfIoResetModule.setStatus("mandatory")
_SpFfIoResetIoController_Type = Integer32
_SpFfIoResetIoController_Object = MibTableColumn
spFfIoResetIoController = _SpFfIoResetIoController_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 22, 1, 6),
    _SpFfIoResetIoController_Type()
)
spFfIoResetIoController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spFfIoResetIoController.setStatus("mandatory")
_MpFfIoLedCritical_Type = Integer32
_MpFfIoLedCritical_Object = MibTableColumn
mpFfIoLedCritical = _MpFfIoLedCritical_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 22, 1, 7),
    _MpFfIoLedCritical_Type()
)
mpFfIoLedCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFfIoLedCritical.setStatus("mandatory")
_MpFfIoLedMajor_Type = Integer32
_MpFfIoLedMajor_Object = MibTableColumn
mpFfIoLedMajor = _MpFfIoLedMajor_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 22, 1, 8),
    _MpFfIoLedMajor_Type()
)
mpFfIoLedMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFfIoLedMajor.setStatus("mandatory")
_MpFfIoLedMinor_Type = Integer32
_MpFfIoLedMinor_Object = MibTableColumn
mpFfIoLedMinor = _MpFfIoLedMinor_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 22, 1, 9),
    _MpFfIoLedMinor_Type()
)
mpFfIoLedMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFfIoLedMinor.setStatus("mandatory")
_MpFfIoLedOutOfService_Type = Integer32
_MpFfIoLedOutOfService_Object = MibTableColumn
mpFfIoLedOutOfService = _MpFfIoLedOutOfService_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 22, 1, 10),
    _MpFfIoLedOutOfService_Type()
)
mpFfIoLedOutOfService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFfIoLedOutOfService.setStatus("mandatory")
_MpFfIoLedNormal_Type = Integer32
_MpFfIoLedNormal_Object = MibTableColumn
mpFfIoLedNormal = _MpFfIoLedNormal_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 22, 1, 11),
    _MpFfIoLedNormal_Type()
)
mpFfIoLedNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFfIoLedNormal.setStatus("mandatory")
_FfMuxDemElectricalTable_Object = MibTable
ffMuxDemElectricalTable = _FfMuxDemElectricalTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 23)
)
if mibBuilder.loadTexts:
    ffMuxDemElectricalTable.setStatus("mandatory")
_FfMuxDemElectricalEntry_Object = MibTableRow
ffMuxDemElectricalEntry = _FfMuxDemElectricalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 23, 1)
)
ffMuxDemElectricalEntry.setIndexNames(
    (0, "CIENA-MIBv2", "shelfId"),
    (0, "CIENA-MIBv2", "slotId"),
)
if mibBuilder.loadTexts:
    ffMuxDemElectricalEntry.setStatus("mandatory")
_MpFfMuxDemElectricalMuxHeater_Type = Integer32
_MpFfMuxDemElectricalMuxHeater_Object = MibTableColumn
mpFfMuxDemElectricalMuxHeater = _MpFfMuxDemElectricalMuxHeater_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 23, 1, 1),
    _MpFfMuxDemElectricalMuxHeater_Type()
)
mpFfMuxDemElectricalMuxHeater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFfMuxDemElectricalMuxHeater.setStatus("mandatory")
_MpFfMuxDemElectricalDemuxHeater_Type = Integer32
_MpFfMuxDemElectricalDemuxHeater_Object = MibTableColumn
mpFfMuxDemElectricalDemuxHeater = _MpFfMuxDemElectricalDemuxHeater_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 23, 1, 2),
    _MpFfMuxDemElectricalDemuxHeater_Type()
)
mpFfMuxDemElectricalDemuxHeater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFfMuxDemElectricalDemuxHeater.setStatus("mandatory")
_MpFfMuxDemElectricalMuxHeaterStatus_Type = Integer32
_MpFfMuxDemElectricalMuxHeaterStatus_Object = MibTableColumn
mpFfMuxDemElectricalMuxHeaterStatus = _MpFfMuxDemElectricalMuxHeaterStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 23, 1, 3),
    _MpFfMuxDemElectricalMuxHeaterStatus_Type()
)
mpFfMuxDemElectricalMuxHeaterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFfMuxDemElectricalMuxHeaterStatus.setStatus("mandatory")
_MpFfMuxDemElectricalDemuxHeaterStatus_Type = Integer32
_MpFfMuxDemElectricalDemuxHeaterStatus_Object = MibTableColumn
mpFfMuxDemElectricalDemuxHeaterStatus = _MpFfMuxDemElectricalDemuxHeaterStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 23, 1, 4),
    _MpFfMuxDemElectricalDemuxHeaterStatus_Type()
)
mpFfMuxDemElectricalDemuxHeaterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFfMuxDemElectricalDemuxHeaterStatus.setStatus("mandatory")
_MpFfMuxDemElectricalMuxOutput_Type = Integer32
_MpFfMuxDemElectricalMuxOutput_Object = MibTableColumn
mpFfMuxDemElectricalMuxOutput = _MpFfMuxDemElectricalMuxOutput_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 23, 1, 5),
    _MpFfMuxDemElectricalMuxOutput_Type()
)
mpFfMuxDemElectricalMuxOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFfMuxDemElectricalMuxOutput.setStatus("mandatory")
_MpFfMuxDemElectricalDemuxInput_Type = Integer32
_MpFfMuxDemElectricalDemuxInput_Object = MibTableColumn
mpFfMuxDemElectricalDemuxInput = _MpFfMuxDemElectricalDemuxInput_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 23, 1, 6),
    _MpFfMuxDemElectricalDemuxInput_Type()
)
mpFfMuxDemElectricalDemuxInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpFfMuxDemElectricalDemuxInput.setStatus("mandatory")
_RcvrTable_Object = MibTable
rcvrTable = _RcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24)
)
if mibBuilder.loadTexts:
    rcvrTable.setStatus("mandatory")
_RcvrEntry_Object = MibTableRow
rcvrEntry = _RcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1)
)
rcvrEntry.setIndexNames(
    (0, "CIENA-MIBv2", "shelfId"),
    (0, "CIENA-MIBv2", "slotId"),
)
if mibBuilder.loadTexts:
    rcvrEntry.setStatus("mandatory")
_MpRcvrTopLaserPower_Type = Integer32
_MpRcvrTopLaserPower_Object = MibTableColumn
mpRcvrTopLaserPower = _MpRcvrTopLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 1),
    _MpRcvrTopLaserPower_Type()
)
mpRcvrTopLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrTopLaserPower.setStatus("mandatory")
_MpRcvrBotLaserPower_Type = Integer32
_MpRcvrBotLaserPower_Object = MibTableColumn
mpRcvrBotLaserPower = _MpRcvrBotLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 2),
    _MpRcvrBotLaserPower_Type()
)
mpRcvrBotLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrBotLaserPower.setStatus("mandatory")
_MpRcvrTopGratingTemp_Type = Integer32
_MpRcvrTopGratingTemp_Object = MibTableColumn
mpRcvrTopGratingTemp = _MpRcvrTopGratingTemp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 3),
    _MpRcvrTopGratingTemp_Type()
)
mpRcvrTopGratingTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrTopGratingTemp.setStatus("mandatory")
_MpRcvrBotGratingTemp_Type = Integer32
_MpRcvrBotGratingTemp_Object = MibTableColumn
mpRcvrBotGratingTemp = _MpRcvrBotGratingTemp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 4),
    _MpRcvrBotGratingTemp_Type()
)
mpRcvrBotGratingTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrBotGratingTemp.setStatus("mandatory")
_MpRcvrTopInputSignal_Type = Integer32
_MpRcvrTopInputSignal_Object = MibTableColumn
mpRcvrTopInputSignal = _MpRcvrTopInputSignal_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 5),
    _MpRcvrTopInputSignal_Type()
)
mpRcvrTopInputSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrTopInputSignal.setStatus("mandatory")
_MpRcvrBotInputSignal_Type = Integer32
_MpRcvrBotInputSignal_Object = MibTableColumn
mpRcvrBotInputSignal = _MpRcvrBotInputSignal_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 6),
    _MpRcvrBotInputSignal_Type()
)
mpRcvrBotInputSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrBotInputSignal.setStatus("mandatory")
_MpRcvrTopLaserCurrent_Type = Integer32
_MpRcvrTopLaserCurrent_Object = MibTableColumn
mpRcvrTopLaserCurrent = _MpRcvrTopLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 7),
    _MpRcvrTopLaserCurrent_Type()
)
mpRcvrTopLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrTopLaserCurrent.setStatus("mandatory")
_MpRcvrBotLaserCurrent_Type = Integer32
_MpRcvrBotLaserCurrent_Object = MibTableColumn
mpRcvrBotLaserCurrent = _MpRcvrBotLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 8),
    _MpRcvrBotLaserCurrent_Type()
)
mpRcvrBotLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrBotLaserCurrent.setStatus("mandatory")
_MpRcvrTopHeaterStatus_Type = Integer32
_MpRcvrTopHeaterStatus_Object = MibTableColumn
mpRcvrTopHeaterStatus = _MpRcvrTopHeaterStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 9),
    _MpRcvrTopHeaterStatus_Type()
)
mpRcvrTopHeaterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrTopHeaterStatus.setStatus("mandatory")
_MpRcvrBotHeaterStatus_Type = Integer32
_MpRcvrBotHeaterStatus_Object = MibTableColumn
mpRcvrBotHeaterStatus = _MpRcvrBotHeaterStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 10),
    _MpRcvrBotHeaterStatus_Type()
)
mpRcvrBotHeaterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrBotHeaterStatus.setStatus("mandatory")
_MpRcvrTopWavelength_Type = Integer32
_MpRcvrTopWavelength_Object = MibTableColumn
mpRcvrTopWavelength = _MpRcvrTopWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 11),
    _MpRcvrTopWavelength_Type()
)
mpRcvrTopWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrTopWavelength.setStatus("mandatory")
_MpRcvrBotWavelength_Type = Integer32
_MpRcvrBotWavelength_Object = MibTableColumn
mpRcvrBotWavelength = _MpRcvrBotWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 12),
    _MpRcvrBotWavelength_Type()
)
mpRcvrBotWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrBotWavelength.setStatus("mandatory")
_SpRcvrTopLaserCurrent_Type = Integer32
_SpRcvrTopLaserCurrent_Object = MibTableColumn
spRcvrTopLaserCurrent = _SpRcvrTopLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 13),
    _SpRcvrTopLaserCurrent_Type()
)
spRcvrTopLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spRcvrTopLaserCurrent.setStatus("mandatory")
_SpRcvrBotLaserCurrent_Type = Integer32
_SpRcvrBotLaserCurrent_Object = MibTableColumn
spRcvrBotLaserCurrent = _SpRcvrBotLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 14),
    _SpRcvrBotLaserCurrent_Type()
)
spRcvrBotLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spRcvrBotLaserCurrent.setStatus("mandatory")
_SpRcvrTopLaserPower_Type = Integer32
_SpRcvrTopLaserPower_Object = MibTableColumn
spRcvrTopLaserPower = _SpRcvrTopLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 15),
    _SpRcvrTopLaserPower_Type()
)
spRcvrTopLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spRcvrTopLaserPower.setStatus("mandatory")
_SpRcvrBotLaserPower_Type = Integer32
_SpRcvrBotLaserPower_Object = MibTableColumn
spRcvrBotLaserPower = _SpRcvrBotLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 16),
    _SpRcvrBotLaserPower_Type()
)
spRcvrBotLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spRcvrBotLaserPower.setStatus("mandatory")
_SpRcvrTopGratingTemp_Type = Integer32
_SpRcvrTopGratingTemp_Object = MibTableColumn
spRcvrTopGratingTemp = _SpRcvrTopGratingTemp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 17),
    _SpRcvrTopGratingTemp_Type()
)
spRcvrTopGratingTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spRcvrTopGratingTemp.setStatus("mandatory")
_SpRcvrBotGratingTemp_Type = Integer32
_SpRcvrBotGratingTemp_Object = MibTableColumn
spRcvrBotGratingTemp = _SpRcvrBotGratingTemp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 18),
    _SpRcvrBotGratingTemp_Type()
)
spRcvrBotGratingTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spRcvrBotGratingTemp.setStatus("mandatory")
_SpRcvrTopLos_Type = Integer32
_SpRcvrTopLos_Object = MibTableColumn
spRcvrTopLos = _SpRcvrTopLos_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 19),
    _SpRcvrTopLos_Type()
)
spRcvrTopLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spRcvrTopLos.setStatus("mandatory")
_SpRcvrBotLos_Type = Integer32
_SpRcvrBotLos_Object = MibTableColumn
spRcvrBotLos = _SpRcvrBotLos_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 20),
    _SpRcvrBotLos_Type()
)
spRcvrBotLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spRcvrBotLos.setStatus("mandatory")
_MpRcvrTopChnlTag1_Type = OctetString
_MpRcvrTopChnlTag1_Object = MibTableColumn
mpRcvrTopChnlTag1 = _MpRcvrTopChnlTag1_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 21),
    _MpRcvrTopChnlTag1_Type()
)
mpRcvrTopChnlTag1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrTopChnlTag1.setStatus("mandatory")
_MpRcvrTopChnlTag2_Type = OctetString
_MpRcvrTopChnlTag2_Object = MibTableColumn
mpRcvrTopChnlTag2 = _MpRcvrTopChnlTag2_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 22),
    _MpRcvrTopChnlTag2_Type()
)
mpRcvrTopChnlTag2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrTopChnlTag2.setStatus("mandatory")
_MpRcvrBotChnlTag1_Type = OctetString
_MpRcvrBotChnlTag1_Object = MibTableColumn
mpRcvrBotChnlTag1 = _MpRcvrBotChnlTag1_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 23),
    _MpRcvrBotChnlTag1_Type()
)
mpRcvrBotChnlTag1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrBotChnlTag1.setStatus("mandatory")
_MpRcvrBotChnlTag2_Type = OctetString
_MpRcvrBotChnlTag2_Object = MibTableColumn
mpRcvrBotChnlTag2 = _MpRcvrBotChnlTag2_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 24),
    _MpRcvrBotChnlTag2_Type()
)
mpRcvrBotChnlTag2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrBotChnlTag2.setStatus("mandatory")
_MpRcvrTopMaint_Type = Integer32
_MpRcvrTopMaint_Object = MibTableColumn
mpRcvrTopMaint = _MpRcvrTopMaint_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 25),
    _MpRcvrTopMaint_Type()
)
mpRcvrTopMaint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrTopMaint.setStatus("mandatory")
_MpRcvrBotMaint_Type = Integer32
_MpRcvrBotMaint_Object = MibTableColumn
mpRcvrBotMaint = _MpRcvrBotMaint_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 26),
    _MpRcvrBotMaint_Type()
)
mpRcvrBotMaint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrBotMaint.setStatus("mandatory")
_MpRcvrTopLaserConfig_Type = Integer32
_MpRcvrTopLaserConfig_Object = MibTableColumn
mpRcvrTopLaserConfig = _MpRcvrTopLaserConfig_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 27),
    _MpRcvrTopLaserConfig_Type()
)
mpRcvrTopLaserConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrTopLaserConfig.setStatus("mandatory")
_MpRcvrBotLaserConfig_Type = Integer32
_MpRcvrBotLaserConfig_Object = MibTableColumn
mpRcvrBotLaserConfig = _MpRcvrBotLaserConfig_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 28),
    _MpRcvrBotLaserConfig_Type()
)
mpRcvrBotLaserConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrBotLaserConfig.setStatus("mandatory")
_MpRcvrTopOpmode_Type = Integer32
_MpRcvrTopOpmode_Object = MibTableColumn
mpRcvrTopOpmode = _MpRcvrTopOpmode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 29),
    _MpRcvrTopOpmode_Type()
)
mpRcvrTopOpmode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrTopOpmode.setStatus("mandatory")
_MpRcvrBotOpmode_Type = Integer32
_MpRcvrBotOpmode_Object = MibTableColumn
mpRcvrBotOpmode = _MpRcvrBotOpmode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 30),
    _MpRcvrBotOpmode_Type()
)
mpRcvrBotOpmode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrBotOpmode.setStatus("mandatory")
_MpRcvrTopLaserState_Type = Integer32
_MpRcvrTopLaserState_Object = MibTableColumn
mpRcvrTopLaserState = _MpRcvrTopLaserState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 31),
    _MpRcvrTopLaserState_Type()
)
mpRcvrTopLaserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrTopLaserState.setStatus("mandatory")
_MpRcvrBotLaserState_Type = Integer32
_MpRcvrBotLaserState_Object = MibTableColumn
mpRcvrBotLaserState = _MpRcvrBotLaserState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 32),
    _MpRcvrBotLaserState_Type()
)
mpRcvrBotLaserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrBotLaserState.setStatus("mandatory")
_MpRcvrTopCV_Type = Integer32
_MpRcvrTopCV_Object = MibTableColumn
mpRcvrTopCV = _MpRcvrTopCV_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 33),
    _MpRcvrTopCV_Type()
)
mpRcvrTopCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrTopCV.setStatus("mandatory")
_MpRcvrBotCV_Type = Integer32
_MpRcvrBotCV_Object = MibTableColumn
mpRcvrBotCV = _MpRcvrBotCV_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 34),
    _MpRcvrBotCV_Type()
)
mpRcvrBotCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrBotCV.setStatus("mandatory")
_MpRcvrTopES_Type = Integer32
_MpRcvrTopES_Object = MibTableColumn
mpRcvrTopES = _MpRcvrTopES_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 35),
    _MpRcvrTopES_Type()
)
mpRcvrTopES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrTopES.setStatus("mandatory")
_MpRcvrBotES_Type = Integer32
_MpRcvrBotES_Object = MibTableColumn
mpRcvrBotES = _MpRcvrBotES_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 36),
    _MpRcvrBotES_Type()
)
mpRcvrBotES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrBotES.setStatus("mandatory")
_MpRcvrTopSES_Type = Integer32
_MpRcvrTopSES_Object = MibTableColumn
mpRcvrTopSES = _MpRcvrTopSES_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 37),
    _MpRcvrTopSES_Type()
)
mpRcvrTopSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrTopSES.setStatus("mandatory")
_MpRcvrBotSES_Type = Integer32
_MpRcvrBotSES_Object = MibTableColumn
mpRcvrBotSES = _MpRcvrBotSES_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 38),
    _MpRcvrBotSES_Type()
)
mpRcvrBotSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrBotSES.setStatus("mandatory")
_MpRcvrTopOFS_Type = Integer32
_MpRcvrTopOFS_Object = MibTableColumn
mpRcvrTopOFS = _MpRcvrTopOFS_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 39),
    _MpRcvrTopOFS_Type()
)
mpRcvrTopOFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrTopOFS.setStatus("mandatory")
_MpRcvrBotOFS_Type = Integer32
_MpRcvrBotOFS_Object = MibTableColumn
mpRcvrBotOFS = _MpRcvrBotOFS_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 40),
    _MpRcvrBotOFS_Type()
)
mpRcvrBotOFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrBotOFS.setStatus("mandatory")
_MpRcvrTopUAS_Type = Integer32
_MpRcvrTopUAS_Object = MibTableColumn
mpRcvrTopUAS = _MpRcvrTopUAS_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 41),
    _MpRcvrTopUAS_Type()
)
mpRcvrTopUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrTopUAS.setStatus("mandatory")
_MpRcvrBotUAS_Type = Integer32
_MpRcvrBotUAS_Object = MibTableColumn
mpRcvrBotUAS = _MpRcvrBotUAS_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 42),
    _MpRcvrBotUAS_Type()
)
mpRcvrBotUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrBotUAS.setStatus("mandatory")
_MpRcvrTopNCSES_Type = Integer32
_MpRcvrTopNCSES_Object = MibTableColumn
mpRcvrTopNCSES = _MpRcvrTopNCSES_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 43),
    _MpRcvrTopNCSES_Type()
)
mpRcvrTopNCSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrTopNCSES.setStatus("mandatory")
_MpRcvrBotNCSES_Type = Integer32
_MpRcvrBotNCSES_Object = MibTableColumn
mpRcvrBotNCSES = _MpRcvrBotNCSES_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 44),
    _MpRcvrBotNCSES_Type()
)
mpRcvrBotNCSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrBotNCSES.setStatus("mandatory")
_MpRcvrTopLastReset_Type = Integer32
_MpRcvrTopLastReset_Object = MibTableColumn
mpRcvrTopLastReset = _MpRcvrTopLastReset_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 45),
    _MpRcvrTopLastReset_Type()
)
mpRcvrTopLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrTopLastReset.setStatus("mandatory")
_MpRcvrBotLastReset_Type = Integer32
_MpRcvrBotLastReset_Object = MibTableColumn
mpRcvrBotLastReset = _MpRcvrBotLastReset_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 46),
    _MpRcvrBotLastReset_Type()
)
mpRcvrBotLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrBotLastReset.setStatus("mandatory")
_MpRcvrTopShutdownCause_Type = Integer32
_MpRcvrTopShutdownCause_Object = MibTableColumn
mpRcvrTopShutdownCause = _MpRcvrTopShutdownCause_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 47),
    _MpRcvrTopShutdownCause_Type()
)
mpRcvrTopShutdownCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrTopShutdownCause.setStatus("mandatory")
_MpRcvrBotShutdownCause_Type = Integer32
_MpRcvrBotShutdownCause_Object = MibTableColumn
mpRcvrBotShutdownCause = _MpRcvrBotShutdownCause_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 48),
    _MpRcvrBotShutdownCause_Type()
)
mpRcvrBotShutdownCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrBotShutdownCause.setStatus("mandatory")
_MpRcvrAutoShutdownEnable_Type = Integer32
_MpRcvrAutoShutdownEnable_Object = MibTableColumn
mpRcvrAutoShutdownEnable = _MpRcvrAutoShutdownEnable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 24, 1, 49),
    _MpRcvrAutoShutdownEnable_Type()
)
mpRcvrAutoShutdownEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRcvrAutoShutdownEnable.setStatus("mandatory")
_XmtrTable_Object = MibTable
xmtrTable = _XmtrTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 25)
)
if mibBuilder.loadTexts:
    xmtrTable.setStatus("mandatory")
_XmtrEntry_Object = MibTableRow
xmtrEntry = _XmtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 25, 1)
)
xmtrEntry.setIndexNames(
    (0, "CIENA-MIBv2", "shelfId"),
    (0, "CIENA-MIBv2", "slotId"),
)
if mibBuilder.loadTexts:
    xmtrEntry.setStatus("mandatory")
_MpXmtrInputSignal_Type = Integer32
_MpXmtrInputSignal_Object = MibTableColumn
mpXmtrInputSignal = _MpXmtrInputSignal_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 25, 1, 1),
    _MpXmtrInputSignal_Type()
)
mpXmtrInputSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpXmtrInputSignal.setStatus("mandatory")
_MpXmtrGratingTemp_Type = Integer32
_MpXmtrGratingTemp_Object = MibTableColumn
mpXmtrGratingTemp = _MpXmtrGratingTemp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 25, 1, 2),
    _MpXmtrGratingTemp_Type()
)
mpXmtrGratingTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpXmtrGratingTemp.setStatus("mandatory")
_SpXmtrGratingTemp_Type = Integer32
_SpXmtrGratingTemp_Object = MibTableColumn
spXmtrGratingTemp = _SpXmtrGratingTemp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 25, 1, 3),
    _SpXmtrGratingTemp_Type()
)
spXmtrGratingTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spXmtrGratingTemp.setStatus("mandatory")
_MpXmtrFreqTrack_Type = Integer32
_MpXmtrFreqTrack_Object = MibTableColumn
mpXmtrFreqTrack = _MpXmtrFreqTrack_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 25, 1, 4),
    _MpXmtrFreqTrack_Type()
)
mpXmtrFreqTrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpXmtrFreqTrack.setStatus("mandatory")
_MpXmtrCV_Type = Integer32
_MpXmtrCV_Object = MibTableColumn
mpXmtrCV = _MpXmtrCV_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 25, 1, 5),
    _MpXmtrCV_Type()
)
mpXmtrCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpXmtrCV.setStatus("mandatory")
_MpXmtrES_Type = Integer32
_MpXmtrES_Object = MibTableColumn
mpXmtrES = _MpXmtrES_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 25, 1, 6),
    _MpXmtrES_Type()
)
mpXmtrES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpXmtrES.setStatus("mandatory")
_MpXmtrSES_Type = Integer32
_MpXmtrSES_Object = MibTableColumn
mpXmtrSES = _MpXmtrSES_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 25, 1, 7),
    _MpXmtrSES_Type()
)
mpXmtrSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpXmtrSES.setStatus("mandatory")
_MpXmtrOFS_Type = Integer32
_MpXmtrOFS_Object = MibTableColumn
mpXmtrOFS = _MpXmtrOFS_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 25, 1, 8),
    _MpXmtrOFS_Type()
)
mpXmtrOFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpXmtrOFS.setStatus("mandatory")
_MpXmtrUAS_Type = Integer32
_MpXmtrUAS_Object = MibTableColumn
mpXmtrUAS = _MpXmtrUAS_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 25, 1, 9),
    _MpXmtrUAS_Type()
)
mpXmtrUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpXmtrUAS.setStatus("mandatory")
_MpXmtrNCSES_Type = Integer32
_MpXmtrNCSES_Object = MibTableColumn
mpXmtrNCSES = _MpXmtrNCSES_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 25, 1, 10),
    _MpXmtrNCSES_Type()
)
mpXmtrNCSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpXmtrNCSES.setStatus("mandatory")
_MpXmtrAutoShutdownEnable_Type = Integer32
_MpXmtrAutoShutdownEnable_Object = MibTableColumn
mpXmtrAutoShutdownEnable = _MpXmtrAutoShutdownEnable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 25, 1, 11),
    _MpXmtrAutoShutdownEnable_Type()
)
mpXmtrAutoShutdownEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpXmtrAutoShutdownEnable.setStatus("mandatory")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1, 4)
)
_EtNodeStatus_Type = MwSeverityLevel
_EtNodeStatus_Object = MibScalar
etNodeStatus = _EtNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 4, 1),
    _EtNodeStatus_Type()
)
etNodeStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etNodeStatus.setStatus("mandatory")
_EtAttrMessage_Type = DisplayString
_EtAttrMessage_Object = MibScalar
etAttrMessage = _EtAttrMessage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 4, 2),
    _EtAttrMessage_Type()
)
etAttrMessage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etAttrMessage.setStatus("mandatory")
_MultiwaveTraps_ObjectIdentity = ObjectIdentity
multiwaveTraps = _MultiwaveTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1, 5)
)

# Managed Objects groups


# Notification objects

mwAttributeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 1, 5, 0, 1)
)
mwAttributeChange.setObjects(
      *(("CIENA-MIBv2", "nodeName"),
        ("CIENA-MIBv2", "etNodeStatus"),
        ("CIENA-MIBv2", "shelfId"),
        ("CIENA-MIBv2", "slotId"),
        ("CIENA-MIBv2", "moduleType"),
        ("CIENA-MIBv2", "moduleStatus"),
        ("CIENA-MIBv2", "alarmAttrId"),
        ("CIENA-MIBv2", "alarmSeverity"),
        ("CIENA-MIBv2", "etAttrMessage"))
)
if mibBuilder.loadTexts:
    mwAttributeChange.setStatus(
        ""
    )

mwAlarmAsserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 1, 5, 0, 2)
)
mwAlarmAsserted.setObjects(
      *(("CIENA-MIBv2", "etNodeStatus"),
        ("CIENA-MIBv2", "shelfId"),
        ("CIENA-MIBv2", "slotId"),
        ("CIENA-MIBv2", "moduleType"),
        ("CIENA-MIBv2", "moduleStatus"),
        ("CIENA-MIBv2", "alarmCriticality"),
        ("CIENA-MIBv2", "alarmSequence"),
        ("CIENA-MIBv2", "alarmCondition"))
)
if mibBuilder.loadTexts:
    mwAlarmAsserted.setStatus(
        ""
    )

mwAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 1, 5, 0, 3)
)
mwAlarmCleared.setObjects(
      *(("CIENA-MIBv2", "etNodeStatus"),
        ("CIENA-MIBv2", "shelfId"),
        ("CIENA-MIBv2", "slotId"),
        ("CIENA-MIBv2", "moduleType"),
        ("CIENA-MIBv2", "moduleStatus"),
        ("CIENA-MIBv2", "alarmCriticality"),
        ("CIENA-MIBv2", "alarmSequence"))
)
if mibBuilder.loadTexts:
    mwAlarmCleared.setStatus(
        ""
    )

mwDumpPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 1, 5, 0, 4)
)
if mibBuilder.loadTexts:
    mwDumpPresent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-MIBv2",
    **{"MwSeverityLevel": MwSeverityLevel,
       "MwAttributeId": MwAttributeId,
       "MwMonitorPointId": MwMonitorPointId,
       "ciena": ciena,
       "multiwaveMgmt": multiwaveMgmt,
       "system": system,
       "ncpModuleInfo": ncpModuleInfo,
       "nodeType": nodeType,
       "nodeName": nodeName,
       "nodeOKLED": nodeOKLED,
       "nodeMajorLED": nodeMajorLED,
       "nodeMinorLED": nodeMinorLED,
       "nodeMaintenanceLED": nodeMaintenanceLED,
       "nCPOkLED": nCPOkLED,
       "ncpMajorLED": ncpMajorLED,
       "ncpMinorLED": ncpMinorLED,
       "ncpMaintenanceLED": ncpMaintenanceLED,
       "ncpTime": ncpTime,
       "nodeTypeStr": nodeTypeStr,
       "nodeAddr": nodeAddr,
       "ncpCrashDumpPresent": ncpCrashDumpPresent,
       "equipment": equipment,
       "multiwave": multiwave,
       "moduleTable": moduleTable,
       "modEntry": modEntry,
       "shelfId": shelfId,
       "slotId": slotId,
       "partId": partId,
       "partNumber": partNumber,
       "serialId": serialId,
       "revisionId": revisionId,
       "moduleType": moduleType,
       "moduleState": moduleState,
       "moduleStatus": moduleStatus,
       "cpResetModule": cpResetModule,
       "isInMaintenanceMode": isInMaintenanceMode,
       "cpResetAccumulators": cpResetAccumulators,
       "slotsLeft": slotsLeft,
       "slotsRight": slotsRight,
       "moduleTypeStr": moduleTypeStr,
       "remodTable": remodTable,
       "remodEntry": remodEntry,
       "mpRemodGratingTemperature": mpRemodGratingTemperature,
       "mpInputSignalLevel": mpInputSignalLevel,
       "spDitherEnable": spDitherEnable,
       "spFreqTrack": spFreqTrack,
       "mpRemodLaserPower": mpRemodLaserPower,
       "mpRemodLaserTemp": mpRemodLaserTemp,
       "mpRemodLaserCurrent": mpRemodLaserCurrent,
       "mpRemodTECCurrent": mpRemodTECCurrent,
       "mpRemodHeatSinkTemperature": mpRemodHeatSinkTemperature,
       "spRemodOperatingMode": spRemodOperatingMode,
       "mpRemodCurrentLimited": mpRemodCurrentLimited,
       "spRemodLaserPower": spRemodLaserPower,
       "spRemodLaserTemperature": spRemodLaserTemperature,
       "mpRemodLaserState": mpRemodLaserState,
       "fcRemodWavelength": fcRemodWavelength,
       "spRemodConfiguredState": spRemodConfiguredState,
       "remodOKLED": remodOKLED,
       "remodMajorLED": remodMajorLED,
       "remodMinorLED": remodMinorLED,
       "remodMaintenanceLED": remodMaintenanceLED,
       "terminalType": terminalType,
       "spGratingTemp": spGratingTemp,
       "remodChannelTag1": remodChannelTag1,
       "remodChannelTag2": remodChannelTag2,
       "pumpTable": pumpTable,
       "pumpEntry": pumpEntry,
       "mpPumpLaserPower": mpPumpLaserPower,
       "mpPumpLaserTemp": mpPumpLaserTemp,
       "mpPumpLaserCurrent": mpPumpLaserCurrent,
       "mpPumpTECCurrent": mpPumpTECCurrent,
       "mpPumpHeatSinkTemperature": mpPumpHeatSinkTemperature,
       "spPumpOperatingMode": spPumpOperatingMode,
       "mpPumpCurrentLimited": mpPumpCurrentLimited,
       "spPumpLaserPower": spPumpLaserPower,
       "spPumpLaserCurrent": spPumpLaserCurrent,
       "spPumpLaserTemp": spPumpLaserTemp,
       "mpPumpLaserState": mpPumpLaserState,
       "fcPumpWavelength": fcPumpWavelength,
       "pumpOKLED": pumpOKLED,
       "pumpMajorLED": pumpMajorLED,
       "pumpMinorLED": pumpMinorLED,
       "pumpMaintenanceLED": pumpMaintenanceLED,
       "spPumpConfiguredState": spPumpConfiguredState,
       "selectorTable": selectorTable,
       "selectorEntry": selectorEntry,
       "fcSelectorWavelengthTop": fcSelectorWavelengthTop,
       "fcSelectorWavelengthBottom": fcSelectorWavelengthBottom,
       "mpSignalLevelTop": mpSignalLevelTop,
       "mpSignalLevelBottom": mpSignalLevelBottom,
       "selectorOKLedTop": selectorOKLedTop,
       "selectorMajorLedTop": selectorMajorLedTop,
       "selectorMinorLedTop": selectorMinorLedTop,
       "selectorMaintenanceLedTop": selectorMaintenanceLedTop,
       "selectorOKLedBottom": selectorOKLedBottom,
       "selectorMajorLedBottom": selectorMajorLedBottom,
       "selectorMinorLedBottom": selectorMinorLedBottom,
       "selectorMaintenanceLedBottom": selectorMaintenanceLedBottom,
       "mpGratingTopTemp": mpGratingTopTemp,
       "mpGratingBottomTemp": mpGratingBottomTemp,
       "spGratingTopTemp": spGratingTopTemp,
       "spGratingBottomTemp": spGratingBottomTemp,
       "selectorChannelTagA1": selectorChannelTagA1,
       "selectorChannelTagA2": selectorChannelTagA2,
       "selectorChannelTagB1": selectorChannelTagB1,
       "selectorChannelTagB2": selectorChannelTagB2,
       "fiberAmpTable": fiberAmpTable,
       "fiberAmpEntry": fiberAmpEntry,
       "fiberAmpTopInputSignalLevel": fiberAmpTopInputSignalLevel,
       "fiberAmpTopOutputSignalLevel": fiberAmpTopOutputSignalLevel,
       "fiberAmpBottomInputSignalLevel": fiberAmpBottomInputSignalLevel,
       "fiberAmpBottomOutputSignalLevel": fiberAmpBottomOutputSignalLevel,
       "fiberAmpTopOKLed": fiberAmpTopOKLed,
       "fiberAmpTopMajorLed": fiberAmpTopMajorLed,
       "fiberAmpTopMinorLed": fiberAmpTopMinorLed,
       "fiberAmpTopMaintenanceLed": fiberAmpTopMaintenanceLed,
       "fiberAmpBottomOKLed": fiberAmpBottomOKLed,
       "fiberAmpBottomMajorLed": fiberAmpBottomMajorLed,
       "fiberAmpBottomMinorLed": fiberAmpBottomMinorLed,
       "fiberAmpBottomMaintenanceLed": fiberAmpBottomMaintenanceLed,
       "shelfPowerTable": shelfPowerTable,
       "shelfPowerEntry": shelfPowerEntry,
       "shelfPowerSource1Fail": shelfPowerSource1Fail,
       "shelfPowerSource2Fail": shelfPowerSource2Fail,
       "shelfPowerSummaryFail": shelfPowerSummaryFail,
       "shelfPowerTemperature": shelfPowerTemperature,
       "shelfPowerFan1Fail": shelfPowerFan1Fail,
       "shelfPowerFan2Fail": shelfPowerFan2Fail,
       "monitorPointTable": monitorPointTable,
       "monitorPointEntry": monitorPointEntry,
       "monitorPointShelfId": monitorPointShelfId,
       "monitorPointSlotId": monitorPointSlotId,
       "monitorPointUnitId": monitorPointUnitId,
       "monitorPointAttributeId": monitorPointAttributeId,
       "measuredValue": measuredValue,
       "highValueLatch": highValueLatch,
       "lowValueLatch": lowValueLatch,
       "averageValue": averageValue,
       "averageSamplesQty": averageSamplesQty,
       "hiMajorThreshold": hiMajorThreshold,
       "hiMinorThreshold": hiMinorThreshold,
       "loMinorThreshold": loMinorThreshold,
       "loMajorThreshold": loMajorThreshold,
       "hiMajorThresholdMode": hiMajorThresholdMode,
       "hiMinorThresholdMode": hiMinorThresholdMode,
       "loMinorThresholdMode": loMinorThresholdMode,
       "loMajorThresholdMode": loMajorThresholdMode,
       "thresholdSource": thresholdSource,
       "averageMethod": averageMethod,
       "cpResetAccumulator": cpResetAccumulator,
       "maxValue": maxValue,
       "minValue": minValue,
       "units": units,
       "thresholdCompareMode": thresholdCompareMode,
       "mwSupportingEMSGroup": mwSupportingEMSGroup,
       "mwSupportEMSTableSize": mwSupportEMSTableSize,
       "mwSupportEMSTable": mwSupportEMSTable,
       "mwSupportEMSEntry": mwSupportEMSEntry,
       "mwEMSNum": mwEMSNum,
       "mwEMSAddrType": mwEMSAddrType,
       "mwEMSAddr": mwEMSAddr,
       "mwEMSName": mwEMSName,
       "mwEMSVersion": mwEMSVersion,
       "alarmTable": alarmTable,
       "oldAlarmEntry": oldAlarmEntry,
       "alarmSeverity": alarmSeverity,
       "alarmTerm": alarmTerm,
       "alarmAttrIx": alarmAttrIx,
       "alarmAttrId": alarmAttrId,
       "mwDSModuleGroup": mwDSModuleGroup,
       "mwDSModuleTable": mwDSModuleTable,
       "mwDSModuleEntry": mwDSModuleEntry,
       "mwDSType": mwDSType,
       "mwDSNum": mwDSNum,
       "mwDSignalName": mwDSignalName,
       "mwDSignalState": mwDSignalState,
       "mwDSignalOffStateName": mwDSignalOffStateName,
       "mwDSignalOnStateName": mwDSignalOnStateName,
       "mwDSCriticality": mwDSCriticality,
       "mwDSAlarmState": mwDSAlarmState,
       "mwNeighborModuleGroup": mwNeighborModuleGroup,
       "mwNeighborTable": mwNeighborTable,
       "mwNeighborEntry": mwNeighborEntry,
       "mwNeighborDirection": mwNeighborDirection,
       "mwNeighborDistance": mwNeighborDistance,
       "mwAddrType": mwAddrType,
       "mwNeighborAddr": mwNeighborAddr,
       "mwAlarmTable": mwAlarmTable,
       "mwAlarmEntry": mwAlarmEntry,
       "alarmSequence": alarmSequence,
       "alarmTime": alarmTime,
       "alarmCriticality": alarmCriticality,
       "alarmAttribute1": alarmAttribute1,
       "alarmAttrSubCode1": alarmAttrSubCode1,
       "alarmAttribute2": alarmAttribute2,
       "alarmAttrSubCode2": alarmAttrSubCode2,
       "alarmAttribute3": alarmAttribute3,
       "alarmAttrSubCode3": alarmAttrSubCode3,
       "alarmAttribute4": alarmAttribute4,
       "alarmAttrSubCode4": alarmAttrSubCode4,
       "alarmCondition": alarmCondition,
       "mwUsersGroup": mwUsersGroup,
       "mwUsersLoggedInTable": mwUsersLoggedInTable,
       "mwUsersLoggedInEntry": mwUsersLoggedInEntry,
       "mwLoginNum": mwLoginNum,
       "mwUserNum": mwUserNum,
       "mwLoggedInFrom": mwLoggedInFrom,
       "mwElapsedLoginTime": mwElapsedLoginTime,
       "mwChangeGroup": mwChangeGroup,
       "mwChangeTable": mwChangeTable,
       "mwChangeEntry": mwChangeEntry,
       "mwChangeNumber": mwChangeNumber,
       "mwLastChangeTime": mwLastChangeTime,
       "mwTableId": mwTableId,
       "scmTable": scmTable,
       "scmEntry": scmEntry,
       "scmLaserPower": scmLaserPower,
       "scmLaserTemperature": scmLaserTemperature,
       "scmLaserCurrent": scmLaserCurrent,
       "scmLaserTECCurrent": scmLaserTECCurrent,
       "scmLaserHeatSinkTemperature": scmLaserHeatSinkTemperature,
       "scmLaserState": scmLaserState,
       "scmLaserWavelength": scmLaserWavelength,
       "scmLaserInputSignalAbsent": scmLaserInputSignalAbsent,
       "scmEastLinkStat": scmEastLinkStat,
       "scmWestLinkStat": scmWestLinkStat,
       "scmFramingMode": scmFramingMode,
       "scmNodeType": scmNodeType,
       "scmSlave": scmSlave,
       "scmOkLED": scmOkLED,
       "scmMajorLED": scmMajorLED,
       "scmMinorLED": scmMinorLED,
       "scmMaintenanceLED": scmMaintenanceLED,
       "scimTable": scimTable,
       "scimEntry": scimEntry,
       "scimTopInput": scimTopInput,
       "scimBottomInput": scimBottomInput,
       "scimTopOutput": scimTopOutput,
       "scimBottomOutput": scimBottomOutput,
       "scimTopOkLED": scimTopOkLED,
       "scimTopMajorLED": scimTopMajorLED,
       "scimTopMinorLED": scimTopMinorLED,
       "scimTopMaintenanceLED": scimTopMaintenanceLED,
       "scimBottomOkLED": scimBottomOkLED,
       "scimBottomMajorLED": scimBottomMajorLED,
       "scimBottomMinorLED": scimBottomMinorLED,
       "scimBottomMaintenanceLED": scimBottomMaintenanceLED,
       "scimTopMaintMode": scimTopMaintMode,
       "scimBottomMaintMode": scimBottomMaintMode,
       "admTable": admTable,
       "admEntry": admEntry,
       "adm1Heater": adm1Heater,
       "adm1Wavelength": adm1Wavelength,
       "adm1HeaterReference": adm1HeaterReference,
       "adm1HeaterStatus": adm1HeaterStatus,
       "adm2Heater": adm2Heater,
       "adm2Wavelength": adm2Wavelength,
       "adm2HeaterReference": adm2HeaterReference,
       "adm2HeaterStatus": adm2HeaterStatus,
       "adm3Heater": adm3Heater,
       "adm3Wavelength": adm3Wavelength,
       "adm3HeaterReference": adm3HeaterReference,
       "adm3HeaterStatus": adm3HeaterStatus,
       "adm4Heater": adm4Heater,
       "adm4Wavelength": adm4Wavelength,
       "adm4HeaterReference": adm4HeaterReference,
       "adm4HeaterStatus": adm4HeaterStatus,
       "admOkLED": admOkLED,
       "admMajorLED": admMajorLED,
       "admMinorLED": admMinorLED,
       "admMaintLED": admMaintLED,
       "owTable": owTable,
       "owEntry": owEntry,
       "owLine1OffHook": owLine1OffHook,
       "owLine2OffHook": owLine2OffHook,
       "admaTable": admaTable,
       "admaEntry": admaEntry,
       "admaTopInput": admaTopInput,
       "admaBottomInput": admaBottomInput,
       "admaTopOutput": admaTopOutput,
       "admaBottomOutput": admaBottomOutput,
       "admaTopPreampOutput": admaTopPreampOutput,
       "admaBottomPreampOutput": admaBottomPreampOutput,
       "admaTopAdmInput": admaTopAdmInput,
       "admaBottomAdmInput": admaBottomAdmInput,
       "admaTopCombinerInput": admaTopCombinerInput,
       "admaBottomCombinerInput": admaBottomCombinerInput,
       "admaTopOkLED": admaTopOkLED,
       "admaTopMajorLED": admaTopMajorLED,
       "admaTopMinorLED": admaTopMinorLED,
       "admaTopMaintenanceLED": admaTopMaintenanceLED,
       "admaBottomOkLED": admaBottomOkLED,
       "admaBottomMajorLED": admaBottomMajorLED,
       "admaBottomMinorLED": admaBottomMinorLED,
       "admaBottomMaintenanceLED": admaBottomMaintenanceLED,
       "admaTopMaintMode": admaTopMaintMode,
       "admaBottomMaintMode": admaBottomMaintMode,
       "mwLoadedImagesGroup": mwLoadedImagesGroup,
       "mwAvailableImagesTable": mwAvailableImagesTable,
       "mwAvailableImageEntry": mwAvailableImageEntry,
       "mwRunningImage": mwRunningImage,
       "mwImageControl": mwImageControl,
       "mwPrimaryImageStatus": mwPrimaryImageStatus,
       "mwPrimaryImageName": mwPrimaryImageName,
       "mwSecondaryImageStatus": mwSecondaryImageStatus,
       "mwSecondaryImageName": mwSecondaryImageName,
       "mwImageLoadFrom": mwImageLoadFrom,
       "mwImageLastStatus": mwImageLastStatus,
       "txcvrTable": txcvrTable,
       "txcvrEntry": txcvrEntry,
       "mpTxcvrGratingTemperature": mpTxcvrGratingTemperature,
       "mpTxcvrSrLaserPower": mpTxcvrSrLaserPower,
       "spTxcvrSrLaserPower": spTxcvrSrLaserPower,
       "mpTxcvrSrLaserCurrent": mpTxcvrSrLaserCurrent,
       "mpTxcvrSrInputSignalLevel": mpTxcvrSrInputSignalLevel,
       "spTxcvrSrLaserConfiguredState": spTxcvrSrLaserConfiguredState,
       "mpTxcvrSrLaserState": mpTxcvrSrLaserState,
       "mpTxcvrSrLaserShutdownCause": mpTxcvrSrLaserShutdownCause,
       "spTxcvrSrLosThreshold": spTxcvrSrLosThreshold,
       "spTxcvrRxMaintenance": spTxcvrRxMaintenance,
       "spTxcvrSrAutoShutdown": spTxcvrSrAutoShutdown,
       "mpTxcvrSrCurrentLimited": mpTxcvrSrCurrentLimited,
       "mpTxcvrDfbLaserPower": mpTxcvrDfbLaserPower,
       "spTxcvrDfbLaserPower": spTxcvrDfbLaserPower,
       "mpTxcvrDfbLaserCurrent": mpTxcvrDfbLaserCurrent,
       "mpTxcvrDfbLaserTemp": mpTxcvrDfbLaserTemp,
       "spTxcvrDfbLaserTemp": spTxcvrDfbLaserTemp,
       "spTxcvrDfbLaserConfiguredState": spTxcvrDfbLaserConfiguredState,
       "mpTxcvrDfbLaserState": mpTxcvrDfbLaserState,
       "spTxcvrDfbSubcarrier": spTxcvrDfbSubcarrier,
       "spTxcvrTxMaintenance": spTxcvrTxMaintenance,
       "mpTxcvrDfbCurrentLimited": mpTxcvrDfbCurrentLimited,
       "mpTxcvrDfbLaserShutdownCause": mpTxcvrDfbLaserShutdownCause,
       "mpTxcvrDfbAutoShutdownEnable": mpTxcvrDfbAutoShutdownEnable,
       "mpTxcvrApdInputSignalLevel": mpTxcvrApdInputSignalLevel,
       "mpTxcvrHeatSinkTemperature": mpTxcvrHeatSinkTemperature,
       "mpTxcvrTECCurrent": mpTxcvrTECCurrent,
       "mpTxcvrTECHeaterStatus": mpTxcvrTECHeaterStatus,
       "mpTxcvrGratingHeaterStatus": mpTxcvrGratingHeaterStatus,
       "fcTxcvrWavelength": fcTxcvrWavelength,
       "txcvrOKLED": txcvrOKLED,
       "txcvrMajorLED": txcvrMajorLED,
       "txcvrMinorLED": txcvrMinorLED,
       "txcvrMaintenanceLED": txcvrMaintenanceLED,
       "txcvrChannelTag1": txcvrChannelTag1,
       "txcvrChannelTag2": txcvrChannelTag2,
       "ffIoTable": ffIoTable,
       "ffIoEntry": ffIoEntry,
       "mpFfIoAmbientTemperature": mpFfIoAmbientTemperature,
       "mpFfIoFanPresent": mpFfIoFanPresent,
       "mpFfIoFanFail": mpFfIoFanFail,
       "mpFfIoFuseFail": mpFfIoFuseFail,
       "spFfIoResetModule": spFfIoResetModule,
       "spFfIoResetIoController": spFfIoResetIoController,
       "mpFfIoLedCritical": mpFfIoLedCritical,
       "mpFfIoLedMajor": mpFfIoLedMajor,
       "mpFfIoLedMinor": mpFfIoLedMinor,
       "mpFfIoLedOutOfService": mpFfIoLedOutOfService,
       "mpFfIoLedNormal": mpFfIoLedNormal,
       "ffMuxDemElectricalTable": ffMuxDemElectricalTable,
       "ffMuxDemElectricalEntry": ffMuxDemElectricalEntry,
       "mpFfMuxDemElectricalMuxHeater": mpFfMuxDemElectricalMuxHeater,
       "mpFfMuxDemElectricalDemuxHeater": mpFfMuxDemElectricalDemuxHeater,
       "mpFfMuxDemElectricalMuxHeaterStatus": mpFfMuxDemElectricalMuxHeaterStatus,
       "mpFfMuxDemElectricalDemuxHeaterStatus": mpFfMuxDemElectricalDemuxHeaterStatus,
       "mpFfMuxDemElectricalMuxOutput": mpFfMuxDemElectricalMuxOutput,
       "mpFfMuxDemElectricalDemuxInput": mpFfMuxDemElectricalDemuxInput,
       "rcvrTable": rcvrTable,
       "rcvrEntry": rcvrEntry,
       "mpRcvrTopLaserPower": mpRcvrTopLaserPower,
       "mpRcvrBotLaserPower": mpRcvrBotLaserPower,
       "mpRcvrTopGratingTemp": mpRcvrTopGratingTemp,
       "mpRcvrBotGratingTemp": mpRcvrBotGratingTemp,
       "mpRcvrTopInputSignal": mpRcvrTopInputSignal,
       "mpRcvrBotInputSignal": mpRcvrBotInputSignal,
       "mpRcvrTopLaserCurrent": mpRcvrTopLaserCurrent,
       "mpRcvrBotLaserCurrent": mpRcvrBotLaserCurrent,
       "mpRcvrTopHeaterStatus": mpRcvrTopHeaterStatus,
       "mpRcvrBotHeaterStatus": mpRcvrBotHeaterStatus,
       "mpRcvrTopWavelength": mpRcvrTopWavelength,
       "mpRcvrBotWavelength": mpRcvrBotWavelength,
       "spRcvrTopLaserCurrent": spRcvrTopLaserCurrent,
       "spRcvrBotLaserCurrent": spRcvrBotLaserCurrent,
       "spRcvrTopLaserPower": spRcvrTopLaserPower,
       "spRcvrBotLaserPower": spRcvrBotLaserPower,
       "spRcvrTopGratingTemp": spRcvrTopGratingTemp,
       "spRcvrBotGratingTemp": spRcvrBotGratingTemp,
       "spRcvrTopLos": spRcvrTopLos,
       "spRcvrBotLos": spRcvrBotLos,
       "mpRcvrTopChnlTag1": mpRcvrTopChnlTag1,
       "mpRcvrTopChnlTag2": mpRcvrTopChnlTag2,
       "mpRcvrBotChnlTag1": mpRcvrBotChnlTag1,
       "mpRcvrBotChnlTag2": mpRcvrBotChnlTag2,
       "mpRcvrTopMaint": mpRcvrTopMaint,
       "mpRcvrBotMaint": mpRcvrBotMaint,
       "mpRcvrTopLaserConfig": mpRcvrTopLaserConfig,
       "mpRcvrBotLaserConfig": mpRcvrBotLaserConfig,
       "mpRcvrTopOpmode": mpRcvrTopOpmode,
       "mpRcvrBotOpmode": mpRcvrBotOpmode,
       "mpRcvrTopLaserState": mpRcvrTopLaserState,
       "mpRcvrBotLaserState": mpRcvrBotLaserState,
       "mpRcvrTopCV": mpRcvrTopCV,
       "mpRcvrBotCV": mpRcvrBotCV,
       "mpRcvrTopES": mpRcvrTopES,
       "mpRcvrBotES": mpRcvrBotES,
       "mpRcvrTopSES": mpRcvrTopSES,
       "mpRcvrBotSES": mpRcvrBotSES,
       "mpRcvrTopOFS": mpRcvrTopOFS,
       "mpRcvrBotOFS": mpRcvrBotOFS,
       "mpRcvrTopUAS": mpRcvrTopUAS,
       "mpRcvrBotUAS": mpRcvrBotUAS,
       "mpRcvrTopNCSES": mpRcvrTopNCSES,
       "mpRcvrBotNCSES": mpRcvrBotNCSES,
       "mpRcvrTopLastReset": mpRcvrTopLastReset,
       "mpRcvrBotLastReset": mpRcvrBotLastReset,
       "mpRcvrTopShutdownCause": mpRcvrTopShutdownCause,
       "mpRcvrBotShutdownCause": mpRcvrBotShutdownCause,
       "mpRcvrAutoShutdownEnable": mpRcvrAutoShutdownEnable,
       "xmtrTable": xmtrTable,
       "xmtrEntry": xmtrEntry,
       "mpXmtrInputSignal": mpXmtrInputSignal,
       "mpXmtrGratingTemp": mpXmtrGratingTemp,
       "spXmtrGratingTemp": spXmtrGratingTemp,
       "mpXmtrFreqTrack": mpXmtrFreqTrack,
       "mpXmtrCV": mpXmtrCV,
       "mpXmtrES": mpXmtrES,
       "mpXmtrSES": mpXmtrSES,
       "mpXmtrOFS": mpXmtrOFS,
       "mpXmtrUAS": mpXmtrUAS,
       "mpXmtrNCSES": mpXmtrNCSES,
       "mpXmtrAutoShutdownEnable": mpXmtrAutoShutdownEnable,
       "traps": traps,
       "etNodeStatus": etNodeStatus,
       "etAttrMessage": etAttrMessage,
       "multiwaveTraps": multiwaveTraps,
       "mwAttributeChange": mwAttributeChange,
       "mwAlarmAsserted": mwAlarmAsserted,
       "mwAlarmCleared": mwAlarmCleared,
       "mwDumpPresent": mwDumpPresent}
)
