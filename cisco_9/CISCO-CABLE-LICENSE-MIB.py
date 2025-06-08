# SNMP MIB module (CISCO-CABLE-LICENSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-CABLE-LICENSE-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:43:27 2025
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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoCableLicenseMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 839)
)
if mibBuilder.loadTexts:
    ciscoCableLicenseMIB.setRevisions(
        ("2017-02-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoCableLicenseInfoTable_Object = MibTable
ciscoCableLicenseInfoTable = _CiscoCableLicenseInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 839, 1)
)
if mibBuilder.loadTexts:
    ciscoCableLicenseInfoTable.setStatus("current")
_CiscoCableLicenseInfoEntry_Object = MibTableRow
ciscoCableLicenseInfoEntry = _CiscoCableLicenseInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 839, 1, 1)
)
ciscoCableLicenseInfoEntry.setIndexNames(
    (0, "CISCO-CABLE-LICENSE-MIB", "ciscoCableLicenseIndex"),
)
if mibBuilder.loadTexts:
    ciscoCableLicenseInfoEntry.setStatus("current")


class _CiscoCableLicenseIndex_Type(Unsigned32):
    """Custom type ciscoCableLicenseIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CiscoCableLicenseIndex_Type.__name__ = "Unsigned32"
_CiscoCableLicenseIndex_Object = MibTableColumn
ciscoCableLicenseIndex = _CiscoCableLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 839, 1, 1, 1),
    _CiscoCableLicenseIndex_Type()
)
ciscoCableLicenseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoCableLicenseIndex.setStatus("current")


class _CiscoCableLicenseFeatureName_Type(SnmpAdminString):
    """Custom type ciscoCableLicenseFeatureName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CiscoCableLicenseFeatureName_Type.__name__ = "SnmpAdminString"
_CiscoCableLicenseFeatureName_Object = MibTableColumn
ciscoCableLicenseFeatureName = _CiscoCableLicenseFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 839, 1, 1, 2),
    _CiscoCableLicenseFeatureName_Type()
)
ciscoCableLicenseFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCableLicenseFeatureName.setStatus("current")


class _CiscoCableLicenseEnforcementEnabled_Type(TruthValue):
    """Custom type ciscoCableLicenseEnforcementEnabled based on TruthValue"""
    defaultValue = 2


_CiscoCableLicenseEnforcementEnabled_Type.__name__ = "TruthValue"
_CiscoCableLicenseEnforcementEnabled_Object = MibTableColumn
ciscoCableLicenseEnforcementEnabled = _CiscoCableLicenseEnforcementEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 839, 1, 1, 3),
    _CiscoCableLicenseEnforcementEnabled_Type()
)
ciscoCableLicenseEnforcementEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoCableLicenseEnforcementEnabled.setStatus("current")
_CiscoCableLicenseCapLimit_Type = Unsigned32
_CiscoCableLicenseCapLimit_Object = MibTableColumn
ciscoCableLicenseCapLimit = _CiscoCableLicenseCapLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 839, 1, 1, 4),
    _CiscoCableLicenseCapLimit_Type()
)
ciscoCableLicenseCapLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoCableLicenseCapLimit.setStatus("current")
_CiscoCableLicenseUsageCountRemaining_Type = Integer32
_CiscoCableLicenseUsageCountRemaining_Object = MibTableColumn
ciscoCableLicenseUsageCountRemaining = _CiscoCableLicenseUsageCountRemaining_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 839, 1, 1, 5),
    _CiscoCableLicenseUsageCountRemaining_Type()
)
ciscoCableLicenseUsageCountRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCableLicenseUsageCountRemaining.setStatus("current")


class _CiscoCableLicenseStatus_Type(Integer32):
    """Custom type ciscoCableLicenseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notCappedEnforced", 1),
          ("cappedEnforced", 2))
    )


_CiscoCableLicenseStatus_Type.__name__ = "Integer32"
_CiscoCableLicenseStatus_Object = MibTableColumn
ciscoCableLicenseStatus = _CiscoCableLicenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 839, 1, 1, 6),
    _CiscoCableLicenseStatus_Type()
)
ciscoCableLicenseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCableLicenseStatus.setStatus("current")


class _CiscoCableLicenseLastActionFailCause_Type(Integer32):
    """Custom type ciscoCableLicenseLastActionFailCause based on Integer32"""
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
        *(("noError", 1),
          ("configLocked", 2),
          ("cappedEnabledAlready", 3),
          ("cappedLessThanUsed", 4),
          ("cappedCountSaveFail", 5),
          ("cmtsNotReady", 6),
          ("wrongValue", 7))
    )


_CiscoCableLicenseLastActionFailCause_Type.__name__ = "Integer32"
_CiscoCableLicenseLastActionFailCause_Object = MibTableColumn
ciscoCableLicenseLastActionFailCause = _CiscoCableLicenseLastActionFailCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 839, 1, 1, 7),
    _CiscoCableLicenseLastActionFailCause_Type()
)
ciscoCableLicenseLastActionFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCableLicenseLastActionFailCause.setStatus("current")
_CiscoCableLicenseLastActionTime_Type = TimeStamp
_CiscoCableLicenseLastActionTime_Object = MibTableColumn
ciscoCableLicenseLastActionTime = _CiscoCableLicenseLastActionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 839, 1, 1, 8),
    _CiscoCableLicenseLastActionTime_Type()
)
ciscoCableLicenseLastActionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCableLicenseLastActionTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CABLE-LICENSE-MIB",
    **{"ciscoCableLicenseMIB": ciscoCableLicenseMIB,
       "ciscoCableLicenseInfoTable": ciscoCableLicenseInfoTable,
       "ciscoCableLicenseInfoEntry": ciscoCableLicenseInfoEntry,
       "ciscoCableLicenseIndex": ciscoCableLicenseIndex,
       "ciscoCableLicenseFeatureName": ciscoCableLicenseFeatureName,
       "ciscoCableLicenseEnforcementEnabled": ciscoCableLicenseEnforcementEnabled,
       "ciscoCableLicenseCapLimit": ciscoCableLicenseCapLimit,
       "ciscoCableLicenseUsageCountRemaining": ciscoCableLicenseUsageCountRemaining,
       "ciscoCableLicenseStatus": ciscoCableLicenseStatus,
       "ciscoCableLicenseLastActionFailCause": ciscoCableLicenseLastActionFailCause,
       "ciscoCableLicenseLastActionTime": ciscoCableLicenseLastActionTime}
)
