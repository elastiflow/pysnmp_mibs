# SNMP MIB module (TROPIC-VTSCONN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-VTSCONN-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:59:16 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(tnPortModules,
 tnVtsConnMIB) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnPortModules",
    "tnVtsConnMIB")


# MODULE-IDENTITY

tnVtsConnMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 4, 4)
)
if mibBuilder.loadTexts:
    tnVtsConnMibModule.setRevisions(
        ("2009-04-27 12:00",
         "2009-05-31 12:00",
         "2009-06-18 12:00",
         "2009-07-07 12:00",
         "2009-07-17 12:00",
         "2010-03-03 12:00",
         "2010-05-18 12:00",
         "2010-06-04 12:00",
         "2010-06-23 12:00",
         "2010-10-14 12:00",
         "2010-10-26 12:00",
         "2011-02-22 12:00",
         "2011-02-25 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AluWdmVtsCmodeMapCMode(TextualConvention, Integer32):
    status = "current"
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
        *(("cvlan", 1),
          ("svlan", 2),
          ("sip", 3),
          ("dip", 4),
          ("sipdip", 5),
          ("port", 6),
          ("untagged", 7))
    )



# MIB Managed Objects in the order of their OIDs

_TnVtsConnConf_ObjectIdentity = ObjectIdentity
tnVtsConnConf = _TnVtsConnConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 1)
)
_TnVtsConnGroups_ObjectIdentity = ObjectIdentity
tnVtsConnGroups = _TnVtsConnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 1, 1)
)
_TnVtsConnCompliances_ObjectIdentity = ObjectIdentity
tnVtsConnCompliances = _TnVtsConnCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 1, 2)
)
_TnVtsConnObjs_ObjectIdentity = ObjectIdentity
tnVtsConnObjs = _TnVtsConnObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2)
)
_TnVtsConnBasics_ObjectIdentity = ObjectIdentity
tnVtsConnBasics = _TnVtsConnBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1)
)
_TnVtsConnTable_Object = MibTable
tnVtsConnTable = _TnVtsConnTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnVtsConnTable.setStatus("current")
_TnVtsConnEntry_Object = MibTableRow
tnVtsConnEntry = _TnVtsConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 1, 1)
)
tnVtsConnEntry.setIndexNames(
    (0, "TROPIC-VTSCONN-MIB", "tnVtsConnSrcIfIndex"),
    (0, "TROPIC-VTSCONN-MIB", "tnVtsConnSrcVts"),
    (0, "TROPIC-VTSCONN-MIB", "tnVtsConnDestIfIndex"),
    (0, "TROPIC-VTSCONN-MIB", "tnVtsConnDestVts"),
)
if mibBuilder.loadTexts:
    tnVtsConnEntry.setStatus("current")
_TnVtsConnSrcIfIndex_Type = InterfaceIndex
_TnVtsConnSrcIfIndex_Object = MibTableColumn
tnVtsConnSrcIfIndex = _TnVtsConnSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 1, 1, 1),
    _TnVtsConnSrcIfIndex_Type()
)
tnVtsConnSrcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVtsConnSrcIfIndex.setStatus("current")
_TnVtsConnSrcVts_Type = Unsigned32
_TnVtsConnSrcVts_Object = MibTableColumn
tnVtsConnSrcVts = _TnVtsConnSrcVts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 1, 1, 2),
    _TnVtsConnSrcVts_Type()
)
tnVtsConnSrcVts.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVtsConnSrcVts.setStatus("current")
_TnVtsConnDestIfIndex_Type = InterfaceIndex
_TnVtsConnDestIfIndex_Object = MibTableColumn
tnVtsConnDestIfIndex = _TnVtsConnDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 1, 1, 3),
    _TnVtsConnDestIfIndex_Type()
)
tnVtsConnDestIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVtsConnDestIfIndex.setStatus("current")
_TnVtsConnDestVts_Type = Unsigned32
_TnVtsConnDestVts_Object = MibTableColumn
tnVtsConnDestVts = _TnVtsConnDestVts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 1, 1, 4),
    _TnVtsConnDestVts_Type()
)
tnVtsConnDestVts.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVtsConnDestVts.setStatus("current")


class _TnVtsConnAdminState_Type(Integer32):
    """Custom type tnVtsConnAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_TnVtsConnAdminState_Type.__name__ = "Integer32"
_TnVtsConnAdminState_Object = MibTableColumn
tnVtsConnAdminState = _TnVtsConnAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 1, 1, 5),
    _TnVtsConnAdminState_Type()
)
tnVtsConnAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVtsConnAdminState.setStatus("current")


class _TnVtsConnOperState_Type(Integer32):
    """Custom type tnVtsConnOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_TnVtsConnOperState_Type.__name__ = "Integer32"
_TnVtsConnOperState_Object = MibTableColumn
tnVtsConnOperState = _TnVtsConnOperState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 1, 1, 6),
    _TnVtsConnOperState_Type()
)
tnVtsConnOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVtsConnOperState.setStatus("current")


class _TnVtsConnBidirectional_Type(TruthValue):
    """Custom type tnVtsConnBidirectional based on TruthValue"""
    defaultValue = 1


_TnVtsConnBidirectional_Type.__name__ = "TruthValue"
_TnVtsConnBidirectional_Object = MibTableColumn
tnVtsConnBidirectional = _TnVtsConnBidirectional_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 1, 1, 7),
    _TnVtsConnBidirectional_Type()
)
tnVtsConnBidirectional.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVtsConnBidirectional.setStatus("current")


class _TnVtsConnName_Type(OctetString):
    """Custom type tnVtsConnName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TnVtsConnName_Type.__name__ = "OctetString"
_TnVtsConnName_Object = MibTableColumn
tnVtsConnName = _TnVtsConnName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 1, 1, 8),
    _TnVtsConnName_Type()
)
tnVtsConnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVtsConnName.setStatus("current")


class _TnVtsConnCIR_Type(Unsigned32):
    """Custom type tnVtsConnCIR based on Unsigned32"""
    defaultValue = 100


_TnVtsConnCIR_Type.__name__ = "Unsigned32"
_TnVtsConnCIR_Object = MibTableColumn
tnVtsConnCIR = _TnVtsConnCIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 1, 1, 9),
    _TnVtsConnCIR_Type()
)
tnVtsConnCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVtsConnCIR.setStatus("current")


class _TnVtsConnEIR_Type(Unsigned32):
    """Custom type tnVtsConnEIR based on Unsigned32"""
    defaultValue = 1000


_TnVtsConnEIR_Type.__name__ = "Unsigned32"
_TnVtsConnEIR_Object = MibTableColumn
tnVtsConnEIR = _TnVtsConnEIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 1, 1, 10),
    _TnVtsConnEIR_Type()
)
tnVtsConnEIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVtsConnEIR.setStatus("current")


class _TnVtsConnCBS_Type(Unsigned32):
    """Custom type tnVtsConnCBS based on Unsigned32"""
    defaultValue = 256


_TnVtsConnCBS_Type.__name__ = "Unsigned32"
_TnVtsConnCBS_Object = MibTableColumn
tnVtsConnCBS = _TnVtsConnCBS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 1, 1, 11),
    _TnVtsConnCBS_Type()
)
tnVtsConnCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVtsConnCBS.setStatus("current")


class _TnVtsConnEBS_Type(Unsigned32):
    """Custom type tnVtsConnEBS based on Unsigned32"""
    defaultValue = 4096


_TnVtsConnEBS_Type.__name__ = "Unsigned32"
_TnVtsConnEBS_Object = MibTableColumn
tnVtsConnEBS = _TnVtsConnEBS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 1, 1, 12),
    _TnVtsConnEBS_Type()
)
tnVtsConnEBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVtsConnEBS.setStatus("current")
_TnVtsConnRowStatus_Type = RowStatus
_TnVtsConnRowStatus_Object = MibTableColumn
tnVtsConnRowStatus = _TnVtsConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 1, 1, 13),
    _TnVtsConnRowStatus_Type()
)
tnVtsConnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVtsConnRowStatus.setStatus("current")
_TnVtsConnId_Type = Unsigned32
_TnVtsConnId_Object = MibTableColumn
tnVtsConnId = _TnVtsConnId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 1, 1, 14),
    _TnVtsConnId_Type()
)
tnVtsConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVtsConnId.setStatus("current")


class _TnVtsConnProtectionState_Type(Integer32):
    """Custom type tnVtsConnProtectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("working", 2),
          ("protection", 3))
    )


_TnVtsConnProtectionState_Type.__name__ = "Integer32"
_TnVtsConnProtectionState_Object = MibTableColumn
tnVtsConnProtectionState = _TnVtsConnProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 1, 1, 15),
    _TnVtsConnProtectionState_Type()
)
tnVtsConnProtectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVtsConnProtectionState.setStatus("current")
_TnVtsMapTable_Object = MibTable
tnVtsMapTable = _TnVtsMapTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tnVtsMapTable.setStatus("current")
_TnVtsMapEntry_Object = MibTableRow
tnVtsMapEntry = _TnVtsMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 2, 1)
)
tnVtsMapEntry.setIndexNames(
    (0, "TROPIC-VTSCONN-MIB", "tnVtsMapIfIndex"),
    (0, "TROPIC-VTSCONN-MIB", "tnVtsMapVts"),
)
if mibBuilder.loadTexts:
    tnVtsMapEntry.setStatus("current")
_TnVtsMapIfIndex_Type = InterfaceIndex
_TnVtsMapIfIndex_Object = MibTableColumn
tnVtsMapIfIndex = _TnVtsMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 2, 1, 1),
    _TnVtsMapIfIndex_Type()
)
tnVtsMapIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVtsMapIfIndex.setStatus("current")
_TnVtsMapVts_Type = Unsigned32
_TnVtsMapVts_Object = MibTableColumn
tnVtsMapVts = _TnVtsMapVts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 2, 1, 2),
    _TnVtsMapVts_Type()
)
tnVtsMapVts.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVtsMapVts.setStatus("current")


class _TnVtsMapCEVLANID_Type(OctetString):
    """Custom type tnVtsMapCEVLANID based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnVtsMapCEVLANID_Type.__name__ = "OctetString"
_TnVtsMapCEVLANID_Object = MibTableColumn
tnVtsMapCEVLANID = _TnVtsMapCEVLANID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 2, 1, 3),
    _TnVtsMapCEVLANID_Type()
)
tnVtsMapCEVLANID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVtsMapCEVLANID.setStatus("current")
_TnVtsMapSVLANID_Type = Unsigned32
_TnVtsMapSVLANID_Object = MibTableColumn
tnVtsMapSVLANID = _TnVtsMapSVLANID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 2, 1, 5),
    _TnVtsMapSVLANID_Type()
)
tnVtsMapSVLANID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVtsMapSVLANID.setStatus("current")
_TnVtsConnIdTable_Object = MibTable
tnVtsConnIdTable = _TnVtsConnIdTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tnVtsConnIdTable.setStatus("current")
_TnVtsConnIdEntry_Object = MibTableRow
tnVtsConnIdEntry = _TnVtsConnIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 3, 1)
)
tnVtsConnIdEntry.setIndexNames(
    (0, "TROPIC-VTSCONN-MIB", "tnVtsConnId"),
)
if mibBuilder.loadTexts:
    tnVtsConnIdEntry.setStatus("current")
_TnVtsConnIdSrcIfIndex_Type = InterfaceIndex
_TnVtsConnIdSrcIfIndex_Object = MibTableColumn
tnVtsConnIdSrcIfIndex = _TnVtsConnIdSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 3, 1, 1),
    _TnVtsConnIdSrcIfIndex_Type()
)
tnVtsConnIdSrcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVtsConnIdSrcIfIndex.setStatus("current")
_TnVtsConnIdSrcVts_Type = Unsigned32
_TnVtsConnIdSrcVts_Object = MibTableColumn
tnVtsConnIdSrcVts = _TnVtsConnIdSrcVts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 3, 1, 2),
    _TnVtsConnIdSrcVts_Type()
)
tnVtsConnIdSrcVts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVtsConnIdSrcVts.setStatus("current")
_TnVtsConnIdDestIfIndex_Type = InterfaceIndex
_TnVtsConnIdDestIfIndex_Object = MibTableColumn
tnVtsConnIdDestIfIndex = _TnVtsConnIdDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 3, 1, 3),
    _TnVtsConnIdDestIfIndex_Type()
)
tnVtsConnIdDestIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVtsConnIdDestIfIndex.setStatus("current")
_TnVtsConnIdDestVts_Type = Unsigned32
_TnVtsConnIdDestVts_Object = MibTableColumn
tnVtsConnIdDestVts = _TnVtsConnIdDestVts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 3, 1, 4),
    _TnVtsConnIdDestVts_Type()
)
tnVtsConnIdDestVts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVtsConnIdDestVts.setStatus("current")
_TnIngressVtsMapTable_Object = MibTable
tnIngressVtsMapTable = _TnIngressVtsMapTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tnIngressVtsMapTable.setStatus("current")
_TnIngressVtsMapEntry_Object = MibTableRow
tnIngressVtsMapEntry = _TnIngressVtsMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 4, 1)
)
tnIngressVtsMapEntry.setIndexNames(
    (0, "TROPIC-VTSCONN-MIB", "tnVtsMapIfIndex"),
    (0, "TROPIC-VTSCONN-MIB", "tnVtsMapVts"),
)
if mibBuilder.loadTexts:
    tnIngressVtsMapEntry.setStatus("current")


class _TnIngressVtsMapCEVLANID_Type(OctetString):
    """Custom type tnIngressVtsMapCEVLANID based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnIngressVtsMapCEVLANID_Type.__name__ = "OctetString"
_TnIngressVtsMapCEVLANID_Object = MibTableColumn
tnIngressVtsMapCEVLANID = _TnIngressVtsMapCEVLANID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 4, 1, 1),
    _TnIngressVtsMapCEVLANID_Type()
)
tnIngressVtsMapCEVLANID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIngressVtsMapCEVLANID.setStatus("current")
_TnIngressVtsMapSVLANID_Type = Unsigned32
_TnIngressVtsMapSVLANID_Object = MibTableColumn
tnIngressVtsMapSVLANID = _TnIngressVtsMapSVLANID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 4, 1, 2),
    _TnIngressVtsMapSVLANID_Type()
)
tnIngressVtsMapSVLANID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIngressVtsMapSVLANID.setStatus("current")
_TnEgressVtsMapTable_Object = MibTable
tnEgressVtsMapTable = _TnEgressVtsMapTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tnEgressVtsMapTable.setStatus("current")
_TnEgressVtsMapEntry_Object = MibTableRow
tnEgressVtsMapEntry = _TnEgressVtsMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 5, 1)
)
tnEgressVtsMapEntry.setIndexNames(
    (0, "TROPIC-VTSCONN-MIB", "tnVtsMapIfIndex"),
    (0, "TROPIC-VTSCONN-MIB", "tnVtsMapVts"),
)
if mibBuilder.loadTexts:
    tnEgressVtsMapEntry.setStatus("current")


class _TnEgressVtsMapCEVLANID_Type(OctetString):
    """Custom type tnEgressVtsMapCEVLANID based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnEgressVtsMapCEVLANID_Type.__name__ = "OctetString"
_TnEgressVtsMapCEVLANID_Object = MibTableColumn
tnEgressVtsMapCEVLANID = _TnEgressVtsMapCEVLANID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 5, 1, 1),
    _TnEgressVtsMapCEVLANID_Type()
)
tnEgressVtsMapCEVLANID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEgressVtsMapCEVLANID.setStatus("current")
_TnEgressVtsMapSVLANID_Type = Unsigned32
_TnEgressVtsMapSVLANID_Object = MibTableColumn
tnEgressVtsMapSVLANID = _TnEgressVtsMapSVLANID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 5, 1, 2),
    _TnEgressVtsMapSVLANID_Type()
)
tnEgressVtsMapSVLANID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEgressVtsMapSVLANID.setStatus("current")
_TnIngressVtsCmodeMapTable_Object = MibTable
tnIngressVtsCmodeMapTable = _TnIngressVtsCmodeMapTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tnIngressVtsCmodeMapTable.setStatus("current")
_TnIngressVtsCmodeMapEntry_Object = MibTableRow
tnIngressVtsCmodeMapEntry = _TnIngressVtsCmodeMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 6, 1)
)
tnIngressVtsCmodeMapEntry.setIndexNames(
    (0, "TROPIC-VTSCONN-MIB", "tnVtsMapIfIndex"),
    (0, "TROPIC-VTSCONN-MIB", "tnVtsMapVts"),
)
if mibBuilder.loadTexts:
    tnIngressVtsCmodeMapEntry.setStatus("current")


class _TnIngressVtsCmodeMapCEVLANID_Type(OctetString):
    """Custom type tnIngressVtsCmodeMapCEVLANID based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnIngressVtsCmodeMapCEVLANID_Type.__name__ = "OctetString"
_TnIngressVtsCmodeMapCEVLANID_Object = MibTableColumn
tnIngressVtsCmodeMapCEVLANID = _TnIngressVtsCmodeMapCEVLANID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 6, 1, 1),
    _TnIngressVtsCmodeMapCEVLANID_Type()
)
tnIngressVtsCmodeMapCEVLANID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIngressVtsCmodeMapCEVLANID.setStatus("current")
_TnIngressVtsCmodeMapSVLANID_Type = Unsigned32
_TnIngressVtsCmodeMapSVLANID_Object = MibTableColumn
tnIngressVtsCmodeMapSVLANID = _TnIngressVtsCmodeMapSVLANID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 6, 1, 2),
    _TnIngressVtsCmodeMapSVLANID_Type()
)
tnIngressVtsCmodeMapSVLANID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIngressVtsCmodeMapSVLANID.setStatus("current")
_TnIngressVtsCmodeMapSIP_Type = IpAddress
_TnIngressVtsCmodeMapSIP_Object = MibTableColumn
tnIngressVtsCmodeMapSIP = _TnIngressVtsCmodeMapSIP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 6, 1, 3),
    _TnIngressVtsCmodeMapSIP_Type()
)
tnIngressVtsCmodeMapSIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIngressVtsCmodeMapSIP.setStatus("current")
_TnIngressVtsCmodeMapDIP_Type = IpAddress
_TnIngressVtsCmodeMapDIP_Object = MibTableColumn
tnIngressVtsCmodeMapDIP = _TnIngressVtsCmodeMapDIP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 6, 1, 4),
    _TnIngressVtsCmodeMapDIP_Type()
)
tnIngressVtsCmodeMapDIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIngressVtsCmodeMapDIP.setStatus("current")
_TnIngressVtsCmodeMapCMode_Type = AluWdmVtsCmodeMapCMode
_TnIngressVtsCmodeMapCMode_Object = MibTableColumn
tnIngressVtsCmodeMapCMode = _TnIngressVtsCmodeMapCMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 6, 1, 5),
    _TnIngressVtsCmodeMapCMode_Type()
)
tnIngressVtsCmodeMapCMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIngressVtsCmodeMapCMode.setStatus("current")
_TnIngressVtsCmodeMapRowStatus_Type = RowStatus
_TnIngressVtsCmodeMapRowStatus_Object = MibTableColumn
tnIngressVtsCmodeMapRowStatus = _TnIngressVtsCmodeMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 6, 1, 6),
    _TnIngressVtsCmodeMapRowStatus_Type()
)
tnIngressVtsCmodeMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIngressVtsCmodeMapRowStatus.setStatus("current")
_TnEgressVtsCmodeMapTable_Object = MibTable
tnEgressVtsCmodeMapTable = _TnEgressVtsCmodeMapTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 7)
)
if mibBuilder.loadTexts:
    tnEgressVtsCmodeMapTable.setStatus("current")
_TnEgressVtsCmodeMapEntry_Object = MibTableRow
tnEgressVtsCmodeMapEntry = _TnEgressVtsCmodeMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 7, 1)
)
tnEgressVtsCmodeMapEntry.setIndexNames(
    (0, "TROPIC-VTSCONN-MIB", "tnVtsMapIfIndex"),
    (0, "TROPIC-VTSCONN-MIB", "tnVtsMapVts"),
)
if mibBuilder.loadTexts:
    tnEgressVtsCmodeMapEntry.setStatus("current")


class _TnEgressVtsCmodeMapCEVLANID_Type(OctetString):
    """Custom type tnEgressVtsCmodeMapCEVLANID based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnEgressVtsCmodeMapCEVLANID_Type.__name__ = "OctetString"
_TnEgressVtsCmodeMapCEVLANID_Object = MibTableColumn
tnEgressVtsCmodeMapCEVLANID = _TnEgressVtsCmodeMapCEVLANID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 7, 1, 1),
    _TnEgressVtsCmodeMapCEVLANID_Type()
)
tnEgressVtsCmodeMapCEVLANID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEgressVtsCmodeMapCEVLANID.setStatus("current")
_TnEgressVtsCmodeMapSVLANID_Type = Unsigned32
_TnEgressVtsCmodeMapSVLANID_Object = MibTableColumn
tnEgressVtsCmodeMapSVLANID = _TnEgressVtsCmodeMapSVLANID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 7, 1, 2),
    _TnEgressVtsCmodeMapSVLANID_Type()
)
tnEgressVtsCmodeMapSVLANID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEgressVtsCmodeMapSVLANID.setStatus("current")
_TnEgressVtsCmodeMapSIP_Type = IpAddress
_TnEgressVtsCmodeMapSIP_Object = MibTableColumn
tnEgressVtsCmodeMapSIP = _TnEgressVtsCmodeMapSIP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 7, 1, 3),
    _TnEgressVtsCmodeMapSIP_Type()
)
tnEgressVtsCmodeMapSIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEgressVtsCmodeMapSIP.setStatus("current")
_TnEgressVtsCmodeMapDIP_Type = IpAddress
_TnEgressVtsCmodeMapDIP_Object = MibTableColumn
tnEgressVtsCmodeMapDIP = _TnEgressVtsCmodeMapDIP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 7, 1, 4),
    _TnEgressVtsCmodeMapDIP_Type()
)
tnEgressVtsCmodeMapDIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEgressVtsCmodeMapDIP.setStatus("current")
_TnEgressVtsCmodeMapCMode_Type = AluWdmVtsCmodeMapCMode
_TnEgressVtsCmodeMapCMode_Object = MibTableColumn
tnEgressVtsCmodeMapCMode = _TnEgressVtsCmodeMapCMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 7, 1, 5),
    _TnEgressVtsCmodeMapCMode_Type()
)
tnEgressVtsCmodeMapCMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEgressVtsCmodeMapCMode.setStatus("current")
_TnEgressVtsCmodeMapRowStatus_Type = RowStatus
_TnEgressVtsCmodeMapRowStatus_Object = MibTableColumn
tnEgressVtsCmodeMapRowStatus = _TnEgressVtsCmodeMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 2, 1, 7, 1, 6),
    _TnEgressVtsCmodeMapRowStatus_Type()
)
tnEgressVtsCmodeMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEgressVtsCmodeMapRowStatus.setStatus("current")

# Managed Objects groups

tnVtsConnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 1, 1, 1)
)
tnVtsConnGroup.setObjects(
      *(("TROPIC-VTSCONN-MIB", "tnVtsConnAdminState"),
        ("TROPIC-VTSCONN-MIB", "tnVtsConnOperState"),
        ("TROPIC-VTSCONN-MIB", "tnVtsConnBidirectional"),
        ("TROPIC-VTSCONN-MIB", "tnVtsConnName"),
        ("TROPIC-VTSCONN-MIB", "tnVtsConnCIR"),
        ("TROPIC-VTSCONN-MIB", "tnVtsConnEIR"),
        ("TROPIC-VTSCONN-MIB", "tnVtsConnCBS"),
        ("TROPIC-VTSCONN-MIB", "tnVtsConnEBS"),
        ("TROPIC-VTSCONN-MIB", "tnVtsConnRowStatus"),
        ("TROPIC-VTSCONN-MIB", "tnVtsConnId"),
        ("TROPIC-VTSCONN-MIB", "tnVtsConnProtectionState"))
)
if mibBuilder.loadTexts:
    tnVtsConnGroup.setStatus("current")

tnVtsMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 1, 1, 2)
)
tnVtsMapGroup.setObjects(
      *(("TROPIC-VTSCONN-MIB", "tnVtsMapCEVLANID"),
        ("TROPIC-VTSCONN-MIB", "tnVtsMapSVLANID"))
)
if mibBuilder.loadTexts:
    tnVtsMapGroup.setStatus("current")

tnVtsConnIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 1, 1, 3)
)
tnVtsConnIdGroup.setObjects(
      *(("TROPIC-VTSCONN-MIB", "tnVtsConnIdSrcIfIndex"),
        ("TROPIC-VTSCONN-MIB", "tnVtsConnIdSrcVts"),
        ("TROPIC-VTSCONN-MIB", "tnVtsConnIdDestIfIndex"),
        ("TROPIC-VTSCONN-MIB", "tnVtsConnIdDestVts"))
)
if mibBuilder.loadTexts:
    tnVtsConnIdGroup.setStatus("current")

tnIngressVtsMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 1, 1, 4)
)
tnIngressVtsMapGroup.setObjects(
      *(("TROPIC-VTSCONN-MIB", "tnIngressVtsMapCEVLANID"),
        ("TROPIC-VTSCONN-MIB", "tnIngressVtsMapSVLANID"))
)
if mibBuilder.loadTexts:
    tnIngressVtsMapGroup.setStatus("current")

tnEgressVtsMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 1, 1, 5)
)
tnEgressVtsMapGroup.setObjects(
      *(("TROPIC-VTSCONN-MIB", "tnEgressVtsMapCEVLANID"),
        ("TROPIC-VTSCONN-MIB", "tnEgressVtsMapSVLANID"))
)
if mibBuilder.loadTexts:
    tnEgressVtsMapGroup.setStatus("current")

tnIngressVtsCmodeMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 1, 1, 6)
)
tnIngressVtsCmodeMapGroup.setObjects(
      *(("TROPIC-VTSCONN-MIB", "tnIngressVtsCmodeMapCEVLANID"),
        ("TROPIC-VTSCONN-MIB", "tnIngressVtsCmodeMapSVLANID"),
        ("TROPIC-VTSCONN-MIB", "tnIngressVtsCmodeMapSIP"),
        ("TROPIC-VTSCONN-MIB", "tnIngressVtsCmodeMapDIP"),
        ("TROPIC-VTSCONN-MIB", "tnIngressVtsCmodeMapCMode"),
        ("TROPIC-VTSCONN-MIB", "tnIngressVtsCmodeMapRowStatus"))
)
if mibBuilder.loadTexts:
    tnIngressVtsCmodeMapGroup.setStatus("current")

tnEgressVtsCmodeMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 1, 1, 7)
)
tnEgressVtsCmodeMapGroup.setObjects(
      *(("TROPIC-VTSCONN-MIB", "tnEgressVtsCmodeMapCEVLANID"),
        ("TROPIC-VTSCONN-MIB", "tnEgressVtsCmodeMapSVLANID"),
        ("TROPIC-VTSCONN-MIB", "tnEgressVtsCmodeMapSIP"),
        ("TROPIC-VTSCONN-MIB", "tnEgressVtsCmodeMapDIP"),
        ("TROPIC-VTSCONN-MIB", "tnEgressVtsCmodeMapCMode"),
        ("TROPIC-VTSCONN-MIB", "tnEgressVtsCmodeMapRowStatus"))
)
if mibBuilder.loadTexts:
    tnEgressVtsCmodeMapGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnVtsConnCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6, 1, 2, 1)
)
tnVtsConnCompliance.setObjects(
      *(("TROPIC-VTSCONN-MIB", "tnVtsConnGroup"),
        ("TROPIC-VTSCONN-MIB", "tnVtsMapGroup"),
        ("TROPIC-VTSCONN-MIB", "tnVtsConnIdGroup"),
        ("TROPIC-VTSCONN-MIB", "tnIngressVtsMapGroup"),
        ("TROPIC-VTSCONN-MIB", "tnEgressVtsMapGroup"),
        ("TROPIC-VTSCONN-MIB", "tnIngressVtsCmodeMapGroup"),
        ("TROPIC-VTSCONN-MIB", "tnEgressVtsCmodeMapGroup"))
)
if mibBuilder.loadTexts:
    tnVtsConnCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-VTSCONN-MIB",
    **{"AluWdmVtsCmodeMapCMode": AluWdmVtsCmodeMapCMode,
       "tnVtsConnMibModule": tnVtsConnMibModule,
       "tnVtsConnConf": tnVtsConnConf,
       "tnVtsConnGroups": tnVtsConnGroups,
       "tnVtsConnGroup": tnVtsConnGroup,
       "tnVtsMapGroup": tnVtsMapGroup,
       "tnVtsConnIdGroup": tnVtsConnIdGroup,
       "tnIngressVtsMapGroup": tnIngressVtsMapGroup,
       "tnEgressVtsMapGroup": tnEgressVtsMapGroup,
       "tnIngressVtsCmodeMapGroup": tnIngressVtsCmodeMapGroup,
       "tnEgressVtsCmodeMapGroup": tnEgressVtsCmodeMapGroup,
       "tnVtsConnCompliances": tnVtsConnCompliances,
       "tnVtsConnCompliance": tnVtsConnCompliance,
       "tnVtsConnObjs": tnVtsConnObjs,
       "tnVtsConnBasics": tnVtsConnBasics,
       "tnVtsConnTable": tnVtsConnTable,
       "tnVtsConnEntry": tnVtsConnEntry,
       "tnVtsConnSrcIfIndex": tnVtsConnSrcIfIndex,
       "tnVtsConnSrcVts": tnVtsConnSrcVts,
       "tnVtsConnDestIfIndex": tnVtsConnDestIfIndex,
       "tnVtsConnDestVts": tnVtsConnDestVts,
       "tnVtsConnAdminState": tnVtsConnAdminState,
       "tnVtsConnOperState": tnVtsConnOperState,
       "tnVtsConnBidirectional": tnVtsConnBidirectional,
       "tnVtsConnName": tnVtsConnName,
       "tnVtsConnCIR": tnVtsConnCIR,
       "tnVtsConnEIR": tnVtsConnEIR,
       "tnVtsConnCBS": tnVtsConnCBS,
       "tnVtsConnEBS": tnVtsConnEBS,
       "tnVtsConnRowStatus": tnVtsConnRowStatus,
       "tnVtsConnId": tnVtsConnId,
       "tnVtsConnProtectionState": tnVtsConnProtectionState,
       "tnVtsMapTable": tnVtsMapTable,
       "tnVtsMapEntry": tnVtsMapEntry,
       "tnVtsMapIfIndex": tnVtsMapIfIndex,
       "tnVtsMapVts": tnVtsMapVts,
       "tnVtsMapCEVLANID": tnVtsMapCEVLANID,
       "tnVtsMapSVLANID": tnVtsMapSVLANID,
       "tnVtsConnIdTable": tnVtsConnIdTable,
       "tnVtsConnIdEntry": tnVtsConnIdEntry,
       "tnVtsConnIdSrcIfIndex": tnVtsConnIdSrcIfIndex,
       "tnVtsConnIdSrcVts": tnVtsConnIdSrcVts,
       "tnVtsConnIdDestIfIndex": tnVtsConnIdDestIfIndex,
       "tnVtsConnIdDestVts": tnVtsConnIdDestVts,
       "tnIngressVtsMapTable": tnIngressVtsMapTable,
       "tnIngressVtsMapEntry": tnIngressVtsMapEntry,
       "tnIngressVtsMapCEVLANID": tnIngressVtsMapCEVLANID,
       "tnIngressVtsMapSVLANID": tnIngressVtsMapSVLANID,
       "tnEgressVtsMapTable": tnEgressVtsMapTable,
       "tnEgressVtsMapEntry": tnEgressVtsMapEntry,
       "tnEgressVtsMapCEVLANID": tnEgressVtsMapCEVLANID,
       "tnEgressVtsMapSVLANID": tnEgressVtsMapSVLANID,
       "tnIngressVtsCmodeMapTable": tnIngressVtsCmodeMapTable,
       "tnIngressVtsCmodeMapEntry": tnIngressVtsCmodeMapEntry,
       "tnIngressVtsCmodeMapCEVLANID": tnIngressVtsCmodeMapCEVLANID,
       "tnIngressVtsCmodeMapSVLANID": tnIngressVtsCmodeMapSVLANID,
       "tnIngressVtsCmodeMapSIP": tnIngressVtsCmodeMapSIP,
       "tnIngressVtsCmodeMapDIP": tnIngressVtsCmodeMapDIP,
       "tnIngressVtsCmodeMapCMode": tnIngressVtsCmodeMapCMode,
       "tnIngressVtsCmodeMapRowStatus": tnIngressVtsCmodeMapRowStatus,
       "tnEgressVtsCmodeMapTable": tnEgressVtsCmodeMapTable,
       "tnEgressVtsCmodeMapEntry": tnEgressVtsCmodeMapEntry,
       "tnEgressVtsCmodeMapCEVLANID": tnEgressVtsCmodeMapCEVLANID,
       "tnEgressVtsCmodeMapSVLANID": tnEgressVtsCmodeMapSVLANID,
       "tnEgressVtsCmodeMapSIP": tnEgressVtsCmodeMapSIP,
       "tnEgressVtsCmodeMapDIP": tnEgressVtsCmodeMapDIP,
       "tnEgressVtsCmodeMapCMode": tnEgressVtsCmodeMapCMode,
       "tnEgressVtsCmodeMapRowStatus": tnEgressVtsCmodeMapRowStatus}
)
