# SNMP MIB module (PEAKBLOCKUPCONVERTERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKBLOCKUPCONVERTERS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:49:01 2025
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

peakBlockUpConverterModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 4)
)
if mibBuilder.loadTexts:
    peakBlockUpConverterModule.setRevisions(
        ("2015-09-15 09:00",
         "2013-04-04 12:00",
         "2012-01-30 12:00",
         "2011-10-31 12:00",
         "2011-06-30 12:00",
         "2010-01-04 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BlockupTable_Object = MibTable
blockupTable = _BlockupTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    blockupTable.setStatus("current")
_BlockupTableEntry_Object = MibTableRow
blockupTableEntry = _BlockupTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 4, 1, 1)
)
blockupTableEntry.setIndexNames(
    (0, "PEAKBLOCKUPCONVERTERS-MIB", "blockupIndex"),
)
if mibBuilder.loadTexts:
    blockupTableEntry.setStatus("current")


class _BlockupIndex_Type(Integer32):
    """Custom type blockupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BlockupIndex_Type.__name__ = "Integer32"
_BlockupIndex_Object = MibTableColumn
blockupIndex = _BlockupIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 4, 1, 1, 1),
    _BlockupIndex_Type()
)
blockupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blockupIndex.setStatus("current")
_BlockupAttenuation_Type = OctetString
_BlockupAttenuation_Object = MibTableColumn
blockupAttenuation = _BlockupAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 4, 1, 1, 2),
    _BlockupAttenuation_Type()
)
blockupAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blockupAttenuation.setStatus("current")


class _BlockupBand_Type(Integer32):
    """Custom type blockupBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BlockupBand_Type.__name__ = "Integer32"
_BlockupBand_Object = MibTableColumn
blockupBand = _BlockupBand_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 4, 1, 1, 3),
    _BlockupBand_Type()
)
blockupBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blockupBand.setStatus("current")
_BlockupMute_Type = MuteType
_BlockupMute_Object = MibTableColumn
blockupMute = _BlockupMute_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 4, 1, 1, 4),
    _BlockupMute_Type()
)
blockupMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blockupMute.setStatus("current")
_BlockupPDIP_Type = OctetString
_BlockupPDIP_Object = MibTableColumn
blockupPDIP = _BlockupPDIP_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 4, 1, 1, 5),
    _BlockupPDIP_Type()
)
blockupPDIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blockupPDIP.setStatus("current")
_BlockupPDOP_Type = OctetString
_BlockupPDOP_Object = MibTableColumn
blockupPDOP = _BlockupPDOP_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 4, 1, 1, 6),
    _BlockupPDOP_Type()
)
blockupPDOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blockupPDOP.setStatus("current")
_BlockupName_Type = OctetString
_BlockupName_Object = MibTableColumn
blockupName = _BlockupName_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 4, 1, 1, 9),
    _BlockupName_Type()
)
blockupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blockupName.setStatus("current")
_BlockupPDIPAlarm_Type = EnableType
_BlockupPDIPAlarm_Object = MibTableColumn
blockupPDIPAlarm = _BlockupPDIPAlarm_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 4, 1, 1, 10),
    _BlockupPDIPAlarm_Type()
)
blockupPDIPAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blockupPDIPAlarm.setStatus("current")
_BlockupPDIPAlLevel_Type = OctetString
_BlockupPDIPAlLevel_Object = MibTableColumn
blockupPDIPAlLevel = _BlockupPDIPAlLevel_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 4, 1, 1, 11),
    _BlockupPDIPAlLevel_Type()
)
blockupPDIPAlLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blockupPDIPAlLevel.setStatus("current")
_BlockupPDCompAlLevel_Type = OctetString
_BlockupPDCompAlLevel_Object = MibTableColumn
blockupPDCompAlLevel = _BlockupPDCompAlLevel_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 4, 1, 1, 12),
    _BlockupPDCompAlLevel_Type()
)
blockupPDCompAlLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blockupPDCompAlLevel.setStatus("current")
_BlockupOKSince_Type = OctetString
_BlockupOKSince_Object = MibTableColumn
blockupOKSince = _BlockupOKSince_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 4, 1, 1, 100),
    _BlockupOKSince_Type()
)
blockupOKSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blockupOKSince.setStatus("current")
_BlockupConvGroups_ObjectIdentity = ObjectIdentity
blockupConvGroups = _BlockupConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 4, 10)
)
_BlockupConvConformance_ObjectIdentity = ObjectIdentity
blockupConvConformance = _BlockupConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 4, 11)
)

# Managed Objects groups

blockupCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 4, 10, 1)
)
blockupCNFReqGrp.setObjects(
    ("PEAKBLOCKUPCONVERTERS-MIB", "blockupOKSince")
)
if mibBuilder.loadTexts:
    blockupCNFReqGrp.setStatus("current")

blockupCNFAttGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 4, 10, 2)
)
blockupCNFAttGrp.setObjects(
    ("PEAKBLOCKUPCONVERTERS-MIB", "blockupAttenuation")
)
if mibBuilder.loadTexts:
    blockupCNFAttGrp.setStatus("current")

blockupCNFBandGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 4, 10, 3)
)
blockupCNFBandGrp.setObjects(
    ("PEAKBLOCKUPCONVERTERS-MIB", "blockupBand")
)
if mibBuilder.loadTexts:
    blockupCNFBandGrp.setStatus("current")

blockupCNFMuteGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 4, 10, 4)
)
blockupCNFMuteGrp.setObjects(
    ("PEAKBLOCKUPCONVERTERS-MIB", "blockupMute")
)
if mibBuilder.loadTexts:
    blockupCNFMuteGrp.setStatus("current")

blockupCNFPowerDetectionGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 4, 10, 5)
)
blockupCNFPowerDetectionGrp.setObjects(
      *(("PEAKBLOCKUPCONVERTERS-MIB", "blockupPDIP"),
        ("PEAKBLOCKUPCONVERTERS-MIB", "blockupPDOP"),
        ("PEAKBLOCKUPCONVERTERS-MIB", "blockupPDIPAlarm"),
        ("PEAKBLOCKUPCONVERTERS-MIB", "blockupPDIPAlLevel"),
        ("PEAKBLOCKUPCONVERTERS-MIB", "blockupPDCompAlLevel"))
)
if mibBuilder.loadTexts:
    blockupCNFPowerDetectionGrp.setStatus("current")

blockupCNFNameGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 4, 10, 6)
)
blockupCNFNameGrp.setObjects(
    ("PEAKBLOCKUPCONVERTERS-MIB", "blockupName")
)
if mibBuilder.loadTexts:
    blockupCNFNameGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

blockupCNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 4, 11, 1)
)
blockupCNFCompliance.setObjects(
      *(("PEAKBLOCKUPCONVERTERS-MIB", "blockupCNFReqGrp"),
        ("PEAKBLOCKUPCONVERTERS-MIB", "blockupCNFNameGrp"),
        ("PEAKBLOCKUPCONVERTERS-MIB", "blockupCNFAttGrp"),
        ("PEAKBLOCKUPCONVERTERS-MIB", "blockupCNFBandGrp"),
        ("PEAKBLOCKUPCONVERTERS-MIB", "blockupCNFMuteGrp"),
        ("PEAKBLOCKUPCONVERTERS-MIB", "blockupCNFPowerDetectionGrp"))
)
if mibBuilder.loadTexts:
    blockupCNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKBLOCKUPCONVERTERS-MIB",
    **{"peakBlockUpConverterModule": peakBlockUpConverterModule,
       "blockupTable": blockupTable,
       "blockupTableEntry": blockupTableEntry,
       "blockupIndex": blockupIndex,
       "blockupAttenuation": blockupAttenuation,
       "blockupBand": blockupBand,
       "blockupMute": blockupMute,
       "blockupPDIP": blockupPDIP,
       "blockupPDOP": blockupPDOP,
       "blockupName": blockupName,
       "blockupPDIPAlarm": blockupPDIPAlarm,
       "blockupPDIPAlLevel": blockupPDIPAlLevel,
       "blockupPDCompAlLevel": blockupPDCompAlLevel,
       "blockupOKSince": blockupOKSince,
       "blockupConvGroups": blockupConvGroups,
       "blockupCNFReqGrp": blockupCNFReqGrp,
       "blockupCNFAttGrp": blockupCNFAttGrp,
       "blockupCNFBandGrp": blockupCNFBandGrp,
       "blockupCNFMuteGrp": blockupCNFMuteGrp,
       "blockupCNFPowerDetectionGrp": blockupCNFPowerDetectionGrp,
       "blockupCNFNameGrp": blockupCNFNameGrp,
       "blockupConvConformance": blockupConvConformance,
       "blockupCNFCompliance": blockupCNFCompliance}
)
