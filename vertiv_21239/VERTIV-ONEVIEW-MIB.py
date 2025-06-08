# SNMP MIB module (VERTIV-ONEVIEW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/vertiv_21239/VERTIV-ONEVIEW-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 20:17:19 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

vertiv = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21239)
)
if mibBuilder.loadTexts:
    vertiv.setRevisions(
        ("2018-06-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Oneview_ObjectIdentity = ObjectIdentity
oneview = _Oneview_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 43)
)
_HostTable_Object = MibTable
hostTable = _HostTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 1)
)
if mibBuilder.loadTexts:
    hostTable.setStatus("current")
_HostEntry_Object = MibTableRow
hostEntry = _HostEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 1, 1)
)
hostEntry.setIndexNames(
    (0, "VERTIV-ONEVIEW-MIB", "hostIndex"),
)
if mibBuilder.loadTexts:
    hostEntry.setStatus("current")


class _HostIndex_Type(Integer32):
    """Custom type hostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HostIndex_Type.__name__ = "Integer32"
_HostIndex_Object = MibTableColumn
hostIndex = _HostIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 1, 1, 1),
    _HostIndex_Type()
)
hostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hostIndex.setStatus("current")
_HostId_Type = OctetString
_HostId_Object = MibTableColumn
hostId = _HostId_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 1, 1, 2),
    _HostId_Type()
)
hostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostId.setStatus("current")


class _HostState_Type(Integer32):
    """Custom type hostState based on Integer32"""
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
        *(("idle", 1),
          ("discovered", 2),
          ("partiallyUnavailable", 3),
          ("unresponsive", 4),
          ("unknown", 5))
    )


_HostState_Type.__name__ = "Integer32"
_HostState_Object = MibTableColumn
hostState = _HostState_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 1, 1, 3),
    _HostState_Type()
)
hostState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostState.setStatus("current")


class _HostType_Type(Integer32):
    """Custom type hostType based on Integer32"""
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
        *(("pdu", 1),
          ("environmental", 2),
          ("ups", 3),
          ("cooling", 4),
          ("unknown", 5))
    )


_HostType_Type.__name__ = "Integer32"
_HostType_Object = MibTableColumn
hostType = _HostType_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 1, 1, 4),
    _HostType_Type()
)
hostType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostType.setStatus("current")


class _HostGroupIndex_Type(Integer32):
    """Custom type hostGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HostGroupIndex_Type.__name__ = "Integer32"
_HostGroupIndex_Object = MibTableColumn
hostGroupIndex = _HostGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 1, 1, 5),
    _HostGroupIndex_Type()
)
hostGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostGroupIndex.setStatus("current")


class _HostGroupName_Type(SnmpAdminString):
    """Custom type hostGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_HostGroupName_Type.__name__ = "SnmpAdminString"
_HostGroupName_Object = MibTableColumn
hostGroupName = _HostGroupName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 1, 1, 6),
    _HostGroupName_Type()
)
hostGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostGroupName.setStatus("current")


class _HostPortWeb_Type(Integer32):
    """Custom type hostPortWeb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_HostPortWeb_Type.__name__ = "Integer32"
_HostPortWeb_Object = MibTableColumn
hostPortWeb = _HostPortWeb_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 1, 1, 7),
    _HostPortWeb_Type()
)
hostPortWeb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostPortWeb.setStatus("current")


class _HostPortSnmp_Type(Integer32):
    """Custom type hostPortSnmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_HostPortSnmp_Type.__name__ = "Integer32"
_HostPortSnmp_Object = MibTableColumn
hostPortSnmp = _HostPortSnmp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 1, 1, 8),
    _HostPortSnmp_Type()
)
hostPortSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostPortSnmp.setStatus("current")
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2)
)
_GroupTable_Object = MibTable
groupTable = _GroupTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 1)
)
if mibBuilder.loadTexts:
    groupTable.setStatus("current")
_GroupEntry_Object = MibTableRow
groupEntry = _GroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 1, 1)
)
groupEntry.setIndexNames(
    (0, "VERTIV-ONEVIEW-MIB", "groupIndex"),
)
if mibBuilder.loadTexts:
    groupEntry.setStatus("current")


class _GroupIndex_Type(Integer32):
    """Custom type groupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_GroupIndex_Type.__name__ = "Integer32"
_GroupIndex_Object = MibTableColumn
groupIndex = _GroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 1, 1, 1),
    _GroupIndex_Type()
)
groupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    groupIndex.setStatus("current")


class _GroupName_Type(SnmpAdminString):
    """Custom type groupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_GroupName_Type.__name__ = "SnmpAdminString"
_GroupName_Object = MibTableColumn
groupName = _GroupName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 1, 1, 2),
    _GroupName_Type()
)
groupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupName.setStatus("current")


class _GroupLabel_Type(SnmpAdminString):
    """Custom type groupLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_GroupLabel_Type.__name__ = "SnmpAdminString"
_GroupLabel_Object = MibTableColumn
groupLabel = _GroupLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 1, 1, 3),
    _GroupLabel_Type()
)
groupLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupLabel.setStatus("current")


class _GroupState_Type(Integer32):
    """Custom type groupState based on Integer32"""
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
        *(("idle", 1),
          ("discovered", 2),
          ("partiallyUnavailable", 3),
          ("unresponsive", 4),
          ("unknown", 5))
    )


_GroupState_Type.__name__ = "Integer32"
_GroupState_Object = MibTableColumn
groupState = _GroupState_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 1, 1, 4),
    _GroupState_Type()
)
groupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupState.setStatus("current")
_GroupPduTotalTable_Object = MibTable
groupPduTotalTable = _GroupPduTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 2)
)
if mibBuilder.loadTexts:
    groupPduTotalTable.setStatus("current")
_GroupPduTotalEntry_Object = MibTableRow
groupPduTotalEntry = _GroupPduTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 2, 1)
)
groupPduTotalEntry.setIndexNames(
    (0, "VERTIV-ONEVIEW-MIB", "groupIndex"),
)
if mibBuilder.loadTexts:
    groupPduTotalEntry.setStatus("current")


class _GroupPduTotalName_Type(SnmpAdminString):
    """Custom type groupPduTotalName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_GroupPduTotalName_Type.__name__ = "SnmpAdminString"
_GroupPduTotalName_Object = MibTableColumn
groupPduTotalName = _GroupPduTotalName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 2, 1, 1),
    _GroupPduTotalName_Type()
)
groupPduTotalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupPduTotalName.setStatus("current")


class _GroupPduTotalPowerMin_Type(Gauge32):
    """Custom type groupPduTotalPowerMin based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_GroupPduTotalPowerMin_Type.__name__ = "Gauge32"
_GroupPduTotalPowerMin_Object = MibTableColumn
groupPduTotalPowerMin = _GroupPduTotalPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 2, 1, 2),
    _GroupPduTotalPowerMin_Type()
)
groupPduTotalPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupPduTotalPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    groupPduTotalPowerMin.setUnits("watts")


class _GroupPduTotalPowerMax_Type(Gauge32):
    """Custom type groupPduTotalPowerMax based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_GroupPduTotalPowerMax_Type.__name__ = "Gauge32"
_GroupPduTotalPowerMax_Object = MibTableColumn
groupPduTotalPowerMax = _GroupPduTotalPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 2, 1, 3),
    _GroupPduTotalPowerMax_Type()
)
groupPduTotalPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupPduTotalPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    groupPduTotalPowerMax.setUnits("watts")


class _GroupPduTotalPowerAvg_Type(Gauge32):
    """Custom type groupPduTotalPowerAvg based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_GroupPduTotalPowerAvg_Type.__name__ = "Gauge32"
_GroupPduTotalPowerAvg_Object = MibTableColumn
groupPduTotalPowerAvg = _GroupPduTotalPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 2, 1, 4),
    _GroupPduTotalPowerAvg_Type()
)
groupPduTotalPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupPduTotalPowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    groupPduTotalPowerAvg.setUnits("watts")


class _GroupPduTotalPowerSum_Type(Gauge32):
    """Custom type groupPduTotalPowerSum based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_GroupPduTotalPowerSum_Type.__name__ = "Gauge32"
_GroupPduTotalPowerSum_Object = MibTableColumn
groupPduTotalPowerSum = _GroupPduTotalPowerSum_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 2, 1, 5),
    _GroupPduTotalPowerSum_Type()
)
groupPduTotalPowerSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupPduTotalPowerSum.setStatus("current")
if mibBuilder.loadTexts:
    groupPduTotalPowerSum.setUnits("watts")


class _GroupPduTotalEnergySum_Type(Gauge32):
    """Custom type groupPduTotalEnergySum based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999000),
    )


_GroupPduTotalEnergySum_Type.__name__ = "Gauge32"
_GroupPduTotalEnergySum_Object = MibTableColumn
groupPduTotalEnergySum = _GroupPduTotalEnergySum_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 2, 1, 6),
    _GroupPduTotalEnergySum_Type()
)
groupPduTotalEnergySum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupPduTotalEnergySum.setStatus("current")
if mibBuilder.loadTexts:
    groupPduTotalEnergySum.setUnits("watt-hours")
_GroupPduPhaseTable_Object = MibTable
groupPduPhaseTable = _GroupPduPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 3)
)
if mibBuilder.loadTexts:
    groupPduPhaseTable.setStatus("current")
_GroupPduPhaseEntry_Object = MibTableRow
groupPduPhaseEntry = _GroupPduPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 3, 1)
)
groupPduPhaseEntry.setIndexNames(
    (0, "VERTIV-ONEVIEW-MIB", "groupIndex"),
    (0, "VERTIV-ONEVIEW-MIB", "groupPduPhaseIndex"),
)
if mibBuilder.loadTexts:
    groupPduPhaseEntry.setStatus("current")


class _GroupPduPhaseIndex_Type(Integer32):
    """Custom type groupPduPhaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_GroupPduPhaseIndex_Type.__name__ = "Integer32"
_GroupPduPhaseIndex_Object = MibTableColumn
groupPduPhaseIndex = _GroupPduPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 3, 1, 1),
    _GroupPduPhaseIndex_Type()
)
groupPduPhaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    groupPduPhaseIndex.setStatus("current")


class _GroupPduPhaseName_Type(SnmpAdminString):
    """Custom type groupPduPhaseName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_GroupPduPhaseName_Type.__name__ = "SnmpAdminString"
_GroupPduPhaseName_Object = MibTableColumn
groupPduPhaseName = _GroupPduPhaseName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 3, 1, 2),
    _GroupPduPhaseName_Type()
)
groupPduPhaseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupPduPhaseName.setStatus("current")


class _GroupPduPhasePowerMin_Type(Gauge32):
    """Custom type groupPduPhasePowerMin based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_GroupPduPhasePowerMin_Type.__name__ = "Gauge32"
_GroupPduPhasePowerMin_Object = MibTableColumn
groupPduPhasePowerMin = _GroupPduPhasePowerMin_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 3, 1, 3),
    _GroupPduPhasePowerMin_Type()
)
groupPduPhasePowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupPduPhasePowerMin.setStatus("current")
if mibBuilder.loadTexts:
    groupPduPhasePowerMin.setUnits("watts")


class _GroupPduPhasePowerMax_Type(Gauge32):
    """Custom type groupPduPhasePowerMax based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_GroupPduPhasePowerMax_Type.__name__ = "Gauge32"
_GroupPduPhasePowerMax_Object = MibTableColumn
groupPduPhasePowerMax = _GroupPduPhasePowerMax_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 3, 1, 4),
    _GroupPduPhasePowerMax_Type()
)
groupPduPhasePowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupPduPhasePowerMax.setStatus("current")
if mibBuilder.loadTexts:
    groupPduPhasePowerMax.setUnits("watts")


class _GroupPduPhasePowerAvg_Type(Gauge32):
    """Custom type groupPduPhasePowerAvg based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_GroupPduPhasePowerAvg_Type.__name__ = "Gauge32"
_GroupPduPhasePowerAvg_Object = MibTableColumn
groupPduPhasePowerAvg = _GroupPduPhasePowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 3, 1, 5),
    _GroupPduPhasePowerAvg_Type()
)
groupPduPhasePowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupPduPhasePowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    groupPduPhasePowerAvg.setUnits("watts")


class _GroupPduPhasePowerSum_Type(Gauge32):
    """Custom type groupPduPhasePowerSum based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_GroupPduPhasePowerSum_Type.__name__ = "Gauge32"
_GroupPduPhasePowerSum_Object = MibTableColumn
groupPduPhasePowerSum = _GroupPduPhasePowerSum_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 3, 1, 6),
    _GroupPduPhasePowerSum_Type()
)
groupPduPhasePowerSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupPduPhasePowerSum.setStatus("current")
if mibBuilder.loadTexts:
    groupPduPhasePowerSum.setUnits("watts")


class _GroupPduPhaseEnergySum_Type(Gauge32):
    """Custom type groupPduPhaseEnergySum based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999000),
    )


_GroupPduPhaseEnergySum_Type.__name__ = "Gauge32"
_GroupPduPhaseEnergySum_Object = MibTableColumn
groupPduPhaseEnergySum = _GroupPduPhaseEnergySum_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 3, 1, 7),
    _GroupPduPhaseEnergySum_Type()
)
groupPduPhaseEnergySum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupPduPhaseEnergySum.setStatus("current")
if mibBuilder.loadTexts:
    groupPduPhaseEnergySum.setUnits("watt-hours")
_GroupUpsTable_Object = MibTable
groupUpsTable = _GroupUpsTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 4)
)
if mibBuilder.loadTexts:
    groupUpsTable.setStatus("current")
_GroupUpsEntry_Object = MibTableRow
groupUpsEntry = _GroupUpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 4, 1)
)
groupUpsEntry.setIndexNames(
    (0, "VERTIV-ONEVIEW-MIB", "groupIndex"),
)
if mibBuilder.loadTexts:
    groupUpsEntry.setStatus("current")


class _GroupUpsName_Type(SnmpAdminString):
    """Custom type groupUpsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_GroupUpsName_Type.__name__ = "SnmpAdminString"
_GroupUpsName_Object = MibTableColumn
groupUpsName = _GroupUpsName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 4, 1, 1),
    _GroupUpsName_Type()
)
groupUpsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupUpsName.setStatus("current")


class _GroupUpsPowerMax_Type(Gauge32):
    """Custom type groupUpsPowerMax based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_GroupUpsPowerMax_Type.__name__ = "Gauge32"
_GroupUpsPowerMax_Object = MibTableColumn
groupUpsPowerMax = _GroupUpsPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 4, 1, 2),
    _GroupUpsPowerMax_Type()
)
groupUpsPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupUpsPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    groupUpsPowerMax.setUnits("watts")


class _GroupUpsPowerAvg_Type(Gauge32):
    """Custom type groupUpsPowerAvg based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_GroupUpsPowerAvg_Type.__name__ = "Gauge32"
_GroupUpsPowerAvg_Object = MibTableColumn
groupUpsPowerAvg = _GroupUpsPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 4, 1, 3),
    _GroupUpsPowerAvg_Type()
)
groupUpsPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupUpsPowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    groupUpsPowerAvg.setUnits("watts")


class _GroupUpsBattAutonomyMin_Type(Gauge32):
    """Custom type groupUpsBattAutonomyMin based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_GroupUpsBattAutonomyMin_Type.__name__ = "Gauge32"
_GroupUpsBattAutonomyMin_Object = MibTableColumn
groupUpsBattAutonomyMin = _GroupUpsBattAutonomyMin_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 4, 1, 4),
    _GroupUpsBattAutonomyMin_Type()
)
groupUpsBattAutonomyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupUpsBattAutonomyMin.setStatus("current")
if mibBuilder.loadTexts:
    groupUpsBattAutonomyMin.setUnits("minutes")


class _GroupUpsBattAutonomyAvg_Type(Gauge32):
    """Custom type groupUpsBattAutonomyAvg based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_GroupUpsBattAutonomyAvg_Type.__name__ = "Gauge32"
_GroupUpsBattAutonomyAvg_Object = MibTableColumn
groupUpsBattAutonomyAvg = _GroupUpsBattAutonomyAvg_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 4, 1, 5),
    _GroupUpsBattAutonomyAvg_Type()
)
groupUpsBattAutonomyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupUpsBattAutonomyAvg.setStatus("current")
if mibBuilder.loadTexts:
    groupUpsBattAutonomyAvg.setUnits("minutes")


class _GroupUpsBattChargeMin_Type(Gauge32):
    """Custom type groupUpsBattChargeMin based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GroupUpsBattChargeMin_Type.__name__ = "Gauge32"
_GroupUpsBattChargeMin_Object = MibTableColumn
groupUpsBattChargeMin = _GroupUpsBattChargeMin_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 4, 1, 6),
    _GroupUpsBattChargeMin_Type()
)
groupUpsBattChargeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupUpsBattChargeMin.setStatus("current")
if mibBuilder.loadTexts:
    groupUpsBattChargeMin.setUnits("%")


class _GroupUpsBattChargeAvg_Type(Gauge32):
    """Custom type groupUpsBattChargeAvg based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GroupUpsBattChargeAvg_Type.__name__ = "Gauge32"
_GroupUpsBattChargeAvg_Object = MibTableColumn
groupUpsBattChargeAvg = _GroupUpsBattChargeAvg_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 4, 1, 7),
    _GroupUpsBattChargeAvg_Type()
)
groupUpsBattChargeAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupUpsBattChargeAvg.setStatus("current")
if mibBuilder.loadTexts:
    groupUpsBattChargeAvg.setUnits("%")
_GroupEnvTable_Object = MibTable
groupEnvTable = _GroupEnvTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 5)
)
if mibBuilder.loadTexts:
    groupEnvTable.setStatus("current")
_GroupEnvEntry_Object = MibTableRow
groupEnvEntry = _GroupEnvEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 5, 1)
)
groupEnvEntry.setIndexNames(
    (0, "VERTIV-ONEVIEW-MIB", "groupIndex"),
)
if mibBuilder.loadTexts:
    groupEnvEntry.setStatus("current")


class _GroupEnvName_Type(SnmpAdminString):
    """Custom type groupEnvName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_GroupEnvName_Type.__name__ = "SnmpAdminString"
_GroupEnvName_Object = MibTableColumn
groupEnvName = _GroupEnvName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 5, 1, 1),
    _GroupEnvName_Type()
)
groupEnvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupEnvName.setStatus("current")


class _GroupEnvTempMin_Type(Integer32):
    """Custom type groupEnvTempMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 2540),
    )


_GroupEnvTempMin_Type.__name__ = "Integer32"
_GroupEnvTempMin_Object = MibTableColumn
groupEnvTempMin = _GroupEnvTempMin_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 5, 1, 2),
    _GroupEnvTempMin_Type()
)
groupEnvTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupEnvTempMin.setStatus("current")


class _GroupEnvTempMax_Type(Integer32):
    """Custom type groupEnvTempMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 2540),
    )


_GroupEnvTempMax_Type.__name__ = "Integer32"
_GroupEnvTempMax_Object = MibTableColumn
groupEnvTempMax = _GroupEnvTempMax_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 5, 1, 3),
    _GroupEnvTempMax_Type()
)
groupEnvTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupEnvTempMax.setStatus("current")


class _GroupEnvTempAvg_Type(Integer32):
    """Custom type groupEnvTempAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 2540),
    )


_GroupEnvTempAvg_Type.__name__ = "Integer32"
_GroupEnvTempAvg_Object = MibTableColumn
groupEnvTempAvg = _GroupEnvTempAvg_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 5, 1, 4),
    _GroupEnvTempAvg_Type()
)
groupEnvTempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupEnvTempAvg.setStatus("current")


class _GroupEnvHumidityMin_Type(Integer32):
    """Custom type groupEnvHumidityMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GroupEnvHumidityMin_Type.__name__ = "Integer32"
_GroupEnvHumidityMin_Object = MibTableColumn
groupEnvHumidityMin = _GroupEnvHumidityMin_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 5, 1, 5),
    _GroupEnvHumidityMin_Type()
)
groupEnvHumidityMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupEnvHumidityMin.setStatus("current")
if mibBuilder.loadTexts:
    groupEnvHumidityMin.setUnits("%")


class _GroupEnvHumidityMax_Type(Integer32):
    """Custom type groupEnvHumidityMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GroupEnvHumidityMax_Type.__name__ = "Integer32"
_GroupEnvHumidityMax_Object = MibTableColumn
groupEnvHumidityMax = _GroupEnvHumidityMax_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 5, 1, 6),
    _GroupEnvHumidityMax_Type()
)
groupEnvHumidityMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupEnvHumidityMax.setStatus("current")
if mibBuilder.loadTexts:
    groupEnvHumidityMax.setUnits("%")


class _GroupEnvHumidityAvg_Type(Integer32):
    """Custom type groupEnvHumidityAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GroupEnvHumidityAvg_Type.__name__ = "Integer32"
_GroupEnvHumidityAvg_Object = MibTableColumn
groupEnvHumidityAvg = _GroupEnvHumidityAvg_Object(
    (1, 3, 6, 1, 4, 1, 21239, 43, 2, 5, 1, 7),
    _GroupEnvHumidityAvg_Type()
)
groupEnvHumidityAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupEnvHumidityAvg.setStatus("current")
if mibBuilder.loadTexts:
    groupEnvHumidityAvg.setUnits("%")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERTIV-ONEVIEW-MIB",
    **{"vertiv": vertiv,
       "oneview": oneview,
       "hostTable": hostTable,
       "hostEntry": hostEntry,
       "hostIndex": hostIndex,
       "hostId": hostId,
       "hostState": hostState,
       "hostType": hostType,
       "hostGroupIndex": hostGroupIndex,
       "hostGroupName": hostGroupName,
       "hostPortWeb": hostPortWeb,
       "hostPortSnmp": hostPortSnmp,
       "groups": groups,
       "groupTable": groupTable,
       "groupEntry": groupEntry,
       "groupIndex": groupIndex,
       "groupName": groupName,
       "groupLabel": groupLabel,
       "groupState": groupState,
       "groupPduTotalTable": groupPduTotalTable,
       "groupPduTotalEntry": groupPduTotalEntry,
       "groupPduTotalName": groupPduTotalName,
       "groupPduTotalPowerMin": groupPduTotalPowerMin,
       "groupPduTotalPowerMax": groupPduTotalPowerMax,
       "groupPduTotalPowerAvg": groupPduTotalPowerAvg,
       "groupPduTotalPowerSum": groupPduTotalPowerSum,
       "groupPduTotalEnergySum": groupPduTotalEnergySum,
       "groupPduPhaseTable": groupPduPhaseTable,
       "groupPduPhaseEntry": groupPduPhaseEntry,
       "groupPduPhaseIndex": groupPduPhaseIndex,
       "groupPduPhaseName": groupPduPhaseName,
       "groupPduPhasePowerMin": groupPduPhasePowerMin,
       "groupPduPhasePowerMax": groupPduPhasePowerMax,
       "groupPduPhasePowerAvg": groupPduPhasePowerAvg,
       "groupPduPhasePowerSum": groupPduPhasePowerSum,
       "groupPduPhaseEnergySum": groupPduPhaseEnergySum,
       "groupUpsTable": groupUpsTable,
       "groupUpsEntry": groupUpsEntry,
       "groupUpsName": groupUpsName,
       "groupUpsPowerMax": groupUpsPowerMax,
       "groupUpsPowerAvg": groupUpsPowerAvg,
       "groupUpsBattAutonomyMin": groupUpsBattAutonomyMin,
       "groupUpsBattAutonomyAvg": groupUpsBattAutonomyAvg,
       "groupUpsBattChargeMin": groupUpsBattChargeMin,
       "groupUpsBattChargeAvg": groupUpsBattChargeAvg,
       "groupEnvTable": groupEnvTable,
       "groupEnvEntry": groupEnvEntry,
       "groupEnvName": groupEnvName,
       "groupEnvTempMin": groupEnvTempMin,
       "groupEnvTempMax": groupEnvTempMax,
       "groupEnvTempAvg": groupEnvTempAvg,
       "groupEnvHumidityMin": groupEnvHumidityMin,
       "groupEnvHumidityMax": groupEnvHumidityMax,
       "groupEnvHumidityAvg": groupEnvHumidityAvg}
)
