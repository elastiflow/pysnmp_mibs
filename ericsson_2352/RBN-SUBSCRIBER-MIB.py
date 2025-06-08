# SNMP MIB module (RBN-SUBSCRIBER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_2352/RBN-SUBSCRIBER-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:10:32 2025
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

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(RbnCircuitHandle,) = mibBuilder.importSymbols(
    "RBN-TC",
    "RbnCircuitHandle")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TruthValue")


# MODULE-IDENTITY

rbnSubscriberMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9)
)
if mibBuilder.loadTexts:
    rbnSubscriberMib.setRevisions(
        ("2003-07-21 00:00",
         "2002-07-02 00:00",
         "2002-06-02 00:00",
         "2001-11-07 00:00",
         "2001-04-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnSubscriberMIBObjects_ObjectIdentity = ObjectIdentity
rbnSubscriberMIBObjects = _RbnSubscriberMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1)
)
_RbnSubscriberConfig_ObjectIdentity = ObjectIdentity
rbnSubscriberConfig = _RbnSubscriberConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1)
)
_RbnSubscriberCfgTable_Object = MibTable
rbnSubscriberCfgTable = _RbnSubscriberCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rbnSubscriberCfgTable.setStatus("current")
_RbnSubscriberCfgEntry_Object = MibTableRow
rbnSubscriberCfgEntry = _RbnSubscriberCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1)
)
rbnSubscriberCfgEntry.setIndexNames(
    (0, "RBN-SUBSCRIBER-MIB", "rbnSubscriberName"),
)
if mibBuilder.loadTexts:
    rbnSubscriberCfgEntry.setStatus("current")


class _RbnSubscriberName_Type(SnmpAdminString):
    """Custom type rbnSubscriberName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RbnSubscriberName_Type.__name__ = "SnmpAdminString"
_RbnSubscriberName_Object = MibTableColumn
rbnSubscriberName = _RbnSubscriberName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 1),
    _RbnSubscriberName_Type()
)
rbnSubscriberName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSubscriberName.setStatus("current")
_RbnSubscriberRowStatus_Type = RowStatus
_RbnSubscriberRowStatus_Object = MibTableColumn
rbnSubscriberRowStatus = _RbnSubscriberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 2),
    _RbnSubscriberRowStatus_Type()
)
rbnSubscriberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberRowStatus.setStatus("current")


class _RbnSubscriberBrgGroup_Type(SnmpAdminString):
    """Custom type rbnSubscriberBrgGroup based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RbnSubscriberBrgGroup_Type.__name__ = "SnmpAdminString"
_RbnSubscriberBrgGroup_Object = MibTableColumn
rbnSubscriberBrgGroup = _RbnSubscriberBrgGroup_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 3),
    _RbnSubscriberBrgGroup_Type()
)
rbnSubscriberBrgGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberBrgGroup.setStatus("current")


class _RbnSubscriberBrgAgingTime_Type(Unsigned32):
    """Custom type rbnSubscriberBrgAgingTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 1000000),
    )


_RbnSubscriberBrgAgingTime_Type.__name__ = "Unsigned32"
_RbnSubscriberBrgAgingTime_Object = MibTableColumn
rbnSubscriberBrgAgingTime = _RbnSubscriberBrgAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 4),
    _RbnSubscriberBrgAgingTime_Type()
)
rbnSubscriberBrgAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberBrgAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubscriberBrgAgingTime.setUnits("seconds")


class _RbnSubscriberBrgPathCost_Type(Unsigned32):
    """Custom type rbnSubscriberBrgPathCost based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RbnSubscriberBrgPathCost_Type.__name__ = "Unsigned32"
_RbnSubscriberBrgPathCost_Object = MibTableColumn
rbnSubscriberBrgPathCost = _RbnSubscriberBrgPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 5),
    _RbnSubscriberBrgPathCost_Type()
)
rbnSubscriberBrgPathCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberBrgPathCost.setStatus("current")


class _RbnSubscriberBrgSpanningDisabled_Type(TruthValue):
    """Custom type rbnSubscriberBrgSpanningDisabled based on TruthValue"""
    defaultValue = 2


_RbnSubscriberBrgSpanningDisabled_Type.__name__ = "TruthValue"
_RbnSubscriberBrgSpanningDisabled_Object = MibTableColumn
rbnSubscriberBrgSpanningDisabled = _RbnSubscriberBrgSpanningDisabled_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 6),
    _RbnSubscriberBrgSpanningDisabled_Type()
)
rbnSubscriberBrgSpanningDisabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberBrgSpanningDisabled.setStatus("current")


class _RbnSubscriberBrgTransBpdu_Type(TruthValue):
    """Custom type rbnSubscriberBrgTransBpdu based on TruthValue"""
    defaultValue = 2


_RbnSubscriberBrgTransBpdu_Type.__name__ = "TruthValue"
_RbnSubscriberBrgTransBpdu_Object = MibTableColumn
rbnSubscriberBrgTransBpdu = _RbnSubscriberBrgTransBpdu_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 7),
    _RbnSubscriberBrgTransBpdu_Type()
)
rbnSubscriberBrgTransBpdu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberBrgTransBpdu.setStatus("current")


class _RbnSubscriberBrgInGroup_Type(SnmpAdminString):
    """Custom type rbnSubscriberBrgInGroup based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RbnSubscriberBrgInGroup_Type.__name__ = "SnmpAdminString"
_RbnSubscriberBrgInGroup_Object = MibTableColumn
rbnSubscriberBrgInGroup = _RbnSubscriberBrgInGroup_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 8),
    _RbnSubscriberBrgInGroup_Type()
)
rbnSubscriberBrgInGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberBrgInGroup.setStatus("current")


class _RbnSubscriberBrgOutGroup_Type(SnmpAdminString):
    """Custom type rbnSubscriberBrgOutGroup based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RbnSubscriberBrgOutGroup_Type.__name__ = "SnmpAdminString"
_RbnSubscriberBrgOutGroup_Object = MibTableColumn
rbnSubscriberBrgOutGroup = _RbnSubscriberBrgOutGroup_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 9),
    _RbnSubscriberBrgOutGroup_Type()
)
rbnSubscriberBrgOutGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberBrgOutGroup.setStatus("current")


class _RbnSubscriberMaxDHCP_Type(Unsigned32):
    """Custom type rbnSubscriberMaxDHCP based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RbnSubscriberMaxDHCP_Type.__name__ = "Unsigned32"
_RbnSubscriberMaxDHCP_Object = MibTableColumn
rbnSubscriberMaxDHCP = _RbnSubscriberMaxDHCP_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 10),
    _RbnSubscriberMaxDHCP_Type()
)
rbnSubscriberMaxDHCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberMaxDHCP.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubscriberMaxDHCP.setUnits("IpAddresses")
_RbnSubscriberDnsPrimaryType_Type = InetAddressType
_RbnSubscriberDnsPrimaryType_Object = MibTableColumn
rbnSubscriberDnsPrimaryType = _RbnSubscriberDnsPrimaryType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 11),
    _RbnSubscriberDnsPrimaryType_Type()
)
rbnSubscriberDnsPrimaryType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberDnsPrimaryType.setStatus("current")


class _RbnSubscriberDnsPrimary_Type(InetAddress):
    """Custom type rbnSubscriberDnsPrimary based on InetAddress"""
    defaultValue = OctetString("")


_RbnSubscriberDnsPrimary_Type.__name__ = "InetAddress"
_RbnSubscriberDnsPrimary_Object = MibTableColumn
rbnSubscriberDnsPrimary = _RbnSubscriberDnsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 12),
    _RbnSubscriberDnsPrimary_Type()
)
rbnSubscriberDnsPrimary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberDnsPrimary.setStatus("current")
_RbnSubscriberDnsSecondaryType_Type = InetAddressType
_RbnSubscriberDnsSecondaryType_Object = MibTableColumn
rbnSubscriberDnsSecondaryType = _RbnSubscriberDnsSecondaryType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 13),
    _RbnSubscriberDnsSecondaryType_Type()
)
rbnSubscriberDnsSecondaryType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberDnsSecondaryType.setStatus("current")


class _RbnSubscriberDnsSecondary_Type(InetAddress):
    """Custom type rbnSubscriberDnsSecondary based on InetAddress"""
    defaultValue = OctetString("")


_RbnSubscriberDnsSecondary_Type.__name__ = "InetAddress"
_RbnSubscriberDnsSecondary_Object = MibTableColumn
rbnSubscriberDnsSecondary = _RbnSubscriberDnsSecondary_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 14),
    _RbnSubscriberDnsSecondary_Type()
)
rbnSubscriberDnsSecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberDnsSecondary.setStatus("current")


class _RbnSubscriberPassword_Type(SnmpAdminString):
    """Custom type rbnSubscriberPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RbnSubscriberPassword_Type.__name__ = "SnmpAdminString"
_RbnSubscriberPassword_Object = MibTableColumn
rbnSubscriberPassword = _RbnSubscriberPassword_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 15),
    _RbnSubscriberPassword_Type()
)
rbnSubscriberPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberPassword.setStatus("current")


class _RbnSubscriberPasswordOut_Type(SnmpAdminString):
    """Custom type rbnSubscriberPasswordOut based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RbnSubscriberPasswordOut_Type.__name__ = "SnmpAdminString"
_RbnSubscriberPasswordOut_Object = MibTableColumn
rbnSubscriberPasswordOut = _RbnSubscriberPasswordOut_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 16),
    _RbnSubscriberPasswordOut_Type()
)
rbnSubscriberPasswordOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberPasswordOut.setStatus("current")


class _RbnSubscriberPoliceRate_Type(Unsigned32):
    """Custom type rbnSubscriberPoliceRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 100000000),
    )


_RbnSubscriberPoliceRate_Type.__name__ = "Unsigned32"
_RbnSubscriberPoliceRate_Object = MibTableColumn
rbnSubscriberPoliceRate = _RbnSubscriberPoliceRate_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 17),
    _RbnSubscriberPoliceRate_Type()
)
rbnSubscriberPoliceRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberPoliceRate.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubscriberPoliceRate.setUnits("kbps")


class _RbnSubscriberPoliceBurst_Type(Unsigned32):
    """Custom type rbnSubscriberPoliceBurst based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_RbnSubscriberPoliceBurst_Type.__name__ = "Unsigned32"
_RbnSubscriberPoliceBurst_Object = MibTableColumn
rbnSubscriberPoliceBurst = _RbnSubscriberPoliceBurst_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 18),
    _RbnSubscriberPoliceBurst_Type()
)
rbnSubscriberPoliceBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberPoliceBurst.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubscriberPoliceBurst.setUnits("octets")


class _RbnSubscriberLimitRate_Type(Unsigned32):
    """Custom type rbnSubscriberLimitRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 100000000),
    )


_RbnSubscriberLimitRate_Type.__name__ = "Unsigned32"
_RbnSubscriberLimitRate_Object = MibTableColumn
rbnSubscriberLimitRate = _RbnSubscriberLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 19),
    _RbnSubscriberLimitRate_Type()
)
rbnSubscriberLimitRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberLimitRate.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubscriberLimitRate.setUnits("kbps")


class _RbnSubscriberLimitBurst_Type(Unsigned32):
    """Custom type rbnSubscriberLimitBurst based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_RbnSubscriberLimitBurst_Type.__name__ = "Unsigned32"
_RbnSubscriberLimitBurst_Object = MibTableColumn
rbnSubscriberLimitBurst = _RbnSubscriberLimitBurst_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 20),
    _RbnSubscriberLimitBurst_Type()
)
rbnSubscriberLimitBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberLimitBurst.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubscriberLimitBurst.setUnits("bytes")


class _RbnSubscriberPortLimit_Type(Unsigned32):
    """Custom type rbnSubscriberPortLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RbnSubscriberPortLimit_Type.__name__ = "Unsigned32"
_RbnSubscriberPortLimit_Object = MibTableColumn
rbnSubscriberPortLimit = _RbnSubscriberPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 21),
    _RbnSubscriberPortLimit_Type()
)
rbnSubscriberPortLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberPortLimit.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubscriberPortLimit.setUnits("sessions")


class _RbnSubscriberPppMtu_Type(Unsigned32):
    """Custom type rbnSubscriberPppMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(128, 16384),
    )


_RbnSubscriberPppMtu_Type.__name__ = "Unsigned32"
_RbnSubscriberPppMtu_Object = MibTableColumn
rbnSubscriberPppMtu = _RbnSubscriberPppMtu_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 22),
    _RbnSubscriberPppMtu_Type()
)
rbnSubscriberPppMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberPppMtu.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubscriberPppMtu.setUnits("octets")


class _RbnSubscriberPppCompression_Type(TruthValue):
    """Custom type rbnSubscriberPppCompression based on TruthValue"""
    defaultValue = 2


_RbnSubscriberPppCompression_Type.__name__ = "TruthValue"
_RbnSubscriberPppCompression_Object = MibTableColumn
rbnSubscriberPppCompression = _RbnSubscriberPppCompression_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 23),
    _RbnSubscriberPppCompression_Type()
)
rbnSubscriberPppCompression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberPppCompression.setStatus("current")


class _RbnSubscriberPppoeMotm_Type(SnmpAdminString):
    """Custom type rbnSubscriberPppoeMotm based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RbnSubscriberPppoeMotm_Type.__name__ = "SnmpAdminString"
_RbnSubscriberPppoeMotm_Object = MibTableColumn
rbnSubscriberPppoeMotm = _RbnSubscriberPppoeMotm_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 24),
    _RbnSubscriberPppoeMotm_Type()
)
rbnSubscriberPppoeMotm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberPppoeMotm.setStatus("current")


class _RbnSubscriberPppoeUrl_Type(SnmpAdminString):
    """Custom type rbnSubscriberPppoeUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RbnSubscriberPppoeUrl_Type.__name__ = "SnmpAdminString"
_RbnSubscriberPppoeUrl_Object = MibTableColumn
rbnSubscriberPppoeUrl = _RbnSubscriberPppoeUrl_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 25),
    _RbnSubscriberPppoeUrl_Type()
)
rbnSubscriberPppoeUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberPppoeUrl.setStatus("current")


class _RbnSubscriberAbsTimeout_Type(Unsigned32):
    """Custom type rbnSubscriberAbsTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 4294967295),
    )


_RbnSubscriberAbsTimeout_Type.__name__ = "Unsigned32"
_RbnSubscriberAbsTimeout_Object = MibTableColumn
rbnSubscriberAbsTimeout = _RbnSubscriberAbsTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 26),
    _RbnSubscriberAbsTimeout_Type()
)
rbnSubscriberAbsTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberAbsTimeout.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubscriberAbsTimeout.setUnits("minutes")


class _RbnSubscriberIdleTimeout_Type(Unsigned32):
    """Custom type rbnSubscriberIdleTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 4294967295),
    )


_RbnSubscriberIdleTimeout_Type.__name__ = "Unsigned32"
_RbnSubscriberIdleTimeout_Object = MibTableColumn
rbnSubscriberIdleTimeout = _RbnSubscriberIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 27),
    _RbnSubscriberIdleTimeout_Type()
)
rbnSubscriberIdleTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubscriberIdleTimeout.setUnits("minutes")


class _RbnSubscriberTunnelDomain_Type(TruthValue):
    """Custom type rbnSubscriberTunnelDomain based on TruthValue"""
    defaultValue = 2


_RbnSubscriberTunnelDomain_Type.__name__ = "TruthValue"
_RbnSubscriberTunnelDomain_Object = MibTableColumn
rbnSubscriberTunnelDomain = _RbnSubscriberTunnelDomain_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 28),
    _RbnSubscriberTunnelDomain_Type()
)
rbnSubscriberTunnelDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberTunnelDomain.setStatus("current")


class _RbnSubscriberTunnelName_Type(SnmpAdminString):
    """Custom type rbnSubscriberTunnelName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RbnSubscriberTunnelName_Type.__name__ = "SnmpAdminString"
_RbnSubscriberTunnelName_Object = MibTableColumn
rbnSubscriberTunnelName = _RbnSubscriberTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 29),
    _RbnSubscriberTunnelName_Type()
)
rbnSubscriberTunnelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberTunnelName.setStatus("current")


class _RbnSubscriberIpInGroup_Type(SnmpAdminString):
    """Custom type rbnSubscriberIpInGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RbnSubscriberIpInGroup_Type.__name__ = "SnmpAdminString"
_RbnSubscriberIpInGroup_Object = MibTableColumn
rbnSubscriberIpInGroup = _RbnSubscriberIpInGroup_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 30),
    _RbnSubscriberIpInGroup_Type()
)
rbnSubscriberIpInGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberIpInGroup.setStatus("current")


class _RbnSubscriberIpOutGroup_Type(SnmpAdminString):
    """Custom type rbnSubscriberIpOutGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RbnSubscriberIpOutGroup_Type.__name__ = "SnmpAdminString"
_RbnSubscriberIpOutGroup_Object = MibTableColumn
rbnSubscriberIpOutGroup = _RbnSubscriberIpOutGroup_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 31),
    _RbnSubscriberIpOutGroup_Type()
)
rbnSubscriberIpOutGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberIpOutGroup.setStatus("current")


class _RbnSubscriberIpMcastGroupMax_Type(Unsigned32):
    """Custom type rbnSubscriberIpMcastGroupMax based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_RbnSubscriberIpMcastGroupMax_Type.__name__ = "Unsigned32"
_RbnSubscriberIpMcastGroupMax_Object = MibTableColumn
rbnSubscriberIpMcastGroupMax = _RbnSubscriberIpMcastGroupMax_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 32),
    _RbnSubscriberIpMcastGroupMax_Type()
)
rbnSubscriberIpMcastGroupMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberIpMcastGroupMax.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubscriberIpMcastGroupMax.setUnits("multicast Groups")


class _RbnSubscriberIpMcastRx_Type(Integer32):
    """Custom type rbnSubscriberIpMcastRx based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("deny", 1),
          ("permit", 2))
    )


_RbnSubscriberIpMcastRx_Type.__name__ = "Integer32"
_RbnSubscriberIpMcastRx_Object = MibTableColumn
rbnSubscriberIpMcastRx = _RbnSubscriberIpMcastRx_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 33),
    _RbnSubscriberIpMcastRx_Type()
)
rbnSubscriberIpMcastRx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberIpMcastRx.setStatus("current")


class _RbnSubscriberIpMcastSend_Type(Integer32):
    """Custom type rbnSubscriberIpMcastSend based on Integer32"""
    defaultValue = 0

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
          ("deny", 1),
          ("permit", 2),
          ("permitUnsolicit", 3))
    )


_RbnSubscriberIpMcastSend_Type.__name__ = "Integer32"
_RbnSubscriberIpMcastSend_Object = MibTableColumn
rbnSubscriberIpMcastSend = _RbnSubscriberIpMcastSend_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 34),
    _RbnSubscriberIpMcastSend_Type()
)
rbnSubscriberIpMcastSend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberIpMcastSend.setStatus("current")


class _RbnSubscriberIpPoolValid_Type(TruthValue):
    """Custom type rbnSubscriberIpPoolValid based on TruthValue"""
    defaultValue = 2


_RbnSubscriberIpPoolValid_Type.__name__ = "TruthValue"
_RbnSubscriberIpPoolValid_Object = MibTableColumn
rbnSubscriberIpPoolValid = _RbnSubscriberIpPoolValid_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 35),
    _RbnSubscriberIpPoolValid_Type()
)
rbnSubscriberIpPoolValid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberIpPoolValid.setStatus("current")


class _RbnSubscriberIpPoolName_Type(SnmpAdminString):
    """Custom type rbnSubscriberIpPoolName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RbnSubscriberIpPoolName_Type.__name__ = "SnmpAdminString"
_RbnSubscriberIpPoolName_Object = MibTableColumn
rbnSubscriberIpPoolName = _RbnSubscriberIpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 36),
    _RbnSubscriberIpPoolName_Type()
)
rbnSubscriberIpPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberIpPoolName.setStatus("current")


class _RbnSubscriberIpSrcValidation_Type(TruthValue):
    """Custom type rbnSubscriberIpSrcValidation based on TruthValue"""
    defaultValue = 2


_RbnSubscriberIpSrcValidation_Type.__name__ = "TruthValue"
_RbnSubscriberIpSrcValidation_Object = MibTableColumn
rbnSubscriberIpSrcValidation = _RbnSubscriberIpSrcValidation_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 37),
    _RbnSubscriberIpSrcValidation_Type()
)
rbnSubscriberIpSrcValidation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberIpSrcValidation.setStatus("current")


class _RbnSubscriberIpTos_Type(Bits):
    """Custom type rbnSubscriberIpTos based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("normal", 0),
          ("minCost", 1),
          ("maxReliability", 2),
          ("maxThroughput", 3),
          ("minDelay", 4))
    )

_RbnSubscriberIpTos_Type.__name__ = "Bits"
_RbnSubscriberIpTos_Object = MibTableColumn
rbnSubscriberIpTos = _RbnSubscriberIpTos_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 38),
    _RbnSubscriberIpTos_Type()
)
rbnSubscriberIpTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberIpTos.setStatus("current")


class _RbnSubscriberClear_Type(TruthValue):
    """Custom type rbnSubscriberClear based on TruthValue"""
    defaultValue = 2


_RbnSubscriberClear_Type.__name__ = "TruthValue"
_RbnSubscriberClear_Object = MibTableColumn
rbnSubscriberClear = _RbnSubscriberClear_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 39),
    _RbnSubscriberClear_Type()
)
rbnSubscriberClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberClear.setStatus("current")


class _RbnSubscriberIpsecPeerName_Type(SnmpAdminString):
    """Custom type rbnSubscriberIpsecPeerName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RbnSubscriberIpsecPeerName_Type.__name__ = "SnmpAdminString"
_RbnSubscriberIpsecPeerName_Object = MibTableColumn
rbnSubscriberIpsecPeerName = _RbnSubscriberIpsecPeerName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 40),
    _RbnSubscriberIpsecPeerName_Type()
)
rbnSubscriberIpsecPeerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberIpsecPeerName.setStatus("current")


class _RbnSubscriberIpsecPolicyName_Type(SnmpAdminString):
    """Custom type rbnSubscriberIpsecPolicyName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RbnSubscriberIpsecPolicyName_Type.__name__ = "SnmpAdminString"
_RbnSubscriberIpsecPolicyName_Object = MibTableColumn
rbnSubscriberIpsecPolicyName = _RbnSubscriberIpsecPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 41),
    _RbnSubscriberIpsecPolicyName_Type()
)
rbnSubscriberIpsecPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberIpsecPolicyName.setStatus("current")


class _RbnSubscriberQosInPolicyName_Type(SnmpAdminString):
    """Custom type rbnSubscriberQosInPolicyName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RbnSubscriberQosInPolicyName_Type.__name__ = "SnmpAdminString"
_RbnSubscriberQosInPolicyName_Object = MibTableColumn
rbnSubscriberQosInPolicyName = _RbnSubscriberQosInPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 42),
    _RbnSubscriberQosInPolicyName_Type()
)
rbnSubscriberQosInPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberQosInPolicyName.setStatus("obsolete")


class _RbnSubscriberQosOutPolicyName_Type(SnmpAdminString):
    """Custom type rbnSubscriberQosOutPolicyName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RbnSubscriberQosOutPolicyName_Type.__name__ = "SnmpAdminString"
_RbnSubscriberQosOutPolicyName_Object = MibTableColumn
rbnSubscriberQosOutPolicyName = _RbnSubscriberQosOutPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 43),
    _RbnSubscriberQosOutPolicyName_Type()
)
rbnSubscriberQosOutPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberQosOutPolicyName.setStatus("obsolete")


class _RbnSubscriberBrgCctAddrMax_Type(Unsigned32):
    """Custom type rbnSubscriberBrgCctAddrMax based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RbnSubscriberBrgCctAddrMax_Type.__name__ = "Unsigned32"
_RbnSubscriberBrgCctAddrMax_Object = MibTableColumn
rbnSubscriberBrgCctAddrMax = _RbnSubscriberBrgCctAddrMax_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 1, 1, 44),
    _RbnSubscriberBrgCctAddrMax_Type()
)
rbnSubscriberBrgCctAddrMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberBrgCctAddrMax.setStatus("current")
_RbnSubscriberIpAddressTable_Object = MibTable
rbnSubscriberIpAddressTable = _RbnSubscriberIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rbnSubscriberIpAddressTable.setStatus("current")
_RbnSubscriberIpAddressEntry_Object = MibTableRow
rbnSubscriberIpAddressEntry = _RbnSubscriberIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 2, 1)
)
rbnSubscriberIpAddressEntry.setIndexNames(
    (0, "RBN-SUBSCRIBER-MIB", "rbnSubscriberName"),
    (0, "RBN-SUBSCRIBER-MIB", "rbnSubscriberIpAddressType"),
    (0, "RBN-SUBSCRIBER-MIB", "rbnSubscriberIpAddress"),
)
if mibBuilder.loadTexts:
    rbnSubscriberIpAddressEntry.setStatus("current")
_RbnSubscriberIpAddressType_Type = InetAddressType
_RbnSubscriberIpAddressType_Object = MibTableColumn
rbnSubscriberIpAddressType = _RbnSubscriberIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 2, 1, 1),
    _RbnSubscriberIpAddressType_Type()
)
rbnSubscriberIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSubscriberIpAddressType.setStatus("current")


class _RbnSubscriberIpAddress_Type(InetAddress):
    """Custom type rbnSubscriberIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_RbnSubscriberIpAddress_Type.__name__ = "InetAddress"
_RbnSubscriberIpAddress_Object = MibTableColumn
rbnSubscriberIpAddress = _RbnSubscriberIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 2, 1, 2),
    _RbnSubscriberIpAddress_Type()
)
rbnSubscriberIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSubscriberIpAddress.setStatus("current")


class _RbnSubscriberIpAddressMaskLength_Type(Unsigned32):
    """Custom type rbnSubscriberIpAddressMaskLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RbnSubscriberIpAddressMaskLength_Type.__name__ = "Unsigned32"
_RbnSubscriberIpAddressMaskLength_Object = MibTableColumn
rbnSubscriberIpAddressMaskLength = _RbnSubscriberIpAddressMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 2, 1, 4),
    _RbnSubscriberIpAddressMaskLength_Type()
)
rbnSubscriberIpAddressMaskLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberIpAddressMaskLength.setStatus("current")
_RbnSubscriberIpAddressRowStatus_Type = RowStatus
_RbnSubscriberIpAddressRowStatus_Object = MibTableColumn
rbnSubscriberIpAddressRowStatus = _RbnSubscriberIpAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 2, 1, 5),
    _RbnSubscriberIpAddressRowStatus_Type()
)
rbnSubscriberIpAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberIpAddressRowStatus.setStatus("current")
_RbnSubscriberArpTable_Object = MibTable
rbnSubscriberArpTable = _RbnSubscriberArpTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 3)
)
if mibBuilder.loadTexts:
    rbnSubscriberArpTable.setStatus("current")
_RbnSubscriberArpEntry_Object = MibTableRow
rbnSubscriberArpEntry = _RbnSubscriberArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 3, 1)
)
rbnSubscriberArpEntry.setIndexNames(
    (0, "RBN-SUBSCRIBER-MIB", "rbnSubscriberName"),
    (0, "RBN-SUBSCRIBER-MIB", "rbnSubscriberArpAddressType"),
    (0, "RBN-SUBSCRIBER-MIB", "rbnSubscriberArpAddress"),
)
if mibBuilder.loadTexts:
    rbnSubscriberArpEntry.setStatus("current")
_RbnSubscriberArpAddressType_Type = InetAddressType
_RbnSubscriberArpAddressType_Object = MibTableColumn
rbnSubscriberArpAddressType = _RbnSubscriberArpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 3, 1, 1),
    _RbnSubscriberArpAddressType_Type()
)
rbnSubscriberArpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSubscriberArpAddressType.setStatus("current")


class _RbnSubscriberArpAddress_Type(InetAddress):
    """Custom type rbnSubscriberArpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_RbnSubscriberArpAddress_Type.__name__ = "InetAddress"
_RbnSubscriberArpAddress_Object = MibTableColumn
rbnSubscriberArpAddress = _RbnSubscriberArpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 3, 1, 2),
    _RbnSubscriberArpAddress_Type()
)
rbnSubscriberArpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSubscriberArpAddress.setStatus("current")
_RbnSubscriberArpMacAddress_Type = MacAddress
_RbnSubscriberArpMacAddress_Object = MibTableColumn
rbnSubscriberArpMacAddress = _RbnSubscriberArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 3, 1, 3),
    _RbnSubscriberArpMacAddress_Type()
)
rbnSubscriberArpMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberArpMacAddress.setStatus("current")
_RbnSubscriberArpRowStatus_Type = RowStatus
_RbnSubscriberArpRowStatus_Object = MibTableColumn
rbnSubscriberArpRowStatus = _RbnSubscriberArpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 3, 1, 4),
    _RbnSubscriberArpRowStatus_Type()
)
rbnSubscriberArpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberArpRowStatus.setStatus("current")
_RbnSubscriberRouteTable_Object = MibTable
rbnSubscriberRouteTable = _RbnSubscriberRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 4)
)
if mibBuilder.loadTexts:
    rbnSubscriberRouteTable.setStatus("current")
_RbnSubscriberRouteEntry_Object = MibTableRow
rbnSubscriberRouteEntry = _RbnSubscriberRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 4, 1)
)
rbnSubscriberRouteEntry.setIndexNames(
    (0, "RBN-SUBSCRIBER-MIB", "rbnSubscriberName"),
    (0, "RBN-SUBSCRIBER-MIB", "rbnSubscriberRteNetworkAddrType"),
    (0, "RBN-SUBSCRIBER-MIB", "rbnSubscriberRteNetworkAddr"),
    (0, "RBN-SUBSCRIBER-MIB", "rbnSubscriberRteNetworkMaskLength"),
)
if mibBuilder.loadTexts:
    rbnSubscriberRouteEntry.setStatus("current")
_RbnSubscriberRteNetworkAddrType_Type = InetAddressType
_RbnSubscriberRteNetworkAddrType_Object = MibTableColumn
rbnSubscriberRteNetworkAddrType = _RbnSubscriberRteNetworkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 4, 1, 1),
    _RbnSubscriberRteNetworkAddrType_Type()
)
rbnSubscriberRteNetworkAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSubscriberRteNetworkAddrType.setStatus("current")


class _RbnSubscriberRteNetworkAddr_Type(InetAddress):
    """Custom type rbnSubscriberRteNetworkAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_RbnSubscriberRteNetworkAddr_Type.__name__ = "InetAddress"
_RbnSubscriberRteNetworkAddr_Object = MibTableColumn
rbnSubscriberRteNetworkAddr = _RbnSubscriberRteNetworkAddr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 4, 1, 2),
    _RbnSubscriberRteNetworkAddr_Type()
)
rbnSubscriberRteNetworkAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSubscriberRteNetworkAddr.setStatus("current")


class _RbnSubscriberRteNetworkMaskLength_Type(Unsigned32):
    """Custom type rbnSubscriberRteNetworkMaskLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RbnSubscriberRteNetworkMaskLength_Type.__name__ = "Unsigned32"
_RbnSubscriberRteNetworkMaskLength_Object = MibTableColumn
rbnSubscriberRteNetworkMaskLength = _RbnSubscriberRteNetworkMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 4, 1, 3),
    _RbnSubscriberRteNetworkMaskLength_Type()
)
rbnSubscriberRteNetworkMaskLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSubscriberRteNetworkMaskLength.setStatus("current")


class _RbnSubscriberRteNextHopType_Type(InetAddressType):
    """Custom type rbnSubscriberRteNextHopType based on InetAddressType"""
    defaultValue = 0


_RbnSubscriberRteNextHopType_Type.__name__ = "InetAddressType"
_RbnSubscriberRteNextHopType_Object = MibTableColumn
rbnSubscriberRteNextHopType = _RbnSubscriberRteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 4, 1, 4),
    _RbnSubscriberRteNextHopType_Type()
)
rbnSubscriberRteNextHopType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberRteNextHopType.setStatus("current")


class _RbnSubscriberRteNextHop_Type(InetAddress):
    """Custom type rbnSubscriberRteNextHop based on InetAddress"""
    defaultValue = OctetString("")


_RbnSubscriberRteNextHop_Type.__name__ = "InetAddress"
_RbnSubscriberRteNextHop_Object = MibTableColumn
rbnSubscriberRteNextHop = _RbnSubscriberRteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 4, 1, 5),
    _RbnSubscriberRteNextHop_Type()
)
rbnSubscriberRteNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberRteNextHop.setStatus("current")
_RbnSubscriberRteRowStatus_Type = RowStatus
_RbnSubscriberRteRowStatus_Object = MibTableColumn
rbnSubscriberRteRowStatus = _RbnSubscriberRteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 4, 1, 6),
    _RbnSubscriberRteRowStatus_Type()
)
rbnSubscriberRteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberRteRowStatus.setStatus("current")
_RbnSubscriberPppoeRteTable_Object = MibTable
rbnSubscriberPppoeRteTable = _RbnSubscriberPppoeRteTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 5)
)
if mibBuilder.loadTexts:
    rbnSubscriberPppoeRteTable.setStatus("current")
_RbnSubscriberPppoeRteEntry_Object = MibTableRow
rbnSubscriberPppoeRteEntry = _RbnSubscriberPppoeRteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 5, 1)
)
rbnSubscriberPppoeRteEntry.setIndexNames(
    (0, "RBN-SUBSCRIBER-MIB", "rbnSubscriberName"),
    (0, "RBN-SUBSCRIBER-MIB", "rbnSubscriberPppoeRteAddrType"),
    (0, "RBN-SUBSCRIBER-MIB", "rbnSubscriberPppoeRteAddr"),
    (0, "RBN-SUBSCRIBER-MIB", "rbnSubscriberPppoeRteMaskLength"),
)
if mibBuilder.loadTexts:
    rbnSubscriberPppoeRteEntry.setStatus("current")
_RbnSubscriberPppoeRteAddrType_Type = InetAddressType
_RbnSubscriberPppoeRteAddrType_Object = MibTableColumn
rbnSubscriberPppoeRteAddrType = _RbnSubscriberPppoeRteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 5, 1, 1),
    _RbnSubscriberPppoeRteAddrType_Type()
)
rbnSubscriberPppoeRteAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSubscriberPppoeRteAddrType.setStatus("current")


class _RbnSubscriberPppoeRteAddr_Type(InetAddress):
    """Custom type rbnSubscriberPppoeRteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_RbnSubscriberPppoeRteAddr_Type.__name__ = "InetAddress"
_RbnSubscriberPppoeRteAddr_Object = MibTableColumn
rbnSubscriberPppoeRteAddr = _RbnSubscriberPppoeRteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 5, 1, 2),
    _RbnSubscriberPppoeRteAddr_Type()
)
rbnSubscriberPppoeRteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSubscriberPppoeRteAddr.setStatus("current")


class _RbnSubscriberPppoeRteMaskLength_Type(Unsigned32):
    """Custom type rbnSubscriberPppoeRteMaskLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RbnSubscriberPppoeRteMaskLength_Type.__name__ = "Unsigned32"
_RbnSubscriberPppoeRteMaskLength_Object = MibTableColumn
rbnSubscriberPppoeRteMaskLength = _RbnSubscriberPppoeRteMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 5, 1, 3),
    _RbnSubscriberPppoeRteMaskLength_Type()
)
rbnSubscriberPppoeRteMaskLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSubscriberPppoeRteMaskLength.setStatus("current")


class _RbnSubscriberPppoeRteMetric_Type(Integer32):
    """Custom type rbnSubscriberPppoeRteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RbnSubscriberPppoeRteMetric_Type.__name__ = "Integer32"
_RbnSubscriberPppoeRteMetric_Object = MibTableColumn
rbnSubscriberPppoeRteMetric = _RbnSubscriberPppoeRteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 5, 1, 4),
    _RbnSubscriberPppoeRteMetric_Type()
)
rbnSubscriberPppoeRteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberPppoeRteMetric.setStatus("current")
_RbnSubscriberPppoeRteRowStatus_Type = RowStatus
_RbnSubscriberPppoeRteRowStatus_Object = MibTableColumn
rbnSubscriberPppoeRteRowStatus = _RbnSubscriberPppoeRteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 1, 5, 1, 5),
    _RbnSubscriberPppoeRteRowStatus_Type()
)
rbnSubscriberPppoeRteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberPppoeRteRowStatus.setStatus("current")
_RbnSubscriberActive_ObjectIdentity = ObjectIdentity
rbnSubscriberActive = _RbnSubscriberActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 2)
)
_RbnSubscriberActiveTable_Object = MibTable
rbnSubscriberActiveTable = _RbnSubscriberActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rbnSubscriberActiveTable.setStatus("current")
_RbnSubscriberActiveEntry_Object = MibTableRow
rbnSubscriberActiveEntry = _RbnSubscriberActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 2, 1, 1)
)
rbnSubscriberActiveEntry.setIndexNames(
    (0, "RBN-SUBSCRIBER-MIB", "rbnSubscriberName"),
    (0, "RBN-SUBSCRIBER-MIB", "rbnSubscriberActiveCircuitHandle"),
)
if mibBuilder.loadTexts:
    rbnSubscriberActiveEntry.setStatus("current")
_RbnSubscriberActiveCircuitHandle_Type = RbnCircuitHandle
_RbnSubscriberActiveCircuitHandle_Object = MibTableColumn
rbnSubscriberActiveCircuitHandle = _RbnSubscriberActiveCircuitHandle_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 2, 1, 1, 1),
    _RbnSubscriberActiveCircuitHandle_Type()
)
rbnSubscriberActiveCircuitHandle.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSubscriberActiveCircuitHandle.setStatus("current")


class _RbnSubscriberActiveCircuitDescr_Type(SnmpAdminString):
    """Custom type rbnSubscriberActiveCircuitDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RbnSubscriberActiveCircuitDescr_Type.__name__ = "SnmpAdminString"
_RbnSubscriberActiveCircuitDescr_Object = MibTableColumn
rbnSubscriberActiveCircuitDescr = _RbnSubscriberActiveCircuitDescr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 2, 1, 1, 2),
    _RbnSubscriberActiveCircuitDescr_Type()
)
rbnSubscriberActiveCircuitDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubscriberActiveCircuitDescr.setStatus("current")
_RbnSubscriberActiveStartTime_Type = DateAndTime
_RbnSubscriberActiveStartTime_Object = MibTableColumn
rbnSubscriberActiveStartTime = _RbnSubscriberActiveStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 2, 1, 1, 3),
    _RbnSubscriberActiveStartTime_Type()
)
rbnSubscriberActiveStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubscriberActiveStartTime.setStatus("current")
_RbnSubscriberActiveClear_Type = TruthValue
_RbnSubscriberActiveClear_Object = MibTableColumn
rbnSubscriberActiveClear = _RbnSubscriberActiveClear_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 2, 1, 1, 4),
    _RbnSubscriberActiveClear_Type()
)
rbnSubscriberActiveClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnSubscriberActiveClear.setStatus("current")
_RbnSubscriberActiveIpTable_Object = MibTable
rbnSubscriberActiveIpTable = _RbnSubscriberActiveIpTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 2, 2)
)
if mibBuilder.loadTexts:
    rbnSubscriberActiveIpTable.setStatus("current")
_RbnSubscriberActiveIpEntry_Object = MibTableRow
rbnSubscriberActiveIpEntry = _RbnSubscriberActiveIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 2, 2, 1)
)
rbnSubscriberActiveIpEntry.setIndexNames(
    (0, "RBN-SUBSCRIBER-MIB", "rbnSubscriberName"),
    (0, "RBN-SUBSCRIBER-MIB", "rbnSubscriberActiveCircuitHandle"),
    (0, "RBN-SUBSCRIBER-MIB", "rbnSubscriberActiveAddrType"),
    (0, "RBN-SUBSCRIBER-MIB", "rbnSubscriberActiveAddr"),
)
if mibBuilder.loadTexts:
    rbnSubscriberActiveIpEntry.setStatus("current")
_RbnSubscriberActiveAddrType_Type = InetAddressType
_RbnSubscriberActiveAddrType_Object = MibTableColumn
rbnSubscriberActiveAddrType = _RbnSubscriberActiveAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 2, 2, 1, 1),
    _RbnSubscriberActiveAddrType_Type()
)
rbnSubscriberActiveAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSubscriberActiveAddrType.setStatus("current")
_RbnSubscriberActiveAddr_Type = InetAddress
_RbnSubscriberActiveAddr_Object = MibTableColumn
rbnSubscriberActiveAddr = _RbnSubscriberActiveAddr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 2, 2, 1, 2),
    _RbnSubscriberActiveAddr_Type()
)
rbnSubscriberActiveAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubscriberActiveAddr.setStatus("current")
_RbnSubscriberClearAllSpinLock_Type = TestAndIncr
_RbnSubscriberClearAllSpinLock_Object = MibScalar
rbnSubscriberClearAllSpinLock = _RbnSubscriberClearAllSpinLock_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 2, 3),
    _RbnSubscriberClearAllSpinLock_Type()
)
rbnSubscriberClearAllSpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnSubscriberClearAllSpinLock.setStatus("current")
_RbnSubscriberClearAllNextIndex_Type = Unsigned32
_RbnSubscriberClearAllNextIndex_Object = MibScalar
rbnSubscriberClearAllNextIndex = _RbnSubscriberClearAllNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 2, 4),
    _RbnSubscriberClearAllNextIndex_Type()
)
rbnSubscriberClearAllNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubscriberClearAllNextIndex.setStatus("current")
_RbnSubscriberClearAllTable_Object = MibTable
rbnSubscriberClearAllTable = _RbnSubscriberClearAllTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 2, 5)
)
if mibBuilder.loadTexts:
    rbnSubscriberClearAllTable.setStatus("current")
_RbnSubscriberClearAllEntry_Object = MibTableRow
rbnSubscriberClearAllEntry = _RbnSubscriberClearAllEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 2, 5, 1)
)
rbnSubscriberClearAllEntry.setIndexNames(
    (0, "RBN-SUBSCRIBER-MIB", "rbnSubscriberClearAllIndex"),
)
if mibBuilder.loadTexts:
    rbnSubscriberClearAllEntry.setStatus("current")
_RbnSubscriberClearAllIndex_Type = Unsigned32
_RbnSubscriberClearAllIndex_Object = MibTableColumn
rbnSubscriberClearAllIndex = _RbnSubscriberClearAllIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 2, 5, 1, 1),
    _RbnSubscriberClearAllIndex_Type()
)
rbnSubscriberClearAllIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSubscriberClearAllIndex.setStatus("current")
_RbnSubscriberClearAllRowStatus_Type = RowStatus
_RbnSubscriberClearAllRowStatus_Object = MibTableColumn
rbnSubscriberClearAllRowStatus = _RbnSubscriberClearAllRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 2, 5, 1, 2),
    _RbnSubscriberClearAllRowStatus_Type()
)
rbnSubscriberClearAllRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnSubscriberClearAllRowStatus.setStatus("current")


class _RbnSubscriberClearAllState_Type(Integer32):
    """Custom type rbnSubscriberClearAllState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notStarted", 0),
          ("running", 1),
          ("completed", 2))
    )


_RbnSubscriberClearAllState_Type.__name__ = "Integer32"
_RbnSubscriberClearAllState_Object = MibTableColumn
rbnSubscriberClearAllState = _RbnSubscriberClearAllState_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 2, 5, 1, 3),
    _RbnSubscriberClearAllState_Type()
)
rbnSubscriberClearAllState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubscriberClearAllState.setStatus("current")
_RbnSubscriberClearAllTime_Type = DateAndTime
_RbnSubscriberClearAllTime_Object = MibTableColumn
rbnSubscriberClearAllTime = _RbnSubscriberClearAllTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 2, 5, 1, 4),
    _RbnSubscriberClearAllTime_Type()
)
rbnSubscriberClearAllTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubscriberClearAllTime.setStatus("current")
_RbnSubscriberTotalActiveCount_Type = Gauge32
_RbnSubscriberTotalActiveCount_Object = MibScalar
rbnSubscriberTotalActiveCount = _RbnSubscriberTotalActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 2, 6),
    _RbnSubscriberTotalActiveCount_Type()
)
rbnSubscriberTotalActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubscriberTotalActiveCount.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubscriberTotalActiveCount.setUnits("subscribers")
_RbnSubscriberCountTable_Object = MibTable
rbnSubscriberCountTable = _RbnSubscriberCountTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 2, 7)
)
if mibBuilder.loadTexts:
    rbnSubscriberCountTable.setStatus("current")
_RbnSubscriberCountEntry_Object = MibTableRow
rbnSubscriberCountEntry = _RbnSubscriberCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 2, 7, 1)
)
rbnSubscriberCountEntry.setIndexNames(
    (0, "RBN-SUBSCRIBER-MIB", "rbnSubscriberEncapsulationType"),
)
if mibBuilder.loadTexts:
    rbnSubscriberCountEntry.setStatus("current")


class _RbnSubscriberEncapsulationType_Type(Integer32):
    """Custom type rbnSubscriberEncapsulationType based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("ppp", 1),
          ("bridged1483", 2),
          ("routed1483", 3),
          ("bridged1490", 4),
          ("routed1490", 5),
          ("multi1483", 6),
          ("multi1490", 7),
          ("dot1q1483", 8),
          ("dot1q1490", 9),
          ("dot1qEnet", 10),
          ("clips", 11),
          ("other", 255))
    )


_RbnSubscriberEncapsulationType_Type.__name__ = "Integer32"
_RbnSubscriberEncapsulationType_Object = MibTableColumn
rbnSubscriberEncapsulationType = _RbnSubscriberEncapsulationType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 2, 7, 1, 1),
    _RbnSubscriberEncapsulationType_Type()
)
rbnSubscriberEncapsulationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSubscriberEncapsulationType.setStatus("current")
_RbnSubscriberActiveCount_Type = Gauge32
_RbnSubscriberActiveCount_Object = MibTableColumn
rbnSubscriberActiveCount = _RbnSubscriberActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 2, 7, 1, 2),
    _RbnSubscriberActiveCount_Type()
)
rbnSubscriberActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubscriberActiveCount.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubscriberActiveCount.setUnits("subscribers")
_RbnSubscriberStats_ObjectIdentity = ObjectIdentity
rbnSubscriberStats = _RbnSubscriberStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 3)
)
_RbnSubscriberStatsTable_Object = MibTable
rbnSubscriberStatsTable = _RbnSubscriberStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rbnSubscriberStatsTable.setStatus("current")
_RbnSubscriberStatsEntry_Object = MibTableRow
rbnSubscriberStatsEntry = _RbnSubscriberStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 3, 1, 1)
)
rbnSubscriberStatsEntry.setIndexNames(
    (0, "RBN-SUBSCRIBER-MIB", "rbnSubscriberName"),
    (0, "RBN-SUBSCRIBER-MIB", "rbnSubscriberActiveCircuitHandle"),
)
if mibBuilder.loadTexts:
    rbnSubscriberStatsEntry.setStatus("current")
_RbnSubscriberOctetsSent_Type = Counter64
_RbnSubscriberOctetsSent_Object = MibTableColumn
rbnSubscriberOctetsSent = _RbnSubscriberOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 3, 1, 1, 1),
    _RbnSubscriberOctetsSent_Type()
)
rbnSubscriberOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubscriberOctetsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubscriberOctetsSent.setUnits("octets")
_RbnSubscriberOctetsReceived_Type = Counter64
_RbnSubscriberOctetsReceived_Object = MibTableColumn
rbnSubscriberOctetsReceived = _RbnSubscriberOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 3, 1, 1, 2),
    _RbnSubscriberOctetsReceived_Type()
)
rbnSubscriberOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubscriberOctetsReceived.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubscriberOctetsReceived.setUnits("octets")
_RbnSubscriberPktsSent_Type = Counter64
_RbnSubscriberPktsSent_Object = MibTableColumn
rbnSubscriberPktsSent = _RbnSubscriberPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 3, 1, 1, 3),
    _RbnSubscriberPktsSent_Type()
)
rbnSubscriberPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubscriberPktsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubscriberPktsSent.setUnits("packets")
_RbnSubscriberPktsReceived_Type = Counter64
_RbnSubscriberPktsReceived_Object = MibTableColumn
rbnSubscriberPktsReceived = _RbnSubscriberPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 3, 1, 1, 4),
    _RbnSubscriberPktsReceived_Type()
)
rbnSubscriberPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubscriberPktsReceived.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubscriberPktsReceived.setUnits("packets")
_RbnSubscriberXmitPktsDropped_Type = Counter32
_RbnSubscriberXmitPktsDropped_Object = MibTableColumn
rbnSubscriberXmitPktsDropped = _RbnSubscriberXmitPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 3, 1, 1, 5),
    _RbnSubscriberXmitPktsDropped_Type()
)
rbnSubscriberXmitPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubscriberXmitPktsDropped.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubscriberXmitPktsDropped.setUnits("packets")
_RbnSubscriberMcastOctetsSent_Type = Counter64
_RbnSubscriberMcastOctetsSent_Object = MibTableColumn
rbnSubscriberMcastOctetsSent = _RbnSubscriberMcastOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 3, 1, 1, 6),
    _RbnSubscriberMcastOctetsSent_Type()
)
rbnSubscriberMcastOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubscriberMcastOctetsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubscriberMcastOctetsSent.setUnits("octets")
_RbnSubscriberMcastOctetsReceived_Type = Counter64
_RbnSubscriberMcastOctetsReceived_Object = MibTableColumn
rbnSubscriberMcastOctetsReceived = _RbnSubscriberMcastOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 3, 1, 1, 7),
    _RbnSubscriberMcastOctetsReceived_Type()
)
rbnSubscriberMcastOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubscriberMcastOctetsReceived.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubscriberMcastOctetsReceived.setUnits("octets")
_RbnSubscriberMcastPktsSent_Type = Counter64
_RbnSubscriberMcastPktsSent_Object = MibTableColumn
rbnSubscriberMcastPktsSent = _RbnSubscriberMcastPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 3, 1, 1, 8),
    _RbnSubscriberMcastPktsSent_Type()
)
rbnSubscriberMcastPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubscriberMcastPktsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubscriberMcastPktsSent.setUnits("packets")
_RbnSubscriberMcastPktsReceived_Type = Counter64
_RbnSubscriberMcastPktsReceived_Object = MibTableColumn
rbnSubscriberMcastPktsReceived = _RbnSubscriberMcastPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 1, 3, 1, 1, 9),
    _RbnSubscriberMcastPktsReceived_Type()
)
rbnSubscriberMcastPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSubscriberMcastPktsReceived.setStatus("current")
if mibBuilder.loadTexts:
    rbnSubscriberMcastPktsReceived.setUnits("packets")
_RbnSubscriberMIBConformance_ObjectIdentity = ObjectIdentity
rbnSubscriberMIBConformance = _RbnSubscriberMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 2)
)
_RbnSubscriberCompliances_ObjectIdentity = ObjectIdentity
rbnSubscriberCompliances = _RbnSubscriberCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 2, 1)
)
_RbnSubscriberGroups_ObjectIdentity = ObjectIdentity
rbnSubscriberGroups = _RbnSubscriberGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 2, 2)
)
_RbnSubscriberMIBNotifications_ObjectIdentity = ObjectIdentity
rbnSubscriberMIBNotifications = _RbnSubscriberMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 3)
)
_RbnSubscriberNotificationsPrefix_ObjectIdentity = ObjectIdentity
rbnSubscriberNotificationsPrefix = _RbnSubscriberNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 3, 0)
)

# Managed Objects groups

rbnSubscriberCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 2, 2, 1)
)
rbnSubscriberCfgGroup.setObjects(
      *(("RBN-SUBSCRIBER-MIB", "rbnSubscriberBrgGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberBrgAgingTime"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberBrgPathCost"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberBrgSpanningDisabled"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberBrgTransBpdu"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberBrgInGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberBrgOutGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberMaxDHCP"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberDnsPrimaryType"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberDnsPrimary"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberDnsSecondaryType"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberDnsSecondary"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPassword"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPasswordOut"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberLimitRate"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberLimitBurst"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPoliceRate"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPoliceBurst"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPortLimit"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPppMtu"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPppCompression"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPppoeMotm"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPppoeUrl"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberAbsTimeout"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIdleTimeout"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberTunnelDomain"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberTunnelName"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpInGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpOutGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpMcastGroupMax"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpMcastRx"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpMcastSend"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpPoolValid"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpPoolName"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpSrcValidation"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpTos"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberRowStatus"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberClear"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpsecPeerName"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpsecPolicyName"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberQosInPolicyName"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberQosOutPolicyName"))
)
if mibBuilder.loadTexts:
    rbnSubscriberCfgGroup.setStatus("obsolete")

rbnSubscriberActiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 2, 2, 2)
)
rbnSubscriberActiveGroup.setObjects(
      *(("RBN-SUBSCRIBER-MIB", "rbnSubscriberActiveCircuitDescr"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberActiveStartTime"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberActiveClear"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberClearAllSpinLock"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberClearAllNextIndex"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberClearAllRowStatus"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberClearAllState"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberClearAllTime"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberTotalActiveCount"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberActiveAddr"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberActiveCount"))
)
if mibBuilder.loadTexts:
    rbnSubscriberActiveGroup.setStatus("current")

rbnSubscriberAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 2, 2, 3)
)
rbnSubscriberAddressGroup.setObjects(
      *(("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpAddressMaskLength"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpAddressRowStatus"))
)
if mibBuilder.loadTexts:
    rbnSubscriberAddressGroup.setStatus("current")

rbnSubscriberArpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 2, 2, 4)
)
rbnSubscriberArpGroup.setObjects(
      *(("RBN-SUBSCRIBER-MIB", "rbnSubscriberArpMacAddress"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberArpRowStatus"))
)
if mibBuilder.loadTexts:
    rbnSubscriberArpGroup.setStatus("current")

rbnSubscriberRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 2, 2, 5)
)
rbnSubscriberRouteGroup.setObjects(
      *(("RBN-SUBSCRIBER-MIB", "rbnSubscriberRteNextHopType"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberRteNextHop"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberRteRowStatus"))
)
if mibBuilder.loadTexts:
    rbnSubscriberRouteGroup.setStatus("current")

rbnSubscriberPppoeRteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 2, 2, 6)
)
rbnSubscriberPppoeRteGroup.setObjects(
      *(("RBN-SUBSCRIBER-MIB", "rbnSubscriberPppoeRteMetric"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPppoeRteRowStatus"))
)
if mibBuilder.loadTexts:
    rbnSubscriberPppoeRteGroup.setStatus("current")

rbnSubscriberStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 2, 2, 7)
)
rbnSubscriberStatsGroup.setObjects(
      *(("RBN-SUBSCRIBER-MIB", "rbnSubscriberOctetsSent"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberOctetsReceived"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPktsSent"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPktsReceived"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberXmitPktsDropped"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberMcastOctetsSent"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberMcastOctetsReceived"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberMcastPktsSent"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberMcastPktsReceived"))
)
if mibBuilder.loadTexts:
    rbnSubscriberStatsGroup.setStatus("current")

rbnSubscriberCfgGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 2, 2, 8)
)
rbnSubscriberCfgGroup2.setObjects(
      *(("RBN-SUBSCRIBER-MIB", "rbnSubscriberBrgGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberBrgAgingTime"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberBrgPathCost"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberBrgSpanningDisabled"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberBrgTransBpdu"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberBrgInGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberBrgOutGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberMaxDHCP"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberDnsPrimaryType"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberDnsPrimary"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberDnsSecondaryType"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberDnsSecondary"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPassword"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPasswordOut"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberLimitRate"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberLimitBurst"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPoliceRate"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPoliceBurst"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPortLimit"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPppMtu"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPppCompression"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPppoeMotm"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPppoeUrl"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberAbsTimeout"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIdleTimeout"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberTunnelDomain"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberTunnelName"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpInGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpOutGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpMcastGroupMax"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpMcastRx"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpMcastSend"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpPoolValid"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpPoolName"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpSrcValidation"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpTos"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberRowStatus"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberClear"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpsecPeerName"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpsecPolicyName"))
)
if mibBuilder.loadTexts:
    rbnSubscriberCfgGroup2.setStatus("obsolete")

rbnSubscriberCfgGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 2, 2, 9)
)
rbnSubscriberCfgGroup3.setObjects(
      *(("RBN-SUBSCRIBER-MIB", "rbnSubscriberBrgGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberBrgAgingTime"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberBrgPathCost"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberBrgSpanningDisabled"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberBrgTransBpdu"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberBrgInGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberBrgOutGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberMaxDHCP"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberDnsPrimaryType"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberDnsPrimary"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberDnsSecondaryType"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberDnsSecondary"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPassword"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPasswordOut"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberLimitRate"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberLimitBurst"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPoliceRate"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPoliceBurst"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPortLimit"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPppMtu"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPppCompression"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPppoeMotm"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPppoeUrl"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberAbsTimeout"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIdleTimeout"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberTunnelDomain"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberTunnelName"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpInGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpOutGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpMcastGroupMax"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpMcastRx"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpMcastSend"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpPoolValid"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpPoolName"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpSrcValidation"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpTos"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberRowStatus"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberClear"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpsecPeerName"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberIpsecPolicyName"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberBrgCctAddrMax"))
)
if mibBuilder.loadTexts:
    rbnSubscriberCfgGroup3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnSubscriberCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 2, 1, 1)
)
rbnSubscriberCompliance.setObjects(
      *(("RBN-SUBSCRIBER-MIB", "rbnSubscriberCfgGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberActiveGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberAddressGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberArpGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberRouteGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPppoeRteGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberStatsGroup"))
)
if mibBuilder.loadTexts:
    rbnSubscriberCompliance.setStatus(
        "obsolete"
    )

rbnSubscriberCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 2, 1, 2)
)
rbnSubscriberCompliance2.setObjects(
      *(("RBN-SUBSCRIBER-MIB", "rbnSubscriberCfgGroup2"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberActiveGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberAddressGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberArpGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberRouteGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPppoeRteGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberStatsGroup"))
)
if mibBuilder.loadTexts:
    rbnSubscriberCompliance2.setStatus(
        "obsolete"
    )

rbnSubscriberCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 9, 2, 1, 3)
)
rbnSubscriberCompliance3.setObjects(
      *(("RBN-SUBSCRIBER-MIB", "rbnSubscriberCfgGroup3"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberActiveGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberAddressGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberArpGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberRouteGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberPppoeRteGroup"),
        ("RBN-SUBSCRIBER-MIB", "rbnSubscriberStatsGroup"))
)
if mibBuilder.loadTexts:
    rbnSubscriberCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-SUBSCRIBER-MIB",
    **{"rbnSubscriberMib": rbnSubscriberMib,
       "rbnSubscriberMIBObjects": rbnSubscriberMIBObjects,
       "rbnSubscriberConfig": rbnSubscriberConfig,
       "rbnSubscriberCfgTable": rbnSubscriberCfgTable,
       "rbnSubscriberCfgEntry": rbnSubscriberCfgEntry,
       "rbnSubscriberName": rbnSubscriberName,
       "rbnSubscriberRowStatus": rbnSubscriberRowStatus,
       "rbnSubscriberBrgGroup": rbnSubscriberBrgGroup,
       "rbnSubscriberBrgAgingTime": rbnSubscriberBrgAgingTime,
       "rbnSubscriberBrgPathCost": rbnSubscriberBrgPathCost,
       "rbnSubscriberBrgSpanningDisabled": rbnSubscriberBrgSpanningDisabled,
       "rbnSubscriberBrgTransBpdu": rbnSubscriberBrgTransBpdu,
       "rbnSubscriberBrgInGroup": rbnSubscriberBrgInGroup,
       "rbnSubscriberBrgOutGroup": rbnSubscriberBrgOutGroup,
       "rbnSubscriberMaxDHCP": rbnSubscriberMaxDHCP,
       "rbnSubscriberDnsPrimaryType": rbnSubscriberDnsPrimaryType,
       "rbnSubscriberDnsPrimary": rbnSubscriberDnsPrimary,
       "rbnSubscriberDnsSecondaryType": rbnSubscriberDnsSecondaryType,
       "rbnSubscriberDnsSecondary": rbnSubscriberDnsSecondary,
       "rbnSubscriberPassword": rbnSubscriberPassword,
       "rbnSubscriberPasswordOut": rbnSubscriberPasswordOut,
       "rbnSubscriberPoliceRate": rbnSubscriberPoliceRate,
       "rbnSubscriberPoliceBurst": rbnSubscriberPoliceBurst,
       "rbnSubscriberLimitRate": rbnSubscriberLimitRate,
       "rbnSubscriberLimitBurst": rbnSubscriberLimitBurst,
       "rbnSubscriberPortLimit": rbnSubscriberPortLimit,
       "rbnSubscriberPppMtu": rbnSubscriberPppMtu,
       "rbnSubscriberPppCompression": rbnSubscriberPppCompression,
       "rbnSubscriberPppoeMotm": rbnSubscriberPppoeMotm,
       "rbnSubscriberPppoeUrl": rbnSubscriberPppoeUrl,
       "rbnSubscriberAbsTimeout": rbnSubscriberAbsTimeout,
       "rbnSubscriberIdleTimeout": rbnSubscriberIdleTimeout,
       "rbnSubscriberTunnelDomain": rbnSubscriberTunnelDomain,
       "rbnSubscriberTunnelName": rbnSubscriberTunnelName,
       "rbnSubscriberIpInGroup": rbnSubscriberIpInGroup,
       "rbnSubscriberIpOutGroup": rbnSubscriberIpOutGroup,
       "rbnSubscriberIpMcastGroupMax": rbnSubscriberIpMcastGroupMax,
       "rbnSubscriberIpMcastRx": rbnSubscriberIpMcastRx,
       "rbnSubscriberIpMcastSend": rbnSubscriberIpMcastSend,
       "rbnSubscriberIpPoolValid": rbnSubscriberIpPoolValid,
       "rbnSubscriberIpPoolName": rbnSubscriberIpPoolName,
       "rbnSubscriberIpSrcValidation": rbnSubscriberIpSrcValidation,
       "rbnSubscriberIpTos": rbnSubscriberIpTos,
       "rbnSubscriberClear": rbnSubscriberClear,
       "rbnSubscriberIpsecPeerName": rbnSubscriberIpsecPeerName,
       "rbnSubscriberIpsecPolicyName": rbnSubscriberIpsecPolicyName,
       "rbnSubscriberQosInPolicyName": rbnSubscriberQosInPolicyName,
       "rbnSubscriberQosOutPolicyName": rbnSubscriberQosOutPolicyName,
       "rbnSubscriberBrgCctAddrMax": rbnSubscriberBrgCctAddrMax,
       "rbnSubscriberIpAddressTable": rbnSubscriberIpAddressTable,
       "rbnSubscriberIpAddressEntry": rbnSubscriberIpAddressEntry,
       "rbnSubscriberIpAddressType": rbnSubscriberIpAddressType,
       "rbnSubscriberIpAddress": rbnSubscriberIpAddress,
       "rbnSubscriberIpAddressMaskLength": rbnSubscriberIpAddressMaskLength,
       "rbnSubscriberIpAddressRowStatus": rbnSubscriberIpAddressRowStatus,
       "rbnSubscriberArpTable": rbnSubscriberArpTable,
       "rbnSubscriberArpEntry": rbnSubscriberArpEntry,
       "rbnSubscriberArpAddressType": rbnSubscriberArpAddressType,
       "rbnSubscriberArpAddress": rbnSubscriberArpAddress,
       "rbnSubscriberArpMacAddress": rbnSubscriberArpMacAddress,
       "rbnSubscriberArpRowStatus": rbnSubscriberArpRowStatus,
       "rbnSubscriberRouteTable": rbnSubscriberRouteTable,
       "rbnSubscriberRouteEntry": rbnSubscriberRouteEntry,
       "rbnSubscriberRteNetworkAddrType": rbnSubscriberRteNetworkAddrType,
       "rbnSubscriberRteNetworkAddr": rbnSubscriberRteNetworkAddr,
       "rbnSubscriberRteNetworkMaskLength": rbnSubscriberRteNetworkMaskLength,
       "rbnSubscriberRteNextHopType": rbnSubscriberRteNextHopType,
       "rbnSubscriberRteNextHop": rbnSubscriberRteNextHop,
       "rbnSubscriberRteRowStatus": rbnSubscriberRteRowStatus,
       "rbnSubscriberPppoeRteTable": rbnSubscriberPppoeRteTable,
       "rbnSubscriberPppoeRteEntry": rbnSubscriberPppoeRteEntry,
       "rbnSubscriberPppoeRteAddrType": rbnSubscriberPppoeRteAddrType,
       "rbnSubscriberPppoeRteAddr": rbnSubscriberPppoeRteAddr,
       "rbnSubscriberPppoeRteMaskLength": rbnSubscriberPppoeRteMaskLength,
       "rbnSubscriberPppoeRteMetric": rbnSubscriberPppoeRteMetric,
       "rbnSubscriberPppoeRteRowStatus": rbnSubscriberPppoeRteRowStatus,
       "rbnSubscriberActive": rbnSubscriberActive,
       "rbnSubscriberActiveTable": rbnSubscriberActiveTable,
       "rbnSubscriberActiveEntry": rbnSubscriberActiveEntry,
       "rbnSubscriberActiveCircuitHandle": rbnSubscriberActiveCircuitHandle,
       "rbnSubscriberActiveCircuitDescr": rbnSubscriberActiveCircuitDescr,
       "rbnSubscriberActiveStartTime": rbnSubscriberActiveStartTime,
       "rbnSubscriberActiveClear": rbnSubscriberActiveClear,
       "rbnSubscriberActiveIpTable": rbnSubscriberActiveIpTable,
       "rbnSubscriberActiveIpEntry": rbnSubscriberActiveIpEntry,
       "rbnSubscriberActiveAddrType": rbnSubscriberActiveAddrType,
       "rbnSubscriberActiveAddr": rbnSubscriberActiveAddr,
       "rbnSubscriberClearAllSpinLock": rbnSubscriberClearAllSpinLock,
       "rbnSubscriberClearAllNextIndex": rbnSubscriberClearAllNextIndex,
       "rbnSubscriberClearAllTable": rbnSubscriberClearAllTable,
       "rbnSubscriberClearAllEntry": rbnSubscriberClearAllEntry,
       "rbnSubscriberClearAllIndex": rbnSubscriberClearAllIndex,
       "rbnSubscriberClearAllRowStatus": rbnSubscriberClearAllRowStatus,
       "rbnSubscriberClearAllState": rbnSubscriberClearAllState,
       "rbnSubscriberClearAllTime": rbnSubscriberClearAllTime,
       "rbnSubscriberTotalActiveCount": rbnSubscriberTotalActiveCount,
       "rbnSubscriberCountTable": rbnSubscriberCountTable,
       "rbnSubscriberCountEntry": rbnSubscriberCountEntry,
       "rbnSubscriberEncapsulationType": rbnSubscriberEncapsulationType,
       "rbnSubscriberActiveCount": rbnSubscriberActiveCount,
       "rbnSubscriberStats": rbnSubscriberStats,
       "rbnSubscriberStatsTable": rbnSubscriberStatsTable,
       "rbnSubscriberStatsEntry": rbnSubscriberStatsEntry,
       "rbnSubscriberOctetsSent": rbnSubscriberOctetsSent,
       "rbnSubscriberOctetsReceived": rbnSubscriberOctetsReceived,
       "rbnSubscriberPktsSent": rbnSubscriberPktsSent,
       "rbnSubscriberPktsReceived": rbnSubscriberPktsReceived,
       "rbnSubscriberXmitPktsDropped": rbnSubscriberXmitPktsDropped,
       "rbnSubscriberMcastOctetsSent": rbnSubscriberMcastOctetsSent,
       "rbnSubscriberMcastOctetsReceived": rbnSubscriberMcastOctetsReceived,
       "rbnSubscriberMcastPktsSent": rbnSubscriberMcastPktsSent,
       "rbnSubscriberMcastPktsReceived": rbnSubscriberMcastPktsReceived,
       "rbnSubscriberMIBConformance": rbnSubscriberMIBConformance,
       "rbnSubscriberCompliances": rbnSubscriberCompliances,
       "rbnSubscriberCompliance": rbnSubscriberCompliance,
       "rbnSubscriberCompliance2": rbnSubscriberCompliance2,
       "rbnSubscriberCompliance3": rbnSubscriberCompliance3,
       "rbnSubscriberGroups": rbnSubscriberGroups,
       "rbnSubscriberCfgGroup": rbnSubscriberCfgGroup,
       "rbnSubscriberActiveGroup": rbnSubscriberActiveGroup,
       "rbnSubscriberAddressGroup": rbnSubscriberAddressGroup,
       "rbnSubscriberArpGroup": rbnSubscriberArpGroup,
       "rbnSubscriberRouteGroup": rbnSubscriberRouteGroup,
       "rbnSubscriberPppoeRteGroup": rbnSubscriberPppoeRteGroup,
       "rbnSubscriberStatsGroup": rbnSubscriberStatsGroup,
       "rbnSubscriberCfgGroup2": rbnSubscriberCfgGroup2,
       "rbnSubscriberCfgGroup3": rbnSubscriberCfgGroup3,
       "rbnSubscriberMIBNotifications": rbnSubscriberMIBNotifications,
       "rbnSubscriberNotificationsPrefix": rbnSubscriberNotificationsPrefix}
)
