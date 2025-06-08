# SNMP MIB module (CISCO-LWAPP-OPENDNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-OPENDNS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:55:05 2025
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

(cLWlanIndex,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    "cLWlanIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

ciscoLwappOpendnsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 837)
)
if mibBuilder.loadTexts:
    ciscoLwappOpendnsMIB.setRevisions(
        ("2018-07-03 00:00",
         "2017-02-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappOpendnsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappOpendnsMIBNotifs = _CiscoLwappOpendnsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 0)
)
_CiscoLwappOpendnsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappOpendnsMIBObjects = _CiscoLwappOpendnsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 1)
)
_CiscoLwappOpendnsTag_ObjectIdentity = ObjectIdentity
ciscoLwappOpendnsTag = _CiscoLwappOpendnsTag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1)
)
_ClaOpendnsProfileTable_Object = MibTable
claOpendnsProfileTable = _ClaOpendnsProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 1)
)
if mibBuilder.loadTexts:
    claOpendnsProfileTable.setStatus("current")
_ClaOpendnsProfileEntry_Object = MibTableRow
claOpendnsProfileEntry = _ClaOpendnsProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 1, 1)
)
claOpendnsProfileEntry.setIndexNames(
    (0, "CISCO-LWAPP-OPENDNS-MIB", "claOpendnsProfileName"),
)
if mibBuilder.loadTexts:
    claOpendnsProfileEntry.setStatus("current")
_ClaOpendnsProfileName_Type = SnmpAdminString
_ClaOpendnsProfileName_Object = MibTableColumn
claOpendnsProfileName = _ClaOpendnsProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 1, 1, 1),
    _ClaOpendnsProfileName_Type()
)
claOpendnsProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    claOpendnsProfileName.setStatus("current")
_ClaOpendnsProfileRowStatus_Type = RowStatus
_ClaOpendnsProfileRowStatus_Object = MibTableColumn
claOpendnsProfileRowStatus = _ClaOpendnsProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 1, 1, 2),
    _ClaOpendnsProfileRowStatus_Type()
)
claOpendnsProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claOpendnsProfileRowStatus.setStatus("current")


class _ClaOpendnsProfileStatus_Type(Integer32):
    """Custom type claOpendnsProfileStatus based on Integer32"""
    defaultValue = 1

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
        *(("notInuse", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4),
          ("inuse", 5))
    )


_ClaOpendnsProfileStatus_Type.__name__ = "Integer32"
_ClaOpendnsProfileStatus_Object = MibTableColumn
claOpendnsProfileStatus = _ClaOpendnsProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 1, 1, 3),
    _ClaOpendnsProfileStatus_Type()
)
claOpendnsProfileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claOpendnsProfileStatus.setStatus("current")
_ClaOpendnsProfileIdentity_Type = SnmpAdminString
_ClaOpendnsProfileIdentity_Object = MibTableColumn
claOpendnsProfileIdentity = _ClaOpendnsProfileIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 1, 1, 4),
    _ClaOpendnsProfileIdentity_Type()
)
claOpendnsProfileIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claOpendnsProfileIdentity.setStatus("current")
_ClaOpendnsWlanTable_Object = MibTable
claOpendnsWlanTable = _ClaOpendnsWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 2)
)
if mibBuilder.loadTexts:
    claOpendnsWlanTable.setStatus("current")
_ClaOpendnsWlanEntry_Object = MibTableRow
claOpendnsWlanEntry = _ClaOpendnsWlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 2, 1)
)
claOpendnsWlanEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    claOpendnsWlanEntry.setStatus("current")


class _ClaOpendnsWlanProfileName_Type(SnmpAdminString):
    """Custom type claOpendnsWlanProfileName based on SnmpAdminString"""
    defaultValue = OctetString("")


_ClaOpendnsWlanProfileName_Type.__name__ = "SnmpAdminString"
_ClaOpendnsWlanProfileName_Object = MibTableColumn
claOpendnsWlanProfileName = _ClaOpendnsWlanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 2, 1, 1),
    _ClaOpendnsWlanProfileName_Type()
)
claOpendnsWlanProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claOpendnsWlanProfileName.setStatus("current")


class _ClaOpendnsWlanMode_Type(Integer32):
    """Custom type claOpendnsWlanMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("force", 2),
          ("copy", 3))
    )


_ClaOpendnsWlanMode_Type.__name__ = "Integer32"
_ClaOpendnsWlanMode_Object = MibTableColumn
claOpendnsWlanMode = _ClaOpendnsWlanMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 2, 1, 2),
    _ClaOpendnsWlanMode_Type()
)
claOpendnsWlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claOpendnsWlanMode.setStatus("current")


class _ClaOpendnsWlanProfileStatus_Type(TruthValue):
    """Custom type claOpendnsWlanProfileStatus based on TruthValue"""
    defaultValue = 2


_ClaOpendnsWlanProfileStatus_Type.__name__ = "TruthValue"
_ClaOpendnsWlanProfileStatus_Object = MibTableColumn
claOpendnsWlanProfileStatus = _ClaOpendnsWlanProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 2, 1, 3),
    _ClaOpendnsWlanProfileStatus_Type()
)
claOpendnsWlanProfileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claOpendnsWlanProfileStatus.setStatus("current")


class _ClaOpendnsWlanDhcpOpt6_Type(TruthValue):
    """Custom type claOpendnsWlanDhcpOpt6 based on TruthValue"""
    defaultValue = 1


_ClaOpendnsWlanDhcpOpt6_Type.__name__ = "TruthValue"
_ClaOpendnsWlanDhcpOpt6_Object = MibTableColumn
claOpendnsWlanDhcpOpt6 = _ClaOpendnsWlanDhcpOpt6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 2, 1, 4),
    _ClaOpendnsWlanDhcpOpt6_Type()
)
claOpendnsWlanDhcpOpt6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claOpendnsWlanDhcpOpt6.setStatus("current")
_CiscoLwappOpendnsConfig_ObjectIdentity = ObjectIdentity
ciscoLwappOpendnsConfig = _CiscoLwappOpendnsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 2)
)


class _ClaOpendnsEnable_Type(TruthValue):
    """Custom type claOpendnsEnable based on TruthValue"""
    defaultValue = 2


_ClaOpendnsEnable_Type.__name__ = "TruthValue"
_ClaOpendnsEnable_Object = MibScalar
claOpendnsEnable = _ClaOpendnsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 2, 1),
    _ClaOpendnsEnable_Type()
)
claOpendnsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claOpendnsEnable.setStatus("current")


class _ClaOpendnsForceEnable_Type(TruthValue):
    """Custom type claOpendnsForceEnable based on TruthValue"""
    defaultValue = 2


_ClaOpendnsForceEnable_Type.__name__ = "TruthValue"
_ClaOpendnsForceEnable_Object = MibScalar
claOpendnsForceEnable = _ClaOpendnsForceEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 2, 2),
    _ClaOpendnsForceEnable_Type()
)
claOpendnsForceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claOpendnsForceEnable.setStatus("current")


class _ClaOpendnsApiToken_Type(SnmpAdminString):
    """Custom type claOpendnsApiToken based on SnmpAdminString"""
    defaultValue = OctetString("")


_ClaOpendnsApiToken_Type.__name__ = "SnmpAdminString"
_ClaOpendnsApiToken_Object = MibScalar
claOpendnsApiToken = _ClaOpendnsApiToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 2, 3),
    _ClaOpendnsApiToken_Type()
)
claOpendnsApiToken.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claOpendnsApiToken.setStatus("current")
_CiscoLwappOpendnsMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappOpendnsMIBConform = _CiscoLwappOpendnsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 2)
)
_CiscoLwappOpendnsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappOpendnsMIBCompliances = _CiscoLwappOpendnsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 2, 1)
)
_CiscoLwappOpendnsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappOpendnsMIBGroups = _CiscoLwappOpendnsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 2, 2)
)

# Managed Objects groups

ciscoLwappOpendnsTagGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 2, 2, 1)
)
ciscoLwappOpendnsTagGroup.setObjects(
      *(("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsProfileRowStatus"),
        ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsWlanProfileName"),
        ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsWlanMode"),
        ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsWlanProfileStatus"),
        ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsProfileStatus"),
        ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsProfileIdentity"))
)
if mibBuilder.loadTexts:
    ciscoLwappOpendnsTagGroup.setStatus("deprecated")

ciscoLwappOpendnsConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 2, 2, 2)
)
ciscoLwappOpendnsConfigGroup.setObjects(
      *(("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsEnable"),
        ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsForceEnable"),
        ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsApiToken"))
)
if mibBuilder.loadTexts:
    ciscoLwappOpendnsConfigGroup.setStatus("current")

ciscoLwappOpendnsTagGroupVer2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 2, 2, 3)
)
ciscoLwappOpendnsTagGroupVer2.setObjects(
      *(("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsProfileRowStatus"),
        ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsWlanProfileName"),
        ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsWlanMode"),
        ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsWlanProfileStatus"),
        ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsProfileStatus"),
        ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsProfileIdentity"),
        ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsWlanDhcpOpt6"))
)
if mibBuilder.loadTexts:
    ciscoLwappOpendnsTagGroupVer2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappOpendnsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 2, 1, 1)
)
ciscoLwappOpendnsMIBCompliance.setObjects(
    ("CISCO-LWAPP-OPENDNS-MIB", "ciscoLwappOpendnsTagGroup")
)
if mibBuilder.loadTexts:
    ciscoLwappOpendnsMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappOpendnsMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 2, 1, 2)
)
ciscoLwappOpendnsMIBComplianceRev1.setObjects(
      *(("CISCO-LWAPP-OPENDNS-MIB", "ciscoLwappOpendnsTagGroup"),
        ("CISCO-LWAPP-OPENDNS-MIB", "ciscoLwappOpendnsConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappOpendnsMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoLwappOpendnsMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 837, 2, 1, 3)
)
ciscoLwappOpendnsMIBComplianceRev2.setObjects(
      *(("CISCO-LWAPP-OPENDNS-MIB", "ciscoLwappOpendnsTagGroup"),
        ("CISCO-LWAPP-OPENDNS-MIB", "ciscoLwappOpendnsConfigGroup"),
        ("CISCO-LWAPP-OPENDNS-MIB", "ciscoLwappOpendnsTagGroupVer2"))
)
if mibBuilder.loadTexts:
    ciscoLwappOpendnsMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-OPENDNS-MIB",
    **{"ciscoLwappOpendnsMIB": ciscoLwappOpendnsMIB,
       "ciscoLwappOpendnsMIBNotifs": ciscoLwappOpendnsMIBNotifs,
       "ciscoLwappOpendnsMIBObjects": ciscoLwappOpendnsMIBObjects,
       "ciscoLwappOpendnsTag": ciscoLwappOpendnsTag,
       "claOpendnsProfileTable": claOpendnsProfileTable,
       "claOpendnsProfileEntry": claOpendnsProfileEntry,
       "claOpendnsProfileName": claOpendnsProfileName,
       "claOpendnsProfileRowStatus": claOpendnsProfileRowStatus,
       "claOpendnsProfileStatus": claOpendnsProfileStatus,
       "claOpendnsProfileIdentity": claOpendnsProfileIdentity,
       "claOpendnsWlanTable": claOpendnsWlanTable,
       "claOpendnsWlanEntry": claOpendnsWlanEntry,
       "claOpendnsWlanProfileName": claOpendnsWlanProfileName,
       "claOpendnsWlanMode": claOpendnsWlanMode,
       "claOpendnsWlanProfileStatus": claOpendnsWlanProfileStatus,
       "claOpendnsWlanDhcpOpt6": claOpendnsWlanDhcpOpt6,
       "ciscoLwappOpendnsConfig": ciscoLwappOpendnsConfig,
       "claOpendnsEnable": claOpendnsEnable,
       "claOpendnsForceEnable": claOpendnsForceEnable,
       "claOpendnsApiToken": claOpendnsApiToken,
       "ciscoLwappOpendnsMIBConform": ciscoLwappOpendnsMIBConform,
       "ciscoLwappOpendnsMIBCompliances": ciscoLwappOpendnsMIBCompliances,
       "ciscoLwappOpendnsMIBCompliance": ciscoLwappOpendnsMIBCompliance,
       "ciscoLwappOpendnsMIBComplianceRev1": ciscoLwappOpendnsMIBComplianceRev1,
       "ciscoLwappOpendnsMIBComplianceRev2": ciscoLwappOpendnsMIBComplianceRev2,
       "ciscoLwappOpendnsMIBGroups": ciscoLwappOpendnsMIBGroups,
       "ciscoLwappOpendnsTagGroup": ciscoLwappOpendnsTagGroup,
       "ciscoLwappOpendnsConfigGroup": ciscoLwappOpendnsConfigGroup,
       "ciscoLwappOpendnsTagGroupVer2": ciscoLwappOpendnsTagGroupVer2}
)
