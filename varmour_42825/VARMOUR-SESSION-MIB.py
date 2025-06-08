# SNMP MIB module (VARMOUR-SESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/varmour_42825/VARMOUR-SESSION-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:05:54 2025
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

(varmourMibs,) = mibBuilder.importSymbols(
    "VARMOUR-SMI",
    "varmourMibs")

(VarmourDevice,) = mibBuilder.importSymbols(
    "VARMOUR-TC",
    "VarmourDevice")


# MODULE-IDENTITY

varmour_session = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VaSession_ObjectIdentity = ObjectIdentity
vaSession = _VaSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 4, 1)
)
_VaSessionTable_Object = MibTable
vaSessionTable = _VaSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    vaSessionTable.setStatus("current")
_VaSessionEntry_Object = MibTableRow
vaSessionEntry = _VaSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 4, 2, 1)
)
vaSessionEntry.setIndexNames(
    (0, "VARMOUR-SESSION-MIB", "vaSessDev"),
)
if mibBuilder.loadTexts:
    vaSessionEntry.setStatus("current")
_VaSessDev_Type = VarmourDevice
_VaSessDev_Object = MibTableColumn
vaSessDev = _VaSessDev_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 4, 2, 1, 1),
    _VaSessDev_Type()
)
vaSessDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSessDev.setStatus("current")
_VaSessMaxNum_Type = Integer32
_VaSessMaxNum_Object = MibTableColumn
vaSessMaxNum = _VaSessMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 4, 2, 1, 2),
    _VaSessMaxNum_Type()
)
vaSessMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSessMaxNum.setStatus("current")
_VaSessActive_Type = Integer32
_VaSessActive_Object = MibTableColumn
vaSessActive = _VaSessActive_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 4, 2, 1, 3),
    _VaSessActive_Type()
)
vaSessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSessActive.setStatus("current")
_VaSessTcp_Type = Integer32
_VaSessTcp_Object = MibTableColumn
vaSessTcp = _VaSessTcp_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 4, 2, 1, 4),
    _VaSessTcp_Type()
)
vaSessTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSessTcp.setStatus("current")
_VaSessUdp_Type = Integer32
_VaSessUdp_Object = MibTableColumn
vaSessUdp = _VaSessUdp_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 4, 2, 1, 5),
    _VaSessUdp_Type()
)
vaSessUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSessUdp.setStatus("current")
_VaSessIcmp_Type = Integer32
_VaSessIcmp_Object = MibTableColumn
vaSessIcmp = _VaSessIcmp_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 4, 2, 1, 6),
    _VaSessIcmp_Type()
)
vaSessIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSessIcmp.setStatus("current")
_VaSessUtil_Type = Integer32
_VaSessUtil_Object = MibTableColumn
vaSessUtil = _VaSessUtil_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 4, 2, 1, 7),
    _VaSessUtil_Type()
)
vaSessUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSessUtil.setStatus("current")
_VaSessCreated_Type = Integer32
_VaSessCreated_Object = MibTableColumn
vaSessCreated = _VaSessCreated_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 4, 2, 1, 8),
    _VaSessCreated_Type()
)
vaSessCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSessCreated.setStatus("current")
_VaSessTcpTimeout_Type = Integer32
_VaSessTcpTimeout_Object = MibTableColumn
vaSessTcpTimeout = _VaSessTcpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 4, 2, 1, 9),
    _VaSessTcpTimeout_Type()
)
vaSessTcpTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSessTcpTimeout.setStatus("current")
_VaSessUdpTimeout_Type = Integer32
_VaSessUdpTimeout_Object = MibTableColumn
vaSessUdpTimeout = _VaSessUdpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 4, 2, 1, 10),
    _VaSessUdpTimeout_Type()
)
vaSessUdpTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSessUdpTimeout.setStatus("current")
_VaSessIcmpTimeout_Type = Integer32
_VaSessIcmpTimeout_Object = MibTableColumn
vaSessIcmpTimeout = _VaSessIcmpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 4, 2, 1, 11),
    _VaSessIcmpTimeout_Type()
)
vaSessIcmpTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSessIcmpTimeout.setStatus("current")
_VaSessMisc_Type = DisplayString
_VaSessMisc_Object = MibTableColumn
vaSessMisc = _VaSessMisc_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 4, 2, 1, 12),
    _VaSessMisc_Type()
)
vaSessMisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSessMisc.setStatus("current")
_VaSessLastSec_Type = Integer32
_VaSessLastSec_Object = MibTableColumn
vaSessLastSec = _VaSessLastSec_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 4, 2, 1, 13),
    _VaSessLastSec_Type()
)
vaSessLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSessLastSec.setStatus("current")
_VaSessLast20Sec_Type = Integer32
_VaSessLast20Sec_Object = MibTableColumn
vaSessLast20Sec = _VaSessLast20Sec_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 4, 2, 1, 14),
    _VaSessLast20Sec_Type()
)
vaSessLast20Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSessLast20Sec.setStatus("current")
_VaSessLastMin_Type = Integer32
_VaSessLastMin_Object = MibTableColumn
vaSessLastMin = _VaSessLastMin_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 4, 2, 1, 15),
    _VaSessLastMin_Type()
)
vaSessLastMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSessLastMin.setStatus("current")
_VaSessLast20Min_Type = Integer32
_VaSessLast20Min_Object = MibTableColumn
vaSessLast20Min = _VaSessLast20Min_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 4, 2, 1, 16),
    _VaSessLast20Min_Type()
)
vaSessLast20Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSessLast20Min.setStatus("current")
_VaSessLastHour_Type = Integer32
_VaSessLastHour_Object = MibTableColumn
vaSessLastHour = _VaSessLastHour_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 4, 2, 1, 17),
    _VaSessLastHour_Type()
)
vaSessLastHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSessLastHour.setStatus("current")
_VaSessRateMisc_Type = DisplayString
_VaSessRateMisc_Object = MibTableColumn
vaSessRateMisc = _VaSessRateMisc_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 4, 2, 1, 18),
    _VaSessRateMisc_Type()
)
vaSessRateMisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSessRateMisc.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VARMOUR-SESSION-MIB",
    **{"varmour-session": varmour_session,
       "vaSession": vaSession,
       "vaSessionTable": vaSessionTable,
       "vaSessionEntry": vaSessionEntry,
       "vaSessDev": vaSessDev,
       "vaSessMaxNum": vaSessMaxNum,
       "vaSessActive": vaSessActive,
       "vaSessTcp": vaSessTcp,
       "vaSessUdp": vaSessUdp,
       "vaSessIcmp": vaSessIcmp,
       "vaSessUtil": vaSessUtil,
       "vaSessCreated": vaSessCreated,
       "vaSessTcpTimeout": vaSessTcpTimeout,
       "vaSessUdpTimeout": vaSessUdpTimeout,
       "vaSessIcmpTimeout": vaSessIcmpTimeout,
       "vaSessMisc": vaSessMisc,
       "vaSessLastSec": vaSessLastSec,
       "vaSessLast20Sec": vaSessLast20Sec,
       "vaSessLastMin": vaSessLastMin,
       "vaSessLast20Min": vaSessLast20Min,
       "vaSessLastHour": vaSessLastHour,
       "vaSessRateMisc": vaSessRateMisc}
)
