# SNMP MIB module (F10-LINK-AGGREGATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/force10_6027/F10-LINK-AGGREGATION-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:18:14 2025
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

(f10Mgmt,) = mibBuilder.importSymbols(
    "FORCE10-SMI",
    "f10Mgmt")

(PortList,) = mibBuilder.importSymbols(
    "FORCE10-TC",
    "PortList")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

f10LinkAggMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2)
)
if mibBuilder.loadTexts:
    f10LinkAggMib.setRevisions(
        ("2013-04-16 00:00",
         "2012-11-26 00:00",
         "2011-07-04 00:00",
         "2003-08-01 00:00",
         "2002-03-12 00:00",
         "2001-03-01 00:00",
         "2000-11-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class F10LacpKey(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )



class F10LacpState(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("lacpActivity", 0),
          ("lacpTimeout", 1),
          ("aggregation", 2),
          ("synchronization", 3),
          ("collecting", 4),
          ("distributing", 5),
          ("defaulted", 6),
          ("expired", 7))
    )


# MIB Managed Objects in the order of their OIDs

_F10LinkAggObjects_ObjectIdentity = ObjectIdentity
f10LinkAggObjects = _F10LinkAggObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1)
)
_F10dot3dAgg_ObjectIdentity = ObjectIdentity
f10dot3dAgg = _F10dot3dAgg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1)
)
_Dot3aAggConfigTable_Object = MibTable
dot3aAggConfigTable = _Dot3aAggConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dot3aAggConfigTable.setStatus("current")
_Dot3aAggConfigEntry_Object = MibTableRow
dot3aAggConfigEntry = _Dot3aAggConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1, 1)
)
dot3aAggConfigEntry.setIndexNames(
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aAggCfgId"),
)
if mibBuilder.loadTexts:
    dot3aAggConfigEntry.setStatus("current")
_Dot3aAggCfgId_Type = Unsigned32
_Dot3aAggCfgId_Object = MibTableColumn
dot3aAggCfgId = _Dot3aAggCfgId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1, 1, 1),
    _Dot3aAggCfgId_Type()
)
dot3aAggCfgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aAggCfgId.setStatus("current")
_Dot3aAggCfgMacAddr_Type = MacAddress
_Dot3aAggCfgMacAddr_Object = MibTableColumn
dot3aAggCfgMacAddr = _Dot3aAggCfgMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1, 1, 2),
    _Dot3aAggCfgMacAddr_Type()
)
dot3aAggCfgMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggCfgMacAddr.setStatus("current")
_Dot3aAggCfgIfIndex_Type = Unsigned32
_Dot3aAggCfgIfIndex_Object = MibTableColumn
dot3aAggCfgIfIndex = _Dot3aAggCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1, 1, 3),
    _Dot3aAggCfgIfIndex_Type()
)
dot3aAggCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggCfgIfIndex.setStatus("current")
_Dot3aAggCfgNumPorts_Type = Unsigned32
_Dot3aAggCfgNumPorts_Object = MibTableColumn
dot3aAggCfgNumPorts = _Dot3aAggCfgNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1, 1, 4),
    _Dot3aAggCfgNumPorts_Type()
)
dot3aAggCfgNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggCfgNumPorts.setStatus("current")
_Dot3aAggCfgPortList_Type = PortList
_Dot3aAggCfgPortList_Object = MibTableColumn
dot3aAggCfgPortList = _Dot3aAggCfgPortList_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1, 1, 5),
    _Dot3aAggCfgPortList_Type()
)
dot3aAggCfgPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggCfgPortList.setStatus("deprecated")
_Dot3aAggCfgPortListString_Type = OctetString
_Dot3aAggCfgPortListString_Object = MibTableColumn
dot3aAggCfgPortListString = _Dot3aAggCfgPortListString_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1, 1, 6),
    _Dot3aAggCfgPortListString_Type()
)
dot3aAggCfgPortListString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggCfgPortListString.setStatus("current")
_Dot3aAggCfgLacpSupported_Type = TruthValue
_Dot3aAggCfgLacpSupported_Object = MibTableColumn
dot3aAggCfgLacpSupported = _Dot3aAggCfgLacpSupported_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1, 1, 7),
    _Dot3aAggCfgLacpSupported_Type()
)
dot3aAggCfgLacpSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggCfgLacpSupported.setStatus("current")


class _Dot3aAggCfgOperStatus_Type(Integer32):
    """Custom type dot3aAggCfgOperStatus based on Integer32"""
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


_Dot3aAggCfgOperStatus_Type.__name__ = "Integer32"
_Dot3aAggCfgOperStatus_Object = MibTableColumn
dot3aAggCfgOperStatus = _Dot3aAggCfgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1, 1, 8),
    _Dot3aAggCfgOperStatus_Type()
)
dot3aAggCfgOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggCfgOperStatus.setStatus("current")
_Dot3aAggStaticTable_Object = MibTable
dot3aAggStaticTable = _Dot3aAggStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dot3aAggStaticTable.setStatus("current")
_Dot3aAggStaticEntry_Object = MibTableRow
dot3aAggStaticEntry = _Dot3aAggStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 2, 1)
)
dot3aAggStaticEntry.setIndexNames(
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aAggIndex"),
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aAggVlanId"),
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aAggMacAddr"),
)
if mibBuilder.loadTexts:
    dot3aAggStaticEntry.setStatus("deprecated")
_Dot3aAggIndex_Type = Unsigned32
_Dot3aAggIndex_Object = MibTableColumn
dot3aAggIndex = _Dot3aAggIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 2, 1, 1),
    _Dot3aAggIndex_Type()
)
dot3aAggIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aAggIndex.setStatus("deprecated")
_Dot3aAggVlanId_Type = Unsigned32
_Dot3aAggVlanId_Object = MibTableColumn
dot3aAggVlanId = _Dot3aAggVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 2, 1, 2),
    _Dot3aAggVlanId_Type()
)
dot3aAggVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aAggVlanId.setStatus("deprecated")
_Dot3aAggMacAddr_Type = MacAddress
_Dot3aAggMacAddr_Object = MibTableColumn
dot3aAggMacAddr = _Dot3aAggMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 2, 1, 3),
    _Dot3aAggMacAddr_Type()
)
dot3aAggMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aAggMacAddr.setStatus("deprecated")


class _Dot3aAggStatus_Type(Integer32):
    """Custom type dot3aAggStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_Dot3aAggStatus_Type.__name__ = "Integer32"
_Dot3aAggStatus_Object = MibTableColumn
dot3aAggStatus = _Dot3aAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 2, 1, 4),
    _Dot3aAggStatus_Type()
)
dot3aAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggStatus.setStatus("deprecated")
_Dot3aAggDistributedPort_Type = OctetString
_Dot3aAggDistributedPort_Object = MibTableColumn
dot3aAggDistributedPort = _Dot3aAggDistributedPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 2, 1, 5),
    _Dot3aAggDistributedPort_Type()
)
dot3aAggDistributedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggDistributedPort.setStatus("deprecated")
_Dot3aAggFdbTable_Object = MibTable
dot3aAggFdbTable = _Dot3aAggFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    dot3aAggFdbTable.setStatus("current")
_Dot3aAggFdbEntry_Object = MibTableRow
dot3aAggFdbEntry = _Dot3aAggFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 3, 1)
)
dot3aAggFdbEntry.setIndexNames(
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aAggFdbIndex"),
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aAggFdbVlanId"),
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aAggFdbMacAddr"),
)
if mibBuilder.loadTexts:
    dot3aAggFdbEntry.setStatus("deprecated")
_Dot3aAggFdbIndex_Type = Unsigned32
_Dot3aAggFdbIndex_Object = MibTableColumn
dot3aAggFdbIndex = _Dot3aAggFdbIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 3, 1, 1),
    _Dot3aAggFdbIndex_Type()
)
dot3aAggFdbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aAggFdbIndex.setStatus("deprecated")
_Dot3aAggFdbVlanId_Type = Unsigned32
_Dot3aAggFdbVlanId_Object = MibTableColumn
dot3aAggFdbVlanId = _Dot3aAggFdbVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 3, 1, 2),
    _Dot3aAggFdbVlanId_Type()
)
dot3aAggFdbVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aAggFdbVlanId.setStatus("deprecated")
_Dot3aAggFdbMacAddr_Type = MacAddress
_Dot3aAggFdbMacAddr_Object = MibTableColumn
dot3aAggFdbMacAddr = _Dot3aAggFdbMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 3, 1, 3),
    _Dot3aAggFdbMacAddr_Type()
)
dot3aAggFdbMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aAggFdbMacAddr.setStatus("deprecated")


class _Dot3aAggFdbStatus_Type(Integer32):
    """Custom type dot3aAggFdbStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_Dot3aAggFdbStatus_Type.__name__ = "Integer32"
_Dot3aAggFdbStatus_Object = MibTableColumn
dot3aAggFdbStatus = _Dot3aAggFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 3, 1, 4),
    _Dot3aAggFdbStatus_Type()
)
dot3aAggFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggFdbStatus.setStatus("deprecated")
_Dot3aAggFdbDistributedPort_Type = OctetString
_Dot3aAggFdbDistributedPort_Object = MibTableColumn
dot3aAggFdbDistributedPort = _Dot3aAggFdbDistributedPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 3, 1, 5),
    _Dot3aAggFdbDistributedPort_Type()
)
dot3aAggFdbDistributedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggFdbDistributedPort.setStatus("deprecated")
_Dot3aCurAggStaticTable_Object = MibTable
dot3aCurAggStaticTable = _Dot3aCurAggStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dot3aCurAggStaticTable.setStatus("current")
_Dot3aCurAggStaticEntry_Object = MibTableRow
dot3aCurAggStaticEntry = _Dot3aCurAggStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 4, 1)
)
dot3aCurAggStaticEntry.setIndexNames(
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aCurAggVlanId"),
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aCurAggMacAddr"),
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aCurAggIndex"),
)
if mibBuilder.loadTexts:
    dot3aCurAggStaticEntry.setStatus("current")
_Dot3aCurAggVlanId_Type = Unsigned32
_Dot3aCurAggVlanId_Object = MibTableColumn
dot3aCurAggVlanId = _Dot3aCurAggVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 4, 1, 1),
    _Dot3aCurAggVlanId_Type()
)
dot3aCurAggVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aCurAggVlanId.setStatus("current")
_Dot3aCurAggMacAddr_Type = MacAddress
_Dot3aCurAggMacAddr_Object = MibTableColumn
dot3aCurAggMacAddr = _Dot3aCurAggMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 4, 1, 2),
    _Dot3aCurAggMacAddr_Type()
)
dot3aCurAggMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aCurAggMacAddr.setStatus("current")
_Dot3aCurAggIndex_Type = Unsigned32
_Dot3aCurAggIndex_Object = MibTableColumn
dot3aCurAggIndex = _Dot3aCurAggIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 4, 1, 3),
    _Dot3aCurAggIndex_Type()
)
dot3aCurAggIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aCurAggIndex.setStatus("current")


class _Dot3aCurAggStatus_Type(Integer32):
    """Custom type dot3aCurAggStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_Dot3aCurAggStatus_Type.__name__ = "Integer32"
_Dot3aCurAggStatus_Object = MibTableColumn
dot3aCurAggStatus = _Dot3aCurAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 4, 1, 4),
    _Dot3aCurAggStatus_Type()
)
dot3aCurAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aCurAggStatus.setStatus("current")
_Dot3aCurAggFdbTable_Object = MibTable
dot3aCurAggFdbTable = _Dot3aCurAggFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    dot3aCurAggFdbTable.setStatus("current")
_Dot3aCurAggFdbEntry_Object = MibTableRow
dot3aCurAggFdbEntry = _Dot3aCurAggFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 5, 1)
)
dot3aCurAggFdbEntry.setIndexNames(
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aCurAggFdbVlanId"),
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aCurAggFdbMacAddr"),
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aCurAggFdbIndex"),
)
if mibBuilder.loadTexts:
    dot3aCurAggFdbEntry.setStatus("current")
_Dot3aCurAggFdbVlanId_Type = Unsigned32
_Dot3aCurAggFdbVlanId_Object = MibTableColumn
dot3aCurAggFdbVlanId = _Dot3aCurAggFdbVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 5, 1, 1),
    _Dot3aCurAggFdbVlanId_Type()
)
dot3aCurAggFdbVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aCurAggFdbVlanId.setStatus("current")
_Dot3aCurAggFdbMacAddr_Type = MacAddress
_Dot3aCurAggFdbMacAddr_Object = MibTableColumn
dot3aCurAggFdbMacAddr = _Dot3aCurAggFdbMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 5, 1, 2),
    _Dot3aCurAggFdbMacAddr_Type()
)
dot3aCurAggFdbMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aCurAggFdbMacAddr.setStatus("current")
_Dot3aCurAggFdbIndex_Type = Unsigned32
_Dot3aCurAggFdbIndex_Object = MibTableColumn
dot3aCurAggFdbIndex = _Dot3aCurAggFdbIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 5, 1, 3),
    _Dot3aCurAggFdbIndex_Type()
)
dot3aCurAggFdbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aCurAggFdbIndex.setStatus("current")


class _Dot3aCurAggFdbStatus_Type(Integer32):
    """Custom type dot3aCurAggFdbStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_Dot3aCurAggFdbStatus_Type.__name__ = "Integer32"
_Dot3aCurAggFdbStatus_Object = MibTableColumn
dot3aCurAggFdbStatus = _Dot3aCurAggFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 5, 1, 4),
    _Dot3aCurAggFdbStatus_Type()
)
dot3aCurAggFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aCurAggFdbStatus.setStatus("current")
_Dot3aCommonAggFdbTable_Object = MibTable
dot3aCommonAggFdbTable = _Dot3aCommonAggFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    dot3aCommonAggFdbTable.setStatus("current")
_Dot3aCommonAggFdbEntry_Object = MibTableRow
dot3aCommonAggFdbEntry = _Dot3aCommonAggFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 6, 1)
)
dot3aCommonAggFdbEntry.setIndexNames(
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aCommonAggFdbIndex"),
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aCommonAggFdbVlanId"),
)
if mibBuilder.loadTexts:
    dot3aCommonAggFdbEntry.setStatus("current")
_Dot3aCommonAggFdbIndex_Type = Unsigned32
_Dot3aCommonAggFdbIndex_Object = MibTableColumn
dot3aCommonAggFdbIndex = _Dot3aCommonAggFdbIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 6, 1, 1),
    _Dot3aCommonAggFdbIndex_Type()
)
dot3aCommonAggFdbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aCommonAggFdbIndex.setStatus("current")
_Dot3aCommonAggFdbVlanId_Type = Unsigned32
_Dot3aCommonAggFdbVlanId_Object = MibTableColumn
dot3aCommonAggFdbVlanId = _Dot3aCommonAggFdbVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 6, 1, 2),
    _Dot3aCommonAggFdbVlanId_Type()
)
dot3aCommonAggFdbVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aCommonAggFdbVlanId.setStatus("current")


class _Dot3aCommonAggFdbTagConfig_Type(Integer32):
    """Custom type dot3aCommonAggFdbTagConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 1),
          ("untagged", 2))
    )


_Dot3aCommonAggFdbTagConfig_Type.__name__ = "Integer32"
_Dot3aCommonAggFdbTagConfig_Object = MibTableColumn
dot3aCommonAggFdbTagConfig = _Dot3aCommonAggFdbTagConfig_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 6, 1, 3),
    _Dot3aCommonAggFdbTagConfig_Type()
)
dot3aCommonAggFdbTagConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aCommonAggFdbTagConfig.setStatus("current")


class _Dot3aCommonAggFdbStatus_Type(Integer32):
    """Custom type dot3aCommonAggFdbStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_Dot3aCommonAggFdbStatus_Type.__name__ = "Integer32"
_Dot3aCommonAggFdbStatus_Object = MibTableColumn
dot3aCommonAggFdbStatus = _Dot3aCommonAggFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 6, 1, 4),
    _Dot3aCommonAggFdbStatus_Type()
)
dot3aCommonAggFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aCommonAggFdbStatus.setStatus("current")
_Dot3adAggPortTable_Object = MibTable
dot3adAggPortTable = _Dot3adAggPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 7)
)
if mibBuilder.loadTexts:
    dot3adAggPortTable.setStatus("current")
_Dot3adAggPortEntry_Object = MibTableRow
dot3adAggPortEntry = _Dot3adAggPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 7, 1)
)
dot3adAggPortEntry.setIndexNames(
    (0, "F10-LINK-AGGREGATION-MIB", "dot3adAggPortIndex"),
)
if mibBuilder.loadTexts:
    dot3adAggPortEntry.setStatus("current")
_Dot3adAggPortIndex_Type = Unsigned32
_Dot3adAggPortIndex_Object = MibTableColumn
dot3adAggPortIndex = _Dot3adAggPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 7, 1, 1),
    _Dot3adAggPortIndex_Type()
)
dot3adAggPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3adAggPortIndex.setStatus("current")
_Dot3adAggPortActorOperKey_Type = F10LacpKey
_Dot3adAggPortActorOperKey_Object = MibTableColumn
dot3adAggPortActorOperKey = _Dot3adAggPortActorOperKey_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 7, 1, 2),
    _Dot3adAggPortActorOperKey_Type()
)
dot3adAggPortActorOperKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortActorOperKey.setStatus("current")
_Dot3adAggPortPartnerOperKey_Type = F10LacpKey
_Dot3adAggPortPartnerOperKey_Object = MibTableColumn
dot3adAggPortPartnerOperKey = _Dot3adAggPortPartnerOperKey_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 7, 1, 3),
    _Dot3adAggPortPartnerOperKey_Type()
)
dot3adAggPortPartnerOperKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerOperKey.setStatus("current")
_Dot3adAggPortActorAdminState_Type = F10LacpState
_Dot3adAggPortActorAdminState_Object = MibTableColumn
dot3adAggPortActorAdminState = _Dot3adAggPortActorAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 7, 1, 4),
    _Dot3adAggPortActorAdminState_Type()
)
dot3adAggPortActorAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortActorAdminState.setStatus("current")
_Dot3adAggPortActorOperState_Type = F10LacpState
_Dot3adAggPortActorOperState_Object = MibTableColumn
dot3adAggPortActorOperState = _Dot3adAggPortActorOperState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 7, 1, 5),
    _Dot3adAggPortActorOperState_Type()
)
dot3adAggPortActorOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortActorOperState.setStatus("current")
_Dot3adAggPortPartnerAdminState_Type = F10LacpState
_Dot3adAggPortPartnerAdminState_Object = MibTableColumn
dot3adAggPortPartnerAdminState = _Dot3adAggPortPartnerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 7, 1, 6),
    _Dot3adAggPortPartnerAdminState_Type()
)
dot3adAggPortPartnerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerAdminState.setStatus("current")
_Dot3adAggPortPartnerOperState_Type = F10LacpState
_Dot3adAggPortPartnerOperState_Object = MibTableColumn
dot3adAggPortPartnerOperState = _Dot3adAggPortPartnerOperState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 7, 1, 7),
    _Dot3adAggPortPartnerOperState_Type()
)
dot3adAggPortPartnerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerOperState.setStatus("current")
_F10LinkAggMgmt_ObjectIdentity = ObjectIdentity
f10LinkAggMgmt = _F10LinkAggMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 2)
)


class _Dot3aClearFdb_Type(Integer32):
    """Custom type dot3aClearFdb based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_Dot3aClearFdb_Type.__name__ = "Integer32"
_Dot3aClearFdb_Object = MibScalar
dot3aClearFdb = _Dot3aClearFdb_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 2, 1),
    _Dot3aClearFdb_Type()
)
dot3aClearFdb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3aClearFdb.setStatus("current")
_F10LinkAggAlarms_ObjectIdentity = ObjectIdentity
f10LinkAggAlarms = _F10LinkAggAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 2)
)
_F10Dot3adAggNotifications_ObjectIdentity = ObjectIdentity
f10Dot3adAggNotifications = _F10Dot3adAggNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 2, 0)
)
_F10LinkBundleNotifications_ObjectIdentity = ObjectIdentity
f10LinkBundleNotifications = _F10LinkBundleNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 2, 1)
)


class _LinkBundleType_Type(Integer32):
    """Custom type linkBundleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ecmpBundle", 1),
          ("lagBundle", 2))
    )


_LinkBundleType_Type.__name__ = "Integer32"
_LinkBundleType_Object = MibScalar
linkBundleType = _LinkBundleType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 2, 2),
    _LinkBundleType_Type()
)
linkBundleType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    linkBundleType.setStatus("current")
_LinkBundleNumber_Type = Integer32
_LinkBundleNumber_Object = MibScalar
linkBundleNumber = _LinkBundleNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 2, 3),
    _LinkBundleNumber_Type()
)
linkBundleNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    linkBundleNumber.setStatus("current")
_F10LinkAggMibConformance_ObjectIdentity = ObjectIdentity
f10LinkAggMibConformance = _F10LinkAggMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 3)
)
_F10LinkAggMibCompliances_ObjectIdentity = ObjectIdentity
f10LinkAggMibCompliances = _F10LinkAggMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 3, 1)
)
_F10LinkAggMibGroups_ObjectIdentity = ObjectIdentity
f10LinkAggMibGroups = _F10LinkAggMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 3, 2)
)

# Managed Objects groups

f10LinkAggCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 3, 2, 1)
)
f10LinkAggCommonGroup.setObjects(
      *(("F10-LINK-AGGREGATION-MIB", "dot3aAggCfgMacAddr"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aAggCfgIfIndex"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aAggCfgNumPorts"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aAggCfgPortListString"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aAggCfgLacpSupported"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aAggCfgOperStatus"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aCurAggStatus"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aCurAggFdbStatus"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aCommonAggFdbTagConfig"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aCommonAggFdbStatus"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aClearFdb"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aAggCfgPortList"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aAggStatus"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aAggDistributedPort"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aAggFdbStatus"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aAggFdbDistributedPort"))
)
if mibBuilder.loadTexts:
    f10LinkAggCommonGroup.setStatus("deprecated")

f10LinkAggCommonGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 3, 2, 2)
)
f10LinkAggCommonGroupRev1.setObjects(
      *(("F10-LINK-AGGREGATION-MIB", "dot3aAggCfgMacAddr"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aAggCfgIfIndex"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aAggCfgNumPorts"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aAggCfgPortListString"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aAggCfgLacpSupported"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aAggCfgOperStatus"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aCurAggStatus"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aCurAggFdbStatus"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aCommonAggFdbTagConfig"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aCommonAggFdbStatus"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aClearFdb"))
)
if mibBuilder.loadTexts:
    f10LinkAggCommonGroupRev1.setStatus("current")

f10LinkAggPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 3, 2, 3)
)
f10LinkAggPortGroup.setObjects(
      *(("F10-LINK-AGGREGATION-MIB", "dot3adAggPortActorOperKey"),
        ("F10-LINK-AGGREGATION-MIB", "dot3adAggPortPartnerOperKey"),
        ("F10-LINK-AGGREGATION-MIB", "dot3adAggPortActorAdminState"),
        ("F10-LINK-AGGREGATION-MIB", "dot3adAggPortActorOperState"),
        ("F10-LINK-AGGREGATION-MIB", "dot3adAggPortPartnerAdminState"),
        ("F10-LINK-AGGREGATION-MIB", "dot3adAggPortPartnerOperState"))
)
if mibBuilder.loadTexts:
    f10LinkAggPortGroup.setStatus("current")

f10LinkAggAlarmObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 3, 2, 5)
)
f10LinkAggAlarmObjectGroup.setObjects(
      *(("F10-LINK-AGGREGATION-MIB", "linkBundleType"),
        ("F10-LINK-AGGREGATION-MIB", "linkBundleNumber"))
)
if mibBuilder.loadTexts:
    f10LinkAggAlarmObjectGroup.setStatus("current")


# Notification objects

dot3adAggLacpStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 2, 0, 1)
)
dot3adAggLacpStateChange.setObjects(
      *(("F10-LINK-AGGREGATION-MIB", "dot3adAggPortActorOperState"),
        ("F10-LINK-AGGREGATION-MIB", "dot3adAggPortPartnerOperState"))
)
if mibBuilder.loadTexts:
    dot3adAggLacpStateChange.setStatus(
        "current"
    )

linkBundleImbalance = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 2, 1, 1)
)
linkBundleImbalance.setObjects(
      *(("F10-LINK-AGGREGATION-MIB", "linkBundleType"),
        ("F10-LINK-AGGREGATION-MIB", "linkBundleNumber"))
)
if mibBuilder.loadTexts:
    linkBundleImbalance.setStatus(
        "current"
    )

linkBundleImbalanceClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 2, 1, 2)
)
linkBundleImbalanceClear.setObjects(
      *(("F10-LINK-AGGREGATION-MIB", "linkBundleType"),
        ("F10-LINK-AGGREGATION-MIB", "linkBundleNumber"))
)
if mibBuilder.loadTexts:
    linkBundleImbalanceClear.setStatus(
        "current"
    )


# Notifications groups

f10LinkAggNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 3, 2, 4)
)
f10LinkAggNotificationGroup.setObjects(
      *(("F10-LINK-AGGREGATION-MIB", "dot3adAggLacpStateChange"),
        ("F10-LINK-AGGREGATION-MIB", "linkBundleImbalance"),
        ("F10-LINK-AGGREGATION-MIB", "linkBundleImbalanceClear"))
)
if mibBuilder.loadTexts:
    f10LinkAggNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

f10LinkAggMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 3, 1, 1)
)
f10LinkAggMibCompliance.setObjects(
    ("F10-LINK-AGGREGATION-MIB", "f10LinkAggCommonGroup")
)
if mibBuilder.loadTexts:
    f10LinkAggMibCompliance.setStatus(
        "deprecated"
    )

f10LinkAggMibComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 3, 1, 2)
)
f10LinkAggMibComplianceRev1.setObjects(
      *(("F10-LINK-AGGREGATION-MIB", "f10LinkAggCommonGroupRev1"),
        ("F10-LINK-AGGREGATION-MIB", "f10LinkAggPortGroup"),
        ("F10-LINK-AGGREGATION-MIB", "f10LinkAggNotificationGroup"))
)
if mibBuilder.loadTexts:
    f10LinkAggMibComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F10-LINK-AGGREGATION-MIB",
    **{"F10LacpKey": F10LacpKey,
       "F10LacpState": F10LacpState,
       "f10LinkAggMib": f10LinkAggMib,
       "f10LinkAggObjects": f10LinkAggObjects,
       "f10dot3dAgg": f10dot3dAgg,
       "dot3aAggConfigTable": dot3aAggConfigTable,
       "dot3aAggConfigEntry": dot3aAggConfigEntry,
       "dot3aAggCfgId": dot3aAggCfgId,
       "dot3aAggCfgMacAddr": dot3aAggCfgMacAddr,
       "dot3aAggCfgIfIndex": dot3aAggCfgIfIndex,
       "dot3aAggCfgNumPorts": dot3aAggCfgNumPorts,
       "dot3aAggCfgPortList": dot3aAggCfgPortList,
       "dot3aAggCfgPortListString": dot3aAggCfgPortListString,
       "dot3aAggCfgLacpSupported": dot3aAggCfgLacpSupported,
       "dot3aAggCfgOperStatus": dot3aAggCfgOperStatus,
       "dot3aAggStaticTable": dot3aAggStaticTable,
       "dot3aAggStaticEntry": dot3aAggStaticEntry,
       "dot3aAggIndex": dot3aAggIndex,
       "dot3aAggVlanId": dot3aAggVlanId,
       "dot3aAggMacAddr": dot3aAggMacAddr,
       "dot3aAggStatus": dot3aAggStatus,
       "dot3aAggDistributedPort": dot3aAggDistributedPort,
       "dot3aAggFdbTable": dot3aAggFdbTable,
       "dot3aAggFdbEntry": dot3aAggFdbEntry,
       "dot3aAggFdbIndex": dot3aAggFdbIndex,
       "dot3aAggFdbVlanId": dot3aAggFdbVlanId,
       "dot3aAggFdbMacAddr": dot3aAggFdbMacAddr,
       "dot3aAggFdbStatus": dot3aAggFdbStatus,
       "dot3aAggFdbDistributedPort": dot3aAggFdbDistributedPort,
       "dot3aCurAggStaticTable": dot3aCurAggStaticTable,
       "dot3aCurAggStaticEntry": dot3aCurAggStaticEntry,
       "dot3aCurAggVlanId": dot3aCurAggVlanId,
       "dot3aCurAggMacAddr": dot3aCurAggMacAddr,
       "dot3aCurAggIndex": dot3aCurAggIndex,
       "dot3aCurAggStatus": dot3aCurAggStatus,
       "dot3aCurAggFdbTable": dot3aCurAggFdbTable,
       "dot3aCurAggFdbEntry": dot3aCurAggFdbEntry,
       "dot3aCurAggFdbVlanId": dot3aCurAggFdbVlanId,
       "dot3aCurAggFdbMacAddr": dot3aCurAggFdbMacAddr,
       "dot3aCurAggFdbIndex": dot3aCurAggFdbIndex,
       "dot3aCurAggFdbStatus": dot3aCurAggFdbStatus,
       "dot3aCommonAggFdbTable": dot3aCommonAggFdbTable,
       "dot3aCommonAggFdbEntry": dot3aCommonAggFdbEntry,
       "dot3aCommonAggFdbIndex": dot3aCommonAggFdbIndex,
       "dot3aCommonAggFdbVlanId": dot3aCommonAggFdbVlanId,
       "dot3aCommonAggFdbTagConfig": dot3aCommonAggFdbTagConfig,
       "dot3aCommonAggFdbStatus": dot3aCommonAggFdbStatus,
       "dot3adAggPortTable": dot3adAggPortTable,
       "dot3adAggPortEntry": dot3adAggPortEntry,
       "dot3adAggPortIndex": dot3adAggPortIndex,
       "dot3adAggPortActorOperKey": dot3adAggPortActorOperKey,
       "dot3adAggPortPartnerOperKey": dot3adAggPortPartnerOperKey,
       "dot3adAggPortActorAdminState": dot3adAggPortActorAdminState,
       "dot3adAggPortActorOperState": dot3adAggPortActorOperState,
       "dot3adAggPortPartnerAdminState": dot3adAggPortPartnerAdminState,
       "dot3adAggPortPartnerOperState": dot3adAggPortPartnerOperState,
       "f10LinkAggMgmt": f10LinkAggMgmt,
       "dot3aClearFdb": dot3aClearFdb,
       "f10LinkAggAlarms": f10LinkAggAlarms,
       "f10Dot3adAggNotifications": f10Dot3adAggNotifications,
       "dot3adAggLacpStateChange": dot3adAggLacpStateChange,
       "f10LinkBundleNotifications": f10LinkBundleNotifications,
       "linkBundleImbalance": linkBundleImbalance,
       "linkBundleImbalanceClear": linkBundleImbalanceClear,
       "linkBundleType": linkBundleType,
       "linkBundleNumber": linkBundleNumber,
       "f10LinkAggMibConformance": f10LinkAggMibConformance,
       "f10LinkAggMibCompliances": f10LinkAggMibCompliances,
       "f10LinkAggMibCompliance": f10LinkAggMibCompliance,
       "f10LinkAggMibComplianceRev1": f10LinkAggMibComplianceRev1,
       "f10LinkAggMibGroups": f10LinkAggMibGroups,
       "f10LinkAggCommonGroup": f10LinkAggCommonGroup,
       "f10LinkAggCommonGroupRev1": f10LinkAggCommonGroupRev1,
       "f10LinkAggPortGroup": f10LinkAggPortGroup,
       "f10LinkAggNotificationGroup": f10LinkAggNotificationGroup,
       "f10LinkAggAlarmObjectGroup": f10LinkAggAlarmObjectGroup}
)
