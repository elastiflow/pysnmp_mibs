# SNMP MIB module (ABB-MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/abb_17268/ABB-MULTICAST-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:23:57 2025
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

(hmPlatform4,) = mibBuilder.importSymbols(
    "ABB-PLATFORM4-MIB",
    "hmPlatform4")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hmPlatform4Multicast = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4)
)
if mibBuilder.loadTexts:
    hmPlatform4Multicast.setRevisions(
        ("2006-02-03 12:00",
         "2002-05-08 14:18")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HmAgentMulticastIGMPConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentMulticastIGMPConfigGroup = _HmAgentMulticastIGMPConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 1)
)


class _HmAgentMulticastIGMPAdminMode_Type(Integer32):
    """Custom type hmAgentMulticastIGMPAdminMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmAgentMulticastIGMPAdminMode_Type.__name__ = "Integer32"
_HmAgentMulticastIGMPAdminMode_Object = MibScalar
hmAgentMulticastIGMPAdminMode = _HmAgentMulticastIGMPAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 1, 1),
    _HmAgentMulticastIGMPAdminMode_Type()
)
hmAgentMulticastIGMPAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentMulticastIGMPAdminMode.setStatus("current")
_HmAgentMulticastIGMPInterfaceTable_Object = MibTable
hmAgentMulticastIGMPInterfaceTable = _HmAgentMulticastIGMPInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 1, 2)
)
if mibBuilder.loadTexts:
    hmAgentMulticastIGMPInterfaceTable.setStatus("current")
_HmAgentMulticastIGMPInterfaceEntry_Object = MibTableRow
hmAgentMulticastIGMPInterfaceEntry = _HmAgentMulticastIGMPInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 1, 2, 1)
)
hmAgentMulticastIGMPInterfaceEntry.setIndexNames(
    (0, "ABB-MULTICAST-MIB", "hmAgentMulticastIGMPInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    hmAgentMulticastIGMPInterfaceEntry.setStatus("current")
_HmAgentMulticastIGMPInterfaceIfIndex_Type = Integer32
_HmAgentMulticastIGMPInterfaceIfIndex_Object = MibTableColumn
hmAgentMulticastIGMPInterfaceIfIndex = _HmAgentMulticastIGMPInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 1, 2, 1, 1),
    _HmAgentMulticastIGMPInterfaceIfIndex_Type()
)
hmAgentMulticastIGMPInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentMulticastIGMPInterfaceIfIndex.setStatus("current")


class _HmAgentMulticastIGMPInterfaceAdminMode_Type(Integer32):
    """Custom type hmAgentMulticastIGMPInterfaceAdminMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmAgentMulticastIGMPInterfaceAdminMode_Type.__name__ = "Integer32"
_HmAgentMulticastIGMPInterfaceAdminMode_Object = MibTableColumn
hmAgentMulticastIGMPInterfaceAdminMode = _HmAgentMulticastIGMPInterfaceAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 1, 2, 1, 2),
    _HmAgentMulticastIGMPInterfaceAdminMode_Type()
)
hmAgentMulticastIGMPInterfaceAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentMulticastIGMPInterfaceAdminMode.setStatus("current")
_HmAgentMulticastPIMConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentMulticastPIMConfigGroup = _HmAgentMulticastPIMConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 2)
)


class _HmAgentMulticastPIMConfigMode_Type(Integer32):
    """Custom type hmAgentMulticastPIMConfigMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sparse", 1),
          ("dense", 2))
    )


_HmAgentMulticastPIMConfigMode_Type.__name__ = "Integer32"
_HmAgentMulticastPIMConfigMode_Object = MibScalar
hmAgentMulticastPIMConfigMode = _HmAgentMulticastPIMConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 2, 1),
    _HmAgentMulticastPIMConfigMode_Type()
)
hmAgentMulticastPIMConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentMulticastPIMConfigMode.setStatus("current")


class _HmAgentMulticastPIMPruneHoldtime_Type(Integer32):
    """Custom type hmAgentMulticastPIMPruneHoldtime based on Integer32"""
    defaultValue = 210

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 64800),
    )


_HmAgentMulticastPIMPruneHoldtime_Type.__name__ = "Integer32"
_HmAgentMulticastPIMPruneHoldtime_Object = MibScalar
hmAgentMulticastPIMPruneHoldtime = _HmAgentMulticastPIMPruneHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 2, 2),
    _HmAgentMulticastPIMPruneHoldtime_Type()
)
hmAgentMulticastPIMPruneHoldtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentMulticastPIMPruneHoldtime.setStatus("current")
_HmAgentMulticastPIMSMConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentMulticastPIMSMConfigGroup = _HmAgentMulticastPIMSMConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 3)
)


class _HmAgentMulticastPIMSMAdminMode_Type(Integer32):
    """Custom type hmAgentMulticastPIMSMAdminMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmAgentMulticastPIMSMAdminMode_Type.__name__ = "Integer32"
_HmAgentMulticastPIMSMAdminMode_Object = MibScalar
hmAgentMulticastPIMSMAdminMode = _HmAgentMulticastPIMSMAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 3, 1),
    _HmAgentMulticastPIMSMAdminMode_Type()
)
hmAgentMulticastPIMSMAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentMulticastPIMSMAdminMode.setStatus("current")


class _HmAgentMulticastPIMSMDataThresholdRate_Type(Integer32):
    """Custom type hmAgentMulticastPIMSMDataThresholdRate based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_HmAgentMulticastPIMSMDataThresholdRate_Type.__name__ = "Integer32"
_HmAgentMulticastPIMSMDataThresholdRate_Object = MibScalar
hmAgentMulticastPIMSMDataThresholdRate = _HmAgentMulticastPIMSMDataThresholdRate_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 3, 2),
    _HmAgentMulticastPIMSMDataThresholdRate_Type()
)
hmAgentMulticastPIMSMDataThresholdRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentMulticastPIMSMDataThresholdRate.setStatus("current")


class _HmAgentMulticastPIMSMRegThresholdRate_Type(Integer32):
    """Custom type hmAgentMulticastPIMSMRegThresholdRate based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_HmAgentMulticastPIMSMRegThresholdRate_Type.__name__ = "Integer32"
_HmAgentMulticastPIMSMRegThresholdRate_Object = MibScalar
hmAgentMulticastPIMSMRegThresholdRate = _HmAgentMulticastPIMSMRegThresholdRate_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 3, 3),
    _HmAgentMulticastPIMSMRegThresholdRate_Type()
)
hmAgentMulticastPIMSMRegThresholdRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentMulticastPIMSMRegThresholdRate.setStatus("current")
_HmAgentMulticastPIMSMStaticRPTable_Object = MibTable
hmAgentMulticastPIMSMStaticRPTable = _HmAgentMulticastPIMSMStaticRPTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 3, 4)
)
if mibBuilder.loadTexts:
    hmAgentMulticastPIMSMStaticRPTable.setStatus("current")
_HmAgentMulticastPIMSMStaticRPEntry_Object = MibTableRow
hmAgentMulticastPIMSMStaticRPEntry = _HmAgentMulticastPIMSMStaticRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 3, 4, 1)
)
hmAgentMulticastPIMSMStaticRPEntry.setIndexNames(
    (0, "ABB-MULTICAST-MIB", "hmAgentMulticastPIMSMStaticRPIpAddr"),
    (0, "ABB-MULTICAST-MIB", "hmAgentMulticastPIMSMStaticRPGroupIpAddr"),
    (0, "ABB-MULTICAST-MIB", "hmAgentMulticastPIMSMStaticRPGroupIpMask"),
)
if mibBuilder.loadTexts:
    hmAgentMulticastPIMSMStaticRPEntry.setStatus("current")
_HmAgentMulticastPIMSMStaticRPIpAddr_Type = IpAddress
_HmAgentMulticastPIMSMStaticRPIpAddr_Object = MibTableColumn
hmAgentMulticastPIMSMStaticRPIpAddr = _HmAgentMulticastPIMSMStaticRPIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 3, 4, 1, 1),
    _HmAgentMulticastPIMSMStaticRPIpAddr_Type()
)
hmAgentMulticastPIMSMStaticRPIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmAgentMulticastPIMSMStaticRPIpAddr.setStatus("current")
_HmAgentMulticastPIMSMStaticRPGroupIpAddr_Type = IpAddress
_HmAgentMulticastPIMSMStaticRPGroupIpAddr_Object = MibTableColumn
hmAgentMulticastPIMSMStaticRPGroupIpAddr = _HmAgentMulticastPIMSMStaticRPGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 3, 4, 1, 2),
    _HmAgentMulticastPIMSMStaticRPGroupIpAddr_Type()
)
hmAgentMulticastPIMSMStaticRPGroupIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmAgentMulticastPIMSMStaticRPGroupIpAddr.setStatus("current")
_HmAgentMulticastPIMSMStaticRPGroupIpMask_Type = IpAddress
_HmAgentMulticastPIMSMStaticRPGroupIpMask_Object = MibTableColumn
hmAgentMulticastPIMSMStaticRPGroupIpMask = _HmAgentMulticastPIMSMStaticRPGroupIpMask_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 3, 4, 1, 3),
    _HmAgentMulticastPIMSMStaticRPGroupIpMask_Type()
)
hmAgentMulticastPIMSMStaticRPGroupIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmAgentMulticastPIMSMStaticRPGroupIpMask.setStatus("current")
_HmAgentMulticastPIMSMStaticRPStatus_Type = RowStatus
_HmAgentMulticastPIMSMStaticRPStatus_Object = MibTableColumn
hmAgentMulticastPIMSMStaticRPStatus = _HmAgentMulticastPIMSMStaticRPStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 3, 4, 1, 4),
    _HmAgentMulticastPIMSMStaticRPStatus_Type()
)
hmAgentMulticastPIMSMStaticRPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmAgentMulticastPIMSMStaticRPStatus.setStatus("current")
_HmAgentMulticastPIMSMInterfaceTable_Object = MibTable
hmAgentMulticastPIMSMInterfaceTable = _HmAgentMulticastPIMSMInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 3, 5)
)
if mibBuilder.loadTexts:
    hmAgentMulticastPIMSMInterfaceTable.setStatus("current")
_HmAgentMulticastPIMSMInterfaceEntry_Object = MibTableRow
hmAgentMulticastPIMSMInterfaceEntry = _HmAgentMulticastPIMSMInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 3, 5, 1)
)
hmAgentMulticastPIMSMInterfaceEntry.setIndexNames(
    (0, "ABB-MULTICAST-MIB", "hmAgentMulticastPIMSMInterfaceIndex"),
)
if mibBuilder.loadTexts:
    hmAgentMulticastPIMSMInterfaceEntry.setStatus("current")
_HmAgentMulticastPIMSMInterfaceIndex_Type = Unsigned32
_HmAgentMulticastPIMSMInterfaceIndex_Object = MibTableColumn
hmAgentMulticastPIMSMInterfaceIndex = _HmAgentMulticastPIMSMInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 3, 5, 1, 1),
    _HmAgentMulticastPIMSMInterfaceIndex_Type()
)
hmAgentMulticastPIMSMInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmAgentMulticastPIMSMInterfaceIndex.setStatus("current")


class _HmAgentMulticastPIMSMInterfaceCBSRHashMaskLength_Type(Unsigned32):
    """Custom type hmAgentMulticastPIMSMInterfaceCBSRHashMaskLength based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_HmAgentMulticastPIMSMInterfaceCBSRHashMaskLength_Type.__name__ = "Unsigned32"
_HmAgentMulticastPIMSMInterfaceCBSRHashMaskLength_Object = MibTableColumn
hmAgentMulticastPIMSMInterfaceCBSRHashMaskLength = _HmAgentMulticastPIMSMInterfaceCBSRHashMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 3, 5, 1, 2),
    _HmAgentMulticastPIMSMInterfaceCBSRHashMaskLength_Type()
)
hmAgentMulticastPIMSMInterfaceCBSRHashMaskLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentMulticastPIMSMInterfaceCBSRHashMaskLength.setStatus("current")


class _HmAgentMulticastPIMSMInterfaceCRPPreference_Type(Integer32):
    """Custom type hmAgentMulticastPIMSMInterfaceCRPPreference based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_HmAgentMulticastPIMSMInterfaceCRPPreference_Type.__name__ = "Integer32"
_HmAgentMulticastPIMSMInterfaceCRPPreference_Object = MibTableColumn
hmAgentMulticastPIMSMInterfaceCRPPreference = _HmAgentMulticastPIMSMInterfaceCRPPreference_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 3, 5, 1, 3),
    _HmAgentMulticastPIMSMInterfaceCRPPreference_Type()
)
hmAgentMulticastPIMSMInterfaceCRPPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentMulticastPIMSMInterfaceCRPPreference.setStatus("current")
_HmAgentMulticastPIMDMConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentMulticastPIMDMConfigGroup = _HmAgentMulticastPIMDMConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 4)
)


class _HmAgentMulticastPIMDMAdminMode_Type(Integer32):
    """Custom type hmAgentMulticastPIMDMAdminMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmAgentMulticastPIMDMAdminMode_Type.__name__ = "Integer32"
_HmAgentMulticastPIMDMAdminMode_Object = MibScalar
hmAgentMulticastPIMDMAdminMode = _HmAgentMulticastPIMDMAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 4, 1),
    _HmAgentMulticastPIMDMAdminMode_Type()
)
hmAgentMulticastPIMDMAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentMulticastPIMDMAdminMode.setStatus("current")
_HmAgentMulticastRoutingConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentMulticastRoutingConfigGroup = _HmAgentMulticastRoutingConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 5)
)


class _HmAgentMulticastRoutingAdminMode_Type(Integer32):
    """Custom type hmAgentMulticastRoutingAdminMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmAgentMulticastRoutingAdminMode_Type.__name__ = "Integer32"
_HmAgentMulticastRoutingAdminMode_Object = MibScalar
hmAgentMulticastRoutingAdminMode = _HmAgentMulticastRoutingAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 5, 1),
    _HmAgentMulticastRoutingAdminMode_Type()
)
hmAgentMulticastRoutingAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentMulticastRoutingAdminMode.setStatus("current")
_HmAgentMulticastDVMRPConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentMulticastDVMRPConfigGroup = _HmAgentMulticastDVMRPConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 6)
)


class _HmAgentMulticastDVMRPAdminMode_Type(Integer32):
    """Custom type hmAgentMulticastDVMRPAdminMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmAgentMulticastDVMRPAdminMode_Type.__name__ = "Integer32"
_HmAgentMulticastDVMRPAdminMode_Object = MibScalar
hmAgentMulticastDVMRPAdminMode = _HmAgentMulticastDVMRPAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 6, 1),
    _HmAgentMulticastDVMRPAdminMode_Type()
)
hmAgentMulticastDVMRPAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentMulticastDVMRPAdminMode.setStatus("current")
_HmAgentSnmpTrapFlagsConfigGroupMulticast_ObjectIdentity = ObjectIdentity
hmAgentSnmpTrapFlagsConfigGroupMulticast = _HmAgentSnmpTrapFlagsConfigGroupMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 7)
)


class _HmAgentSnmpDVMRPTrapFlag_Type(Integer32):
    """Custom type hmAgentSnmpDVMRPTrapFlag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmAgentSnmpDVMRPTrapFlag_Type.__name__ = "Integer32"
_HmAgentSnmpDVMRPTrapFlag_Object = MibScalar
hmAgentSnmpDVMRPTrapFlag = _HmAgentSnmpDVMRPTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 7, 1),
    _HmAgentSnmpDVMRPTrapFlag_Type()
)
hmAgentSnmpDVMRPTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSnmpDVMRPTrapFlag.setStatus("current")


class _HmAgentSnmpPIMTrapFlag_Type(Integer32):
    """Custom type hmAgentSnmpPIMTrapFlag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmAgentSnmpPIMTrapFlag_Type.__name__ = "Integer32"
_HmAgentSnmpPIMTrapFlag_Object = MibScalar
hmAgentSnmpPIMTrapFlag = _HmAgentSnmpPIMTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 15, 4, 7, 2),
    _HmAgentSnmpPIMTrapFlag_Type()
)
hmAgentSnmpPIMTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSnmpPIMTrapFlag.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ABB-MULTICAST-MIB",
    **{"hmPlatform4Multicast": hmPlatform4Multicast,
       "hmAgentMulticastIGMPConfigGroup": hmAgentMulticastIGMPConfigGroup,
       "hmAgentMulticastIGMPAdminMode": hmAgentMulticastIGMPAdminMode,
       "hmAgentMulticastIGMPInterfaceTable": hmAgentMulticastIGMPInterfaceTable,
       "hmAgentMulticastIGMPInterfaceEntry": hmAgentMulticastIGMPInterfaceEntry,
       "hmAgentMulticastIGMPInterfaceIfIndex": hmAgentMulticastIGMPInterfaceIfIndex,
       "hmAgentMulticastIGMPInterfaceAdminMode": hmAgentMulticastIGMPInterfaceAdminMode,
       "hmAgentMulticastPIMConfigGroup": hmAgentMulticastPIMConfigGroup,
       "hmAgentMulticastPIMConfigMode": hmAgentMulticastPIMConfigMode,
       "hmAgentMulticastPIMPruneHoldtime": hmAgentMulticastPIMPruneHoldtime,
       "hmAgentMulticastPIMSMConfigGroup": hmAgentMulticastPIMSMConfigGroup,
       "hmAgentMulticastPIMSMAdminMode": hmAgentMulticastPIMSMAdminMode,
       "hmAgentMulticastPIMSMDataThresholdRate": hmAgentMulticastPIMSMDataThresholdRate,
       "hmAgentMulticastPIMSMRegThresholdRate": hmAgentMulticastPIMSMRegThresholdRate,
       "hmAgentMulticastPIMSMStaticRPTable": hmAgentMulticastPIMSMStaticRPTable,
       "hmAgentMulticastPIMSMStaticRPEntry": hmAgentMulticastPIMSMStaticRPEntry,
       "hmAgentMulticastPIMSMStaticRPIpAddr": hmAgentMulticastPIMSMStaticRPIpAddr,
       "hmAgentMulticastPIMSMStaticRPGroupIpAddr": hmAgentMulticastPIMSMStaticRPGroupIpAddr,
       "hmAgentMulticastPIMSMStaticRPGroupIpMask": hmAgentMulticastPIMSMStaticRPGroupIpMask,
       "hmAgentMulticastPIMSMStaticRPStatus": hmAgentMulticastPIMSMStaticRPStatus,
       "hmAgentMulticastPIMSMInterfaceTable": hmAgentMulticastPIMSMInterfaceTable,
       "hmAgentMulticastPIMSMInterfaceEntry": hmAgentMulticastPIMSMInterfaceEntry,
       "hmAgentMulticastPIMSMInterfaceIndex": hmAgentMulticastPIMSMInterfaceIndex,
       "hmAgentMulticastPIMSMInterfaceCBSRHashMaskLength": hmAgentMulticastPIMSMInterfaceCBSRHashMaskLength,
       "hmAgentMulticastPIMSMInterfaceCRPPreference": hmAgentMulticastPIMSMInterfaceCRPPreference,
       "hmAgentMulticastPIMDMConfigGroup": hmAgentMulticastPIMDMConfigGroup,
       "hmAgentMulticastPIMDMAdminMode": hmAgentMulticastPIMDMAdminMode,
       "hmAgentMulticastRoutingConfigGroup": hmAgentMulticastRoutingConfigGroup,
       "hmAgentMulticastRoutingAdminMode": hmAgentMulticastRoutingAdminMode,
       "hmAgentMulticastDVMRPConfigGroup": hmAgentMulticastDVMRPConfigGroup,
       "hmAgentMulticastDVMRPAdminMode": hmAgentMulticastDVMRPAdminMode,
       "hmAgentSnmpTrapFlagsConfigGroupMulticast": hmAgentSnmpTrapFlagsConfigGroupMulticast,
       "hmAgentSnmpDVMRPTrapFlag": hmAgentSnmpDVMRPTrapFlag,
       "hmAgentSnmpPIMTrapFlag": hmAgentSnmpPIMTrapFlag}
)
