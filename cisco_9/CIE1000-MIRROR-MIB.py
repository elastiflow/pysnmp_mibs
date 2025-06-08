# SNMP MIB module (CIE1000-MIRROR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CIE1000-MIRROR-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 20:26:42 2025
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

(CIE1000InterfaceIndex,
 CIE1000PortList,
 CIE1000Unsigned16,
 CIE1000VlanListQuarter) = mibBuilder.importSymbols(
    "CIE1000-TC",
    "CIE1000InterfaceIndex",
    "CIE1000PortList",
    "CIE1000Unsigned16",
    "CIE1000VlanListQuarter")

(cie1000SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCO-IE1000-MIB",
    "cie1000SwitchMgmt")

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

cie1000MirrorMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15)
)
if mibBuilder.loadTexts:
    cie1000MirrorMib.setRevisions(
        ("2014-07-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CIE1000mirrorSessionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mirror", 0),
          ("rMirrorSource", 1),
          ("rMirrorDestination", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Cie1000MirrorMibObjects_ObjectIdentity = ObjectIdentity
cie1000MirrorMibObjects = _Cie1000MirrorMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 1)
)
_Cie1000MirrorCapabilities_ObjectIdentity = ObjectIdentity
cie1000MirrorCapabilities = _Cie1000MirrorCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 1, 1)
)
_Cie1000MirrorCapabilitiesSessionCountMax_Type = Integer32
_Cie1000MirrorCapabilitiesSessionCountMax_Object = MibScalar
cie1000MirrorCapabilitiesSessionCountMax = _Cie1000MirrorCapabilitiesSessionCountMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 1, 1, 1),
    _Cie1000MirrorCapabilitiesSessionCountMax_Type()
)
cie1000MirrorCapabilitiesSessionCountMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MirrorCapabilitiesSessionCountMax.setStatus("current")
_Cie1000MirrorCapabilitiesSessionSourceCountMax_Type = Integer32
_Cie1000MirrorCapabilitiesSessionSourceCountMax_Object = MibScalar
cie1000MirrorCapabilitiesSessionSourceCountMax = _Cie1000MirrorCapabilitiesSessionSourceCountMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 1, 1, 2),
    _Cie1000MirrorCapabilitiesSessionSourceCountMax_Type()
)
cie1000MirrorCapabilitiesSessionSourceCountMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MirrorCapabilitiesSessionSourceCountMax.setStatus("current")
_Cie1000MirrorCapabilitiesRMirrorSuport_Type = TruthValue
_Cie1000MirrorCapabilitiesRMirrorSuport_Object = MibScalar
cie1000MirrorCapabilitiesRMirrorSuport = _Cie1000MirrorCapabilitiesRMirrorSuport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 1, 1, 3),
    _Cie1000MirrorCapabilitiesRMirrorSuport_Type()
)
cie1000MirrorCapabilitiesRMirrorSuport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MirrorCapabilitiesRMirrorSuport.setStatus("current")
_Cie1000MirrorCapabilitiesInternalReflectorPortSupport_Type = TruthValue
_Cie1000MirrorCapabilitiesInternalReflectorPortSupport_Object = MibScalar
cie1000MirrorCapabilitiesInternalReflectorPortSupport = _Cie1000MirrorCapabilitiesInternalReflectorPortSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 1, 1, 4),
    _Cie1000MirrorCapabilitiesInternalReflectorPortSupport_Type()
)
cie1000MirrorCapabilitiesInternalReflectorPortSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MirrorCapabilitiesInternalReflectorPortSupport.setStatus("current")
_Cie1000MirrorCapabilitiesCpuMirrorSupport_Type = TruthValue
_Cie1000MirrorCapabilitiesCpuMirrorSupport_Object = MibScalar
cie1000MirrorCapabilitiesCpuMirrorSupport = _Cie1000MirrorCapabilitiesCpuMirrorSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 1, 1, 5),
    _Cie1000MirrorCapabilitiesCpuMirrorSupport_Type()
)
cie1000MirrorCapabilitiesCpuMirrorSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MirrorCapabilitiesCpuMirrorSupport.setStatus("current")
_Cie1000MirrorConfig_ObjectIdentity = ObjectIdentity
cie1000MirrorConfig = _Cie1000MirrorConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 1, 2)
)
_Cie1000MirrorConfigSessionTable_Object = MibTable
cie1000MirrorConfigSessionTable = _Cie1000MirrorConfigSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cie1000MirrorConfigSessionTable.setStatus("current")
_Cie1000MirrorConfigSessionEntry_Object = MibTableRow
cie1000MirrorConfigSessionEntry = _Cie1000MirrorConfigSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 1, 2, 1, 1)
)
cie1000MirrorConfigSessionEntry.setIndexNames(
    (0, "CIE1000-MIRROR-MIB", "cie1000MirrorConfigSessionSessionId"),
)
if mibBuilder.loadTexts:
    cie1000MirrorConfigSessionEntry.setStatus("current")


class _Cie1000MirrorConfigSessionSessionId_Type(Integer32):
    """Custom type cie1000MirrorConfigSessionSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Cie1000MirrorConfigSessionSessionId_Type.__name__ = "Integer32"
_Cie1000MirrorConfigSessionSessionId_Object = MibTableColumn
cie1000MirrorConfigSessionSessionId = _Cie1000MirrorConfigSessionSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 1, 2, 1, 1, 1),
    _Cie1000MirrorConfigSessionSessionId_Type()
)
cie1000MirrorConfigSessionSessionId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000MirrorConfigSessionSessionId.setStatus("current")
_Cie1000MirrorConfigSessionMode_Type = TruthValue
_Cie1000MirrorConfigSessionMode_Object = MibTableColumn
cie1000MirrorConfigSessionMode = _Cie1000MirrorConfigSessionMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 1, 2, 1, 1, 2),
    _Cie1000MirrorConfigSessionMode_Type()
)
cie1000MirrorConfigSessionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MirrorConfigSessionMode.setStatus("current")
_Cie1000MirrorConfigSessionType_Type = CIE1000mirrorSessionType
_Cie1000MirrorConfigSessionType_Object = MibTableColumn
cie1000MirrorConfigSessionType = _Cie1000MirrorConfigSessionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 1, 2, 1, 1, 3),
    _Cie1000MirrorConfigSessionType_Type()
)
cie1000MirrorConfigSessionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MirrorConfigSessionType.setStatus("current")
_Cie1000MirrorConfigSessionRMirrorVlan_Type = CIE1000Unsigned16
_Cie1000MirrorConfigSessionRMirrorVlan_Object = MibTableColumn
cie1000MirrorConfigSessionRMirrorVlan = _Cie1000MirrorConfigSessionRMirrorVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 1, 2, 1, 1, 4),
    _Cie1000MirrorConfigSessionRMirrorVlan_Type()
)
cie1000MirrorConfigSessionRMirrorVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MirrorConfigSessionRMirrorVlan.setStatus("current")
_Cie1000MirrorConfigSessionReflectorPort_Type = CIE1000InterfaceIndex
_Cie1000MirrorConfigSessionReflectorPort_Object = MibTableColumn
cie1000MirrorConfigSessionReflectorPort = _Cie1000MirrorConfigSessionReflectorPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 1, 2, 1, 1, 5),
    _Cie1000MirrorConfigSessionReflectorPort_Type()
)
cie1000MirrorConfigSessionReflectorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MirrorConfigSessionReflectorPort.setStatus("current")
_Cie1000MirrorConfigSessionStripInnerTag_Type = TruthValue
_Cie1000MirrorConfigSessionStripInnerTag_Object = MibTableColumn
cie1000MirrorConfigSessionStripInnerTag = _Cie1000MirrorConfigSessionStripInnerTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 1, 2, 1, 1, 6),
    _Cie1000MirrorConfigSessionStripInnerTag_Type()
)
cie1000MirrorConfigSessionStripInnerTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MirrorConfigSessionStripInnerTag.setStatus("current")
_Cie1000MirrorConfigSessionSourceVlans0KTo1K_Type = CIE1000VlanListQuarter
_Cie1000MirrorConfigSessionSourceVlans0KTo1K_Object = MibTableColumn
cie1000MirrorConfigSessionSourceVlans0KTo1K = _Cie1000MirrorConfigSessionSourceVlans0KTo1K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 1, 2, 1, 1, 7),
    _Cie1000MirrorConfigSessionSourceVlans0KTo1K_Type()
)
cie1000MirrorConfigSessionSourceVlans0KTo1K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MirrorConfigSessionSourceVlans0KTo1K.setStatus("current")
_Cie1000MirrorConfigSessionSourceVlans1KTo2K_Type = CIE1000VlanListQuarter
_Cie1000MirrorConfigSessionSourceVlans1KTo2K_Object = MibTableColumn
cie1000MirrorConfigSessionSourceVlans1KTo2K = _Cie1000MirrorConfigSessionSourceVlans1KTo2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 1, 2, 1, 1, 8),
    _Cie1000MirrorConfigSessionSourceVlans1KTo2K_Type()
)
cie1000MirrorConfigSessionSourceVlans1KTo2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MirrorConfigSessionSourceVlans1KTo2K.setStatus("current")
_Cie1000MirrorConfigSessionSourceVlans2KTo3K_Type = CIE1000VlanListQuarter
_Cie1000MirrorConfigSessionSourceVlans2KTo3K_Object = MibTableColumn
cie1000MirrorConfigSessionSourceVlans2KTo3K = _Cie1000MirrorConfigSessionSourceVlans2KTo3K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 1, 2, 1, 1, 9),
    _Cie1000MirrorConfigSessionSourceVlans2KTo3K_Type()
)
cie1000MirrorConfigSessionSourceVlans2KTo3K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MirrorConfigSessionSourceVlans2KTo3K.setStatus("current")
_Cie1000MirrorConfigSessionSourceVlans3KTo4K_Type = CIE1000VlanListQuarter
_Cie1000MirrorConfigSessionSourceVlans3KTo4K_Object = MibTableColumn
cie1000MirrorConfigSessionSourceVlans3KTo4K = _Cie1000MirrorConfigSessionSourceVlans3KTo4K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 1, 2, 1, 1, 10),
    _Cie1000MirrorConfigSessionSourceVlans3KTo4K_Type()
)
cie1000MirrorConfigSessionSourceVlans3KTo4K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MirrorConfigSessionSourceVlans3KTo4K.setStatus("current")
_Cie1000MirrorConfigSessionSourcePortListRx_Type = CIE1000PortList
_Cie1000MirrorConfigSessionSourcePortListRx_Object = MibTableColumn
cie1000MirrorConfigSessionSourcePortListRx = _Cie1000MirrorConfigSessionSourcePortListRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 1, 2, 1, 1, 11),
    _Cie1000MirrorConfigSessionSourcePortListRx_Type()
)
cie1000MirrorConfigSessionSourcePortListRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MirrorConfigSessionSourcePortListRx.setStatus("current")
_Cie1000MirrorConfigSessionSourcePortListTx_Type = CIE1000PortList
_Cie1000MirrorConfigSessionSourcePortListTx_Object = MibTableColumn
cie1000MirrorConfigSessionSourcePortListTx = _Cie1000MirrorConfigSessionSourcePortListTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 1, 2, 1, 1, 12),
    _Cie1000MirrorConfigSessionSourcePortListTx_Type()
)
cie1000MirrorConfigSessionSourcePortListTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MirrorConfigSessionSourcePortListTx.setStatus("current")
_Cie1000MirrorConfigSessionCpuRx_Type = TruthValue
_Cie1000MirrorConfigSessionCpuRx_Object = MibTableColumn
cie1000MirrorConfigSessionCpuRx = _Cie1000MirrorConfigSessionCpuRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 1, 2, 1, 1, 13),
    _Cie1000MirrorConfigSessionCpuRx_Type()
)
cie1000MirrorConfigSessionCpuRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MirrorConfigSessionCpuRx.setStatus("current")
_Cie1000MirrorConfigSessionCpuTx_Type = TruthValue
_Cie1000MirrorConfigSessionCpuTx_Object = MibTableColumn
cie1000MirrorConfigSessionCpuTx = _Cie1000MirrorConfigSessionCpuTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 1, 2, 1, 1, 14),
    _Cie1000MirrorConfigSessionCpuTx_Type()
)
cie1000MirrorConfigSessionCpuTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MirrorConfigSessionCpuTx.setStatus("current")
_Cie1000MirrorConfigSessionDestinationPortList_Type = CIE1000PortList
_Cie1000MirrorConfigSessionDestinationPortList_Object = MibTableColumn
cie1000MirrorConfigSessionDestinationPortList = _Cie1000MirrorConfigSessionDestinationPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 1, 2, 1, 1, 15),
    _Cie1000MirrorConfigSessionDestinationPortList_Type()
)
cie1000MirrorConfigSessionDestinationPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MirrorConfigSessionDestinationPortList.setStatus("current")
_Cie1000MirrorMibConformance_ObjectIdentity = ObjectIdentity
cie1000MirrorMibConformance = _Cie1000MirrorMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 2)
)
_Cie1000MirrorMibCompliances_ObjectIdentity = ObjectIdentity
cie1000MirrorMibCompliances = _Cie1000MirrorMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 2, 1)
)
_Cie1000MirrorMibGroups_ObjectIdentity = ObjectIdentity
cie1000MirrorMibGroups = _Cie1000MirrorMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 2, 2)
)

# Managed Objects groups

cie1000MirrorCapabilitiesInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 2, 2, 1)
)
cie1000MirrorCapabilitiesInfoGroup.setObjects(
      *(("CIE1000-MIRROR-MIB", "cie1000MirrorCapabilitiesSessionCountMax"),
        ("CIE1000-MIRROR-MIB", "cie1000MirrorCapabilitiesSessionSourceCountMax"),
        ("CIE1000-MIRROR-MIB", "cie1000MirrorCapabilitiesRMirrorSuport"),
        ("CIE1000-MIRROR-MIB", "cie1000MirrorCapabilitiesInternalReflectorPortSupport"),
        ("CIE1000-MIRROR-MIB", "cie1000MirrorCapabilitiesCpuMirrorSupport"))
)
if mibBuilder.loadTexts:
    cie1000MirrorCapabilitiesInfoGroup.setStatus("current")

cie1000MirrorConfigSessionTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 2, 2, 2)
)
cie1000MirrorConfigSessionTableInfoGroup.setObjects(
      *(("CIE1000-MIRROR-MIB", "cie1000MirrorConfigSessionSessionId"),
        ("CIE1000-MIRROR-MIB", "cie1000MirrorConfigSessionMode"),
        ("CIE1000-MIRROR-MIB", "cie1000MirrorConfigSessionType"),
        ("CIE1000-MIRROR-MIB", "cie1000MirrorConfigSessionRMirrorVlan"),
        ("CIE1000-MIRROR-MIB", "cie1000MirrorConfigSessionReflectorPort"),
        ("CIE1000-MIRROR-MIB", "cie1000MirrorConfigSessionStripInnerTag"),
        ("CIE1000-MIRROR-MIB", "cie1000MirrorConfigSessionSourceVlans0KTo1K"),
        ("CIE1000-MIRROR-MIB", "cie1000MirrorConfigSessionSourceVlans1KTo2K"),
        ("CIE1000-MIRROR-MIB", "cie1000MirrorConfigSessionSourceVlans2KTo3K"),
        ("CIE1000-MIRROR-MIB", "cie1000MirrorConfigSessionSourceVlans3KTo4K"),
        ("CIE1000-MIRROR-MIB", "cie1000MirrorConfigSessionSourcePortListRx"),
        ("CIE1000-MIRROR-MIB", "cie1000MirrorConfigSessionSourcePortListTx"),
        ("CIE1000-MIRROR-MIB", "cie1000MirrorConfigSessionCpuRx"),
        ("CIE1000-MIRROR-MIB", "cie1000MirrorConfigSessionCpuTx"),
        ("CIE1000-MIRROR-MIB", "cie1000MirrorConfigSessionDestinationPortList"))
)
if mibBuilder.loadTexts:
    cie1000MirrorConfigSessionTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cie1000MirrorMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 15, 2, 1, 1)
)
cie1000MirrorMibCompliance.setObjects(
      *(("CIE1000-MIRROR-MIB", "cie1000MirrorCapabilitiesInfoGroup"),
        ("CIE1000-MIRROR-MIB", "cie1000MirrorConfigSessionTableInfoGroup"))
)
if mibBuilder.loadTexts:
    cie1000MirrorMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIE1000-MIRROR-MIB",
    **{"CIE1000mirrorSessionType": CIE1000mirrorSessionType,
       "cie1000MirrorMib": cie1000MirrorMib,
       "cie1000MirrorMibObjects": cie1000MirrorMibObjects,
       "cie1000MirrorCapabilities": cie1000MirrorCapabilities,
       "cie1000MirrorCapabilitiesSessionCountMax": cie1000MirrorCapabilitiesSessionCountMax,
       "cie1000MirrorCapabilitiesSessionSourceCountMax": cie1000MirrorCapabilitiesSessionSourceCountMax,
       "cie1000MirrorCapabilitiesRMirrorSuport": cie1000MirrorCapabilitiesRMirrorSuport,
       "cie1000MirrorCapabilitiesInternalReflectorPortSupport": cie1000MirrorCapabilitiesInternalReflectorPortSupport,
       "cie1000MirrorCapabilitiesCpuMirrorSupport": cie1000MirrorCapabilitiesCpuMirrorSupport,
       "cie1000MirrorConfig": cie1000MirrorConfig,
       "cie1000MirrorConfigSessionTable": cie1000MirrorConfigSessionTable,
       "cie1000MirrorConfigSessionEntry": cie1000MirrorConfigSessionEntry,
       "cie1000MirrorConfigSessionSessionId": cie1000MirrorConfigSessionSessionId,
       "cie1000MirrorConfigSessionMode": cie1000MirrorConfigSessionMode,
       "cie1000MirrorConfigSessionType": cie1000MirrorConfigSessionType,
       "cie1000MirrorConfigSessionRMirrorVlan": cie1000MirrorConfigSessionRMirrorVlan,
       "cie1000MirrorConfigSessionReflectorPort": cie1000MirrorConfigSessionReflectorPort,
       "cie1000MirrorConfigSessionStripInnerTag": cie1000MirrorConfigSessionStripInnerTag,
       "cie1000MirrorConfigSessionSourceVlans0KTo1K": cie1000MirrorConfigSessionSourceVlans0KTo1K,
       "cie1000MirrorConfigSessionSourceVlans1KTo2K": cie1000MirrorConfigSessionSourceVlans1KTo2K,
       "cie1000MirrorConfigSessionSourceVlans2KTo3K": cie1000MirrorConfigSessionSourceVlans2KTo3K,
       "cie1000MirrorConfigSessionSourceVlans3KTo4K": cie1000MirrorConfigSessionSourceVlans3KTo4K,
       "cie1000MirrorConfigSessionSourcePortListRx": cie1000MirrorConfigSessionSourcePortListRx,
       "cie1000MirrorConfigSessionSourcePortListTx": cie1000MirrorConfigSessionSourcePortListTx,
       "cie1000MirrorConfigSessionCpuRx": cie1000MirrorConfigSessionCpuRx,
       "cie1000MirrorConfigSessionCpuTx": cie1000MirrorConfigSessionCpuTx,
       "cie1000MirrorConfigSessionDestinationPortList": cie1000MirrorConfigSessionDestinationPortList,
       "cie1000MirrorMibConformance": cie1000MirrorMibConformance,
       "cie1000MirrorMibCompliances": cie1000MirrorMibCompliances,
       "cie1000MirrorMibCompliance": cie1000MirrorMibCompliance,
       "cie1000MirrorMibGroups": cie1000MirrorMibGroups,
       "cie1000MirrorCapabilitiesInfoGroup": cie1000MirrorCapabilitiesInfoGroup,
       "cie1000MirrorConfigSessionTableInfoGroup": cie1000MirrorConfigSessionTableInfoGroup}
)
