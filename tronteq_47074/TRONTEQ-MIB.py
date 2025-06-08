# SNMP MIB module (TRONTEQ-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/tronteq_47074/TRONTEQ-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:05:15 2025
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

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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
 NotificationType,
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
    "NotificationType",
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

tronteqElectronic = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47074)
)
if mibBuilder.loadTexts:
    tronteqElectronic.setRevisions(
        ("2016-10-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47074, 2)
)
_Roqstar_ObjectIdentity = ObjectIdentity
roqstar = _Roqstar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47074, 2, 1)
)
_EightPortLite_ObjectIdentity = ObjectIdentity
eightPortLite = _EightPortLite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47074, 2, 1, 1)
)
_EightPortManaged_ObjectIdentity = ObjectIdentity
eightPortManaged = _EightPortManaged_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47074, 2, 1, 2)
)
_TenPortSecurity_ObjectIdentity = ObjectIdentity
tenPortSecurity = _TenPortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47074, 2, 1, 3)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47074, 3)
)
_TrapTempHighAlarm_ObjectIdentity = ObjectIdentity
trapTempHighAlarm = _TrapTempHighAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47074, 3, 2)
)
_TrapTempLowAlarm_ObjectIdentity = ObjectIdentity
trapTempLowAlarm = _TrapTempLowAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47074, 3, 3)
)
_TrapTempNormalAlarm_ObjectIdentity = ObjectIdentity
trapTempNormalAlarm = _TrapTempNormalAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47074, 3, 4)
)
_CableDiag_ObjectIdentity = ObjectIdentity
cableDiag = _CableDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47074, 4)
)
_CableDiagIfNumber_Type = Integer32
_CableDiagIfNumber_Object = MibScalar
cableDiagIfNumber = _CableDiagIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 47074, 4, 1),
    _CableDiagIfNumber_Type()
)
cableDiagIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagIfNumber.setStatus("current")
_CableDiagTable_Object = MibTable
cableDiagTable = _CableDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 47074, 4, 2)
)
if mibBuilder.loadTexts:
    cableDiagTable.setStatus("current")
_CableDiagEntry_Object = MibTableRow
cableDiagEntry = _CableDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 47074, 4, 2, 1)
)
cableDiagEntry.setIndexNames(
    (0, "TRONTEQ-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cableDiagEntry.setStatus("current")


class _IfIndex_Type(Integer32):
    """Custom type ifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IfIndex_Type.__name__ = "Integer32"
_IfIndex_Object = MibTableColumn
ifIndex = _IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 47074, 4, 2, 1, 1),
    _IfIndex_Type()
)
ifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifIndex.setStatus("current")
_DiagType_Type = DisplayString
_DiagType_Object = MibTableColumn
diagType = _DiagType_Object(
    (1, 3, 6, 1, 4, 1, 47074, 4, 2, 1, 2),
    _DiagType_Type()
)
diagType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagType.setStatus("current")


class _DiagState_Type(Integer32):
    """Custom type diagState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notStarted", 1),
          ("inProgress", 2),
          ("failed", 3),
          ("finished", 4))
    )


_DiagState_Type.__name__ = "Integer32"
_DiagState_Object = MibTableColumn
diagState = _DiagState_Object(
    (1, 3, 6, 1, 4, 1, 47074, 4, 2, 1, 3),
    _DiagState_Type()
)
diagState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagState.setStatus("current")
_PairNumber_Type = Integer32
_PairNumber_Object = MibTableColumn
pairNumber = _PairNumber_Object(
    (1, 3, 6, 1, 4, 1, 47074, 4, 2, 1, 4),
    _PairNumber_Type()
)
pairNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pairNumber.setStatus("current")
_Result_Type = ObjectIdentifier
_Result_Object = MibTableColumn
result = _Result_Object(
    (1, 3, 6, 1, 4, 1, 47074, 4, 2, 1, 5),
    _Result_Type()
)
result.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    result.setStatus("current")
_PairTable_Object = MibTable
pairTable = _PairTable_Object(
    (1, 3, 6, 1, 4, 1, 47074, 4, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    pairTable.setStatus("current")
_PairEntry_Object = MibTableRow
pairEntry = _PairEntry_Object(
    (1, 3, 6, 1, 4, 1, 47074, 4, 2, 1, 5, 1, 1)
)
pairEntry.setIndexNames(
    (0, "TRONTEQ-MIB", "pairIndex"),
)
if mibBuilder.loadTexts:
    pairEntry.setStatus("current")


class _PairIndex_Type(Integer32):
    """Custom type pairIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PairIndex_Type.__name__ = "Integer32"
_PairIndex_Object = MibTableColumn
pairIndex = _PairIndex_Object(
    (1, 3, 6, 1, 4, 1, 47074, 4, 2, 1, 5, 1, 1, 1),
    _PairIndex_Type()
)
pairIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pairIndex.setStatus("current")
_PairState_Type = DisplayString
_PairState_Object = MibTableColumn
pairState = _PairState_Object(
    (1, 3, 6, 1, 4, 1, 47074, 4, 2, 1, 5, 1, 1, 2),
    _PairState_Type()
)
pairState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pairState.setStatus("current")
_FaultDistance_Type = Integer32
_FaultDistance_Object = MibTableColumn
faultDistance = _FaultDistance_Object(
    (1, 3, 6, 1, 4, 1, 47074, 4, 2, 1, 5, 1, 1, 3),
    _FaultDistance_Type()
)
faultDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultDistance.setStatus("current")

# Managed Objects groups


# Notification objects

temphighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 47074, 3, 2, 0, 1)
)
if mibBuilder.loadTexts:
    temphighTrap.setStatus(
        ""
    )

templowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 47074, 3, 3, 0, 2)
)
if mibBuilder.loadTexts:
    templowTrap.setStatus(
        ""
    )

tempnormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 47074, 3, 4, 0, 3)
)
if mibBuilder.loadTexts:
    tempnormalTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRONTEQ-MIB",
    **{"tronteqElectronic": tronteqElectronic,
       "products": products,
       "roqstar": roqstar,
       "eightPortLite": eightPortLite,
       "eightPortManaged": eightPortManaged,
       "tenPortSecurity": tenPortSecurity,
       "traps": traps,
       "trapTempHighAlarm": trapTempHighAlarm,
       "temphighTrap": temphighTrap,
       "trapTempLowAlarm": trapTempLowAlarm,
       "templowTrap": templowTrap,
       "trapTempNormalAlarm": trapTempNormalAlarm,
       "tempnormalTrap": tempnormalTrap,
       "cableDiag": cableDiag,
       "cableDiagIfNumber": cableDiagIfNumber,
       "cableDiagTable": cableDiagTable,
       "cableDiagEntry": cableDiagEntry,
       "ifIndex": ifIndex,
       "diagType": diagType,
       "diagState": diagState,
       "pairNumber": pairNumber,
       "result": result,
       "pairTable": pairTable,
       "pairEntry": pairEntry,
       "pairIndex": pairIndex,
       "pairState": pairState,
       "faultDistance": faultDistance}
)
