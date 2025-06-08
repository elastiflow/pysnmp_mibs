# SNMP MIB module (TOFINO-ADJACENCY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/tofino_40856/TOFINO-ADJACENCY-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:05:03 2025
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

(LldpChassisId,
 LldpChassisIdSubtype,
 LldpManAddress,
 LldpPortId,
 LldpPortIdSubtype) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpChassisId",
    "LldpChassisIdSubtype",
    "LldpManAddress",
    "LldpPortId",
    "LldpPortIdSubtype")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(tofinoDevices,) = mibBuilder.importSymbols(
    "TOFINO-TC-MIB",
    "tofinoDevices")


# MODULE-IDENTITY

tofinoAdjacencyMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 40856, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tofinoAdjacencyMib.setRevisions(
        ("2012-11-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TofinoTSAPortTypeSyntax(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TofinoAdjacencyMibNotifications_ObjectIdentity = ObjectIdentity
tofinoAdjacencyMibNotifications = _TofinoAdjacencyMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40856, 1, 3, 1, 0)
)
_TofinoAdjacencyMibObjects_ObjectIdentity = ObjectIdentity
tofinoAdjacencyMibObjects = _TofinoAdjacencyMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40856, 1, 3, 1, 1)
)
_TofinoAdjacencyTimeLastDiscoveredManually_Type = TimeTicks
_TofinoAdjacencyTimeLastDiscoveredManually_Object = MibScalar
tofinoAdjacencyTimeLastDiscoveredManually = _TofinoAdjacencyTimeLastDiscoveredManually_Object(
    (1, 3, 6, 1, 4, 1, 40856, 1, 3, 1, 1, 1),
    _TofinoAdjacencyTimeLastDiscoveredManually_Type()
)
tofinoAdjacencyTimeLastDiscoveredManually.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tofinoAdjacencyTimeLastDiscoveredManually.setStatus("current")
_TofinoAdjacencyTable_Object = MibTable
tofinoAdjacencyTable = _TofinoAdjacencyTable_Object(
    (1, 3, 6, 1, 4, 1, 40856, 1, 3, 1, 1, 10)
)
if mibBuilder.loadTexts:
    tofinoAdjacencyTable.setStatus("current")
_TofinoAdjacencyEntry_Object = MibTableRow
tofinoAdjacencyEntry = _TofinoAdjacencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 40856, 1, 3, 1, 1, 10, 1)
)
tofinoAdjacencyEntry.setIndexNames(
    (0, "TOFINO-ADJACENCY-MIB", "tofinoTSATofinoID"),
)
if mibBuilder.loadTexts:
    tofinoAdjacencyEntry.setStatus("current")


class _TofinoTSATofinoID_Type(OctetString):
    """Custom type tofinoTSATofinoID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_TofinoTSATofinoID_Type.__name__ = "OctetString"
_TofinoTSATofinoID_Object = MibTableColumn
tofinoTSATofinoID = _TofinoTSATofinoID_Object(
    (1, 3, 6, 1, 4, 1, 40856, 1, 3, 1, 1, 10, 1, 1),
    _TofinoTSATofinoID_Type()
)
tofinoTSATofinoID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tofinoTSATofinoID.setStatus("current")
_TofinoTSALastVisible_Type = TimeTicks
_TofinoTSALastVisible_Object = MibTableColumn
tofinoTSALastVisible = _TofinoTSALastVisible_Object(
    (1, 3, 6, 1, 4, 1, 40856, 1, 3, 1, 1, 10, 1, 2),
    _TofinoTSALastVisible_Type()
)
tofinoTSALastVisible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tofinoTSALastVisible.setStatus("current")
_TofinoTSAMacAddress_Type = MacAddress
_TofinoTSAMacAddress_Object = MibTableColumn
tofinoTSAMacAddress = _TofinoTSAMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 40856, 1, 3, 1, 1, 10, 1, 3),
    _TofinoTSAMacAddress_Type()
)
tofinoTSAMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tofinoTSAMacAddress.setStatus("current")
_TofinoPortAdjacencyTable_Object = MibTable
tofinoPortAdjacencyTable = _TofinoPortAdjacencyTable_Object(
    (1, 3, 6, 1, 4, 1, 40856, 1, 3, 1, 1, 11)
)
if mibBuilder.loadTexts:
    tofinoPortAdjacencyTable.setStatus("current")
_TofinoPortAdjacencyEntry_Object = MibTableRow
tofinoPortAdjacencyEntry = _TofinoPortAdjacencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 40856, 1, 3, 1, 1, 11, 1)
)
tofinoPortAdjacencyEntry.setIndexNames(
    (0, "TOFINO-ADJACENCY-MIB", "tofinoTSATofinoID"),
    (0, "TOFINO-ADJACENCY-MIB", "tofinoTSAPortIndex"),
)
if mibBuilder.loadTexts:
    tofinoPortAdjacencyEntry.setStatus("current")
_TofinoTSAPortIndex_Type = InterfaceIndex
_TofinoTSAPortIndex_Object = MibTableColumn
tofinoTSAPortIndex = _TofinoTSAPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 40856, 1, 3, 1, 1, 11, 1, 1),
    _TofinoTSAPortIndex_Type()
)
tofinoTSAPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tofinoTSAPortIndex.setStatus("current")
_TofinoTSAPortType_Type = TofinoTSAPortTypeSyntax
_TofinoTSAPortType_Object = MibTableColumn
tofinoTSAPortType = _TofinoTSAPortType_Object(
    (1, 3, 6, 1, 4, 1, 40856, 1, 3, 1, 1, 11, 1, 2),
    _TofinoTSAPortType_Type()
)
tofinoTSAPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tofinoTSAPortType.setStatus("current")
_TofinoRXLLDPListenChassisIdSubtype_Type = LldpChassisIdSubtype
_TofinoRXLLDPListenChassisIdSubtype_Object = MibTableColumn
tofinoRXLLDPListenChassisIdSubtype = _TofinoRXLLDPListenChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 40856, 1, 3, 1, 1, 11, 1, 3),
    _TofinoRXLLDPListenChassisIdSubtype_Type()
)
tofinoRXLLDPListenChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tofinoRXLLDPListenChassisIdSubtype.setStatus("current")
_TofinoRXLLDPListenChassisId_Type = LldpChassisId
_TofinoRXLLDPListenChassisId_Object = MibTableColumn
tofinoRXLLDPListenChassisId = _TofinoRXLLDPListenChassisId_Object(
    (1, 3, 6, 1, 4, 1, 40856, 1, 3, 1, 1, 11, 1, 4),
    _TofinoRXLLDPListenChassisId_Type()
)
tofinoRXLLDPListenChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tofinoRXLLDPListenChassisId.setStatus("current")
_TofinoRXLLDPListenPortIdSubtype_Type = LldpPortIdSubtype
_TofinoRXLLDPListenPortIdSubtype_Object = MibTableColumn
tofinoRXLLDPListenPortIdSubtype = _TofinoRXLLDPListenPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 40856, 1, 3, 1, 1, 11, 1, 5),
    _TofinoRXLLDPListenPortIdSubtype_Type()
)
tofinoRXLLDPListenPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tofinoRXLLDPListenPortIdSubtype.setStatus("current")
_TofinoRXLLDPListenPortId_Type = LldpPortId
_TofinoRXLLDPListenPortId_Object = MibTableColumn
tofinoRXLLDPListenPortId = _TofinoRXLLDPListenPortId_Object(
    (1, 3, 6, 1, 4, 1, 40856, 1, 3, 1, 1, 11, 1, 6),
    _TofinoRXLLDPListenPortId_Type()
)
tofinoRXLLDPListenPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tofinoRXLLDPListenPortId.setStatus("current")
_TofinoRXLLDPRemManAddr_Type = LldpManAddress
_TofinoRXLLDPRemManAddr_Object = MibTableColumn
tofinoRXLLDPRemManAddr = _TofinoRXLLDPRemManAddr_Object(
    (1, 3, 6, 1, 4, 1, 40856, 1, 3, 1, 1, 11, 1, 7),
    _TofinoRXLLDPRemManAddr_Type()
)
tofinoRXLLDPRemManAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tofinoRXLLDPRemManAddr.setStatus("current")
_TofinoRXRSTPMacAddress_Type = MacAddress
_TofinoRXRSTPMacAddress_Object = MibTableColumn
tofinoRXRSTPMacAddress = _TofinoRXRSTPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 40856, 1, 3, 1, 1, 11, 1, 8),
    _TofinoRXRSTPMacAddress_Type()
)
tofinoRXRSTPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tofinoRXRSTPMacAddress.setStatus("current")
_TofinoAdjacencyMibConformance_ObjectIdentity = ObjectIdentity
tofinoAdjacencyMibConformance = _TofinoAdjacencyMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40856, 1, 3, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TOFINO-ADJACENCY-MIB",
    **{"TofinoTSAPortTypeSyntax": TofinoTSAPortTypeSyntax,
       "tofinoAdjacencyMib": tofinoAdjacencyMib,
       "tofinoAdjacencyMibNotifications": tofinoAdjacencyMibNotifications,
       "tofinoAdjacencyMibObjects": tofinoAdjacencyMibObjects,
       "tofinoAdjacencyTimeLastDiscoveredManually": tofinoAdjacencyTimeLastDiscoveredManually,
       "tofinoAdjacencyTable": tofinoAdjacencyTable,
       "tofinoAdjacencyEntry": tofinoAdjacencyEntry,
       "tofinoTSATofinoID": tofinoTSATofinoID,
       "tofinoTSALastVisible": tofinoTSALastVisible,
       "tofinoTSAMacAddress": tofinoTSAMacAddress,
       "tofinoPortAdjacencyTable": tofinoPortAdjacencyTable,
       "tofinoPortAdjacencyEntry": tofinoPortAdjacencyEntry,
       "tofinoTSAPortIndex": tofinoTSAPortIndex,
       "tofinoTSAPortType": tofinoTSAPortType,
       "tofinoRXLLDPListenChassisIdSubtype": tofinoRXLLDPListenChassisIdSubtype,
       "tofinoRXLLDPListenChassisId": tofinoRXLLDPListenChassisId,
       "tofinoRXLLDPListenPortIdSubtype": tofinoRXLLDPListenPortIdSubtype,
       "tofinoRXLLDPListenPortId": tofinoRXLLDPListenPortId,
       "tofinoRXLLDPRemManAddr": tofinoRXLLDPRemManAddr,
       "tofinoRXRSTPMacAddress": tofinoRXRSTPMacAddress,
       "tofinoAdjacencyMibConformance": tofinoAdjacencyMibConformance}
)
