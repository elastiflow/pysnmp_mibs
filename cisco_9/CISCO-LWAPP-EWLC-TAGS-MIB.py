# SNMP MIB module (CISCO-LWAPP-EWLC-TAGS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-TAGS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:55:04 2025
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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappTagsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 987)
)
if mibBuilder.loadTexts:
    ciscoLwappTagsMIB.setRevisions(
        ("2018-09-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappTagsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappTagsMIBNotifs = _CiscoLwappTagsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 0)
)
_CiscoLwappApLocationConfig_ObjectIdentity = ObjectIdentity
ciscoLwappApLocationConfig = _CiscoLwappApLocationConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 0, 13)
)
_CLApLocationConfigTable_Object = MibTable
cLApLocationConfigTable = _CLApLocationConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 0, 13, 1)
)
if mibBuilder.loadTexts:
    cLApLocationConfigTable.setStatus("current")
_CLApLocationConfigEntry_Object = MibTableRow
cLApLocationConfigEntry = _CLApLocationConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 0, 13, 1, 1)
)
cLApLocationConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-EWLC-TAGS-MIB", "cLApLocationName"),
)
if mibBuilder.loadTexts:
    cLApLocationConfigEntry.setStatus("current")
_CLApLocationName_Type = SnmpAdminString
_CLApLocationName_Object = MibTableColumn
cLApLocationName = _CLApLocationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 0, 13, 1, 1, 1),
    _CLApLocationName_Type()
)
cLApLocationName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApLocationName.setStatus("current")
_CLApLocationSiteTag_Type = SnmpAdminString
_CLApLocationSiteTag_Object = MibTableColumn
cLApLocationSiteTag = _CLApLocationSiteTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 0, 13, 1, 1, 2),
    _CLApLocationSiteTag_Type()
)
cLApLocationSiteTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLocationSiteTag.setStatus("current")
_CLApLocationRfTag_Type = SnmpAdminString
_CLApLocationRfTag_Object = MibTableColumn
cLApLocationRfTag = _CLApLocationRfTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 0, 13, 1, 1, 3),
    _CLApLocationRfTag_Type()
)
cLApLocationRfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLocationRfTag.setStatus("current")
_CLApLocationPolicyTag_Type = SnmpAdminString
_CLApLocationPolicyTag_Object = MibTableColumn
cLApLocationPolicyTag = _CLApLocationPolicyTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 0, 13, 1, 1, 4),
    _CLApLocationPolicyTag_Type()
)
cLApLocationPolicyTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLocationPolicyTag.setStatus("current")
_CLApLocationConfigRowStatus_Type = RowStatus
_CLApLocationConfigRowStatus_Object = MibTableColumn
cLApLocationConfigRowStatus = _CLApLocationConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 0, 13, 1, 1, 5),
    _CLApLocationConfigRowStatus_Type()
)
cLApLocationConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApLocationConfigRowStatus.setStatus("current")
_CLApLocationDesc_Type = SnmpAdminString
_CLApLocationDesc_Object = MibTableColumn
cLApLocationDesc = _CLApLocationDesc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 0, 13, 1, 1, 6),
    _CLApLocationDesc_Type()
)
cLApLocationDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLocationDesc.setStatus("current")
_CiscoLwappAssociatedApsConfig_ObjectIdentity = ObjectIdentity
ciscoLwappAssociatedApsConfig = _CiscoLwappAssociatedApsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 0, 14)
)
_CLAssociatedApsConfigTable_Object = MibTable
cLAssociatedApsConfigTable = _CLAssociatedApsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 0, 14, 1)
)
if mibBuilder.loadTexts:
    cLAssociatedApsConfigTable.setStatus("current")
_CLAssociatedApsConfigEntry_Object = MibTableRow
cLAssociatedApsConfigEntry = _CLAssociatedApsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 0, 14, 1, 1)
)
cLAssociatedApsConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-EWLC-TAGS-MIB", "cLApLocationName"),
    (0, "CISCO-LWAPP-EWLC-TAGS-MIB", "cLAssociatedApsApMac"),
)
if mibBuilder.loadTexts:
    cLAssociatedApsConfigEntry.setStatus("current")
_CLAssociatedApsApMac_Type = MacAddress
_CLAssociatedApsApMac_Object = MibTableColumn
cLAssociatedApsApMac = _CLAssociatedApsApMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 0, 14, 1, 1, 1),
    _CLAssociatedApsApMac_Type()
)
cLAssociatedApsApMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLAssociatedApsApMac.setStatus("current")
_CLAssociatedApsConfigRowStatus_Type = RowStatus
_CLAssociatedApsConfigRowStatus_Object = MibTableColumn
cLAssociatedApsConfigRowStatus = _CLAssociatedApsConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 0, 14, 1, 1, 2),
    _CLAssociatedApsConfigRowStatus_Type()
)
cLAssociatedApsConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLAssociatedApsConfigRowStatus.setStatus("current")
_CiscoLwappTagsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappTagsMIBObjects = _CiscoLwappTagsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1)
)
_CiscoLwappPolicyTagConfig_ObjectIdentity = ObjectIdentity
ciscoLwappPolicyTagConfig = _CiscoLwappPolicyTagConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 1)
)
_CLPolicyTagConfigTable_Object = MibTable
cLPolicyTagConfigTable = _CLPolicyTagConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cLPolicyTagConfigTable.setStatus("current")
_CLPolicyTagConfigEntry_Object = MibTableRow
cLPolicyTagConfigEntry = _CLPolicyTagConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 1, 1, 1)
)
cLPolicyTagConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-EWLC-TAGS-MIB", "cLPolicyTagName"),
)
if mibBuilder.loadTexts:
    cLPolicyTagConfigEntry.setStatus("current")


class _CLPolicyTagName_Type(SnmpAdminString):
    """Custom type cLPolicyTagName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLPolicyTagName_Type.__name__ = "SnmpAdminString"
_CLPolicyTagName_Object = MibTableColumn
cLPolicyTagName = _CLPolicyTagName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 1, 1, 1, 1),
    _CLPolicyTagName_Type()
)
cLPolicyTagName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLPolicyTagName.setStatus("current")


class _CLPolicyTagDescription_Type(SnmpAdminString):
    """Custom type cLPolicyTagDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLPolicyTagDescription_Type.__name__ = "SnmpAdminString"
_CLPolicyTagDescription_Object = MibTableColumn
cLPolicyTagDescription = _CLPolicyTagDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 1, 1, 1, 2),
    _CLPolicyTagDescription_Type()
)
cLPolicyTagDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLPolicyTagDescription.setStatus("current")
_CLPolicyTagRowStatus_Type = RowStatus
_CLPolicyTagRowStatus_Object = MibTableColumn
cLPolicyTagRowStatus = _CLPolicyTagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 1, 1, 1, 3),
    _CLPolicyTagRowStatus_Type()
)
cLPolicyTagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicyTagRowStatus.setStatus("current")
_CLPolicyProfileConfigTable_Object = MibTable
cLPolicyProfileConfigTable = _CLPolicyProfileConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cLPolicyProfileConfigTable.setStatus("current")
_CLPolicyProfileConfigEntry_Object = MibTableRow
cLPolicyProfileConfigEntry = _CLPolicyProfileConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 1, 2, 1)
)
cLPolicyProfileConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-EWLC-TAGS-MIB", "cLPolicyTagName"),
    (0, "CISCO-LWAPP-EWLC-TAGS-MIB", "cLProfileName"),
)
if mibBuilder.loadTexts:
    cLPolicyProfileConfigEntry.setStatus("current")


class _CLProfileName_Type(SnmpAdminString):
    """Custom type cLProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLProfileName_Type.__name__ = "SnmpAdminString"
_CLProfileName_Object = MibTableColumn
cLProfileName = _CLProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 1, 2, 1, 1),
    _CLProfileName_Type()
)
cLProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLProfileName.setStatus("current")


class _CLPolicyProfileName_Type(SnmpAdminString):
    """Custom type cLPolicyProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLPolicyProfileName_Type.__name__ = "SnmpAdminString"
_CLPolicyProfileName_Object = MibTableColumn
cLPolicyProfileName = _CLPolicyProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 1, 2, 1, 2),
    _CLPolicyProfileName_Type()
)
cLPolicyProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicyProfileName.setStatus("current")
_CLPolicyProfileRowStatus_Type = RowStatus
_CLPolicyProfileRowStatus_Object = MibTableColumn
cLPolicyProfileRowStatus = _CLPolicyProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 1, 2, 1, 3),
    _CLPolicyProfileRowStatus_Type()
)
cLPolicyProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicyProfileRowStatus.setStatus("current")
_CLRlanPolicyProfileConfigTable_Object = MibTable
cLRlanPolicyProfileConfigTable = _CLRlanPolicyProfileConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cLRlanPolicyProfileConfigTable.setStatus("current")
_CLRlanPolicyProfileConfigEntry_Object = MibTableRow
cLRlanPolicyProfileConfigEntry = _CLRlanPolicyProfileConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 1, 3, 1)
)
cLRlanPolicyProfileConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-EWLC-TAGS-MIB", "cLPolicyTagName"),
    (0, "CISCO-LWAPP-EWLC-TAGS-MIB", "cLRlanPortID"),
)
if mibBuilder.loadTexts:
    cLRlanPolicyProfileConfigEntry.setStatus("current")


class _CLRlanPortID_Type(Integer32):
    """Custom type cLRlanPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CLRlanPortID_Type.__name__ = "Integer32"
_CLRlanPortID_Object = MibTableColumn
cLRlanPortID = _CLRlanPortID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 1, 3, 1, 1),
    _CLRlanPortID_Type()
)
cLRlanPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLRlanPortID.setStatus("current")


class _CLRlanProfile_Type(SnmpAdminString):
    """Custom type cLRlanProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLRlanProfile_Type.__name__ = "SnmpAdminString"
_CLRlanProfile_Object = MibTableColumn
cLRlanProfile = _CLRlanProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 1, 3, 1, 2),
    _CLRlanProfile_Type()
)
cLRlanProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanProfile.setStatus("current")


class _CLRlanPolicyProfile_Type(SnmpAdminString):
    """Custom type cLRlanPolicyProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLRlanPolicyProfile_Type.__name__ = "SnmpAdminString"
_CLRlanPolicyProfile_Object = MibTableColumn
cLRlanPolicyProfile = _CLRlanPolicyProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 1, 3, 1, 3),
    _CLRlanPolicyProfile_Type()
)
cLRlanPolicyProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanPolicyProfile.setStatus("current")
_CLRlanPolicyProfileRowStatus_Type = RowStatus
_CLRlanPolicyProfileRowStatus_Object = MibTableColumn
cLRlanPolicyProfileRowStatus = _CLRlanPolicyProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 1, 3, 1, 4),
    _CLRlanPolicyProfileRowStatus_Type()
)
cLRlanPolicyProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRlanPolicyProfileRowStatus.setStatus("current")
_CiscoLwappSiteTagConfig_ObjectIdentity = ObjectIdentity
ciscoLwappSiteTagConfig = _CiscoLwappSiteTagConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 2)
)
_CLSiteTagConfigTable_Object = MibTable
cLSiteTagConfigTable = _CLSiteTagConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cLSiteTagConfigTable.setStatus("current")
_CLSiteTagConfigEntry_Object = MibTableRow
cLSiteTagConfigEntry = _CLSiteTagConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 2, 1, 1)
)
cLSiteTagConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-EWLC-TAGS-MIB", "cLSiteTagName"),
)
if mibBuilder.loadTexts:
    cLSiteTagConfigEntry.setStatus("current")


class _CLSiteTagName_Type(SnmpAdminString):
    """Custom type cLSiteTagName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLSiteTagName_Type.__name__ = "SnmpAdminString"
_CLSiteTagName_Object = MibTableColumn
cLSiteTagName = _CLSiteTagName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 2, 1, 1, 1),
    _CLSiteTagName_Type()
)
cLSiteTagName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLSiteTagName.setStatus("current")
_CLSiteTagRowStatus_Type = RowStatus
_CLSiteTagRowStatus_Object = MibTableColumn
cLSiteTagRowStatus = _CLSiteTagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 2, 1, 1, 2),
    _CLSiteTagRowStatus_Type()
)
cLSiteTagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLSiteTagRowStatus.setStatus("current")


class _CLApJoinProfName_Type(SnmpAdminString):
    """Custom type cLApJoinProfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLApJoinProfName_Type.__name__ = "SnmpAdminString"
_CLApJoinProfName_Object = MibTableColumn
cLApJoinProfName = _CLApJoinProfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 2, 1, 1, 3),
    _CLApJoinProfName_Type()
)
cLApJoinProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApJoinProfName.setStatus("current")


class _CLFlexProfName_Type(SnmpAdminString):
    """Custom type cLFlexProfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLFlexProfName_Type.__name__ = "SnmpAdminString"
_CLFlexProfName_Object = MibTableColumn
cLFlexProfName = _CLFlexProfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 2, 1, 1, 4),
    _CLFlexProfName_Type()
)
cLFlexProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLFlexProfName.setStatus("current")


class _CLSiteTagDescription_Type(SnmpAdminString):
    """Custom type cLSiteTagDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLSiteTagDescription_Type.__name__ = "SnmpAdminString"
_CLSiteTagDescription_Object = MibTableColumn
cLSiteTagDescription = _CLSiteTagDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 2, 1, 1, 5),
    _CLSiteTagDescription_Type()
)
cLSiteTagDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSiteTagDescription.setStatus("current")


class _CLReapSiteUpgradeStart_Type(Integer32):
    """Custom type cLReapSiteUpgradeStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("initiatePrimary", 1),
          ("initiateBackup", 2),
          ("abort", 3))
    )


_CLReapSiteUpgradeStart_Type.__name__ = "Integer32"
_CLReapSiteUpgradeStart_Object = MibTableColumn
cLReapSiteUpgradeStart = _CLReapSiteUpgradeStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 2, 1, 1, 6),
    _CLReapSiteUpgradeStart_Type()
)
cLReapSiteUpgradeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapSiteUpgradeStart.setStatus("current")


class _CLReapSiteTagStartCertificateDownload_Type(TruthValue):
    """Custom type cLReapSiteTagStartCertificateDownload based on TruthValue"""
    defaultValue = 2


_CLReapSiteTagStartCertificateDownload_Type.__name__ = "TruthValue"
_CLReapSiteTagStartCertificateDownload_Object = MibTableColumn
cLReapSiteTagStartCertificateDownload = _CLReapSiteTagStartCertificateDownload_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 2, 1, 1, 7),
    _CLReapSiteTagStartCertificateDownload_Type()
)
cLReapSiteTagStartCertificateDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapSiteTagStartCertificateDownload.setStatus("current")


class _CLIsLocalSite_Type(TruthValue):
    """Custom type cLIsLocalSite based on TruthValue"""
    defaultValue = 1


_CLIsLocalSite_Type.__name__ = "TruthValue"
_CLIsLocalSite_Object = MibTableColumn
cLIsLocalSite = _CLIsLocalSite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 2, 1, 1, 8),
    _CLIsLocalSite_Type()
)
cLIsLocalSite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLIsLocalSite.setStatus("current")
_CiscoLwappRfTagConfig_ObjectIdentity = ObjectIdentity
ciscoLwappRfTagConfig = _CiscoLwappRfTagConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 3)
)
_CLRfTagConfigTable_Object = MibTable
cLRfTagConfigTable = _CLRfTagConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cLRfTagConfigTable.setStatus("current")
_CLRfTagConfigEntry_Object = MibTableRow
cLRfTagConfigEntry = _CLRfTagConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 3, 1, 1)
)
cLRfTagConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-EWLC-TAGS-MIB", "cLRfTagName"),
)
if mibBuilder.loadTexts:
    cLRfTagConfigEntry.setStatus("current")


class _CLRfTagName_Type(SnmpAdminString):
    """Custom type cLRfTagName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLRfTagName_Type.__name__ = "SnmpAdminString"
_CLRfTagName_Object = MibTableColumn
cLRfTagName = _CLRfTagName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 3, 1, 1, 1),
    _CLRfTagName_Type()
)
cLRfTagName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLRfTagName.setStatus("current")
_CLRfTagRowStatus_Type = RowStatus
_CLRfTagRowStatus_Object = MibTableColumn
cLRfTagRowStatus = _CLRfTagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 3, 1, 1, 2),
    _CLRfTagRowStatus_Type()
)
cLRfTagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRfTagRowStatus.setStatus("current")


class _CL11aRfProfName_Type(SnmpAdminString):
    """Custom type cL11aRfProfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CL11aRfProfName_Type.__name__ = "SnmpAdminString"
_CL11aRfProfName_Object = MibTableColumn
cL11aRfProfName = _CL11aRfProfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 3, 1, 1, 3),
    _CL11aRfProfName_Type()
)
cL11aRfProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cL11aRfProfName.setStatus("current")


class _CL11bRfProfName_Type(SnmpAdminString):
    """Custom type cL11bRfProfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CL11bRfProfName_Type.__name__ = "SnmpAdminString"
_CL11bRfProfName_Object = MibTableColumn
cL11bRfProfName = _CL11bRfProfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 3, 1, 1, 4),
    _CL11bRfProfName_Type()
)
cL11bRfProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cL11bRfProfName.setStatus("current")


class _CLRfTagDescription_Type(SnmpAdminString):
    """Custom type cLRfTagDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLRfTagDescription_Type.__name__ = "SnmpAdminString"
_CLRfTagDescription_Object = MibTableColumn
cLRfTagDescription = _CLRfTagDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 3, 1, 1, 5),
    _CLRfTagDescription_Type()
)
cLRfTagDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRfTagDescription.setStatus("current")


class _CL6GHzBandRfProfName_Type(SnmpAdminString):
    """Custom type cL6GHzBandRfProfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CL6GHzBandRfProfName_Type.__name__ = "SnmpAdminString"
_CL6GHzBandRfProfName_Object = MibTableColumn
cL6GHzBandRfProfName = _CL6GHzBandRfProfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 3, 1, 1, 6),
    _CL6GHzBandRfProfName_Type()
)
cL6GHzBandRfProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cL6GHzBandRfProfName.setStatus("current")
_CiscoLwappApTag_ObjectIdentity = ObjectIdentity
ciscoLwappApTag = _CiscoLwappApTag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 4)
)
_CLApConfigTagTable_Object = MibTable
cLApConfigTagTable = _CLApConfigTagTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cLApConfigTagTable.setStatus("current")
_CLApConfigTagEntry_Object = MibTableRow
cLApConfigTagEntry = _CLApConfigTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 4, 1, 1)
)
cLApConfigTagEntry.setIndexNames(
    (0, "CISCO-LWAPP-EWLC-TAGS-MIB", "cLApConfigTagSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLApConfigTagEntry.setStatus("current")
_CLApConfigTagSysMacAddress_Type = MacAddress
_CLApConfigTagSysMacAddress_Object = MibTableColumn
cLApConfigTagSysMacAddress = _CLApConfigTagSysMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 4, 1, 1, 1),
    _CLApConfigTagSysMacAddress_Type()
)
cLApConfigTagSysMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApConfigTagSysMacAddress.setStatus("current")


class _CLApConfigPolicyTagName_Type(SnmpAdminString):
    """Custom type cLApConfigPolicyTagName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLApConfigPolicyTagName_Type.__name__ = "SnmpAdminString"
_CLApConfigPolicyTagName_Object = MibTableColumn
cLApConfigPolicyTagName = _CLApConfigPolicyTagName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 4, 1, 1, 2),
    _CLApConfigPolicyTagName_Type()
)
cLApConfigPolicyTagName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApConfigPolicyTagName.setStatus("current")


class _CLApConfigRfTagName_Type(SnmpAdminString):
    """Custom type cLApConfigRfTagName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLApConfigRfTagName_Type.__name__ = "SnmpAdminString"
_CLApConfigRfTagName_Object = MibTableColumn
cLApConfigRfTagName = _CLApConfigRfTagName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 4, 1, 1, 3),
    _CLApConfigRfTagName_Type()
)
cLApConfigRfTagName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApConfigRfTagName.setStatus("current")


class _CLApConfigSiteTagName_Type(SnmpAdminString):
    """Custom type cLApConfigSiteTagName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLApConfigSiteTagName_Type.__name__ = "SnmpAdminString"
_CLApConfigSiteTagName_Object = MibTableColumn
cLApConfigSiteTagName = _CLApConfigSiteTagName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 4, 1, 1, 4),
    _CLApConfigSiteTagName_Type()
)
cLApConfigSiteTagName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApConfigSiteTagName.setStatus("current")
_CLApConfigTagRowStatus_Type = RowStatus
_CLApConfigTagRowStatus_Object = MibTableColumn
cLApConfigTagRowStatus = _CLApConfigTagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 4, 1, 1, 5),
    _CLApConfigTagRowStatus_Type()
)
cLApConfigTagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApConfigTagRowStatus.setStatus("current")
_CLApTagSrcTable_Object = MibTable
cLApTagSrcTable = _CLApTagSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cLApTagSrcTable.setStatus("current")
_CLApTagSrcEntry_Object = MibTableRow
cLApTagSrcEntry = _CLApTagSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 4, 2, 1)
)
cLApTagSrcEntry.setIndexNames(
    (0, "CISCO-LWAPP-EWLC-TAGS-MIB", "cLApTagSrcPriority"),
)
if mibBuilder.loadTexts:
    cLApTagSrcEntry.setStatus("current")


class _CLApTagSrcPriority_Type(Integer32):
    """Custom type cLApTagSrcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CLApTagSrcPriority_Type.__name__ = "Integer32"
_CLApTagSrcPriority_Object = MibTableColumn
cLApTagSrcPriority = _CLApTagSrcPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 4, 2, 1, 1),
    _CLApTagSrcPriority_Type()
)
cLApTagSrcPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApTagSrcPriority.setStatus("current")
_CLApTagSrcRowStatus_Type = RowStatus
_CLApTagSrcRowStatus_Object = MibTableColumn
cLApTagSrcRowStatus = _CLApTagSrcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 4, 2, 1, 2),
    _CLApTagSrcRowStatus_Type()
)
cLApTagSrcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApTagSrcRowStatus.setStatus("current")


class _CLApTagSrcList_Type(Integer32):
    """Custom type cLApTagSrcList based on Integer32"""
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
        *(("none", 1),
          ("static", 2),
          ("filter", 3),
          ("ap", 4),
          ("default", 5),
          ("location", 6))
    )


_CLApTagSrcList_Type.__name__ = "Integer32"
_CLApTagSrcList_Object = MibTableColumn
cLApTagSrcList = _CLApTagSrcList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 4, 2, 1, 3),
    _CLApTagSrcList_Type()
)
cLApTagSrcList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApTagSrcList.setStatus("current")
_CiscoLwappApFilter_ObjectIdentity = ObjectIdentity
ciscoLwappApFilter = _CiscoLwappApFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 5)
)
_CLApFilterTable_Object = MibTable
cLApFilterTable = _CLApFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cLApFilterTable.setStatus("current")
_CLApFilterEntry_Object = MibTableRow
cLApFilterEntry = _CLApFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 5, 1, 1)
)
cLApFilterEntry.setIndexNames(
    (0, "CISCO-LWAPP-EWLC-TAGS-MIB", "cLApFilterName"),
)
if mibBuilder.loadTexts:
    cLApFilterEntry.setStatus("current")


class _CLApFilterName_Type(SnmpAdminString):
    """Custom type cLApFilterName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLApFilterName_Type.__name__ = "SnmpAdminString"
_CLApFilterName_Object = MibTableColumn
cLApFilterName = _CLApFilterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 5, 1, 1, 1),
    _CLApFilterName_Type()
)
cLApFilterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApFilterName.setStatus("current")
_CLApFilterRowStatus_Type = RowStatus
_CLApFilterRowStatus_Object = MibTableColumn
cLApFilterRowStatus = _CLApFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 5, 1, 1, 2),
    _CLApFilterRowStatus_Type()
)
cLApFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApFilterRowStatus.setStatus("current")
_CLApFilterNameApNameRule_Type = SnmpAdminString
_CLApFilterNameApNameRule_Object = MibTableColumn
cLApFilterNameApNameRule = _CLApFilterNameApNameRule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 5, 1, 1, 3),
    _CLApFilterNameApNameRule_Type()
)
cLApFilterNameApNameRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApFilterNameApNameRule.setStatus("current")
_CLApFilterPolicyTag_Type = SnmpAdminString
_CLApFilterPolicyTag_Object = MibTableColumn
cLApFilterPolicyTag = _CLApFilterPolicyTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 5, 1, 1, 4),
    _CLApFilterPolicyTag_Type()
)
cLApFilterPolicyTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApFilterPolicyTag.setStatus("current")
_CLApFilterSiteTag_Type = SnmpAdminString
_CLApFilterSiteTag_Object = MibTableColumn
cLApFilterSiteTag = _CLApFilterSiteTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 5, 1, 1, 5),
    _CLApFilterSiteTag_Type()
)
cLApFilterSiteTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApFilterSiteTag.setStatus("current")
_CLApFilterRfTag_Type = SnmpAdminString
_CLApFilterRfTag_Object = MibTableColumn
cLApFilterRfTag = _CLApFilterRfTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 5, 1, 1, 6),
    _CLApFilterRfTag_Type()
)
cLApFilterRfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApFilterRfTag.setStatus("current")
_CLApFilterPriorityTable_Object = MibTable
cLApFilterPriorityTable = _CLApFilterPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cLApFilterPriorityTable.setStatus("current")
_CLApFilterPriorityEntry_Object = MibTableRow
cLApFilterPriorityEntry = _CLApFilterPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 5, 2, 1)
)
cLApFilterPriorityEntry.setIndexNames(
    (0, "CISCO-LWAPP-EWLC-TAGS-MIB", "cLApFilterPriority"),
)
if mibBuilder.loadTexts:
    cLApFilterPriorityEntry.setStatus("current")


class _CLApFilterPriority_Type(Integer32):
    """Custom type cLApFilterPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_CLApFilterPriority_Type.__name__ = "Integer32"
_CLApFilterPriority_Object = MibTableColumn
cLApFilterPriority = _CLApFilterPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 5, 2, 1, 1),
    _CLApFilterPriority_Type()
)
cLApFilterPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApFilterPriority.setStatus("current")
_CLApFilterPriorityRowStatus_Type = RowStatus
_CLApFilterPriorityRowStatus_Object = MibTableColumn
cLApFilterPriorityRowStatus = _CLApFilterPriorityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 5, 2, 1, 2),
    _CLApFilterPriorityRowStatus_Type()
)
cLApFilterPriorityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApFilterPriorityRowStatus.setStatus("current")
_CLApFilterPriorityFilterName_Type = SnmpAdminString
_CLApFilterPriorityFilterName_Object = MibTableColumn
cLApFilterPriorityFilterName = _CLApFilterPriorityFilterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 1, 5, 2, 1, 3),
    _CLApFilterPriorityFilterName_Type()
)
cLApFilterPriorityFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApFilterPriorityFilterName.setStatus("current")
_CiscoLwappTagsMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappTagsMIBConform = _CiscoLwappTagsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 2)
)
_CiscoLwappTagsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappTagsMIBCompliances = _CiscoLwappTagsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 2, 1)
)
_CiscoLwappTagsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappTagsMIBGroups = _CiscoLwappTagsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 2, 2)
)

# Managed Objects groups

ciscoLwappTagsConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 2, 2, 1)
)
ciscoLwappTagsConfigGroup.setObjects(
      *(("CISCO-LWAPP-EWLC-TAGS-MIB", "cLPolicyTagDescription"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLPolicyTagRowStatus"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLPolicyProfileName"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLPolicyProfileRowStatus"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLRfTagRowStatus"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLRfTagDescription"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cL11aRfProfName"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cL11bRfProfName"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cL6GHzBandRfProfName"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLSiteTagRowStatus"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLApJoinProfName"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLFlexProfName"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLSiteTagDescription"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLReapSiteUpgradeStart"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLReapSiteTagStartCertificateDownload"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLIsLocalSite"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLApConfigPolicyTagName"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLApConfigRfTagName"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLApConfigSiteTagName"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLApConfigTagRowStatus"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLApTagSrcRowStatus"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLApTagSrcList"))
)
if mibBuilder.loadTexts:
    ciscoLwappTagsConfigGroup.setStatus("current")

ciscoLwappFilterConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 2, 2, 2)
)
ciscoLwappFilterConfigGroup.setObjects(
      *(("CISCO-LWAPP-EWLC-TAGS-MIB", "cLApFilterRowStatus"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLApFilterNameApNameRule"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLApFilterPolicyTag"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLApFilterRfTag"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLApFilterSiteTag"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLApFilterPriorityRowStatus"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLApFilterPriorityFilterName"))
)
if mibBuilder.loadTexts:
    ciscoLwappFilterConfigGroup.setStatus("current")

ciscoLwappRlanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 2, 2, 3)
)
ciscoLwappRlanConfigGroup.setObjects(
      *(("CISCO-LWAPP-EWLC-TAGS-MIB", "cLRlanPolicyProfile"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLRlanPolicyProfileRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappRlanConfigGroup.setStatus("current")

ciscoLwappApLocationConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 2, 2, 4)
)
ciscoLwappApLocationConfigGroup.setObjects(
      *(("CISCO-LWAPP-EWLC-TAGS-MIB", "cLApLocationSiteTag"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLApLocationRfTag"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLApLocationPolicyTag"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLApLocationConfigRowStatus"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLApLocationDesc"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "cLAssociatedApsConfigRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappApLocationConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappTagsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 987, 2, 1, 1)
)
ciscoLwappTagsMIBCompliance.setObjects(
      *(("CISCO-LWAPP-EWLC-TAGS-MIB", "ciscoLwappTagsConfigGroup"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "ciscoLwappFilterConfigGroup"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "ciscoLwappRlanConfigGroup"),
        ("CISCO-LWAPP-EWLC-TAGS-MIB", "ciscoLwappApLocationConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappTagsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-EWLC-TAGS-MIB",
    **{"ciscoLwappTagsMIB": ciscoLwappTagsMIB,
       "ciscoLwappTagsMIBNotifs": ciscoLwappTagsMIBNotifs,
       "ciscoLwappApLocationConfig": ciscoLwappApLocationConfig,
       "cLApLocationConfigTable": cLApLocationConfigTable,
       "cLApLocationConfigEntry": cLApLocationConfigEntry,
       "cLApLocationName": cLApLocationName,
       "cLApLocationSiteTag": cLApLocationSiteTag,
       "cLApLocationRfTag": cLApLocationRfTag,
       "cLApLocationPolicyTag": cLApLocationPolicyTag,
       "cLApLocationConfigRowStatus": cLApLocationConfigRowStatus,
       "cLApLocationDesc": cLApLocationDesc,
       "ciscoLwappAssociatedApsConfig": ciscoLwappAssociatedApsConfig,
       "cLAssociatedApsConfigTable": cLAssociatedApsConfigTable,
       "cLAssociatedApsConfigEntry": cLAssociatedApsConfigEntry,
       "cLAssociatedApsApMac": cLAssociatedApsApMac,
       "cLAssociatedApsConfigRowStatus": cLAssociatedApsConfigRowStatus,
       "ciscoLwappTagsMIBObjects": ciscoLwappTagsMIBObjects,
       "ciscoLwappPolicyTagConfig": ciscoLwappPolicyTagConfig,
       "cLPolicyTagConfigTable": cLPolicyTagConfigTable,
       "cLPolicyTagConfigEntry": cLPolicyTagConfigEntry,
       "cLPolicyTagName": cLPolicyTagName,
       "cLPolicyTagDescription": cLPolicyTagDescription,
       "cLPolicyTagRowStatus": cLPolicyTagRowStatus,
       "cLPolicyProfileConfigTable": cLPolicyProfileConfigTable,
       "cLPolicyProfileConfigEntry": cLPolicyProfileConfigEntry,
       "cLProfileName": cLProfileName,
       "cLPolicyProfileName": cLPolicyProfileName,
       "cLPolicyProfileRowStatus": cLPolicyProfileRowStatus,
       "cLRlanPolicyProfileConfigTable": cLRlanPolicyProfileConfigTable,
       "cLRlanPolicyProfileConfigEntry": cLRlanPolicyProfileConfigEntry,
       "cLRlanPortID": cLRlanPortID,
       "cLRlanProfile": cLRlanProfile,
       "cLRlanPolicyProfile": cLRlanPolicyProfile,
       "cLRlanPolicyProfileRowStatus": cLRlanPolicyProfileRowStatus,
       "ciscoLwappSiteTagConfig": ciscoLwappSiteTagConfig,
       "cLSiteTagConfigTable": cLSiteTagConfigTable,
       "cLSiteTagConfigEntry": cLSiteTagConfigEntry,
       "cLSiteTagName": cLSiteTagName,
       "cLSiteTagRowStatus": cLSiteTagRowStatus,
       "cLApJoinProfName": cLApJoinProfName,
       "cLFlexProfName": cLFlexProfName,
       "cLSiteTagDescription": cLSiteTagDescription,
       "cLReapSiteUpgradeStart": cLReapSiteUpgradeStart,
       "cLReapSiteTagStartCertificateDownload": cLReapSiteTagStartCertificateDownload,
       "cLIsLocalSite": cLIsLocalSite,
       "ciscoLwappRfTagConfig": ciscoLwappRfTagConfig,
       "cLRfTagConfigTable": cLRfTagConfigTable,
       "cLRfTagConfigEntry": cLRfTagConfigEntry,
       "cLRfTagName": cLRfTagName,
       "cLRfTagRowStatus": cLRfTagRowStatus,
       "cL11aRfProfName": cL11aRfProfName,
       "cL11bRfProfName": cL11bRfProfName,
       "cLRfTagDescription": cLRfTagDescription,
       "cL6GHzBandRfProfName": cL6GHzBandRfProfName,
       "ciscoLwappApTag": ciscoLwappApTag,
       "cLApConfigTagTable": cLApConfigTagTable,
       "cLApConfigTagEntry": cLApConfigTagEntry,
       "cLApConfigTagSysMacAddress": cLApConfigTagSysMacAddress,
       "cLApConfigPolicyTagName": cLApConfigPolicyTagName,
       "cLApConfigRfTagName": cLApConfigRfTagName,
       "cLApConfigSiteTagName": cLApConfigSiteTagName,
       "cLApConfigTagRowStatus": cLApConfigTagRowStatus,
       "cLApTagSrcTable": cLApTagSrcTable,
       "cLApTagSrcEntry": cLApTagSrcEntry,
       "cLApTagSrcPriority": cLApTagSrcPriority,
       "cLApTagSrcRowStatus": cLApTagSrcRowStatus,
       "cLApTagSrcList": cLApTagSrcList,
       "ciscoLwappApFilter": ciscoLwappApFilter,
       "cLApFilterTable": cLApFilterTable,
       "cLApFilterEntry": cLApFilterEntry,
       "cLApFilterName": cLApFilterName,
       "cLApFilterRowStatus": cLApFilterRowStatus,
       "cLApFilterNameApNameRule": cLApFilterNameApNameRule,
       "cLApFilterPolicyTag": cLApFilterPolicyTag,
       "cLApFilterSiteTag": cLApFilterSiteTag,
       "cLApFilterRfTag": cLApFilterRfTag,
       "cLApFilterPriorityTable": cLApFilterPriorityTable,
       "cLApFilterPriorityEntry": cLApFilterPriorityEntry,
       "cLApFilterPriority": cLApFilterPriority,
       "cLApFilterPriorityRowStatus": cLApFilterPriorityRowStatus,
       "cLApFilterPriorityFilterName": cLApFilterPriorityFilterName,
       "ciscoLwappTagsMIBConform": ciscoLwappTagsMIBConform,
       "ciscoLwappTagsMIBCompliances": ciscoLwappTagsMIBCompliances,
       "ciscoLwappTagsMIBCompliance": ciscoLwappTagsMIBCompliance,
       "ciscoLwappTagsMIBGroups": ciscoLwappTagsMIBGroups,
       "ciscoLwappTagsConfigGroup": ciscoLwappTagsConfigGroup,
       "ciscoLwappFilterConfigGroup": ciscoLwappFilterConfigGroup,
       "ciscoLwappRlanConfigGroup": ciscoLwappRlanConfigGroup,
       "ciscoLwappApLocationConfigGroup": ciscoLwappApLocationConfigGroup}
)
