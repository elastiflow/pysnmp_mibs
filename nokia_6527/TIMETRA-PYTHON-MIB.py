# SNMP MIB module (TIMETRA-PYTHON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-PYTHON-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:37:32 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TDirection,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxActionType,
 TmnxAdminState,
 TmnxDisplayStringURL,
 TmnxOperState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TDirection",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxDisplayStringURL",
    "TmnxOperState")


# MODULE-IDENTITY

timetraPythonMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 87)
)
if mibBuilder.loadTexts:
    timetraPythonMIBModule.setRevisions(
        ("2015-01-01 12:00",
         "2014-01-01 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxProtection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("hmacSha256", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxPythonConformance_ObjectIdentity = ObjectIdentity
tmnxPythonConformance = _TmnxPythonConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 87)
)
_TmnxPythonCompliances_ObjectIdentity = ObjectIdentity
tmnxPythonCompliances = _TmnxPythonCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 87, 1)
)
_TmnxPythonGroups_ObjectIdentity = ObjectIdentity
tmnxPythonGroups = _TmnxPythonGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 87, 2)
)
_TmnxPythonNotifGroups_ObjectIdentity = ObjectIdentity
tmnxPythonNotifGroups = _TmnxPythonNotifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 87, 3)
)
_TmnxPython_ObjectIdentity = ObjectIdentity
tmnxPython = _TmnxPython_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87)
)
_TmnxPythonObjs_ObjectIdentity = ObjectIdentity
tmnxPythonObjs = _TmnxPythonObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1)
)
_TmnxPythonScriptTableLastCh_Type = TimeStamp
_TmnxPythonScriptTableLastCh_Object = MibScalar
tmnxPythonScriptTableLastCh = _TmnxPythonScriptTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 1),
    _TmnxPythonScriptTableLastCh_Type()
)
tmnxPythonScriptTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPythonScriptTableLastCh.setStatus("current")
_TmnxPythonScriptTable_Object = MibTable
tmnxPythonScriptTable = _TmnxPythonScriptTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxPythonScriptTable.setStatus("current")
_TmnxPythonScriptEntry_Object = MibTableRow
tmnxPythonScriptEntry = _TmnxPythonScriptEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 2, 1)
)
tmnxPythonScriptEntry.setIndexNames(
    (0, "TIMETRA-PYTHON-MIB", "tmnxPythonScriptName"),
)
if mibBuilder.loadTexts:
    tmnxPythonScriptEntry.setStatus("current")
_TmnxPythonScriptName_Type = TNamedItem
_TmnxPythonScriptName_Object = MibTableColumn
tmnxPythonScriptName = _TmnxPythonScriptName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 2, 1, 1),
    _TmnxPythonScriptName_Type()
)
tmnxPythonScriptName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPythonScriptName.setStatus("current")
_TmnxPythonScriptRowStatus_Type = RowStatus
_TmnxPythonScriptRowStatus_Object = MibTableColumn
tmnxPythonScriptRowStatus = _TmnxPythonScriptRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 2, 1, 2),
    _TmnxPythonScriptRowStatus_Type()
)
tmnxPythonScriptRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPythonScriptRowStatus.setStatus("current")
_TmnxPythonScriptLastChanged_Type = TimeStamp
_TmnxPythonScriptLastChanged_Object = MibTableColumn
tmnxPythonScriptLastChanged = _TmnxPythonScriptLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 2, 1, 3),
    _TmnxPythonScriptLastChanged_Type()
)
tmnxPythonScriptLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPythonScriptLastChanged.setStatus("current")


class _TmnxPythonScriptAdminState_Type(TmnxAdminState):
    """Custom type tmnxPythonScriptAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxPythonScriptAdminState_Type.__name__ = "TmnxAdminState"
_TmnxPythonScriptAdminState_Object = MibTableColumn
tmnxPythonScriptAdminState = _TmnxPythonScriptAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 2, 1, 4),
    _TmnxPythonScriptAdminState_Type()
)
tmnxPythonScriptAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPythonScriptAdminState.setStatus("current")
_TmnxPythonScriptOperState_Type = TmnxOperState
_TmnxPythonScriptOperState_Object = MibTableColumn
tmnxPythonScriptOperState = _TmnxPythonScriptOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 2, 1, 5),
    _TmnxPythonScriptOperState_Type()
)
tmnxPythonScriptOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPythonScriptOperState.setStatus("current")


class _TmnxPythonScriptDescription_Type(TItemDescription):
    """Custom type tmnxPythonScriptDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxPythonScriptDescription_Type.__name__ = "TItemDescription"
_TmnxPythonScriptDescription_Object = MibTableColumn
tmnxPythonScriptDescription = _TmnxPythonScriptDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 2, 1, 6),
    _TmnxPythonScriptDescription_Type()
)
tmnxPythonScriptDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPythonScriptDescription.setStatus("current")


class _TmnxPythonScriptOnFail_Type(Integer32):
    """Custom type tmnxPythonScriptOnFail based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passthrough", 1),
          ("drop", 2))
    )


_TmnxPythonScriptOnFail_Type.__name__ = "Integer32"
_TmnxPythonScriptOnFail_Object = MibTableColumn
tmnxPythonScriptOnFail = _TmnxPythonScriptOnFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 2, 1, 7),
    _TmnxPythonScriptOnFail_Type()
)
tmnxPythonScriptOnFail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPythonScriptOnFail.setStatus("current")


class _TmnxPythonScriptProtection_Type(TmnxProtection):
    """Custom type tmnxPythonScriptProtection based on TmnxProtection"""
    defaultValue = 1


_TmnxPythonScriptProtection_Type.__name__ = "TmnxProtection"
_TmnxPythonScriptProtection_Object = MibTableColumn
tmnxPythonScriptProtection = _TmnxPythonScriptProtection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 2, 1, 8),
    _TmnxPythonScriptProtection_Type()
)
tmnxPythonScriptProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPythonScriptProtection.setStatus("current")


class _TmnxPythonScriptProtectionKey_Type(DisplayString):
    """Custom type tmnxPythonScriptProtectionKey based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TmnxPythonScriptProtectionKey_Type.__name__ = "DisplayString"
_TmnxPythonScriptProtectionKey_Object = MibTableColumn
tmnxPythonScriptProtectionKey = _TmnxPythonScriptProtectionKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 2, 1, 9),
    _TmnxPythonScriptProtectionKey_Type()
)
tmnxPythonScriptProtectionKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPythonScriptProtectionKey.setStatus("current")


class _TmnxPythonScriptPrimaryUrl_Type(TmnxDisplayStringURL):
    """Custom type tmnxPythonScriptPrimaryUrl based on TmnxDisplayStringURL"""
    defaultHexValue = ""


_TmnxPythonScriptPrimaryUrl_Type.__name__ = "TmnxDisplayStringURL"
_TmnxPythonScriptPrimaryUrl_Object = MibTableColumn
tmnxPythonScriptPrimaryUrl = _TmnxPythonScriptPrimaryUrl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 2, 1, 10),
    _TmnxPythonScriptPrimaryUrl_Type()
)
tmnxPythonScriptPrimaryUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPythonScriptPrimaryUrl.setStatus("current")


class _TmnxPythonScriptSecondaryUrl_Type(TmnxDisplayStringURL):
    """Custom type tmnxPythonScriptSecondaryUrl based on TmnxDisplayStringURL"""
    defaultHexValue = ""


_TmnxPythonScriptSecondaryUrl_Type.__name__ = "TmnxDisplayStringURL"
_TmnxPythonScriptSecondaryUrl_Object = MibTableColumn
tmnxPythonScriptSecondaryUrl = _TmnxPythonScriptSecondaryUrl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 2, 1, 11),
    _TmnxPythonScriptSecondaryUrl_Type()
)
tmnxPythonScriptSecondaryUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPythonScriptSecondaryUrl.setStatus("current")


class _TmnxPythonScriptTertiaryUrl_Type(TmnxDisplayStringURL):
    """Custom type tmnxPythonScriptTertiaryUrl based on TmnxDisplayStringURL"""
    defaultHexValue = ""


_TmnxPythonScriptTertiaryUrl_Type.__name__ = "TmnxDisplayStringURL"
_TmnxPythonScriptTertiaryUrl_Object = MibTableColumn
tmnxPythonScriptTertiaryUrl = _TmnxPythonScriptTertiaryUrl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 2, 1, 12),
    _TmnxPythonScriptTertiaryUrl_Type()
)
tmnxPythonScriptTertiaryUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPythonScriptTertiaryUrl.setStatus("current")


class _TmnxPythonScriptActiveUrl_Type(Integer32):
    """Custom type tmnxPythonScriptActiveUrl based on Integer32"""
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
          ("primary", 1),
          ("secondary", 2),
          ("tertiary", 3))
    )


_TmnxPythonScriptActiveUrl_Type.__name__ = "Integer32"
_TmnxPythonScriptActiveUrl_Object = MibTableColumn
tmnxPythonScriptActiveUrl = _TmnxPythonScriptActiveUrl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 2, 1, 13),
    _TmnxPythonScriptActiveUrl_Type()
)
tmnxPythonScriptActiveUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPythonScriptActiveUrl.setStatus("current")


class _TmnxPythonScriptReloadAction_Type(TmnxActionType):
    """Custom type tmnxPythonScriptReloadAction based on TmnxActionType"""
    defaultValue = 2


_TmnxPythonScriptReloadAction_Type.__name__ = "TmnxActionType"
_TmnxPythonScriptReloadAction_Object = MibTableColumn
tmnxPythonScriptReloadAction = _TmnxPythonScriptReloadAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 2, 1, 50),
    _TmnxPythonScriptReloadAction_Type()
)
tmnxPythonScriptReloadAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPythonScriptReloadAction.setStatus("current")
_TmnxPythonPolicyTableLastCh_Type = TimeStamp
_TmnxPythonPolicyTableLastCh_Object = MibScalar
tmnxPythonPolicyTableLastCh = _TmnxPythonPolicyTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 3),
    _TmnxPythonPolicyTableLastCh_Type()
)
tmnxPythonPolicyTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPythonPolicyTableLastCh.setStatus("current")
_TmnxPythonPolicyTable_Object = MibTable
tmnxPythonPolicyTable = _TmnxPythonPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxPythonPolicyTable.setStatus("current")
_TmnxPythonPolicyEntry_Object = MibTableRow
tmnxPythonPolicyEntry = _TmnxPythonPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 4, 1)
)
tmnxPythonPolicyEntry.setIndexNames(
    (0, "TIMETRA-PYTHON-MIB", "tmnxPyPlcyName"),
)
if mibBuilder.loadTexts:
    tmnxPythonPolicyEntry.setStatus("current")
_TmnxPyPlcyName_Type = TNamedItem
_TmnxPyPlcyName_Object = MibTableColumn
tmnxPyPlcyName = _TmnxPyPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 4, 1, 1),
    _TmnxPyPlcyName_Type()
)
tmnxPyPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPyPlcyName.setStatus("current")
_TmnxPyPlcyRowStatus_Type = RowStatus
_TmnxPyPlcyRowStatus_Object = MibTableColumn
tmnxPyPlcyRowStatus = _TmnxPyPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 4, 1, 2),
    _TmnxPyPlcyRowStatus_Type()
)
tmnxPyPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPyPlcyRowStatus.setStatus("current")
_TmnxPyPlcyLastChanged_Type = TimeStamp
_TmnxPyPlcyLastChanged_Object = MibTableColumn
tmnxPyPlcyLastChanged = _TmnxPyPlcyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 4, 1, 3),
    _TmnxPyPlcyLastChanged_Type()
)
tmnxPyPlcyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPyPlcyLastChanged.setStatus("current")


class _TmnxPyPlcyDescription_Type(TItemDescription):
    """Custom type tmnxPyPlcyDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxPyPlcyDescription_Type.__name__ = "TItemDescription"
_TmnxPyPlcyDescription_Object = MibTableColumn
tmnxPyPlcyDescription = _TmnxPyPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 4, 1, 4),
    _TmnxPyPlcyDescription_Type()
)
tmnxPyPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPyPlcyDescription.setStatus("current")
_TmnxPythonPolicyCacheTableLastCh_Type = TimeStamp
_TmnxPythonPolicyCacheTableLastCh_Object = MibScalar
tmnxPythonPolicyCacheTableLastCh = _TmnxPythonPolicyCacheTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 5),
    _TmnxPythonPolicyCacheTableLastCh_Type()
)
tmnxPythonPolicyCacheTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPythonPolicyCacheTableLastCh.setStatus("current")
_TmnxPythonPolicyCacheTable_Object = MibTable
tmnxPythonPolicyCacheTable = _TmnxPythonPolicyCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxPythonPolicyCacheTable.setStatus("current")
_TmnxPythonPolicyCacheEntry_Object = MibTableRow
tmnxPythonPolicyCacheEntry = _TmnxPythonPolicyCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 6, 1)
)
tmnxPythonPolicyCacheEntry.setIndexNames(
    (0, "TIMETRA-PYTHON-MIB", "tmnxPyPlcyName"),
)
if mibBuilder.loadTexts:
    tmnxPythonPolicyCacheEntry.setStatus("current")
_TmnxPyPlcyCacheRowStatus_Type = RowStatus
_TmnxPyPlcyCacheRowStatus_Object = MibTableColumn
tmnxPyPlcyCacheRowStatus = _TmnxPyPlcyCacheRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 6, 1, 1),
    _TmnxPyPlcyCacheRowStatus_Type()
)
tmnxPyPlcyCacheRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPyPlcyCacheRowStatus.setStatus("current")


class _TmnxPyPlcyCacheEntrySize_Type(Integer32):
    """Custom type tmnxPyPlcyCacheEntrySize based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 2048),
    )


_TmnxPyPlcyCacheEntrySize_Type.__name__ = "Integer32"
_TmnxPyPlcyCacheEntrySize_Object = MibTableColumn
tmnxPyPlcyCacheEntrySize = _TmnxPyPlcyCacheEntrySize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 6, 1, 2),
    _TmnxPyPlcyCacheEntrySize_Type()
)
tmnxPyPlcyCacheEntrySize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPyPlcyCacheEntrySize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPyPlcyCacheEntrySize.setUnits("bytes")


class _TmnxPyPlcyCacheMaxEntries_Type(Integer32):
    """Custom type tmnxPyPlcyCacheMaxEntries based on Integer32"""
    defaultValue = 128000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_TmnxPyPlcyCacheMaxEntries_Type.__name__ = "Integer32"
_TmnxPyPlcyCacheMaxEntries_Object = MibTableColumn
tmnxPyPlcyCacheMaxEntries = _TmnxPyPlcyCacheMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 6, 1, 3),
    _TmnxPyPlcyCacheMaxEntries_Type()
)
tmnxPyPlcyCacheMaxEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPyPlcyCacheMaxEntries.setStatus("current")


class _TmnxPyPlcyCacheMaxLifetime_Type(Integer32):
    """Custom type tmnxPyPlcyCacheMaxLifetime based on Integer32"""
    defaultValue = 86400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_TmnxPyPlcyCacheMaxLifetime_Type.__name__ = "Integer32"
_TmnxPyPlcyCacheMaxLifetime_Object = MibTableColumn
tmnxPyPlcyCacheMaxLifetime = _TmnxPyPlcyCacheMaxLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 6, 1, 4),
    _TmnxPyPlcyCacheMaxLifetime_Type()
)
tmnxPyPlcyCacheMaxLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPyPlcyCacheMaxLifetime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPyPlcyCacheMaxLifetime.setUnits("seconds")


class _TmnxPyPlcyCacheAdminState_Type(TmnxAdminState):
    """Custom type tmnxPyPlcyCacheAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxPyPlcyCacheAdminState_Type.__name__ = "TmnxAdminState"
_TmnxPyPlcyCacheAdminState_Object = MibTableColumn
tmnxPyPlcyCacheAdminState = _TmnxPyPlcyCacheAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 6, 1, 5),
    _TmnxPyPlcyCacheAdminState_Type()
)
tmnxPyPlcyCacheAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPyPlcyCacheAdminState.setStatus("current")
_TmnxPyPlcyCacheLastChanged_Type = TimeStamp
_TmnxPyPlcyCacheLastChanged_Object = MibTableColumn
tmnxPyPlcyCacheLastChanged = _TmnxPyPlcyCacheLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 6, 1, 6),
    _TmnxPyPlcyCacheLastChanged_Type()
)
tmnxPyPlcyCacheLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPyPlcyCacheLastChanged.setStatus("current")


class _TmnxPyPlcyCachePersistent_Type(TruthValue):
    """Custom type tmnxPyPlcyCachePersistent based on TruthValue"""
    defaultValue = 2


_TmnxPyPlcyCachePersistent_Type.__name__ = "TruthValue"
_TmnxPyPlcyCachePersistent_Object = MibTableColumn
tmnxPyPlcyCachePersistent = _TmnxPyPlcyCachePersistent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 6, 1, 10),
    _TmnxPyPlcyCachePersistent_Type()
)
tmnxPyPlcyCachePersistent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPyPlcyCachePersistent.setStatus("current")


class _TmnxPyPlcyCacheMinLifetimeMcs_Type(Unsigned32):
    """Custom type tmnxPyPlcyCacheMinLifetimeMcs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_TmnxPyPlcyCacheMinLifetimeMcs_Type.__name__ = "Unsigned32"
_TmnxPyPlcyCacheMinLifetimeMcs_Object = MibTableColumn
tmnxPyPlcyCacheMinLifetimeMcs = _TmnxPyPlcyCacheMinLifetimeMcs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 6, 1, 11),
    _TmnxPyPlcyCacheMinLifetimeMcs_Type()
)
tmnxPyPlcyCacheMinLifetimeMcs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPyPlcyCacheMinLifetimeMcs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPyPlcyCacheMinLifetimeMcs.setUnits("seconds")


class _TmnxPyPlcyCacheMinLifetimeHa_Type(Unsigned32):
    """Custom type tmnxPyPlcyCacheMinLifetimeHa based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_TmnxPyPlcyCacheMinLifetimeHa_Type.__name__ = "Unsigned32"
_TmnxPyPlcyCacheMinLifetimeHa_Object = MibTableColumn
tmnxPyPlcyCacheMinLifetimeHa = _TmnxPyPlcyCacheMinLifetimeHa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 6, 1, 12),
    _TmnxPyPlcyCacheMinLifetimeHa_Type()
)
tmnxPyPlcyCacheMinLifetimeHa.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPyPlcyCacheMinLifetimeHa.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPyPlcyCacheMinLifetimeHa.setUnits("seconds")


class _TmnxPyPlcyCacheMinLifetimePers_Type(Unsigned32):
    """Custom type tmnxPyPlcyCacheMinLifetimePers based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_TmnxPyPlcyCacheMinLifetimePers_Type.__name__ = "Unsigned32"
_TmnxPyPlcyCacheMinLifetimePers_Object = MibTableColumn
tmnxPyPlcyCacheMinLifetimePers = _TmnxPyPlcyCacheMinLifetimePers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 6, 1, 13),
    _TmnxPyPlcyCacheMinLifetimePers_Type()
)
tmnxPyPlcyCacheMinLifetimePers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPyPlcyCacheMinLifetimePers.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPyPlcyCacheMinLifetimePers.setUnits("seconds")
_TmnxPyPlcyCacheNumberOfEntries_Type = Gauge32
_TmnxPyPlcyCacheNumberOfEntries_Object = MibTableColumn
tmnxPyPlcyCacheNumberOfEntries = _TmnxPyPlcyCacheNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 6, 1, 14),
    _TmnxPyPlcyCacheNumberOfEntries_Type()
)
tmnxPyPlcyCacheNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPyPlcyCacheNumberOfEntries.setStatus("current")
_TmnxPythonPolicyMessageTblLstCh_Type = TimeStamp
_TmnxPythonPolicyMessageTblLstCh_Object = MibScalar
tmnxPythonPolicyMessageTblLstCh = _TmnxPythonPolicyMessageTblLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 7),
    _TmnxPythonPolicyMessageTblLstCh_Type()
)
tmnxPythonPolicyMessageTblLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPythonPolicyMessageTblLstCh.setStatus("current")
_TmnxPythonPolicyMessageTable_Object = MibTable
tmnxPythonPolicyMessageTable = _TmnxPythonPolicyMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxPythonPolicyMessageTable.setStatus("current")
_TmnxPythonPolicyMessageEntry_Object = MibTableRow
tmnxPythonPolicyMessageEntry = _TmnxPythonPolicyMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 8, 1)
)
tmnxPythonPolicyMessageEntry.setIndexNames(
    (0, "TIMETRA-PYTHON-MIB", "tmnxPyPlcyName"),
    (0, "TIMETRA-PYTHON-MIB", "tmnxPyPlcyMessageType"),
    (0, "TIMETRA-PYTHON-MIB", "tmnxPyPlcyMessageDirection"),
)
if mibBuilder.loadTexts:
    tmnxPythonPolicyMessageEntry.setStatus("current")


class _TmnxPyPlcyMessageType_Type(Integer32):
    """Custom type tmnxPyPlcyMessageType based on Integer32"""
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
              1001,
              1002,
              1003,
              1004,
              1005,
              1006,
              1007,
              1008,
              1009,
              1010,
              1011,
              1012,
              1013,
              2001,
              2002,
              2003,
              2004,
              2005,
              2006,
              2007,
              2008,
              2009,
              2010,
              2011,
              2012,
              2013,
              3001,
              3002,
              3003,
              3004,
              3005,
              3006,
              3007,
              3008,
              3009,
              3010,
              3011,
              3012)
        )
    )
    namedValues = NamedValues(
        *(("radiusAccessRequest", 1),
          ("radiusAccessAccept", 2),
          ("radiusAccessReject", 3),
          ("radiusAccountingRequest", 4),
          ("radiusAccountingResponse", 5),
          ("radiusAccessChallenge", 6),
          ("radiusDisconnectRequest", 7),
          ("radiusChangeOfAuthorizationRequest", 8),
          ("dhcpDiscover", 1001),
          ("dhcpOffer", 1002),
          ("dhcpRequest", 1003),
          ("dhcpDecline", 1004),
          ("dhcpAck", 1005),
          ("dhcpNak", 1006),
          ("dhcpRelease", 1007),
          ("dhcpInform", 1008),
          ("dhcpForceRenew", 1009),
          ("dhcpLeaseQuery", 1010),
          ("dhcpLeaseUnassigned", 1011),
          ("dhcpLeaseUnknown", 1012),
          ("dhcpLeaseActive", 1013),
          ("dhcp6Solicit", 2001),
          ("dhcp6Advertise", 2002),
          ("dhcp6Request", 2003),
          ("dhcp6Confirm", 2004),
          ("dhcp6Renew", 2005),
          ("dhcp6Rebind", 2006),
          ("dhcp6Reply", 2007),
          ("dhcp6Release", 2008),
          ("dhcp6Decline", 2009),
          ("dhcp6Reconfigure", 2010),
          ("dhcp6InfoRequest", 2011),
          ("dhcp6RelayForward", 2012),
          ("dhcp6RelayReply", 2013),
          ("diameterCCR", 3001),
          ("diameterCCA", 3002),
          ("diameterRAR", 3003),
          ("diameterRAA", 3004),
          ("diameterCER", 3005),
          ("diameterCEA", 3006),
          ("diameterDWR", 3007),
          ("diameterDWA", 3008),
          ("diameterDPR", 3009),
          ("diameterDPA", 3010),
          ("diameterASR", 3011),
          ("diameterASA", 3012))
    )


_TmnxPyPlcyMessageType_Type.__name__ = "Integer32"
_TmnxPyPlcyMessageType_Object = MibTableColumn
tmnxPyPlcyMessageType = _TmnxPyPlcyMessageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 8, 1, 2),
    _TmnxPyPlcyMessageType_Type()
)
tmnxPyPlcyMessageType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPyPlcyMessageType.setStatus("current")


class _TmnxPyPlcyMessageDirection_Type(TDirection):
    """Custom type tmnxPyPlcyMessageDirection based on TDirection"""
    subtypeSpec = TDirection.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_TmnxPyPlcyMessageDirection_Type.__name__ = "TDirection"
_TmnxPyPlcyMessageDirection_Object = MibTableColumn
tmnxPyPlcyMessageDirection = _TmnxPyPlcyMessageDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 8, 1, 3),
    _TmnxPyPlcyMessageDirection_Type()
)
tmnxPyPlcyMessageDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPyPlcyMessageDirection.setStatus("current")
_TmnxPyPlcyMessageRowStatus_Type = RowStatus
_TmnxPyPlcyMessageRowStatus_Object = MibTableColumn
tmnxPyPlcyMessageRowStatus = _TmnxPyPlcyMessageRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 8, 1, 4),
    _TmnxPyPlcyMessageRowStatus_Type()
)
tmnxPyPlcyMessageRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPyPlcyMessageRowStatus.setStatus("current")
_TmnxPyPlcyMessageLastChanged_Type = TimeStamp
_TmnxPyPlcyMessageLastChanged_Object = MibTableColumn
tmnxPyPlcyMessageLastChanged = _TmnxPyPlcyMessageLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 8, 1, 5),
    _TmnxPyPlcyMessageLastChanged_Type()
)
tmnxPyPlcyMessageLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPyPlcyMessageLastChanged.setStatus("current")
_TmnxPyPlcyMessagePyScript_Type = TNamedItem
_TmnxPyPlcyMessagePyScript_Object = MibTableColumn
tmnxPyPlcyMessagePyScript = _TmnxPyPlcyMessagePyScript_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 8, 1, 6),
    _TmnxPyPlcyMessagePyScript_Type()
)
tmnxPyPlcyMessagePyScript.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPyPlcyMessagePyScript.setStatus("current")
_TmnxPythonProtectAction_ObjectIdentity = ObjectIdentity
tmnxPythonProtectAction = _TmnxPythonProtectAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 9)
)


class _TmnxPythonProtectFileUrl_Type(TmnxDisplayStringURL):
    """Custom type tmnxPythonProtectFileUrl based on TmnxDisplayStringURL"""
    defaultHexValue = ""


_TmnxPythonProtectFileUrl_Type.__name__ = "TmnxDisplayStringURL"
_TmnxPythonProtectFileUrl_Object = MibScalar
tmnxPythonProtectFileUrl = _TmnxPythonProtectFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 9, 1),
    _TmnxPythonProtectFileUrl_Type()
)
tmnxPythonProtectFileUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPythonProtectFileUrl.setStatus("current")


class _TmnxPythonProtectDestFileUrl_Type(TmnxDisplayStringURL):
    """Custom type tmnxPythonProtectDestFileUrl based on TmnxDisplayStringURL"""
    defaultHexValue = ""


_TmnxPythonProtectDestFileUrl_Type.__name__ = "TmnxDisplayStringURL"
_TmnxPythonProtectDestFileUrl_Object = MibScalar
tmnxPythonProtectDestFileUrl = _TmnxPythonProtectDestFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 9, 2),
    _TmnxPythonProtectDestFileUrl_Type()
)
tmnxPythonProtectDestFileUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPythonProtectDestFileUrl.setStatus("current")


class _TmnxPythonProtectType_Type(TmnxProtection):
    """Custom type tmnxPythonProtectType based on TmnxProtection"""
    defaultValue = 1


_TmnxPythonProtectType_Type.__name__ = "TmnxProtection"
_TmnxPythonProtectType_Object = MibScalar
tmnxPythonProtectType = _TmnxPythonProtectType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 9, 3),
    _TmnxPythonProtectType_Type()
)
tmnxPythonProtectType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPythonProtectType.setStatus("current")


class _TmnxPythonProtectKey_Type(DisplayString):
    """Custom type tmnxPythonProtectKey based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TmnxPythonProtectKey_Type.__name__ = "DisplayString"
_TmnxPythonProtectKey_Object = MibScalar
tmnxPythonProtectKey = _TmnxPythonProtectKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 9, 4),
    _TmnxPythonProtectKey_Type()
)
tmnxPythonProtectKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPythonProtectKey.setStatus("current")
_TmnxPythonProtectActionGo_Type = TmnxActionType
_TmnxPythonProtectActionGo_Object = MibScalar
tmnxPythonProtectActionGo = _TmnxPythonProtectActionGo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 9, 5),
    _TmnxPythonProtectActionGo_Type()
)
tmnxPythonProtectActionGo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPythonProtectActionGo.setStatus("current")
_TmnxPythonProtectActionSuccess_Type = TruthValue
_TmnxPythonProtectActionSuccess_Object = MibScalar
tmnxPythonProtectActionSuccess = _TmnxPythonProtectActionSuccess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 9, 6),
    _TmnxPythonProtectActionSuccess_Type()
)
tmnxPythonProtectActionSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPythonProtectActionSuccess.setStatus("current")
_TmnxPythonProtectActionTime_Type = TimeStamp
_TmnxPythonProtectActionTime_Object = MibScalar
tmnxPythonProtectActionTime = _TmnxPythonProtectActionTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 1, 9, 7),
    _TmnxPythonProtectActionTime_Type()
)
tmnxPythonProtectActionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPythonProtectActionTime.setStatus("current")
_TmnxPythonNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxPythonNotificationObjs = _TmnxPythonNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 87, 2)
)
_TmnxPythonNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxPythonNotifyPrefix = _TmnxPythonNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 87)
)
_TmnxPythonNotifications_ObjectIdentity = ObjectIdentity
tmnxPythonNotifications = _TmnxPythonNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 87, 0)
)

# Managed Objects groups

tmnxPythonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 87, 2, 1)
)
tmnxPythonGroup.setObjects(
      *(("TIMETRA-PYTHON-MIB", "tmnxPythonScriptTableLastCh"),
        ("TIMETRA-PYTHON-MIB", "tmnxPythonScriptRowStatus"),
        ("TIMETRA-PYTHON-MIB", "tmnxPythonScriptLastChanged"),
        ("TIMETRA-PYTHON-MIB", "tmnxPythonScriptDescription"),
        ("TIMETRA-PYTHON-MIB", "tmnxPythonScriptOnFail"),
        ("TIMETRA-PYTHON-MIB", "tmnxPythonScriptProtection"),
        ("TIMETRA-PYTHON-MIB", "tmnxPythonScriptProtectionKey"),
        ("TIMETRA-PYTHON-MIB", "tmnxPythonScriptAdminState"),
        ("TIMETRA-PYTHON-MIB", "tmnxPythonScriptOperState"),
        ("TIMETRA-PYTHON-MIB", "tmnxPythonScriptPrimaryUrl"),
        ("TIMETRA-PYTHON-MIB", "tmnxPythonScriptSecondaryUrl"),
        ("TIMETRA-PYTHON-MIB", "tmnxPythonScriptTertiaryUrl"),
        ("TIMETRA-PYTHON-MIB", "tmnxPythonScriptActiveUrl"),
        ("TIMETRA-PYTHON-MIB", "tmnxPythonScriptReloadAction"),
        ("TIMETRA-PYTHON-MIB", "tmnxPythonPolicyTableLastCh"),
        ("TIMETRA-PYTHON-MIB", "tmnxPyPlcyRowStatus"),
        ("TIMETRA-PYTHON-MIB", "tmnxPyPlcyLastChanged"),
        ("TIMETRA-PYTHON-MIB", "tmnxPyPlcyDescription"),
        ("TIMETRA-PYTHON-MIB", "tmnxPythonPolicyCacheTableLastCh"),
        ("TIMETRA-PYTHON-MIB", "tmnxPyPlcyCacheRowStatus"),
        ("TIMETRA-PYTHON-MIB", "tmnxPyPlcyCacheEntrySize"),
        ("TIMETRA-PYTHON-MIB", "tmnxPyPlcyCacheMaxEntries"),
        ("TIMETRA-PYTHON-MIB", "tmnxPyPlcyCacheMaxLifetime"),
        ("TIMETRA-PYTHON-MIB", "tmnxPyPlcyCacheAdminState"),
        ("TIMETRA-PYTHON-MIB", "tmnxPyPlcyCacheLastChanged"),
        ("TIMETRA-PYTHON-MIB", "tmnxPyPlcyCachePersistent"),
        ("TIMETRA-PYTHON-MIB", "tmnxPyPlcyCacheMinLifetimeMcs"),
        ("TIMETRA-PYTHON-MIB", "tmnxPyPlcyCacheMinLifetimeHa"),
        ("TIMETRA-PYTHON-MIB", "tmnxPyPlcyCacheMinLifetimePers"),
        ("TIMETRA-PYTHON-MIB", "tmnxPyPlcyCacheNumberOfEntries"),
        ("TIMETRA-PYTHON-MIB", "tmnxPythonProtectFileUrl"),
        ("TIMETRA-PYTHON-MIB", "tmnxPythonProtectDestFileUrl"),
        ("TIMETRA-PYTHON-MIB", "tmnxPythonProtectType"),
        ("TIMETRA-PYTHON-MIB", "tmnxPythonProtectKey"),
        ("TIMETRA-PYTHON-MIB", "tmnxPythonProtectActionGo"),
        ("TIMETRA-PYTHON-MIB", "tmnxPythonProtectActionSuccess"),
        ("TIMETRA-PYTHON-MIB", "tmnxPythonProtectActionTime"),
        ("TIMETRA-PYTHON-MIB", "tmnxPythonPolicyMessageTblLstCh"),
        ("TIMETRA-PYTHON-MIB", "tmnxPyPlcyMessageRowStatus"),
        ("TIMETRA-PYTHON-MIB", "tmnxPyPlcyMessageLastChanged"),
        ("TIMETRA-PYTHON-MIB", "tmnxPyPlcyMessagePyScript"))
)
if mibBuilder.loadTexts:
    tmnxPythonGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tmnxPythonCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 87, 1, 1)
)
tmnxPythonCompliance.setObjects(
    ("TIMETRA-PYTHON-MIB", "tmnxPythonGroup")
)
if mibBuilder.loadTexts:
    tmnxPythonCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-PYTHON-MIB",
    **{"TmnxProtection": TmnxProtection,
       "timetraPythonMIBModule": timetraPythonMIBModule,
       "tmnxPythonConformance": tmnxPythonConformance,
       "tmnxPythonCompliances": tmnxPythonCompliances,
       "tmnxPythonCompliance": tmnxPythonCompliance,
       "tmnxPythonGroups": tmnxPythonGroups,
       "tmnxPythonGroup": tmnxPythonGroup,
       "tmnxPythonNotifGroups": tmnxPythonNotifGroups,
       "tmnxPython": tmnxPython,
       "tmnxPythonObjs": tmnxPythonObjs,
       "tmnxPythonScriptTableLastCh": tmnxPythonScriptTableLastCh,
       "tmnxPythonScriptTable": tmnxPythonScriptTable,
       "tmnxPythonScriptEntry": tmnxPythonScriptEntry,
       "tmnxPythonScriptName": tmnxPythonScriptName,
       "tmnxPythonScriptRowStatus": tmnxPythonScriptRowStatus,
       "tmnxPythonScriptLastChanged": tmnxPythonScriptLastChanged,
       "tmnxPythonScriptAdminState": tmnxPythonScriptAdminState,
       "tmnxPythonScriptOperState": tmnxPythonScriptOperState,
       "tmnxPythonScriptDescription": tmnxPythonScriptDescription,
       "tmnxPythonScriptOnFail": tmnxPythonScriptOnFail,
       "tmnxPythonScriptProtection": tmnxPythonScriptProtection,
       "tmnxPythonScriptProtectionKey": tmnxPythonScriptProtectionKey,
       "tmnxPythonScriptPrimaryUrl": tmnxPythonScriptPrimaryUrl,
       "tmnxPythonScriptSecondaryUrl": tmnxPythonScriptSecondaryUrl,
       "tmnxPythonScriptTertiaryUrl": tmnxPythonScriptTertiaryUrl,
       "tmnxPythonScriptActiveUrl": tmnxPythonScriptActiveUrl,
       "tmnxPythonScriptReloadAction": tmnxPythonScriptReloadAction,
       "tmnxPythonPolicyTableLastCh": tmnxPythonPolicyTableLastCh,
       "tmnxPythonPolicyTable": tmnxPythonPolicyTable,
       "tmnxPythonPolicyEntry": tmnxPythonPolicyEntry,
       "tmnxPyPlcyName": tmnxPyPlcyName,
       "tmnxPyPlcyRowStatus": tmnxPyPlcyRowStatus,
       "tmnxPyPlcyLastChanged": tmnxPyPlcyLastChanged,
       "tmnxPyPlcyDescription": tmnxPyPlcyDescription,
       "tmnxPythonPolicyCacheTableLastCh": tmnxPythonPolicyCacheTableLastCh,
       "tmnxPythonPolicyCacheTable": tmnxPythonPolicyCacheTable,
       "tmnxPythonPolicyCacheEntry": tmnxPythonPolicyCacheEntry,
       "tmnxPyPlcyCacheRowStatus": tmnxPyPlcyCacheRowStatus,
       "tmnxPyPlcyCacheEntrySize": tmnxPyPlcyCacheEntrySize,
       "tmnxPyPlcyCacheMaxEntries": tmnxPyPlcyCacheMaxEntries,
       "tmnxPyPlcyCacheMaxLifetime": tmnxPyPlcyCacheMaxLifetime,
       "tmnxPyPlcyCacheAdminState": tmnxPyPlcyCacheAdminState,
       "tmnxPyPlcyCacheLastChanged": tmnxPyPlcyCacheLastChanged,
       "tmnxPyPlcyCachePersistent": tmnxPyPlcyCachePersistent,
       "tmnxPyPlcyCacheMinLifetimeMcs": tmnxPyPlcyCacheMinLifetimeMcs,
       "tmnxPyPlcyCacheMinLifetimeHa": tmnxPyPlcyCacheMinLifetimeHa,
       "tmnxPyPlcyCacheMinLifetimePers": tmnxPyPlcyCacheMinLifetimePers,
       "tmnxPyPlcyCacheNumberOfEntries": tmnxPyPlcyCacheNumberOfEntries,
       "tmnxPythonPolicyMessageTblLstCh": tmnxPythonPolicyMessageTblLstCh,
       "tmnxPythonPolicyMessageTable": tmnxPythonPolicyMessageTable,
       "tmnxPythonPolicyMessageEntry": tmnxPythonPolicyMessageEntry,
       "tmnxPyPlcyMessageType": tmnxPyPlcyMessageType,
       "tmnxPyPlcyMessageDirection": tmnxPyPlcyMessageDirection,
       "tmnxPyPlcyMessageRowStatus": tmnxPyPlcyMessageRowStatus,
       "tmnxPyPlcyMessageLastChanged": tmnxPyPlcyMessageLastChanged,
       "tmnxPyPlcyMessagePyScript": tmnxPyPlcyMessagePyScript,
       "tmnxPythonProtectAction": tmnxPythonProtectAction,
       "tmnxPythonProtectFileUrl": tmnxPythonProtectFileUrl,
       "tmnxPythonProtectDestFileUrl": tmnxPythonProtectDestFileUrl,
       "tmnxPythonProtectType": tmnxPythonProtectType,
       "tmnxPythonProtectKey": tmnxPythonProtectKey,
       "tmnxPythonProtectActionGo": tmnxPythonProtectActionGo,
       "tmnxPythonProtectActionSuccess": tmnxPythonProtectActionSuccess,
       "tmnxPythonProtectActionTime": tmnxPythonProtectActionTime,
       "tmnxPythonNotificationObjs": tmnxPythonNotificationObjs,
       "tmnxPythonNotifyPrefix": tmnxPythonNotifyPrefix,
       "tmnxPythonNotifications": tmnxPythonNotifications}
)
