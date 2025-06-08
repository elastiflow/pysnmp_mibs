# SNMP MIB module (PEAKLINEAMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKLINEAMP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:49:02 2025
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

(EnableType,
 MuteType,
 converters) = mibBuilder.importSymbols(
    "PEAKDEFINITIONS-MIB",
    "EnableType",
    "MuteType",
    "converters")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

peakLineAmplifierModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 8)
)
if mibBuilder.loadTexts:
    peakLineAmplifierModule.setRevisions(
        ("2015-09-15 09:00",
         "2013-04-04 12:00",
         "2012-01-30 12:00",
         "2011-01-04 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LineampTable_Object = MibTable
lineampTable = _LineampTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    lineampTable.setStatus("current")
_LineampTableEntry_Object = MibTableRow
lineampTableEntry = _LineampTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 8, 1, 1)
)
lineampTableEntry.setIndexNames(
    (0, "PEAKLINEAMP-MIB", "lineampIndex"),
)
if mibBuilder.loadTexts:
    lineampTableEntry.setStatus("current")


class _LineampIndex_Type(Integer32):
    """Custom type lineampIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_LineampIndex_Type.__name__ = "Integer32"
_LineampIndex_Object = MibTableColumn
lineampIndex = _LineampIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 8, 1, 1, 1),
    _LineampIndex_Type()
)
lineampIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lineampIndex.setStatus("current")
_LineampAttenuation_Type = OctetString
_LineampAttenuation_Object = MibTableColumn
lineampAttenuation = _LineampAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 8, 1, 1, 2),
    _LineampAttenuation_Type()
)
lineampAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineampAttenuation.setStatus("current")


class _LineampBand_Type(Integer32):
    """Custom type lineampBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_LineampBand_Type.__name__ = "Integer32"
_LineampBand_Object = MibTableColumn
lineampBand = _LineampBand_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 8, 1, 1, 3),
    _LineampBand_Type()
)
lineampBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineampBand.setStatus("current")
_LineampMute_Type = MuteType
_LineampMute_Object = MibTableColumn
lineampMute = _LineampMute_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 8, 1, 1, 4),
    _LineampMute_Type()
)
lineampMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineampMute.setStatus("current")
_LineampPDIP_Type = OctetString
_LineampPDIP_Object = MibTableColumn
lineampPDIP = _LineampPDIP_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 8, 1, 1, 5),
    _LineampPDIP_Type()
)
lineampPDIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineampPDIP.setStatus("current")
_LineampPDOP_Type = OctetString
_LineampPDOP_Object = MibTableColumn
lineampPDOP = _LineampPDOP_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 8, 1, 1, 6),
    _LineampPDOP_Type()
)
lineampPDOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineampPDOP.setStatus("current")
_LineampName_Type = OctetString
_LineampName_Object = MibTableColumn
lineampName = _LineampName_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 8, 1, 1, 9),
    _LineampName_Type()
)
lineampName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineampName.setStatus("current")
_LineampPDIPAlarm_Type = EnableType
_LineampPDIPAlarm_Object = MibTableColumn
lineampPDIPAlarm = _LineampPDIPAlarm_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 8, 1, 1, 10),
    _LineampPDIPAlarm_Type()
)
lineampPDIPAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineampPDIPAlarm.setStatus("current")
_LineampPDIPAlLevel_Type = OctetString
_LineampPDIPAlLevel_Object = MibTableColumn
lineampPDIPAlLevel = _LineampPDIPAlLevel_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 8, 1, 1, 11),
    _LineampPDIPAlLevel_Type()
)
lineampPDIPAlLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineampPDIPAlLevel.setStatus("current")
_LineampPDCompAlLevel_Type = OctetString
_LineampPDCompAlLevel_Object = MibTableColumn
lineampPDCompAlLevel = _LineampPDCompAlLevel_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 8, 1, 1, 12),
    _LineampPDCompAlLevel_Type()
)
lineampPDCompAlLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineampPDCompAlLevel.setStatus("current")
_LineampOKSince_Type = OctetString
_LineampOKSince_Object = MibTableColumn
lineampOKSince = _LineampOKSince_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 8, 1, 1, 100),
    _LineampOKSince_Type()
)
lineampOKSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineampOKSince.setStatus("current")
_LineampGroups_ObjectIdentity = ObjectIdentity
lineampGroups = _LineampGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 8, 10)
)
_LineampConformance_ObjectIdentity = ObjectIdentity
lineampConformance = _LineampConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 8, 11)
)

# Managed Objects groups

lineampCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 8, 10, 1)
)
lineampCNFReqGrp.setObjects(
    ("PEAKLINEAMP-MIB", "lineampOKSince")
)
if mibBuilder.loadTexts:
    lineampCNFReqGrp.setStatus("current")

lineampCNFAttGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 8, 10, 2)
)
lineampCNFAttGrp.setObjects(
    ("PEAKLINEAMP-MIB", "lineampAttenuation")
)
if mibBuilder.loadTexts:
    lineampCNFAttGrp.setStatus("current")

lineampCNFBandGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 8, 10, 3)
)
lineampCNFBandGrp.setObjects(
    ("PEAKLINEAMP-MIB", "lineampBand")
)
if mibBuilder.loadTexts:
    lineampCNFBandGrp.setStatus("current")

lineampCNFMuteGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 8, 10, 4)
)
lineampCNFMuteGrp.setObjects(
    ("PEAKLINEAMP-MIB", "lineampMute")
)
if mibBuilder.loadTexts:
    lineampCNFMuteGrp.setStatus("current")

lineampCNFPowerDetectionGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 8, 10, 5)
)
lineampCNFPowerDetectionGrp.setObjects(
      *(("PEAKLINEAMP-MIB", "lineampPDIP"),
        ("PEAKLINEAMP-MIB", "lineampPDOP"),
        ("PEAKLINEAMP-MIB", "lineampPDIPAlarm"),
        ("PEAKLINEAMP-MIB", "lineampPDIPAlLevel"),
        ("PEAKLINEAMP-MIB", "lineampPDCompAlLevel"))
)
if mibBuilder.loadTexts:
    lineampCNFPowerDetectionGrp.setStatus("current")

lineampCNFNameGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 8, 10, 6)
)
lineampCNFNameGrp.setObjects(
    ("PEAKLINEAMP-MIB", "lineampName")
)
if mibBuilder.loadTexts:
    lineampCNFNameGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lineampCNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 8, 11, 1)
)
lineampCNFCompliance.setObjects(
      *(("PEAKLINEAMP-MIB", "lineampCNFReqGrp"),
        ("PEAKLINEAMP-MIB", "lineampCNFNameGrp"),
        ("PEAKLINEAMP-MIB", "lineampCNFAttGrp"),
        ("PEAKLINEAMP-MIB", "lineampCNFBandGrp"),
        ("PEAKLINEAMP-MIB", "lineampCNFMuteGrp"),
        ("PEAKLINEAMP-MIB", "lineampCNFPowerDetectionGrp"))
)
if mibBuilder.loadTexts:
    lineampCNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKLINEAMP-MIB",
    **{"peakLineAmplifierModule": peakLineAmplifierModule,
       "lineampTable": lineampTable,
       "lineampTableEntry": lineampTableEntry,
       "lineampIndex": lineampIndex,
       "lineampAttenuation": lineampAttenuation,
       "lineampBand": lineampBand,
       "lineampMute": lineampMute,
       "lineampPDIP": lineampPDIP,
       "lineampPDOP": lineampPDOP,
       "lineampName": lineampName,
       "lineampPDIPAlarm": lineampPDIPAlarm,
       "lineampPDIPAlLevel": lineampPDIPAlLevel,
       "lineampPDCompAlLevel": lineampPDCompAlLevel,
       "lineampOKSince": lineampOKSince,
       "lineampGroups": lineampGroups,
       "lineampCNFReqGrp": lineampCNFReqGrp,
       "lineampCNFAttGrp": lineampCNFAttGrp,
       "lineampCNFBandGrp": lineampCNFBandGrp,
       "lineampCNFMuteGrp": lineampCNFMuteGrp,
       "lineampCNFPowerDetectionGrp": lineampCNFPowerDetectionGrp,
       "lineampCNFNameGrp": lineampCNFNameGrp,
       "lineampConformance": lineampConformance,
       "lineampCNFCompliance": lineampCNFCompliance}
)
