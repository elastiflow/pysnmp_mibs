# SNMP MIB module (CISCO-DATA-AALX-PROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-DATA-AALX-PROFILE-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:02:45 2025
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

(cmgwIndex,) = mibBuilder.importSymbols(
    "CISCO-MEDIA-GATEWAY-MIB",
    "cmgwIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoDataAalxProfileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 347)
)
if mibBuilder.loadTexts:
    ciscoDataAalxProfileMIB.setRevisions(
        ("2003-02-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CdapMIBNotifications_ObjectIdentity = ObjectIdentity
cdapMIBNotifications = _CdapMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 347, 0)
)
_CdapMIBObjects_ObjectIdentity = ObjectIdentity
cdapMIBObjects = _CdapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 347, 1)
)
_CdapNx64ProfileConfig_ObjectIdentity = ObjectIdentity
cdapNx64ProfileConfig = _CdapNx64ProfileConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 347, 1, 1)
)
_CdapNx64ProfileTable_Object = MibTable
cdapNx64ProfileTable = _CdapNx64ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 347, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cdapNx64ProfileTable.setStatus("current")
_CdapNx64ProfileEntry_Object = MibTableRow
cdapNx64ProfileEntry = _CdapNx64ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 347, 1, 1, 1, 1)
)
cdapNx64ProfileEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-DATA-AALX-PROFILE-MIB", "cdapNx64ProfileIndex"),
)
if mibBuilder.loadTexts:
    cdapNx64ProfileEntry.setStatus("current")


class _CdapNx64ProfileIndex_Type(Integer32):
    """Custom type cdapNx64ProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CdapNx64ProfileIndex_Type.__name__ = "Integer32"
_CdapNx64ProfileIndex_Object = MibTableColumn
cdapNx64ProfileIndex = _CdapNx64ProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 347, 1, 1, 1, 1, 1),
    _CdapNx64ProfileIndex_Type()
)
cdapNx64ProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdapNx64ProfileIndex.setStatus("current")


class _CdapNx64TransportMode_Type(Integer32):
    """Custom type cdapNx64TransportMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hdlc", 1),
          ("transparent", 2))
    )


_CdapNx64TransportMode_Type.__name__ = "Integer32"
_CdapNx64TransportMode_Object = MibTableColumn
cdapNx64TransportMode = _CdapNx64TransportMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 347, 1, 1, 1, 1, 2),
    _CdapNx64TransportMode_Type()
)
cdapNx64TransportMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdapNx64TransportMode.setStatus("current")


class _CdapNx64FrameFillPattern_Type(Integer32):
    """Custom type cdapNx64FrameFillPattern based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hdlcPattern", 1),
          ("idlePattern", 2))
    )


_CdapNx64FrameFillPattern_Type.__name__ = "Integer32"
_CdapNx64FrameFillPattern_Object = MibTableColumn
cdapNx64FrameFillPattern = _CdapNx64FrameFillPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 347, 1, 1, 1, 1, 3),
    _CdapNx64FrameFillPattern_Type()
)
cdapNx64FrameFillPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdapNx64FrameFillPattern.setStatus("current")


class _CdapNx64InterFrameGapFlagCount_Type(Unsigned32):
    """Custom type cdapNx64InterFrameGapFlagCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CdapNx64InterFrameGapFlagCount_Type.__name__ = "Unsigned32"
_CdapNx64InterFrameGapFlagCount_Object = MibTableColumn
cdapNx64InterFrameGapFlagCount = _CdapNx64InterFrameGapFlagCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 347, 1, 1, 1, 1, 4),
    _CdapNx64InterFrameGapFlagCount_Type()
)
cdapNx64InterFrameGapFlagCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdapNx64InterFrameGapFlagCount.setStatus("current")


class _CdapNx64BitInversion_Type(TruthValue):
    """Custom type cdapNx64BitInversion based on TruthValue"""
    defaultValue = 2


_CdapNx64BitInversion_Type.__name__ = "TruthValue"
_CdapNx64BitInversion_Object = MibTableColumn
cdapNx64BitInversion = _CdapNx64BitInversion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 347, 1, 1, 1, 1, 5),
    _CdapNx64BitInversion_Type()
)
cdapNx64BitInversion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdapNx64BitInversion.setStatus("current")
_CdapNx64ProfileInUse_Type = Gauge32
_CdapNx64ProfileInUse_Object = MibTableColumn
cdapNx64ProfileInUse = _CdapNx64ProfileInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 347, 1, 1, 1, 1, 6),
    _CdapNx64ProfileInUse_Type()
)
cdapNx64ProfileInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdapNx64ProfileInUse.setStatus("current")
_CdapNx64RowStatus_Type = RowStatus
_CdapNx64RowStatus_Object = MibTableColumn
cdapNx64RowStatus = _CdapNx64RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 347, 1, 1, 1, 1, 7),
    _CdapNx64RowStatus_Type()
)
cdapNx64RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdapNx64RowStatus.setStatus("current")
_CdapNx64Aal1ProfileConfig_ObjectIdentity = ObjectIdentity
cdapNx64Aal1ProfileConfig = _CdapNx64Aal1ProfileConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 347, 1, 2)
)
_CdapNx64Aal1ProfileTable_Object = MibTable
cdapNx64Aal1ProfileTable = _CdapNx64Aal1ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 347, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cdapNx64Aal1ProfileTable.setStatus("current")
_CdapNx64Aal1ProfileEntry_Object = MibTableRow
cdapNx64Aal1ProfileEntry = _CdapNx64Aal1ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 347, 1, 2, 1, 1)
)
cdapNx64Aal1ProfileEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-DATA-AALX-PROFILE-MIB", "cdapNx64Aal1ProfileIndex"),
)
if mibBuilder.loadTexts:
    cdapNx64Aal1ProfileEntry.setStatus("current")


class _CdapNx64Aal1ProfileIndex_Type(Integer32):
    """Custom type cdapNx64Aal1ProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CdapNx64Aal1ProfileIndex_Type.__name__ = "Integer32"
_CdapNx64Aal1ProfileIndex_Object = MibTableColumn
cdapNx64Aal1ProfileIndex = _CdapNx64Aal1ProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 347, 1, 2, 1, 1, 1),
    _CdapNx64Aal1ProfileIndex_Type()
)
cdapNx64Aal1ProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdapNx64Aal1ProfileIndex.setStatus("current")


class _CdapNx64Aal1Encoding_Type(Integer32):
    """Custom type cdapNx64Aal1Encoding based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("g711ulaw", 1),
          ("g711alaw", 2),
          ("clearChannel", 3))
    )


_CdapNx64Aal1Encoding_Type.__name__ = "Integer32"
_CdapNx64Aal1Encoding_Object = MibTableColumn
cdapNx64Aal1Encoding = _CdapNx64Aal1Encoding_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 347, 1, 2, 1, 1, 2),
    _CdapNx64Aal1Encoding_Type()
)
cdapNx64Aal1Encoding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdapNx64Aal1Encoding.setStatus("current")


class _CdapNx64Aal1CellFill_Type(Integer32):
    """Custom type cdapNx64Aal1CellFill based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cellFill40bytes", 1),
          ("cellFill44bytes", 2),
          ("cellFill47bytes", 3))
    )


_CdapNx64Aal1CellFill_Type.__name__ = "Integer32"
_CdapNx64Aal1CellFill_Object = MibTableColumn
cdapNx64Aal1CellFill = _CdapNx64Aal1CellFill_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 347, 1, 2, 1, 1, 3),
    _CdapNx64Aal1CellFill_Type()
)
cdapNx64Aal1CellFill.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdapNx64Aal1CellFill.setStatus("current")
_CdapNx64Aal1ProfileInUse_Type = Gauge32
_CdapNx64Aal1ProfileInUse_Object = MibTableColumn
cdapNx64Aal1ProfileInUse = _CdapNx64Aal1ProfileInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 347, 1, 2, 1, 1, 4),
    _CdapNx64Aal1ProfileInUse_Type()
)
cdapNx64Aal1ProfileInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdapNx64Aal1ProfileInUse.setStatus("current")
_CdapNx64Aal1RowStatus_Type = RowStatus
_CdapNx64Aal1RowStatus_Object = MibTableColumn
cdapNx64Aal1RowStatus = _CdapNx64Aal1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 347, 1, 2, 1, 1, 5),
    _CdapNx64Aal1RowStatus_Type()
)
cdapNx64Aal1RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdapNx64Aal1RowStatus.setStatus("current")
_CdapNx64ProfileMIBConformance_ObjectIdentity = ObjectIdentity
cdapNx64ProfileMIBConformance = _CdapNx64ProfileMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 347, 2)
)
_CdapNx64MIBCompliances_ObjectIdentity = ObjectIdentity
cdapNx64MIBCompliances = _CdapNx64MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 347, 2, 1)
)
_CdapNx64MIBGroups_ObjectIdentity = ObjectIdentity
cdapNx64MIBGroups = _CdapNx64MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 347, 2, 2)
)

# Managed Objects groups

cdapNx64ProfileMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 347, 2, 2, 1)
)
cdapNx64ProfileMIBGroup.setObjects(
      *(("CISCO-DATA-AALX-PROFILE-MIB", "cdapNx64TransportMode"),
        ("CISCO-DATA-AALX-PROFILE-MIB", "cdapNx64FrameFillPattern"),
        ("CISCO-DATA-AALX-PROFILE-MIB", "cdapNx64InterFrameGapFlagCount"),
        ("CISCO-DATA-AALX-PROFILE-MIB", "cdapNx64BitInversion"),
        ("CISCO-DATA-AALX-PROFILE-MIB", "cdapNx64ProfileInUse"),
        ("CISCO-DATA-AALX-PROFILE-MIB", "cdapNx64RowStatus"))
)
if mibBuilder.loadTexts:
    cdapNx64ProfileMIBGroup.setStatus("current")

cdapNx64Aal1ProfileMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 347, 2, 2, 2)
)
cdapNx64Aal1ProfileMIBGroup.setObjects(
      *(("CISCO-DATA-AALX-PROFILE-MIB", "cdapNx64Aal1Encoding"),
        ("CISCO-DATA-AALX-PROFILE-MIB", "cdapNx64Aal1CellFill"),
        ("CISCO-DATA-AALX-PROFILE-MIB", "cdapNx64Aal1ProfileInUse"),
        ("CISCO-DATA-AALX-PROFILE-MIB", "cdapNx64Aal1RowStatus"))
)
if mibBuilder.loadTexts:
    cdapNx64Aal1ProfileMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cdapNx64MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 347, 2, 1, 1)
)
cdapNx64MIBCompliance.setObjects(
      *(("CISCO-DATA-AALX-PROFILE-MIB", "cdapNx64ProfileMIBGroup"),
        ("CISCO-DATA-AALX-PROFILE-MIB", "cdapNx64Aal1ProfileMIBGroup"))
)
if mibBuilder.loadTexts:
    cdapNx64MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DATA-AALX-PROFILE-MIB",
    **{"ciscoDataAalxProfileMIB": ciscoDataAalxProfileMIB,
       "cdapMIBNotifications": cdapMIBNotifications,
       "cdapMIBObjects": cdapMIBObjects,
       "cdapNx64ProfileConfig": cdapNx64ProfileConfig,
       "cdapNx64ProfileTable": cdapNx64ProfileTable,
       "cdapNx64ProfileEntry": cdapNx64ProfileEntry,
       "cdapNx64ProfileIndex": cdapNx64ProfileIndex,
       "cdapNx64TransportMode": cdapNx64TransportMode,
       "cdapNx64FrameFillPattern": cdapNx64FrameFillPattern,
       "cdapNx64InterFrameGapFlagCount": cdapNx64InterFrameGapFlagCount,
       "cdapNx64BitInversion": cdapNx64BitInversion,
       "cdapNx64ProfileInUse": cdapNx64ProfileInUse,
       "cdapNx64RowStatus": cdapNx64RowStatus,
       "cdapNx64Aal1ProfileConfig": cdapNx64Aal1ProfileConfig,
       "cdapNx64Aal1ProfileTable": cdapNx64Aal1ProfileTable,
       "cdapNx64Aal1ProfileEntry": cdapNx64Aal1ProfileEntry,
       "cdapNx64Aal1ProfileIndex": cdapNx64Aal1ProfileIndex,
       "cdapNx64Aal1Encoding": cdapNx64Aal1Encoding,
       "cdapNx64Aal1CellFill": cdapNx64Aal1CellFill,
       "cdapNx64Aal1ProfileInUse": cdapNx64Aal1ProfileInUse,
       "cdapNx64Aal1RowStatus": cdapNx64Aal1RowStatus,
       "cdapNx64ProfileMIBConformance": cdapNx64ProfileMIBConformance,
       "cdapNx64MIBCompliances": cdapNx64MIBCompliances,
       "cdapNx64MIBCompliance": cdapNx64MIBCompliance,
       "cdapNx64MIBGroups": cdapNx64MIBGroups,
       "cdapNx64ProfileMIBGroup": cdapNx64ProfileMIBGroup,
       "cdapNx64Aal1ProfileMIBGroup": cdapNx64Aal1ProfileMIBGroup}
)
