# SNMP MIB module (CISCO-LWAPP-NBAR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-NBAR-MIB.mib
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoLwappNbarMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 841)
)
if mibBuilder.loadTexts:
    ciscoLwappNbarMIB.setRevisions(
        ("2018-02-08 00:00",
         "2017-04-27 00:00",
         "2012-06-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappNbarMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappNbarMIBNotifs = _CiscoLwappNbarMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 0)
)
_CiscoLwappNbarMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappNbarMIBObjects = _CiscoLwappNbarMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1)
)
_CiscoLwappNbarTableObjects_ObjectIdentity = ObjectIdentity
ciscoLwappNbarTableObjects = _CiscoLwappNbarTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1)
)
_CLNbarAVCProfileTable_Object = MibTable
cLNbarAVCProfileTable = _CLNbarAVCProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cLNbarAVCProfileTable.setStatus("current")
_CLNbarAVCProfileEntry_Object = MibTableRow
cLNbarAVCProfileEntry = _CLNbarAVCProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 1, 1)
)
cLNbarAVCProfileEntry.setIndexNames(
    (0, "CISCO-LWAPP-NBAR-MIB", "cLNbarAVCProfileName"),
)
if mibBuilder.loadTexts:
    cLNbarAVCProfileEntry.setStatus("current")


class _CLNbarAVCProfileName_Type(SnmpAdminString):
    """Custom type cLNbarAVCProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLNbarAVCProfileName_Type.__name__ = "SnmpAdminString"
_CLNbarAVCProfileName_Object = MibTableColumn
cLNbarAVCProfileName = _CLNbarAVCProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 1, 1, 1),
    _CLNbarAVCProfileName_Type()
)
cLNbarAVCProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLNbarAVCProfileName.setStatus("current")
_CLNbarAVCProfileRowStatus_Type = RowStatus
_CLNbarAVCProfileRowStatus_Object = MibTableColumn
cLNbarAVCProfileRowStatus = _CLNbarAVCProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 1, 1, 2),
    _CLNbarAVCProfileRowStatus_Type()
)
cLNbarAVCProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNbarAVCProfileRowStatus.setStatus("current")
_CLNbarAVCRuleTable_Object = MibTable
cLNbarAVCRuleTable = _CLNbarAVCRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cLNbarAVCRuleTable.setStatus("current")
_CLNbarAVCRuleEntry_Object = MibTableRow
cLNbarAVCRuleEntry = _CLNbarAVCRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 2, 1)
)
cLNbarAVCRuleEntry.setIndexNames(
    (0, "CISCO-LWAPP-NBAR-MIB", "cLNbarAVCProfileName"),
    (0, "CISCO-LWAPP-NBAR-MIB", "cLNbarAVCRuleApplicationName"),
)
if mibBuilder.loadTexts:
    cLNbarAVCRuleEntry.setStatus("current")


class _CLNbarAVCRuleProfileName_Type(SnmpAdminString):
    """Custom type cLNbarAVCRuleProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLNbarAVCRuleProfileName_Type.__name__ = "SnmpAdminString"
_CLNbarAVCRuleProfileName_Object = MibTableColumn
cLNbarAVCRuleProfileName = _CLNbarAVCRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 2, 1, 1),
    _CLNbarAVCRuleProfileName_Type()
)
cLNbarAVCRuleProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLNbarAVCRuleProfileName.setStatus("current")
_CLNbarAVCRuleApplicationName_Type = SnmpAdminString
_CLNbarAVCRuleApplicationName_Object = MibTableColumn
cLNbarAVCRuleApplicationName = _CLNbarAVCRuleApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 2, 1, 2),
    _CLNbarAVCRuleApplicationName_Type()
)
cLNbarAVCRuleApplicationName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLNbarAVCRuleApplicationName.setStatus("current")
_CLNbarAVCRuleApplicationGroupName_Type = SnmpAdminString
_CLNbarAVCRuleApplicationGroupName_Object = MibTableColumn
cLNbarAVCRuleApplicationGroupName = _CLNbarAVCRuleApplicationGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 2, 1, 3),
    _CLNbarAVCRuleApplicationGroupName_Type()
)
cLNbarAVCRuleApplicationGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNbarAVCRuleApplicationGroupName.setStatus("current")


class _CLNbarAVCRuleApplicationAction_Type(Integer32):
    """Custom type cLNbarAVCRuleApplicationAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("mark", 3),
          ("ratelimit", 4))
    )


_CLNbarAVCRuleApplicationAction_Type.__name__ = "Integer32"
_CLNbarAVCRuleApplicationAction_Object = MibTableColumn
cLNbarAVCRuleApplicationAction = _CLNbarAVCRuleApplicationAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 2, 1, 4),
    _CLNbarAVCRuleApplicationAction_Type()
)
cLNbarAVCRuleApplicationAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNbarAVCRuleApplicationAction.setStatus("current")
_CLNbarAVCRuleDscpValue_Type = Unsigned32
_CLNbarAVCRuleDscpValue_Object = MibTableColumn
cLNbarAVCRuleDscpValue = _CLNbarAVCRuleDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 2, 1, 5),
    _CLNbarAVCRuleDscpValue_Type()
)
cLNbarAVCRuleDscpValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNbarAVCRuleDscpValue.setStatus("current")
_CLNbarAVCRuleRowStatus_Type = RowStatus
_CLNbarAVCRuleRowStatus_Object = MibTableColumn
cLNbarAVCRuleRowStatus = _CLNbarAVCRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 2, 1, 6),
    _CLNbarAVCRuleRowStatus_Type()
)
cLNbarAVCRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNbarAVCRuleRowStatus.setStatus("current")
_CLNbarAVCRuleAppAvgRateLimit_Type = Unsigned32
_CLNbarAVCRuleAppAvgRateLimit_Object = MibTableColumn
cLNbarAVCRuleAppAvgRateLimit = _CLNbarAVCRuleAppAvgRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 2, 1, 7),
    _CLNbarAVCRuleAppAvgRateLimit_Type()
)
cLNbarAVCRuleAppAvgRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNbarAVCRuleAppAvgRateLimit.setStatus("current")
_CLNbarAVCRuleAppBurstRateLimit_Type = Unsigned32
_CLNbarAVCRuleAppBurstRateLimit_Object = MibTableColumn
cLNbarAVCRuleAppBurstRateLimit = _CLNbarAVCRuleAppBurstRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 2, 1, 8),
    _CLNbarAVCRuleAppBurstRateLimit_Type()
)
cLNbarAVCRuleAppBurstRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNbarAVCRuleAppBurstRateLimit.setStatus("current")
_CLNbarAVCFlexProfileTable_Object = MibTable
cLNbarAVCFlexProfileTable = _CLNbarAVCFlexProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cLNbarAVCFlexProfileTable.setStatus("current")
_CLNbarAVCFlexProfileEntry_Object = MibTableRow
cLNbarAVCFlexProfileEntry = _CLNbarAVCFlexProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 3, 1)
)
cLNbarAVCFlexProfileEntry.setIndexNames(
    (0, "CISCO-LWAPP-NBAR-MIB", "cLNbarAVCFlexProfileName"),
)
if mibBuilder.loadTexts:
    cLNbarAVCFlexProfileEntry.setStatus("current")


class _CLNbarAVCFlexProfileName_Type(SnmpAdminString):
    """Custom type cLNbarAVCFlexProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLNbarAVCFlexProfileName_Type.__name__ = "SnmpAdminString"
_CLNbarAVCFlexProfileName_Object = MibTableColumn
cLNbarAVCFlexProfileName = _CLNbarAVCFlexProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 3, 1, 1),
    _CLNbarAVCFlexProfileName_Type()
)
cLNbarAVCFlexProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLNbarAVCFlexProfileName.setStatus("current")


class _CLNbarAVCFlexProfileApply_Type(Integer32):
    """Custom type cLNbarAVCFlexProfileApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("modified", 0),
          ("apply", 1))
    )


_CLNbarAVCFlexProfileApply_Type.__name__ = "Integer32"
_CLNbarAVCFlexProfileApply_Object = MibTableColumn
cLNbarAVCFlexProfileApply = _CLNbarAVCFlexProfileApply_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 3, 1, 2),
    _CLNbarAVCFlexProfileApply_Type()
)
cLNbarAVCFlexProfileApply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNbarAVCFlexProfileApply.setStatus("current")
_CLNbarAVCFlexProfileRowStatus_Type = RowStatus
_CLNbarAVCFlexProfileRowStatus_Object = MibTableColumn
cLNbarAVCFlexProfileRowStatus = _CLNbarAVCFlexProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 3, 1, 3),
    _CLNbarAVCFlexProfileRowStatus_Type()
)
cLNbarAVCFlexProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNbarAVCFlexProfileRowStatus.setStatus("current")
_CLNbarAVCFlexRuleTable_Object = MibTable
cLNbarAVCFlexRuleTable = _CLNbarAVCFlexRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cLNbarAVCFlexRuleTable.setStatus("current")
_CLNbarAVCFlexRuleEntry_Object = MibTableRow
cLNbarAVCFlexRuleEntry = _CLNbarAVCFlexRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 4, 1)
)
cLNbarAVCFlexRuleEntry.setIndexNames(
    (0, "CISCO-LWAPP-NBAR-MIB", "cLNbarAVCFlexProfileName"),
    (0, "CISCO-LWAPP-NBAR-MIB", "cLNbarAVCFlexRuleApplicationName"),
)
if mibBuilder.loadTexts:
    cLNbarAVCFlexRuleEntry.setStatus("current")


class _CLNbarAVCFlexRuleProfileName_Type(SnmpAdminString):
    """Custom type cLNbarAVCFlexRuleProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLNbarAVCFlexRuleProfileName_Type.__name__ = "SnmpAdminString"
_CLNbarAVCFlexRuleProfileName_Object = MibTableColumn
cLNbarAVCFlexRuleProfileName = _CLNbarAVCFlexRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 4, 1, 1),
    _CLNbarAVCFlexRuleProfileName_Type()
)
cLNbarAVCFlexRuleProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLNbarAVCFlexRuleProfileName.setStatus("current")
_CLNbarAVCFlexRuleApplicationName_Type = SnmpAdminString
_CLNbarAVCFlexRuleApplicationName_Object = MibTableColumn
cLNbarAVCFlexRuleApplicationName = _CLNbarAVCFlexRuleApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 4, 1, 2),
    _CLNbarAVCFlexRuleApplicationName_Type()
)
cLNbarAVCFlexRuleApplicationName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLNbarAVCFlexRuleApplicationName.setStatus("current")
_CLNbarAVCFlexRuleApplicationGroupName_Type = SnmpAdminString
_CLNbarAVCFlexRuleApplicationGroupName_Object = MibTableColumn
cLNbarAVCFlexRuleApplicationGroupName = _CLNbarAVCFlexRuleApplicationGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 4, 1, 3),
    _CLNbarAVCFlexRuleApplicationGroupName_Type()
)
cLNbarAVCFlexRuleApplicationGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNbarAVCFlexRuleApplicationGroupName.setStatus("current")


class _CLNbarAVCFlexRuleApplicationAction_Type(Integer32):
    """Custom type cLNbarAVCFlexRuleApplicationAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("mark", 3),
          ("ratelimit", 4))
    )


_CLNbarAVCFlexRuleApplicationAction_Type.__name__ = "Integer32"
_CLNbarAVCFlexRuleApplicationAction_Object = MibTableColumn
cLNbarAVCFlexRuleApplicationAction = _CLNbarAVCFlexRuleApplicationAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 4, 1, 4),
    _CLNbarAVCFlexRuleApplicationAction_Type()
)
cLNbarAVCFlexRuleApplicationAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNbarAVCFlexRuleApplicationAction.setStatus("current")
_CLNbarAVCFlexRuleDscpValue_Type = Unsigned32
_CLNbarAVCFlexRuleDscpValue_Object = MibTableColumn
cLNbarAVCFlexRuleDscpValue = _CLNbarAVCFlexRuleDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 4, 1, 5),
    _CLNbarAVCFlexRuleDscpValue_Type()
)
cLNbarAVCFlexRuleDscpValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNbarAVCFlexRuleDscpValue.setStatus("current")
_CLNbarAVCFlexRuleRowStatus_Type = RowStatus
_CLNbarAVCFlexRuleRowStatus_Object = MibTableColumn
cLNbarAVCFlexRuleRowStatus = _CLNbarAVCFlexRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 4, 1, 6),
    _CLNbarAVCFlexRuleRowStatus_Type()
)
cLNbarAVCFlexRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNbarAVCFlexRuleRowStatus.setStatus("current")
_CLNbarAVCFlexRuleAppAvgRateLimit_Type = Unsigned32
_CLNbarAVCFlexRuleAppAvgRateLimit_Object = MibTableColumn
cLNbarAVCFlexRuleAppAvgRateLimit = _CLNbarAVCFlexRuleAppAvgRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 4, 1, 7),
    _CLNbarAVCFlexRuleAppAvgRateLimit_Type()
)
cLNbarAVCFlexRuleAppAvgRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNbarAVCFlexRuleAppAvgRateLimit.setStatus("current")
_CLNbarAVCFlexRuleAppBurstRateLimit_Type = Unsigned32
_CLNbarAVCFlexRuleAppBurstRateLimit_Object = MibTableColumn
cLNbarAVCFlexRuleAppBurstRateLimit = _CLNbarAVCFlexRuleAppBurstRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 1, 4, 1, 8),
    _CLNbarAVCFlexRuleAppBurstRateLimit_Type()
)
cLNbarAVCFlexRuleAppBurstRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNbarAVCFlexRuleAppBurstRateLimit.setStatus("current")
_CiscoLwappNbarGlobalObjects_ObjectIdentity = ObjectIdentity
ciscoLwappNbarGlobalObjects = _CiscoLwappNbarGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 2)
)
_CLNbarAVCEngineVersion_Type = OctetString
_CLNbarAVCEngineVersion_Object = MibScalar
cLNbarAVCEngineVersion = _CLNbarAVCEngineVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 2, 1),
    _CLNbarAVCEngineVersion_Type()
)
cLNbarAVCEngineVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLNbarAVCEngineVersion.setStatus("current")
_CLNbarAVCProtoPackName_Type = OctetString
_CLNbarAVCProtoPackName_Object = MibScalar
cLNbarAVCProtoPackName = _CLNbarAVCProtoPackName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 2, 2),
    _CLNbarAVCProtoPackName_Type()
)
cLNbarAVCProtoPackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLNbarAVCProtoPackName.setStatus("current")
_CLNbarAVCProtoPackVer_Type = OctetString
_CLNbarAVCProtoPackVer_Object = MibScalar
cLNbarAVCProtoPackVer = _CLNbarAVCProtoPackVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 2, 3),
    _CLNbarAVCProtoPackVer_Type()
)
cLNbarAVCProtoPackVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLNbarAVCProtoPackVer.setStatus("current")
_CLNbarAVCFlexEngineVersion_Type = OctetString
_CLNbarAVCFlexEngineVersion_Object = MibScalar
cLNbarAVCFlexEngineVersion = _CLNbarAVCFlexEngineVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 2, 4),
    _CLNbarAVCFlexEngineVersion_Type()
)
cLNbarAVCFlexEngineVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLNbarAVCFlexEngineVersion.setStatus("current")
_CLNbarAVCFlexProtoPackName_Type = OctetString
_CLNbarAVCFlexProtoPackName_Object = MibScalar
cLNbarAVCFlexProtoPackName = _CLNbarAVCFlexProtoPackName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 2, 5),
    _CLNbarAVCFlexProtoPackName_Type()
)
cLNbarAVCFlexProtoPackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLNbarAVCFlexProtoPackName.setStatus("current")
_CLNbarAVCFlexProtoPackVer_Type = OctetString
_CLNbarAVCFlexProtoPackVer_Object = MibScalar
cLNbarAVCFlexProtoPackVer = _CLNbarAVCFlexProtoPackVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 1, 2, 6),
    _CLNbarAVCFlexProtoPackVer_Type()
)
cLNbarAVCFlexProtoPackVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLNbarAVCFlexProtoPackVer.setStatus("current")
_CiscoLwappNbarMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappNbarMIBConform = _CiscoLwappNbarMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 2)
)
_CiscoLwappNbarMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappNbarMIBCompliances = _CiscoLwappNbarMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 2, 1)
)
_CiscoLwappNbarMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappNbarMIBGroups = _CiscoLwappNbarMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 2, 2)
)

# Managed Objects groups

cLNbarConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 2, 2, 1)
)
cLNbarConfigGroup.setObjects(
      *(("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCProfileName"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCProfileRowStatus"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCRuleProfileName"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCRuleApplicationName"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCRuleApplicationGroupName"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCRuleApplicationAction"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCRuleDscpValue"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCRuleRowStatus"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCFlexProfileName"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCFlexProfileRowStatus"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCFlexRuleProfileName"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCFlexRuleApplicationName"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCFlexRuleApplicationGroupName"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCFlexRuleApplicationAction"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCFlexRuleDscpValue"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCFlexRuleRowStatus"))
)
if mibBuilder.loadTexts:
    cLNbarConfigGroup.setStatus("current")

cLNbarGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 2, 2, 2)
)
cLNbarGlobalGroup.setObjects(
      *(("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCEngineVersion"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCProtoPackVer"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCProtoPackName"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCFlexEngineVersion"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCFlexProtoPackVer"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCFlexProtoPackName"))
)
if mibBuilder.loadTexts:
    cLNbarGlobalGroup.setStatus("current")


# Notification objects

cLAVCProtoPackLoadNotifFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 0, 1)
)
cLAVCProtoPackLoadNotifFailed.setObjects(
      *(("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCProtoPackName"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCProtoPackVer"))
)
if mibBuilder.loadTexts:
    cLAVCProtoPackLoadNotifFailed.setStatus(
        "current"
    )

cLAVCProtoPackLoadNotifSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 0, 2)
)
cLAVCProtoPackLoadNotifSuccess.setObjects(
      *(("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCProtoPackName"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarAVCProtoPackVer"))
)
if mibBuilder.loadTexts:
    cLAVCProtoPackLoadNotifSuccess.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappNbarMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 841, 2, 1, 1)
)
ciscoLwappNbarMIBCompliance.setObjects(
      *(("CISCO-LWAPP-NBAR-MIB", "cLNbarConfigGroup"),
        ("CISCO-LWAPP-NBAR-MIB", "cLNbarGlobalGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappNbarMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-NBAR-MIB",
    **{"ciscoLwappNbarMIB": ciscoLwappNbarMIB,
       "ciscoLwappNbarMIBNotifs": ciscoLwappNbarMIBNotifs,
       "cLAVCProtoPackLoadNotifFailed": cLAVCProtoPackLoadNotifFailed,
       "cLAVCProtoPackLoadNotifSuccess": cLAVCProtoPackLoadNotifSuccess,
       "ciscoLwappNbarMIBObjects": ciscoLwappNbarMIBObjects,
       "ciscoLwappNbarTableObjects": ciscoLwappNbarTableObjects,
       "cLNbarAVCProfileTable": cLNbarAVCProfileTable,
       "cLNbarAVCProfileEntry": cLNbarAVCProfileEntry,
       "cLNbarAVCProfileName": cLNbarAVCProfileName,
       "cLNbarAVCProfileRowStatus": cLNbarAVCProfileRowStatus,
       "cLNbarAVCRuleTable": cLNbarAVCRuleTable,
       "cLNbarAVCRuleEntry": cLNbarAVCRuleEntry,
       "cLNbarAVCRuleProfileName": cLNbarAVCRuleProfileName,
       "cLNbarAVCRuleApplicationName": cLNbarAVCRuleApplicationName,
       "cLNbarAVCRuleApplicationGroupName": cLNbarAVCRuleApplicationGroupName,
       "cLNbarAVCRuleApplicationAction": cLNbarAVCRuleApplicationAction,
       "cLNbarAVCRuleDscpValue": cLNbarAVCRuleDscpValue,
       "cLNbarAVCRuleRowStatus": cLNbarAVCRuleRowStatus,
       "cLNbarAVCRuleAppAvgRateLimit": cLNbarAVCRuleAppAvgRateLimit,
       "cLNbarAVCRuleAppBurstRateLimit": cLNbarAVCRuleAppBurstRateLimit,
       "cLNbarAVCFlexProfileTable": cLNbarAVCFlexProfileTable,
       "cLNbarAVCFlexProfileEntry": cLNbarAVCFlexProfileEntry,
       "cLNbarAVCFlexProfileName": cLNbarAVCFlexProfileName,
       "cLNbarAVCFlexProfileApply": cLNbarAVCFlexProfileApply,
       "cLNbarAVCFlexProfileRowStatus": cLNbarAVCFlexProfileRowStatus,
       "cLNbarAVCFlexRuleTable": cLNbarAVCFlexRuleTable,
       "cLNbarAVCFlexRuleEntry": cLNbarAVCFlexRuleEntry,
       "cLNbarAVCFlexRuleProfileName": cLNbarAVCFlexRuleProfileName,
       "cLNbarAVCFlexRuleApplicationName": cLNbarAVCFlexRuleApplicationName,
       "cLNbarAVCFlexRuleApplicationGroupName": cLNbarAVCFlexRuleApplicationGroupName,
       "cLNbarAVCFlexRuleApplicationAction": cLNbarAVCFlexRuleApplicationAction,
       "cLNbarAVCFlexRuleDscpValue": cLNbarAVCFlexRuleDscpValue,
       "cLNbarAVCFlexRuleRowStatus": cLNbarAVCFlexRuleRowStatus,
       "cLNbarAVCFlexRuleAppAvgRateLimit": cLNbarAVCFlexRuleAppAvgRateLimit,
       "cLNbarAVCFlexRuleAppBurstRateLimit": cLNbarAVCFlexRuleAppBurstRateLimit,
       "ciscoLwappNbarGlobalObjects": ciscoLwappNbarGlobalObjects,
       "cLNbarAVCEngineVersion": cLNbarAVCEngineVersion,
       "cLNbarAVCProtoPackName": cLNbarAVCProtoPackName,
       "cLNbarAVCProtoPackVer": cLNbarAVCProtoPackVer,
       "cLNbarAVCFlexEngineVersion": cLNbarAVCFlexEngineVersion,
       "cLNbarAVCFlexProtoPackName": cLNbarAVCFlexProtoPackName,
       "cLNbarAVCFlexProtoPackVer": cLNbarAVCFlexProtoPackVer,
       "ciscoLwappNbarMIBConform": ciscoLwappNbarMIBConform,
       "ciscoLwappNbarMIBCompliances": ciscoLwappNbarMIBCompliances,
       "ciscoLwappNbarMIBCompliance": ciscoLwappNbarMIBCompliance,
       "ciscoLwappNbarMIBGroups": ciscoLwappNbarMIBGroups,
       "cLNbarConfigGroup": cLNbarConfigGroup,
       "cLNbarGlobalGroup": cLNbarGlobalGroup}
)
