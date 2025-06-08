# SNMP MIB module (RUIJIE-RSTP-MSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-RSTP-MSTP-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:02:06 2025
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

(BridgeId,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "ConfigStatus",
    "IfIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieStpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16)
)
if mibBuilder.loadTexts:
    ruijieStpMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieStpMIBObjects_ObjectIdentity = ObjectIdentity
ruijieStpMIBObjects = _RuijieStpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 1)
)


class _RuijieSysStpStatus_Type(EnabledStatus):
    """Custom type ruijieSysStpStatus based on EnabledStatus"""
    defaultValue = 2


_RuijieSysStpStatus_Type.__name__ = "EnabledStatus"
_RuijieSysStpStatus_Object = MibScalar
ruijieSysStpStatus = _RuijieSysStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 1, 1),
    _RuijieSysStpStatus_Type()
)
ruijieSysStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSysStpStatus.setStatus("current")
_RuijieSysStpReset_Type = Integer32
_RuijieSysStpReset_Object = MibScalar
ruijieSysStpReset = _RuijieSysStpReset_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 1, 2),
    _RuijieSysStpReset_Type()
)
ruijieSysStpReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSysStpReset.setStatus("current")
_RuijieStpExtPortTable_Object = MibTable
ruijieStpExtPortTable = _RuijieStpExtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieStpExtPortTable.setStatus("current")
_RuijieStpExtPortEntry_Object = MibTableRow
ruijieStpExtPortEntry = _RuijieStpExtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 1, 3, 1)
)
ruijieStpExtPortEntry.setIndexNames(
    (0, "RUIJIE-RSTP-MSTP-MIB", "ruijieStpPortIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieStpExtPortEntry.setStatus("current")
_RuijieStpPortIfIndex_Type = IfIndex
_RuijieStpPortIfIndex_Object = MibTableColumn
ruijieStpPortIfIndex = _RuijieStpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 1, 3, 1, 1),
    _RuijieStpPortIfIndex_Type()
)
ruijieStpPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStpPortIfIndex.setStatus("current")


class _RuijieStpPortAdminPathCost_Type(Integer32):
    """Custom type ruijieStpPortAdminPathCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_RuijieStpPortAdminPathCost_Type.__name__ = "Integer32"
_RuijieStpPortAdminPathCost_Object = MibTableColumn
ruijieStpPortAdminPathCost = _RuijieStpPortAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 1, 3, 1, 2),
    _RuijieStpPortAdminPathCost_Type()
)
ruijieStpPortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieStpPortAdminPathCost.setStatus("current")


class _RuijieStpPortOperPathCost_Type(Integer32):
    """Custom type ruijieStpPortOperPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_RuijieStpPortOperPathCost_Type.__name__ = "Integer32"
_RuijieStpPortOperPathCost_Object = MibTableColumn
ruijieStpPortOperPathCost = _RuijieStpPortOperPathCost_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 1, 3, 1, 3),
    _RuijieStpPortOperPathCost_Type()
)
ruijieStpPortOperPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStpPortOperPathCost.setStatus("current")


class _RuijieStpPortRole_Type(Integer32):
    """Custom type ruijieStpPortRole based on Integer32"""
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
        *(("disabledPort", 1),
          ("alternatePort", 2),
          ("backupPort", 3),
          ("rootPort", 4),
          ("designatedPort", 5),
          ("masterPort", 6))
    )


_RuijieStpPortRole_Type.__name__ = "Integer32"
_RuijieStpPortRole_Object = MibTableColumn
ruijieStpPortRole = _RuijieStpPortRole_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 1, 3, 1, 4),
    _RuijieStpPortRole_Type()
)
ruijieStpPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStpPortRole.setStatus("current")
_RuijieRstpMIBObjects_ObjectIdentity = ObjectIdentity
ruijieRstpMIBObjects = _RuijieRstpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 2)
)


class _RuijieStpVersion_Type(Integer32):
    """Custom type ruijieStpVersion based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stpCompatible", 0),
          ("rstp", 2),
          ("mstp", 3))
    )


_RuijieStpVersion_Type.__name__ = "Integer32"
_RuijieStpVersion_Object = MibScalar
ruijieStpVersion = _RuijieStpVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 2, 1),
    _RuijieStpVersion_Type()
)
ruijieStpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieStpVersion.setStatus("current")


class _RuijieStpTxHoldCount_Type(Integer32):
    """Custom type ruijieStpTxHoldCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RuijieStpTxHoldCount_Type.__name__ = "Integer32"
_RuijieStpTxHoldCount_Object = MibScalar
ruijieStpTxHoldCount = _RuijieStpTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 2, 2),
    _RuijieStpTxHoldCount_Type()
)
ruijieStpTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieStpTxHoldCount.setStatus("current")


class _RuijieStpPathCostDefault_Type(Integer32):
    """Custom type ruijieStpPathCostDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stp8021d1998", 1),
          ("stp8021t2001", 2))
    )


_RuijieStpPathCostDefault_Type.__name__ = "Integer32"
_RuijieStpPathCostDefault_Object = MibScalar
ruijieStpPathCostDefault = _RuijieStpPathCostDefault_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 2, 3),
    _RuijieStpPathCostDefault_Type()
)
ruijieStpPathCostDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieStpPathCostDefault.setStatus("current")
_RuijieRstpExtPortTable_Object = MibTable
ruijieRstpExtPortTable = _RuijieRstpExtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 2, 4)
)
if mibBuilder.loadTexts:
    ruijieRstpExtPortTable.setStatus("current")
_RuijieRstpExtPortEntry_Object = MibTableRow
ruijieRstpExtPortEntry = _RuijieRstpExtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 2, 4, 1)
)
ruijieRstpExtPortEntry.setIndexNames(
    (0, "RUIJIE-RSTP-MSTP-MIB", "ruijieRstpExtPortIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieRstpExtPortEntry.setStatus("current")
_RuijieRstpExtPortIfIndex_Type = IfIndex
_RuijieRstpExtPortIfIndex_Object = MibTableColumn
ruijieRstpExtPortIfIndex = _RuijieRstpExtPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 2, 4, 1, 1),
    _RuijieRstpExtPortIfIndex_Type()
)
ruijieRstpExtPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRstpExtPortIfIndex.setStatus("current")
_RuijieStpPortProtocolMigration_Type = TruthValue
_RuijieStpPortProtocolMigration_Object = MibTableColumn
ruijieStpPortProtocolMigration = _RuijieStpPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 2, 4, 1, 2),
    _RuijieStpPortProtocolMigration_Type()
)
ruijieStpPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieStpPortProtocolMigration.setStatus("current")
_RuijieStpPortAdminEdgePort_Type = TruthValue
_RuijieStpPortAdminEdgePort_Object = MibTableColumn
ruijieStpPortAdminEdgePort = _RuijieStpPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 2, 4, 1, 3),
    _RuijieStpPortAdminEdgePort_Type()
)
ruijieStpPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieStpPortAdminEdgePort.setStatus("current")
_RuijieStpPortOperEdgePort_Type = TruthValue
_RuijieStpPortOperEdgePort_Object = MibTableColumn
ruijieStpPortOperEdgePort = _RuijieStpPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 2, 4, 1, 4),
    _RuijieStpPortOperEdgePort_Type()
)
ruijieStpPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStpPortOperEdgePort.setStatus("current")


class _RuijieStpPortAdminPointToPoint_Type(Integer32):
    """Custom type ruijieStpPortAdminPointToPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceTrue", 0),
          ("forceFalse", 1),
          ("auto", 2))
    )


_RuijieStpPortAdminPointToPoint_Type.__name__ = "Integer32"
_RuijieStpPortAdminPointToPoint_Object = MibTableColumn
ruijieStpPortAdminPointToPoint = _RuijieStpPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 2, 4, 1, 5),
    _RuijieStpPortAdminPointToPoint_Type()
)
ruijieStpPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieStpPortAdminPointToPoint.setStatus("current")
_RuijieStpPortOperPointToPoint_Type = TruthValue
_RuijieStpPortOperPointToPoint_Object = MibTableColumn
ruijieStpPortOperPointToPoint = _RuijieStpPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 2, 4, 1, 6),
    _RuijieStpPortOperPointToPoint_Type()
)
ruijieStpPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStpPortOperPointToPoint.setStatus("current")
_RuijieStpPortBpduGuard_Type = EnabledStatus
_RuijieStpPortBpduGuard_Object = MibTableColumn
ruijieStpPortBpduGuard = _RuijieStpPortBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 2, 4, 1, 7),
    _RuijieStpPortBpduGuard_Type()
)
ruijieStpPortBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieStpPortBpduGuard.setStatus("current")
_RuijieStpPortBpduFilter_Type = EnabledStatus
_RuijieStpPortBpduFilter_Object = MibTableColumn
ruijieStpPortBpduFilter = _RuijieStpPortBpduFilter_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 2, 4, 1, 8),
    _RuijieStpPortBpduFilter_Type()
)
ruijieStpPortBpduFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieStpPortBpduFilter.setStatus("current")
_RuijieStpBpduGuard_Type = EnabledStatus
_RuijieStpBpduGuard_Object = MibScalar
ruijieStpBpduGuard = _RuijieStpBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 2, 5),
    _RuijieStpBpduGuard_Type()
)
ruijieStpBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieStpBpduGuard.setStatus("current")
_RuijieStpBpduFilter_Type = EnabledStatus
_RuijieStpBpduFilter_Object = MibScalar
ruijieStpBpduFilter = _RuijieStpBpduFilter_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 2, 6),
    _RuijieStpBpduFilter_Type()
)
ruijieStpBpduFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieStpBpduFilter.setStatus("current")
_RuijieStpCistRegionRoot_Type = BridgeId
_RuijieStpCistRegionRoot_Object = MibScalar
ruijieStpCistRegionRoot = _RuijieStpCistRegionRoot_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 2, 7),
    _RuijieStpCistRegionRoot_Type()
)
ruijieStpCistRegionRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStpCistRegionRoot.setStatus("current")
_RuijieStpCistPathCost_Type = Integer32
_RuijieStpCistPathCost_Object = MibScalar
ruijieStpCistPathCost = _RuijieStpCistPathCost_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 2, 8),
    _RuijieStpCistPathCost_Type()
)
ruijieStpCistPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStpCistPathCost.setStatus("current")
_RuijieMstpMIBObjects_ObjectIdentity = ObjectIdentity
ruijieMstpMIBObjects = _RuijieMstpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3)
)
_RuijieStpMstiMaxInstanceNumber_Type = Integer32
_RuijieStpMstiMaxInstanceNumber_Object = MibScalar
ruijieStpMstiMaxInstanceNumber = _RuijieStpMstiMaxInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 1),
    _RuijieStpMstiMaxInstanceNumber_Type()
)
ruijieStpMstiMaxInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStpMstiMaxInstanceNumber.setStatus("current")


class _RuijieStpMstiRegionName_Type(DisplayString):
    """Custom type ruijieStpMstiRegionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieStpMstiRegionName_Type.__name__ = "DisplayString"
_RuijieStpMstiRegionName_Object = MibScalar
ruijieStpMstiRegionName = _RuijieStpMstiRegionName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 2),
    _RuijieStpMstiRegionName_Type()
)
ruijieStpMstiRegionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieStpMstiRegionName.setStatus("current")


class _RuijieStpMstiRegionRevision_Type(Integer32):
    """Custom type ruijieStpMstiRegionRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieStpMstiRegionRevision_Type.__name__ = "Integer32"
_RuijieStpMstiRegionRevision_Object = MibScalar
ruijieStpMstiRegionRevision = _RuijieStpMstiRegionRevision_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 3),
    _RuijieStpMstiRegionRevision_Type()
)
ruijieStpMstiRegionRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieStpMstiRegionRevision.setStatus("current")


class _RuijieStpMstiMaxHopNumber_Type(Integer32):
    """Custom type ruijieStpMstiMaxHopNumber based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_RuijieStpMstiMaxHopNumber_Type.__name__ = "Integer32"
_RuijieStpMstiMaxHopNumber_Object = MibScalar
ruijieStpMstiMaxHopNumber = _RuijieStpMstiMaxHopNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 4),
    _RuijieStpMstiMaxHopNumber_Type()
)
ruijieStpMstiMaxHopNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieStpMstiMaxHopNumber.setStatus("current")
_RuijieStpMstiInstanceTable_Object = MibTable
ruijieStpMstiInstanceTable = _RuijieStpMstiInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 5)
)
if mibBuilder.loadTexts:
    ruijieStpMstiInstanceTable.setStatus("current")
_RuijieStpMstiInstanceEntry_Object = MibTableRow
ruijieStpMstiInstanceEntry = _RuijieStpMstiInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 5, 1)
)
ruijieStpMstiInstanceEntry.setIndexNames(
    (0, "RUIJIE-RSTP-MSTP-MIB", "ruijieStpMstiInstanceIndex"),
)
if mibBuilder.loadTexts:
    ruijieStpMstiInstanceEntry.setStatus("current")


class _RuijieStpMstiInstanceIndex_Type(Integer32):
    """Custom type ruijieStpMstiInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_RuijieStpMstiInstanceIndex_Type.__name__ = "Integer32"
_RuijieStpMstiInstanceIndex_Object = MibTableColumn
ruijieStpMstiInstanceIndex = _RuijieStpMstiInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 5, 1, 1),
    _RuijieStpMstiInstanceIndex_Type()
)
ruijieStpMstiInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStpMstiInstanceIndex.setStatus("current")


class _RuijieStpMstiInstanceVlansAddMapped_Type(OctetString):
    """Custom type ruijieStpMstiInstanceVlansAddMapped based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_RuijieStpMstiInstanceVlansAddMapped_Type.__name__ = "OctetString"
_RuijieStpMstiInstanceVlansAddMapped_Object = MibTableColumn
ruijieStpMstiInstanceVlansAddMapped = _RuijieStpMstiInstanceVlansAddMapped_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 5, 1, 2),
    _RuijieStpMstiInstanceVlansAddMapped_Type()
)
ruijieStpMstiInstanceVlansAddMapped.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieStpMstiInstanceVlansAddMapped.setStatus("current")


class _RuijieStpMstiInstanceVlansDeleteMapped_Type(OctetString):
    """Custom type ruijieStpMstiInstanceVlansDeleteMapped based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_RuijieStpMstiInstanceVlansDeleteMapped_Type.__name__ = "OctetString"
_RuijieStpMstiInstanceVlansDeleteMapped_Object = MibTableColumn
ruijieStpMstiInstanceVlansDeleteMapped = _RuijieStpMstiInstanceVlansDeleteMapped_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 5, 1, 3),
    _RuijieStpMstiInstanceVlansDeleteMapped_Type()
)
ruijieStpMstiInstanceVlansDeleteMapped.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieStpMstiInstanceVlansDeleteMapped.setStatus("current")


class _RuijieStpMstiInstanceVlansGetMapped_Type(OctetString):
    """Custom type ruijieStpMstiInstanceVlansGetMapped based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_RuijieStpMstiInstanceVlansGetMapped_Type.__name__ = "OctetString"
_RuijieStpMstiInstanceVlansGetMapped_Object = MibTableColumn
ruijieStpMstiInstanceVlansGetMapped = _RuijieStpMstiInstanceVlansGetMapped_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 5, 1, 4),
    _RuijieStpMstiInstanceVlansGetMapped_Type()
)
ruijieStpMstiInstanceVlansGetMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStpMstiInstanceVlansGetMapped.setStatus("current")


class _RuijieStpMstiInstanceRemainingHopCount_Type(Integer32):
    """Custom type ruijieStpMstiInstanceRemainingHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_RuijieStpMstiInstanceRemainingHopCount_Type.__name__ = "Integer32"
_RuijieStpMstiInstanceRemainingHopCount_Object = MibTableColumn
ruijieStpMstiInstanceRemainingHopCount = _RuijieStpMstiInstanceRemainingHopCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 5, 1, 5),
    _RuijieStpMstiInstanceRemainingHopCount_Type()
)
ruijieStpMstiInstanceRemainingHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStpMstiInstanceRemainingHopCount.setStatus("current")


class _RuijieStpMstiPriority_Type(Integer32):
    """Custom type ruijieStpMstiPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieStpMstiPriority_Type.__name__ = "Integer32"
_RuijieStpMstiPriority_Object = MibTableColumn
ruijieStpMstiPriority = _RuijieStpMstiPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 5, 1, 6),
    _RuijieStpMstiPriority_Type()
)
ruijieStpMstiPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieStpMstiPriority.setStatus("current")
_RuijieStpMstiTimeSinceTopologyChange_Type = TimeTicks
_RuijieStpMstiTimeSinceTopologyChange_Object = MibTableColumn
ruijieStpMstiTimeSinceTopologyChange = _RuijieStpMstiTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 5, 1, 7),
    _RuijieStpMstiTimeSinceTopologyChange_Type()
)
ruijieStpMstiTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStpMstiTimeSinceTopologyChange.setStatus("current")
_RuijieStpMstiTopChanges_Type = Integer32
_RuijieStpMstiTopChanges_Object = MibTableColumn
ruijieStpMstiTopChanges = _RuijieStpMstiTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 5, 1, 8),
    _RuijieStpMstiTopChanges_Type()
)
ruijieStpMstiTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStpMstiTopChanges.setStatus("current")
_RuijieStpMstiDesignatedRoot_Type = BridgeId
_RuijieStpMstiDesignatedRoot_Object = MibTableColumn
ruijieStpMstiDesignatedRoot = _RuijieStpMstiDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 5, 1, 9),
    _RuijieStpMstiDesignatedRoot_Type()
)
ruijieStpMstiDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStpMstiDesignatedRoot.setStatus("current")
_RuijieStpMstiRootCost_Type = Integer32
_RuijieStpMstiRootCost_Object = MibTableColumn
ruijieStpMstiRootCost = _RuijieStpMstiRootCost_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 5, 1, 10),
    _RuijieStpMstiRootCost_Type()
)
ruijieStpMstiRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStpMstiRootCost.setStatus("current")
_RuijieStpMstiRootPort_Type = Integer32
_RuijieStpMstiRootPort_Object = MibTableColumn
ruijieStpMstiRootPort = _RuijieStpMstiRootPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 5, 1, 11),
    _RuijieStpMstiRootPort_Type()
)
ruijieStpMstiRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStpMstiRootPort.setStatus("current")
_RuijieStpMstiInstanceEntryStatus_Type = ConfigStatus
_RuijieStpMstiInstanceEntryStatus_Object = MibTableColumn
ruijieStpMstiInstanceEntryStatus = _RuijieStpMstiInstanceEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 5, 1, 12),
    _RuijieStpMstiInstanceEntryStatus_Type()
)
ruijieStpMstiInstanceEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieStpMstiInstanceEntryStatus.setStatus("current")
_RuijieStpPortMstiInstanceTable_Object = MibTable
ruijieStpPortMstiInstanceTable = _RuijieStpPortMstiInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 6)
)
if mibBuilder.loadTexts:
    ruijieStpPortMstiInstanceTable.setStatus("current")
_RuijieStpPortMstiInstanceEntry_Object = MibTableRow
ruijieStpPortMstiInstanceEntry = _RuijieStpPortMstiInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 6, 1)
)
ruijieStpPortMstiInstanceEntry.setIndexNames(
    (0, "RUIJIE-RSTP-MSTP-MIB", "ruijieStpMstiInstanceIndex"),
    (0, "RUIJIE-RSTP-MSTP-MIB", "ruijieStpPortMstiIndex"),
)
if mibBuilder.loadTexts:
    ruijieStpPortMstiInstanceEntry.setStatus("current")
_RuijieStpPortMstiIndex_Type = Integer32
_RuijieStpPortMstiIndex_Object = MibTableColumn
ruijieStpPortMstiIndex = _RuijieStpPortMstiIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 6, 1, 1),
    _RuijieStpPortMstiIndex_Type()
)
ruijieStpPortMstiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieStpPortMstiIndex.setStatus("current")


class _RuijieStpPortMstiState_Type(Integer32):
    """Custom type ruijieStpPortMstiState based on Integer32"""
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
        *(("disabled", 1),
          ("blocking", 2),
          ("listening", 3),
          ("learning", 4),
          ("forwarding", 5),
          ("broken", 6),
          ("discard", 7))
    )


_RuijieStpPortMstiState_Type.__name__ = "Integer32"
_RuijieStpPortMstiState_Object = MibTableColumn
ruijieStpPortMstiState = _RuijieStpPortMstiState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 6, 1, 2),
    _RuijieStpPortMstiState_Type()
)
ruijieStpPortMstiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStpPortMstiState.setStatus("current")
_RuijieStpPortMstiAdminPathCost_Type = Integer32
_RuijieStpPortMstiAdminPathCost_Object = MibTableColumn
ruijieStpPortMstiAdminPathCost = _RuijieStpPortMstiAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 6, 1, 3),
    _RuijieStpPortMstiAdminPathCost_Type()
)
ruijieStpPortMstiAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieStpPortMstiAdminPathCost.setStatus("current")
_RuijieStpPortMstiOperPathCost_Type = Counter32
_RuijieStpPortMstiOperPathCost_Object = MibTableColumn
ruijieStpPortMstiOperPathCost = _RuijieStpPortMstiOperPathCost_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 6, 1, 4),
    _RuijieStpPortMstiOperPathCost_Type()
)
ruijieStpPortMstiOperPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStpPortMstiOperPathCost.setStatus("current")


class _RuijieStpPortMstiPriority_Type(Integer32):
    """Custom type ruijieStpPortMstiPriority based on Integer32"""
    defaultValue = 128


_RuijieStpPortMstiPriority_Type.__name__ = "Integer32"
_RuijieStpPortMstiPriority_Object = MibTableColumn
ruijieStpPortMstiPriority = _RuijieStpPortMstiPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 6, 1, 5),
    _RuijieStpPortMstiPriority_Type()
)
ruijieStpPortMstiPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieStpPortMstiPriority.setStatus("current")
_RuijieStpPortMstiDesignatedRoot_Type = BridgeId
_RuijieStpPortMstiDesignatedRoot_Object = MibTableColumn
ruijieStpPortMstiDesignatedRoot = _RuijieStpPortMstiDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 6, 1, 6),
    _RuijieStpPortMstiDesignatedRoot_Type()
)
ruijieStpPortMstiDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStpPortMstiDesignatedRoot.setStatus("current")
_RuijieStpPortMstiDesignatedCost_Type = Integer32
_RuijieStpPortMstiDesignatedCost_Object = MibTableColumn
ruijieStpPortMstiDesignatedCost = _RuijieStpPortMstiDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 6, 1, 7),
    _RuijieStpPortMstiDesignatedCost_Type()
)
ruijieStpPortMstiDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStpPortMstiDesignatedCost.setStatus("current")
_RuijieStpPortMstiDesignatedBridge_Type = BridgeId
_RuijieStpPortMstiDesignatedBridge_Object = MibTableColumn
ruijieStpPortMstiDesignatedBridge = _RuijieStpPortMstiDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 6, 1, 8),
    _RuijieStpPortMstiDesignatedBridge_Type()
)
ruijieStpPortMstiDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStpPortMstiDesignatedBridge.setStatus("current")


class _RuijieStpPortMstiDesignatedPort_Type(OctetString):
    """Custom type ruijieStpPortMstiDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_RuijieStpPortMstiDesignatedPort_Type.__name__ = "OctetString"
_RuijieStpPortMstiDesignatedPort_Object = MibTableColumn
ruijieStpPortMstiDesignatedPort = _RuijieStpPortMstiDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 6, 1, 9),
    _RuijieStpPortMstiDesignatedPort_Type()
)
ruijieStpPortMstiDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStpPortMstiDesignatedPort.setStatus("current")


class _RuijieStpPortMstiPortRole_Type(Integer32):
    """Custom type ruijieStpPortMstiPortRole based on Integer32"""
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
        *(("disabledPort", 1),
          ("alternatePort", 2),
          ("backupPort", 3),
          ("rootPort", 4),
          ("designatedPort", 5),
          ("masterPort", 6))
    )


_RuijieStpPortMstiPortRole_Type.__name__ = "Integer32"
_RuijieStpPortMstiPortRole_Object = MibTableColumn
ruijieStpPortMstiPortRole = _RuijieStpPortMstiPortRole_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 6, 1, 10),
    _RuijieStpPortMstiPortRole_Type()
)
ruijieStpPortMstiPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStpPortMstiPortRole.setStatus("current")
_RuijieStpPortMstiPortForwardTransitions_Type = Integer32
_RuijieStpPortMstiPortForwardTransitions_Object = MibTableColumn
ruijieStpPortMstiPortForwardTransitions = _RuijieStpPortMstiPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 6, 1, 11),
    _RuijieStpPortMstiPortForwardTransitions_Type()
)
ruijieStpPortMstiPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStpPortMstiPortForwardTransitions.setStatus("current")
_RuijieStpMstiReset_Type = Integer32
_RuijieStpMstiReset_Object = MibScalar
ruijieStpMstiReset = _RuijieStpMstiReset_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 7),
    _RuijieStpMstiReset_Type()
)
ruijieStpMstiReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieStpMstiReset.setStatus("current")
_RuijieStpCistVlansAddMapped_Type = OctetString
_RuijieStpCistVlansAddMapped_Object = MibScalar
ruijieStpCistVlansAddMapped = _RuijieStpCistVlansAddMapped_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 8),
    _RuijieStpCistVlansAddMapped_Type()
)
ruijieStpCistVlansAddMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieStpCistVlansAddMapped.setStatus("current")
_RuijieStpCistVlansGetMapped_Type = OctetString
_RuijieStpCistVlansGetMapped_Object = MibScalar
ruijieStpCistVlansGetMapped = _RuijieStpCistVlansGetMapped_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 9),
    _RuijieStpCistVlansGetMapped_Type()
)
ruijieStpCistVlansGetMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStpCistVlansGetMapped.setStatus("current")
_RuijieStpCistRemainingHopCount_Type = Integer32
_RuijieStpCistRemainingHopCount_Object = MibScalar
ruijieStpCistRemainingHopCount = _RuijieStpCistRemainingHopCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 3, 10),
    _RuijieStpCistRemainingHopCount_Type()
)
ruijieStpCistRemainingHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStpCistRemainingHopCount.setStatus("current")
_StpExternConformance_ObjectIdentity = ObjectIdentity
stpExternConformance = _StpExternConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 4)
)
_StpExternGroups_ObjectIdentity = ObjectIdentity
stpExternGroups = _StpExternGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 4, 1)
)
_RstpConformance_ObjectIdentity = ObjectIdentity
rstpConformance = _RstpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 5)
)
_RstpGroups_ObjectIdentity = ObjectIdentity
rstpGroups = _RstpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 5, 1)
)
_RstpCompliances_ObjectIdentity = ObjectIdentity
rstpCompliances = _RstpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 5, 2)
)
_MstpConformance_ObjectIdentity = ObjectIdentity
mstpConformance = _MstpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 6)
)
_MstpGroups_ObjectIdentity = ObjectIdentity
mstpGroups = _MstpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 6, 1)
)
_MstpCompliances_ObjectIdentity = ObjectIdentity
mstpCompliances = _MstpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 6, 2)
)

# Managed Objects groups

stpExternGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 4, 1, 1)
)
stpExternGroup.setObjects(
      *(("RUIJIE-RSTP-MSTP-MIB", "ruijieSysStpStatus"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieSysStpReset"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpPortIfIndex"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpPortAdminPathCost"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpPortOperPathCost"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpPortRole"))
)
if mibBuilder.loadTexts:
    stpExternGroup.setStatus("current")

rstpBridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 5, 1, 1)
)
rstpBridgeGroup.setObjects(
      *(("RUIJIE-RSTP-MSTP-MIB", "ruijieStpVersion"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpTxHoldCount"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpBpduGuard"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpBpduFilter"))
)
if mibBuilder.loadTexts:
    rstpBridgeGroup.setStatus("current")

rstpDefaultPathCostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 5, 1, 2)
)
rstpDefaultPathCostGroup.setObjects(
    ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpPathCostDefault")
)
if mibBuilder.loadTexts:
    rstpDefaultPathCostGroup.setStatus("current")

rstpPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 5, 1, 3)
)
rstpPortGroup.setObjects(
      *(("RUIJIE-RSTP-MSTP-MIB", "ruijieRstpExtPortIfIndex"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpPortProtocolMigration"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpPortAdminEdgePort"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpPortOperEdgePort"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpPortAdminPointToPoint"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpPortOperPointToPoint"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpPortBpduGuard"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpPortBpduFilter"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpCistRegionRoot"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpCistPathCost"))
)
if mibBuilder.loadTexts:
    rstpPortGroup.setStatus("current")

mstpBridgeRegionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 6, 1, 1)
)
mstpBridgeRegionGroup.setObjects(
      *(("RUIJIE-RSTP-MSTP-MIB", "ruijieStpMstiMaxInstanceNumber"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpMstiRegionName"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpMstiRegionRevision"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpMstiMaxHopNumber"))
)
if mibBuilder.loadTexts:
    mstpBridgeRegionGroup.setStatus("current")

mstpMstiBridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 6, 1, 2)
)
mstpMstiBridgeGroup.setObjects(
      *(("RUIJIE-RSTP-MSTP-MIB", "ruijieStpMstiInstanceIndex"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpMstiInstanceVlansAddMapped"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpMstiInstanceVlansDeleteMapped"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpMstiInstanceVlansGetMapped"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpMstiInstanceRemainingHopCount"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpMstiPriority"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpMstiTimeSinceTopologyChange"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpMstiTopChanges"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpMstiDesignatedRoot"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpMstiRootCost"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpMstiRootPort"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpMstiInstanceEntryStatus"))
)
if mibBuilder.loadTexts:
    mstpMstiBridgeGroup.setStatus("current")

mstpMstiPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 6, 1, 3)
)
mstpMstiPortGroup.setObjects(
      *(("RUIJIE-RSTP-MSTP-MIB", "ruijieStpPortMstiState"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpPortMstiAdminPathCost"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpPortMstiOperPathCost"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpPortMstiPriority"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpPortMstiDesignatedRoot"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpPortMstiDesignatedCost"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpPortMstiDesignatedBridge"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpPortMstiDesignatedPort"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpPortMstiPortRole"),
        ("RUIJIE-RSTP-MSTP-MIB", "ruijieStpPortMstiPortForwardTransitions"))
)
if mibBuilder.loadTexts:
    mstpMstiPortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rstpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 5, 2, 1)
)
rstpCompliance.setObjects(
      *(("RUIJIE-RSTP-MSTP-MIB", "rstpBridgeGroup"),
        ("RUIJIE-RSTP-MSTP-MIB", "rstpDefaultPathCostGroup"),
        ("RUIJIE-RSTP-MSTP-MIB", "rstpPortGroup"),
        ("RUIJIE-RSTP-MSTP-MIB", "rstpDefaultPathCostGroup"))
)
if mibBuilder.loadTexts:
    rstpCompliance.setStatus(
        "current"
    )

mstpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 16, 6, 2, 1)
)
mstpCompliance.setObjects(
      *(("RUIJIE-RSTP-MSTP-MIB", "mstpBridgeRegionGroup"),
        ("RUIJIE-RSTP-MSTP-MIB", "mstpMstiBridgeGroup"),
        ("RUIJIE-RSTP-MSTP-MIB", "mstpMstiPortGroup"))
)
if mibBuilder.loadTexts:
    mstpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-RSTP-MSTP-MIB",
    **{"ruijieStpMIB": ruijieStpMIB,
       "ruijieStpMIBObjects": ruijieStpMIBObjects,
       "ruijieSysStpStatus": ruijieSysStpStatus,
       "ruijieSysStpReset": ruijieSysStpReset,
       "ruijieStpExtPortTable": ruijieStpExtPortTable,
       "ruijieStpExtPortEntry": ruijieStpExtPortEntry,
       "ruijieStpPortIfIndex": ruijieStpPortIfIndex,
       "ruijieStpPortAdminPathCost": ruijieStpPortAdminPathCost,
       "ruijieStpPortOperPathCost": ruijieStpPortOperPathCost,
       "ruijieStpPortRole": ruijieStpPortRole,
       "ruijieRstpMIBObjects": ruijieRstpMIBObjects,
       "ruijieStpVersion": ruijieStpVersion,
       "ruijieStpTxHoldCount": ruijieStpTxHoldCount,
       "ruijieStpPathCostDefault": ruijieStpPathCostDefault,
       "ruijieRstpExtPortTable": ruijieRstpExtPortTable,
       "ruijieRstpExtPortEntry": ruijieRstpExtPortEntry,
       "ruijieRstpExtPortIfIndex": ruijieRstpExtPortIfIndex,
       "ruijieStpPortProtocolMigration": ruijieStpPortProtocolMigration,
       "ruijieStpPortAdminEdgePort": ruijieStpPortAdminEdgePort,
       "ruijieStpPortOperEdgePort": ruijieStpPortOperEdgePort,
       "ruijieStpPortAdminPointToPoint": ruijieStpPortAdminPointToPoint,
       "ruijieStpPortOperPointToPoint": ruijieStpPortOperPointToPoint,
       "ruijieStpPortBpduGuard": ruijieStpPortBpduGuard,
       "ruijieStpPortBpduFilter": ruijieStpPortBpduFilter,
       "ruijieStpBpduGuard": ruijieStpBpduGuard,
       "ruijieStpBpduFilter": ruijieStpBpduFilter,
       "ruijieStpCistRegionRoot": ruijieStpCistRegionRoot,
       "ruijieStpCistPathCost": ruijieStpCistPathCost,
       "ruijieMstpMIBObjects": ruijieMstpMIBObjects,
       "ruijieStpMstiMaxInstanceNumber": ruijieStpMstiMaxInstanceNumber,
       "ruijieStpMstiRegionName": ruijieStpMstiRegionName,
       "ruijieStpMstiRegionRevision": ruijieStpMstiRegionRevision,
       "ruijieStpMstiMaxHopNumber": ruijieStpMstiMaxHopNumber,
       "ruijieStpMstiInstanceTable": ruijieStpMstiInstanceTable,
       "ruijieStpMstiInstanceEntry": ruijieStpMstiInstanceEntry,
       "ruijieStpMstiInstanceIndex": ruijieStpMstiInstanceIndex,
       "ruijieStpMstiInstanceVlansAddMapped": ruijieStpMstiInstanceVlansAddMapped,
       "ruijieStpMstiInstanceVlansDeleteMapped": ruijieStpMstiInstanceVlansDeleteMapped,
       "ruijieStpMstiInstanceVlansGetMapped": ruijieStpMstiInstanceVlansGetMapped,
       "ruijieStpMstiInstanceRemainingHopCount": ruijieStpMstiInstanceRemainingHopCount,
       "ruijieStpMstiPriority": ruijieStpMstiPriority,
       "ruijieStpMstiTimeSinceTopologyChange": ruijieStpMstiTimeSinceTopologyChange,
       "ruijieStpMstiTopChanges": ruijieStpMstiTopChanges,
       "ruijieStpMstiDesignatedRoot": ruijieStpMstiDesignatedRoot,
       "ruijieStpMstiRootCost": ruijieStpMstiRootCost,
       "ruijieStpMstiRootPort": ruijieStpMstiRootPort,
       "ruijieStpMstiInstanceEntryStatus": ruijieStpMstiInstanceEntryStatus,
       "ruijieStpPortMstiInstanceTable": ruijieStpPortMstiInstanceTable,
       "ruijieStpPortMstiInstanceEntry": ruijieStpPortMstiInstanceEntry,
       "ruijieStpPortMstiIndex": ruijieStpPortMstiIndex,
       "ruijieStpPortMstiState": ruijieStpPortMstiState,
       "ruijieStpPortMstiAdminPathCost": ruijieStpPortMstiAdminPathCost,
       "ruijieStpPortMstiOperPathCost": ruijieStpPortMstiOperPathCost,
       "ruijieStpPortMstiPriority": ruijieStpPortMstiPriority,
       "ruijieStpPortMstiDesignatedRoot": ruijieStpPortMstiDesignatedRoot,
       "ruijieStpPortMstiDesignatedCost": ruijieStpPortMstiDesignatedCost,
       "ruijieStpPortMstiDesignatedBridge": ruijieStpPortMstiDesignatedBridge,
       "ruijieStpPortMstiDesignatedPort": ruijieStpPortMstiDesignatedPort,
       "ruijieStpPortMstiPortRole": ruijieStpPortMstiPortRole,
       "ruijieStpPortMstiPortForwardTransitions": ruijieStpPortMstiPortForwardTransitions,
       "ruijieStpMstiReset": ruijieStpMstiReset,
       "ruijieStpCistVlansAddMapped": ruijieStpCistVlansAddMapped,
       "ruijieStpCistVlansGetMapped": ruijieStpCistVlansGetMapped,
       "ruijieStpCistRemainingHopCount": ruijieStpCistRemainingHopCount,
       "stpExternConformance": stpExternConformance,
       "stpExternGroups": stpExternGroups,
       "stpExternGroup": stpExternGroup,
       "rstpConformance": rstpConformance,
       "rstpGroups": rstpGroups,
       "rstpBridgeGroup": rstpBridgeGroup,
       "rstpDefaultPathCostGroup": rstpDefaultPathCostGroup,
       "rstpPortGroup": rstpPortGroup,
       "rstpCompliances": rstpCompliances,
       "rstpCompliance": rstpCompliance,
       "mstpConformance": mstpConformance,
       "mstpGroups": mstpGroups,
       "mstpBridgeRegionGroup": mstpBridgeRegionGroup,
       "mstpMstiBridgeGroup": mstpMstiBridgeGroup,
       "mstpMstiPortGroup": mstpMstiPortGroup,
       "mstpCompliances": mstpCompliances,
       "mstpCompliance": mstpCompliance}
)
