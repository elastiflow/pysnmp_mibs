# SNMP MIB module (CISCO-IPSEC-PROF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-IPSEC-PROF-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:31:29 2025
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

(CLApIfType,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-TC-MIB",
    "CLApIfType")

(cLAPGroupName,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    "cLAPGroupName")

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
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappIPSECPROFMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 999998)
)
if mibBuilder.loadTexts:
    ciscoLwappIPSECPROFMIB.setRevisions(
        ("2011-11-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappIpsecProfMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappIpsecProfMIBNotifs = _CiscoLwappIpsecProfMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 999998, 0)
)
_CiscoLwappIpsecProfMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappIpsecProfMIBObjects = _CiscoLwappIpsecProfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 999998, 1)
)
_CiscoLwappIpsecProfConfig_ObjectIdentity = ObjectIdentity
ciscoLwappIpsecProfConfig = _CiscoLwappIpsecProfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 999998, 1, 1)
)
_CLIpsecProfileTable_Object = MibTable
cLIpsecProfileTable = _CLIpsecProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999998, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cLIpsecProfileTable.setStatus("current")
_CLIpsecProfileEntry_Object = MibTableRow
cLIpsecProfileEntry = _CLIpsecProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999998, 1, 1, 1, 1)
)
cLIpsecProfileEntry.setIndexNames(
    (0, "CISCO-IPSEC-PROF-MIB", "cLIpsecProfileName"),
)
if mibBuilder.loadTexts:
    cLIpsecProfileEntry.setStatus("current")


class _CLIpsecProfileName_Type(SnmpAdminString):
    """Custom type cLIpsecProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CLIpsecProfileName_Type.__name__ = "SnmpAdminString"
_CLIpsecProfileName_Object = MibTableColumn
cLIpsecProfileName = _CLIpsecProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999998, 1, 1, 1, 1, 1),
    _CLIpsecProfileName_Type()
)
cLIpsecProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLIpsecProfileName.setStatus("current")


class _CLIpsecProfAuthType_Type(Integer32):
    """Custom type cLIpsecProfAuthType based on Integer32"""
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
        *(("none", 0),
          ("hmacMd5", 1),
          ("hmacsha1", 2),
          ("hmacsha256", 3),
          ("hmacsha384", 4))
    )


_CLIpsecProfAuthType_Type.__name__ = "Integer32"
_CLIpsecProfAuthType_Object = MibTableColumn
cLIpsecProfAuthType = _CLIpsecProfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999998, 1, 1, 1, 1, 2),
    _CLIpsecProfAuthType_Type()
)
cLIpsecProfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpsecProfAuthType.setStatus("current")


class _CLIpsecProfEncrType_Type(Integer32):
    """Custom type cLIpsecProfEncrType based on Integer32"""
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
        *(("none", 0),
          ("des", 1),
          ("tripleDes", 2),
          ("aesCbc", 3),
          ("aes256Cbc", 4),
          ("aes128gcm", 5),
          ("aes256gcm", 6))
    )


_CLIpsecProfEncrType_Type.__name__ = "Integer32"
_CLIpsecProfEncrType_Object = MibTableColumn
cLIpsecProfEncrType = _CLIpsecProfEncrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999998, 1, 1, 1, 1, 3),
    _CLIpsecProfEncrType_Type()
)
cLIpsecProfEncrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpsecProfEncrType.setStatus("current")


class _CLIpsecProfIkeVersion_Type(Integer32):
    """Custom type cLIpsecProfIkeVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ike", 0),
          ("v1", 1),
          ("v2", 2))
    )


_CLIpsecProfIkeVersion_Type.__name__ = "Integer32"
_CLIpsecProfIkeVersion_Object = MibTableColumn
cLIpsecProfIkeVersion = _CLIpsecProfIkeVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999998, 1, 1, 1, 1, 4),
    _CLIpsecProfIkeVersion_Type()
)
cLIpsecProfIkeVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpsecProfIkeVersion.setStatus("current")


class _CLIpsecProfIkeLifetime_Type(Unsigned32):
    """Custom type cLIpsecProfIkeLifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 84600),
    )


_CLIpsecProfIkeLifetime_Type.__name__ = "Unsigned32"
_CLIpsecProfIkeLifetime_Object = MibTableColumn
cLIpsecProfIkeLifetime = _CLIpsecProfIkeLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999998, 1, 1, 1, 1, 5),
    _CLIpsecProfIkeLifetime_Type()
)
cLIpsecProfIkeLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpsecProfIkeLifetime.setStatus("current")


class _CLIpsecProfPhase2Lifetime_Type(Unsigned32):
    """Custom type cLIpsecProfPhase2Lifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 84600),
    )


_CLIpsecProfPhase2Lifetime_Type.__name__ = "Unsigned32"
_CLIpsecProfPhase2Lifetime_Object = MibTableColumn
cLIpsecProfPhase2Lifetime = _CLIpsecProfPhase2Lifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999998, 1, 1, 1, 1, 6),
    _CLIpsecProfPhase2Lifetime_Type()
)
cLIpsecProfPhase2Lifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpsecProfPhase2Lifetime.setStatus("current")


class _CLIpsecProfIKEPhase1_Type(Integer32):
    """Custom type cLIpsecProfIKEPhase1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("agressive", 2))
    )


_CLIpsecProfIKEPhase1_Type.__name__ = "Integer32"
_CLIpsecProfIKEPhase1_Object = MibTableColumn
cLIpsecProfIKEPhase1 = _CLIpsecProfIKEPhase1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999998, 1, 1, 1, 1, 7),
    _CLIpsecProfIKEPhase1_Type()
)
cLIpsecProfIKEPhase1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpsecProfIKEPhase1.setStatus("current")


class _CLIpsecProfIKEDHGroup_Type(Integer32):
    """Custom type cLIpsecProfIKEDHGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              14,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("group1", 1),
          ("group2", 2),
          ("group5", 5),
          ("group14", 14),
          ("group19", 19),
          ("group20", 20))
    )


_CLIpsecProfIKEDHGroup_Type.__name__ = "Integer32"
_CLIpsecProfIKEDHGroup_Object = MibTableColumn
cLIpsecProfIKEDHGroup = _CLIpsecProfIKEDHGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999998, 1, 1, 1, 1, 8),
    _CLIpsecProfIKEDHGroup_Type()
)
cLIpsecProfIKEDHGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpsecProfIKEDHGroup.setStatus("current")


class _CLIpsecProfAuthMode_Type(Integer32):
    """Custom type cLIpsecProfAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("psk", 1),
          ("cert", 2))
    )


_CLIpsecProfAuthMode_Type.__name__ = "Integer32"
_CLIpsecProfAuthMode_Object = MibTableColumn
cLIpsecProfAuthMode = _CLIpsecProfAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999998, 1, 1, 1, 1, 9),
    _CLIpsecProfAuthMode_Type()
)
cLIpsecProfAuthMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpsecProfAuthMode.setStatus("current")


class _CLIpsecProfAuthPSK_Type(OctetString):
    """Custom type cLIpsecProfAuthPSK based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CLIpsecProfAuthPSK_Type.__name__ = "OctetString"
_CLIpsecProfAuthPSK_Object = MibTableColumn
cLIpsecProfAuthPSK = _CLIpsecProfAuthPSK_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999998, 1, 1, 1, 1, 10),
    _CLIpsecProfAuthPSK_Type()
)
cLIpsecProfAuthPSK.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpsecProfAuthPSK.setStatus("current")


class _CLIpsecProfAuthModeKeyFormat_Type(Integer32):
    """Custom type cLIpsecProfAuthModeKeyFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hex", 1),
          ("ascii", 2))
    )


_CLIpsecProfAuthModeKeyFormat_Type.__name__ = "Integer32"
_CLIpsecProfAuthModeKeyFormat_Object = MibTableColumn
cLIpsecProfAuthModeKeyFormat = _CLIpsecProfAuthModeKeyFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999998, 1, 1, 1, 1, 11),
    _CLIpsecProfAuthModeKeyFormat_Type()
)
cLIpsecProfAuthModeKeyFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpsecProfAuthModeKeyFormat.setStatus("current")


class _CLIpsecProfPeerIdType_Type(Integer32):
    """Custom type cLIpsecProfPeerIdType based on Integer32"""
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
        *(("none", 0),
          ("fqdn", 1),
          ("user-fqdn", 2),
          ("dn", 3),
          ("ip", 4))
    )


_CLIpsecProfPeerIdType_Type.__name__ = "Integer32"
_CLIpsecProfPeerIdType_Object = MibTableColumn
cLIpsecProfPeerIdType = _CLIpsecProfPeerIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999998, 1, 1, 1, 1, 12),
    _CLIpsecProfPeerIdType_Type()
)
cLIpsecProfPeerIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpsecProfPeerIdType.setStatus("current")


class _CLIpsecProfPeerIdValue_Type(OctetString):
    """Custom type cLIpsecProfPeerIdValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CLIpsecProfPeerIdValue_Type.__name__ = "OctetString"
_CLIpsecProfPeerIdValue_Object = MibTableColumn
cLIpsecProfPeerIdValue = _CLIpsecProfPeerIdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999998, 1, 1, 1, 1, 13),
    _CLIpsecProfPeerIdValue_Type()
)
cLIpsecProfPeerIdValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpsecProfPeerIdValue.setStatus("current")
_CLIpsecProfileRowStatus_Type = RowStatus
_CLIpsecProfileRowStatus_Object = MibTableColumn
cLIpsecProfileRowStatus = _CLIpsecProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999998, 1, 1, 1, 1, 14),
    _CLIpsecProfileRowStatus_Type()
)
cLIpsecProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLIpsecProfileRowStatus.setStatus("current")
_CiscoLwappIpsecProfMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappIpsecProfMIBConform = _CiscoLwappIpsecProfMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 999998, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IPSEC-PROF-MIB",
    **{"ciscoLwappIPSECPROFMIB": ciscoLwappIPSECPROFMIB,
       "ciscoLwappIpsecProfMIBNotifs": ciscoLwappIpsecProfMIBNotifs,
       "ciscoLwappIpsecProfMIBObjects": ciscoLwappIpsecProfMIBObjects,
       "ciscoLwappIpsecProfConfig": ciscoLwappIpsecProfConfig,
       "cLIpsecProfileTable": cLIpsecProfileTable,
       "cLIpsecProfileEntry": cLIpsecProfileEntry,
       "cLIpsecProfileName": cLIpsecProfileName,
       "cLIpsecProfAuthType": cLIpsecProfAuthType,
       "cLIpsecProfEncrType": cLIpsecProfEncrType,
       "cLIpsecProfIkeVersion": cLIpsecProfIkeVersion,
       "cLIpsecProfIkeLifetime": cLIpsecProfIkeLifetime,
       "cLIpsecProfPhase2Lifetime": cLIpsecProfPhase2Lifetime,
       "cLIpsecProfIKEPhase1": cLIpsecProfIKEPhase1,
       "cLIpsecProfIKEDHGroup": cLIpsecProfIKEDHGroup,
       "cLIpsecProfAuthMode": cLIpsecProfAuthMode,
       "cLIpsecProfAuthPSK": cLIpsecProfAuthPSK,
       "cLIpsecProfAuthModeKeyFormat": cLIpsecProfAuthModeKeyFormat,
       "cLIpsecProfPeerIdType": cLIpsecProfPeerIdType,
       "cLIpsecProfPeerIdValue": cLIpsecProfPeerIdValue,
       "cLIpsecProfileRowStatus": cLIpsecProfileRowStatus,
       "ciscoLwappIpsecProfMIBConform": ciscoLwappIpsecProfMIBConform}
)
