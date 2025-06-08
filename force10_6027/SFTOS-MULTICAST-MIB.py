# SNMP MIB module (SFTOS-MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/force10_6027/SFTOS-MULTICAST-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:18:01 2025
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

(sFTOS,) = mibBuilder.importSymbols(
    "FORCE10-REF-MIB",
    "sFTOS")

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

sFTOSMulticast = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    sFTOSMulticast.setRevisions(
        ("2005-02-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentMulticastIGMPConfigGroup_ObjectIdentity = ObjectIdentity
agentMulticastIGMPConfigGroup = _AgentMulticastIGMPConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 1)
)


class _AgentMulticastIGMPAdminMode_Type(Integer32):
    """Custom type agentMulticastIGMPAdminMode based on Integer32"""
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


_AgentMulticastIGMPAdminMode_Type.__name__ = "Integer32"
_AgentMulticastIGMPAdminMode_Object = MibScalar
agentMulticastIGMPAdminMode = _AgentMulticastIGMPAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 1, 1),
    _AgentMulticastIGMPAdminMode_Type()
)
agentMulticastIGMPAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastIGMPAdminMode.setStatus("current")
_AgentMulticastIGMPInterfaceTable_Object = MibTable
agentMulticastIGMPInterfaceTable = _AgentMulticastIGMPInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    agentMulticastIGMPInterfaceTable.setStatus("current")
_AgentMulticastIGMPInterfaceEntry_Object = MibTableRow
agentMulticastIGMPInterfaceEntry = _AgentMulticastIGMPInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 1, 2, 1)
)
agentMulticastIGMPInterfaceEntry.setIndexNames(
    (0, "SFTOS-MULTICAST-MIB", "agentMulticastIGMPInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    agentMulticastIGMPInterfaceEntry.setStatus("current")
_AgentMulticastIGMPInterfaceIfIndex_Type = Integer32
_AgentMulticastIGMPInterfaceIfIndex_Object = MibTableColumn
agentMulticastIGMPInterfaceIfIndex = _AgentMulticastIGMPInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 1, 2, 1, 1),
    _AgentMulticastIGMPInterfaceIfIndex_Type()
)
agentMulticastIGMPInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMulticastIGMPInterfaceIfIndex.setStatus("current")


class _AgentMulticastIGMPInterfaceAdminMode_Type(Integer32):
    """Custom type agentMulticastIGMPInterfaceAdminMode based on Integer32"""
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


_AgentMulticastIGMPInterfaceAdminMode_Type.__name__ = "Integer32"
_AgentMulticastIGMPInterfaceAdminMode_Object = MibTableColumn
agentMulticastIGMPInterfaceAdminMode = _AgentMulticastIGMPInterfaceAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 1, 2, 1, 2),
    _AgentMulticastIGMPInterfaceAdminMode_Type()
)
agentMulticastIGMPInterfaceAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastIGMPInterfaceAdminMode.setStatus("current")
_AgentMulticastPIMConfigGroup_ObjectIdentity = ObjectIdentity
agentMulticastPIMConfigGroup = _AgentMulticastPIMConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 2)
)


class _AgentMulticastPIMConfigMode_Type(Integer32):
    """Custom type agentMulticastPIMConfigMode based on Integer32"""
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


_AgentMulticastPIMConfigMode_Type.__name__ = "Integer32"
_AgentMulticastPIMConfigMode_Object = MibScalar
agentMulticastPIMConfigMode = _AgentMulticastPIMConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 2, 1),
    _AgentMulticastPIMConfigMode_Type()
)
agentMulticastPIMConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastPIMConfigMode.setStatus("current")
_AgentMulticastPIMSMConfigGroup_ObjectIdentity = ObjectIdentity
agentMulticastPIMSMConfigGroup = _AgentMulticastPIMSMConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 3)
)


class _AgentMulticastPIMSMAdminMode_Type(Integer32):
    """Custom type agentMulticastPIMSMAdminMode based on Integer32"""
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


_AgentMulticastPIMSMAdminMode_Type.__name__ = "Integer32"
_AgentMulticastPIMSMAdminMode_Object = MibScalar
agentMulticastPIMSMAdminMode = _AgentMulticastPIMSMAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 3, 1),
    _AgentMulticastPIMSMAdminMode_Type()
)
agentMulticastPIMSMAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastPIMSMAdminMode.setStatus("current")


class _AgentMulticastPIMSMDataThresholdRate_Type(Integer32):
    """Custom type agentMulticastPIMSMDataThresholdRate based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_AgentMulticastPIMSMDataThresholdRate_Type.__name__ = "Integer32"
_AgentMulticastPIMSMDataThresholdRate_Object = MibScalar
agentMulticastPIMSMDataThresholdRate = _AgentMulticastPIMSMDataThresholdRate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 3, 2),
    _AgentMulticastPIMSMDataThresholdRate_Type()
)
agentMulticastPIMSMDataThresholdRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastPIMSMDataThresholdRate.setStatus("current")


class _AgentMulticastPIMSMRegThresholdRate_Type(Integer32):
    """Custom type agentMulticastPIMSMRegThresholdRate based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_AgentMulticastPIMSMRegThresholdRate_Type.__name__ = "Integer32"
_AgentMulticastPIMSMRegThresholdRate_Object = MibScalar
agentMulticastPIMSMRegThresholdRate = _AgentMulticastPIMSMRegThresholdRate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 3, 3),
    _AgentMulticastPIMSMRegThresholdRate_Type()
)
agentMulticastPIMSMRegThresholdRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastPIMSMRegThresholdRate.setStatus("current")
_AgentMulticastPIMSMStaticRPTable_Object = MibTable
agentMulticastPIMSMStaticRPTable = _AgentMulticastPIMSMStaticRPTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 3, 4)
)
if mibBuilder.loadTexts:
    agentMulticastPIMSMStaticRPTable.setStatus("current")
_AgentMulticastPIMSMStaticRPEntry_Object = MibTableRow
agentMulticastPIMSMStaticRPEntry = _AgentMulticastPIMSMStaticRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 3, 4, 1)
)
agentMulticastPIMSMStaticRPEntry.setIndexNames(
    (0, "SFTOS-MULTICAST-MIB", "agentMulticastPIMSMStaticRPIpAddr"),
    (0, "SFTOS-MULTICAST-MIB", "agentMulticastPIMSMStaticRPGroupIpAddr"),
    (0, "SFTOS-MULTICAST-MIB", "agentMulticastPIMSMStaticRPGroupIpMask"),
)
if mibBuilder.loadTexts:
    agentMulticastPIMSMStaticRPEntry.setStatus("current")
_AgentMulticastPIMSMStaticRPIpAddr_Type = IpAddress
_AgentMulticastPIMSMStaticRPIpAddr_Object = MibTableColumn
agentMulticastPIMSMStaticRPIpAddr = _AgentMulticastPIMSMStaticRPIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 3, 4, 1, 1),
    _AgentMulticastPIMSMStaticRPIpAddr_Type()
)
agentMulticastPIMSMStaticRPIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentMulticastPIMSMStaticRPIpAddr.setStatus("current")
_AgentMulticastPIMSMStaticRPGroupIpAddr_Type = IpAddress
_AgentMulticastPIMSMStaticRPGroupIpAddr_Object = MibTableColumn
agentMulticastPIMSMStaticRPGroupIpAddr = _AgentMulticastPIMSMStaticRPGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 3, 4, 1, 2),
    _AgentMulticastPIMSMStaticRPGroupIpAddr_Type()
)
agentMulticastPIMSMStaticRPGroupIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentMulticastPIMSMStaticRPGroupIpAddr.setStatus("current")
_AgentMulticastPIMSMStaticRPGroupIpMask_Type = IpAddress
_AgentMulticastPIMSMStaticRPGroupIpMask_Object = MibTableColumn
agentMulticastPIMSMStaticRPGroupIpMask = _AgentMulticastPIMSMStaticRPGroupIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 3, 4, 1, 3),
    _AgentMulticastPIMSMStaticRPGroupIpMask_Type()
)
agentMulticastPIMSMStaticRPGroupIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentMulticastPIMSMStaticRPGroupIpMask.setStatus("current")
_AgentMulticastPIMSMStaticRPStatus_Type = RowStatus
_AgentMulticastPIMSMStaticRPStatus_Object = MibTableColumn
agentMulticastPIMSMStaticRPStatus = _AgentMulticastPIMSMStaticRPStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 3, 4, 1, 4),
    _AgentMulticastPIMSMStaticRPStatus_Type()
)
agentMulticastPIMSMStaticRPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastPIMSMStaticRPStatus.setStatus("current")
_AgentMulticastPIMSMInterfaceTable_Object = MibTable
agentMulticastPIMSMInterfaceTable = _AgentMulticastPIMSMInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 3, 5)
)
if mibBuilder.loadTexts:
    agentMulticastPIMSMInterfaceTable.setStatus("current")
_AgentMulticastPIMSMInterfaceEntry_Object = MibTableRow
agentMulticastPIMSMInterfaceEntry = _AgentMulticastPIMSMInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 3, 5, 1)
)
agentMulticastPIMSMInterfaceEntry.setIndexNames(
    (0, "SFTOS-MULTICAST-MIB", "agentMulticastPIMSMInterfaceIndex"),
)
if mibBuilder.loadTexts:
    agentMulticastPIMSMInterfaceEntry.setStatus("current")
_AgentMulticastPIMSMInterfaceIndex_Type = Unsigned32
_AgentMulticastPIMSMInterfaceIndex_Object = MibTableColumn
agentMulticastPIMSMInterfaceIndex = _AgentMulticastPIMSMInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 3, 5, 1, 1),
    _AgentMulticastPIMSMInterfaceIndex_Type()
)
agentMulticastPIMSMInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentMulticastPIMSMInterfaceIndex.setStatus("current")


class _AgentMulticastPIMSMInterfaceCBSRHashMaskLength_Type(Unsigned32):
    """Custom type agentMulticastPIMSMInterfaceCBSRHashMaskLength based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AgentMulticastPIMSMInterfaceCBSRHashMaskLength_Type.__name__ = "Unsigned32"
_AgentMulticastPIMSMInterfaceCBSRHashMaskLength_Object = MibTableColumn
agentMulticastPIMSMInterfaceCBSRHashMaskLength = _AgentMulticastPIMSMInterfaceCBSRHashMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 3, 5, 1, 2),
    _AgentMulticastPIMSMInterfaceCBSRHashMaskLength_Type()
)
agentMulticastPIMSMInterfaceCBSRHashMaskLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastPIMSMInterfaceCBSRHashMaskLength.setStatus("current")


class _AgentMulticastPIMSMInterfaceCRPPreference_Type(Integer32):
    """Custom type agentMulticastPIMSMInterfaceCRPPreference based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_AgentMulticastPIMSMInterfaceCRPPreference_Type.__name__ = "Integer32"
_AgentMulticastPIMSMInterfaceCRPPreference_Object = MibTableColumn
agentMulticastPIMSMInterfaceCRPPreference = _AgentMulticastPIMSMInterfaceCRPPreference_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 3, 5, 1, 3),
    _AgentMulticastPIMSMInterfaceCRPPreference_Type()
)
agentMulticastPIMSMInterfaceCRPPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastPIMSMInterfaceCRPPreference.setStatus("current")
_AgentMulticastPIMDMConfigGroup_ObjectIdentity = ObjectIdentity
agentMulticastPIMDMConfigGroup = _AgentMulticastPIMDMConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 4)
)


class _AgentMulticastPIMDMAdminMode_Type(Integer32):
    """Custom type agentMulticastPIMDMAdminMode based on Integer32"""
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


_AgentMulticastPIMDMAdminMode_Type.__name__ = "Integer32"
_AgentMulticastPIMDMAdminMode_Object = MibScalar
agentMulticastPIMDMAdminMode = _AgentMulticastPIMDMAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 4, 1),
    _AgentMulticastPIMDMAdminMode_Type()
)
agentMulticastPIMDMAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastPIMDMAdminMode.setStatus("current")
_AgentMulticastRoutingConfigGroup_ObjectIdentity = ObjectIdentity
agentMulticastRoutingConfigGroup = _AgentMulticastRoutingConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 5)
)


class _AgentMulticastRoutingAdminMode_Type(Integer32):
    """Custom type agentMulticastRoutingAdminMode based on Integer32"""
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


_AgentMulticastRoutingAdminMode_Type.__name__ = "Integer32"
_AgentMulticastRoutingAdminMode_Object = MibScalar
agentMulticastRoutingAdminMode = _AgentMulticastRoutingAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 5, 1),
    _AgentMulticastRoutingAdminMode_Type()
)
agentMulticastRoutingAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastRoutingAdminMode.setStatus("current")
_AgentMulticastDVMRPConfigGroup_ObjectIdentity = ObjectIdentity
agentMulticastDVMRPConfigGroup = _AgentMulticastDVMRPConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 6)
)


class _AgentMulticastDVMRPAdminMode_Type(Integer32):
    """Custom type agentMulticastDVMRPAdminMode based on Integer32"""
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


_AgentMulticastDVMRPAdminMode_Type.__name__ = "Integer32"
_AgentMulticastDVMRPAdminMode_Object = MibScalar
agentMulticastDVMRPAdminMode = _AgentMulticastDVMRPAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 6, 1),
    _AgentMulticastDVMRPAdminMode_Type()
)
agentMulticastDVMRPAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastDVMRPAdminMode.setStatus("current")
_AgentSnmpTrapFlagsConfigGroupMulticast_ObjectIdentity = ObjectIdentity
agentSnmpTrapFlagsConfigGroupMulticast = _AgentSnmpTrapFlagsConfigGroupMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 7)
)


class _AgentSnmpDVMRPTrapFlag_Type(Integer32):
    """Custom type agentSnmpDVMRPTrapFlag based on Integer32"""
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


_AgentSnmpDVMRPTrapFlag_Type.__name__ = "Integer32"
_AgentSnmpDVMRPTrapFlag_Object = MibScalar
agentSnmpDVMRPTrapFlag = _AgentSnmpDVMRPTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 7, 1),
    _AgentSnmpDVMRPTrapFlag_Type()
)
agentSnmpDVMRPTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpDVMRPTrapFlag.setStatus("current")


class _AgentSnmpPIMTrapFlag_Type(Integer32):
    """Custom type agentSnmpPIMTrapFlag based on Integer32"""
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


_AgentSnmpPIMTrapFlag_Type.__name__ = "Integer32"
_AgentSnmpPIMTrapFlag_Object = MibScalar
agentSnmpPIMTrapFlag = _AgentSnmpPIMTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 4, 7, 2),
    _AgentSnmpPIMTrapFlag_Type()
)
agentSnmpPIMTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpPIMTrapFlag.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SFTOS-MULTICAST-MIB",
    **{"sFTOSMulticast": sFTOSMulticast,
       "agentMulticastIGMPConfigGroup": agentMulticastIGMPConfigGroup,
       "agentMulticastIGMPAdminMode": agentMulticastIGMPAdminMode,
       "agentMulticastIGMPInterfaceTable": agentMulticastIGMPInterfaceTable,
       "agentMulticastIGMPInterfaceEntry": agentMulticastIGMPInterfaceEntry,
       "agentMulticastIGMPInterfaceIfIndex": agentMulticastIGMPInterfaceIfIndex,
       "agentMulticastIGMPInterfaceAdminMode": agentMulticastIGMPInterfaceAdminMode,
       "agentMulticastPIMConfigGroup": agentMulticastPIMConfigGroup,
       "agentMulticastPIMConfigMode": agentMulticastPIMConfigMode,
       "agentMulticastPIMSMConfigGroup": agentMulticastPIMSMConfigGroup,
       "agentMulticastPIMSMAdminMode": agentMulticastPIMSMAdminMode,
       "agentMulticastPIMSMDataThresholdRate": agentMulticastPIMSMDataThresholdRate,
       "agentMulticastPIMSMRegThresholdRate": agentMulticastPIMSMRegThresholdRate,
       "agentMulticastPIMSMStaticRPTable": agentMulticastPIMSMStaticRPTable,
       "agentMulticastPIMSMStaticRPEntry": agentMulticastPIMSMStaticRPEntry,
       "agentMulticastPIMSMStaticRPIpAddr": agentMulticastPIMSMStaticRPIpAddr,
       "agentMulticastPIMSMStaticRPGroupIpAddr": agentMulticastPIMSMStaticRPGroupIpAddr,
       "agentMulticastPIMSMStaticRPGroupIpMask": agentMulticastPIMSMStaticRPGroupIpMask,
       "agentMulticastPIMSMStaticRPStatus": agentMulticastPIMSMStaticRPStatus,
       "agentMulticastPIMSMInterfaceTable": agentMulticastPIMSMInterfaceTable,
       "agentMulticastPIMSMInterfaceEntry": agentMulticastPIMSMInterfaceEntry,
       "agentMulticastPIMSMInterfaceIndex": agentMulticastPIMSMInterfaceIndex,
       "agentMulticastPIMSMInterfaceCBSRHashMaskLength": agentMulticastPIMSMInterfaceCBSRHashMaskLength,
       "agentMulticastPIMSMInterfaceCRPPreference": agentMulticastPIMSMInterfaceCRPPreference,
       "agentMulticastPIMDMConfigGroup": agentMulticastPIMDMConfigGroup,
       "agentMulticastPIMDMAdminMode": agentMulticastPIMDMAdminMode,
       "agentMulticastRoutingConfigGroup": agentMulticastRoutingConfigGroup,
       "agentMulticastRoutingAdminMode": agentMulticastRoutingAdminMode,
       "agentMulticastDVMRPConfigGroup": agentMulticastDVMRPConfigGroup,
       "agentMulticastDVMRPAdminMode": agentMulticastDVMRPAdminMode,
       "agentSnmpTrapFlagsConfigGroupMulticast": agentSnmpTrapFlagsConfigGroupMulticast,
       "agentSnmpDVMRPTrapFlag": agentSnmpDVMRPTrapFlag,
       "agentSnmpPIMTrapFlag": agentSnmpPIMTrapFlag}
)
